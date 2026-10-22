#!/usr/bin/env python3
"""Validate INSTOSINT evidence bundles.

Two layers of checks:

1. Structural validation against schema/evidence-bundle.schema.json
   (uses `jsonschema` when installed; degrades to the built-in checks below
   when it is not).
2. Semantic checks the schema cannot express:
   - unique and resolvable IDs across every collection
   - every relationship, hypothesis, lead, and conclusion traces to real evidence
   - lead score arithmetic and quality band agree with the scoring model
   - no invented percentages, no placeholder values in non-synthetic bundles
   - suggestion observations carry the canonical required fields

Usage:
    python scripts/validate_bundle.py                 # validate examples/
    python scripts/validate_bundle.py path/to/bundle.json
    python scripts/validate_bundle.py examples/synthetic-example

Exit codes: 0 = clean (warnings allowed), 1 = errors found, 2 = bad invocation.
"""

from __future__ import annotations

import json
import re
import sys
from pathlib import Path
from typing import Any, Iterable

REPO_ROOT = Path(__file__).resolve().parent.parent
SCHEMA_PATH = REPO_ROOT / "schema" / "evidence-bundle.schema.json"

ID_COLLECTIONS = {
    "nodes": "node",
    "sources": "source",
    "observations": "observation",
    "relationships": "relationship",
    "hypotheses": "hypothesis",
    "leads": "lead",
    "unknowns": "unknown",
    "conclusions": "conclusion",
}

NODE_ID_RE = re.compile(
    r"^(ACCOUNT|POST|COMMENT|IMAGE|VIDEO|HASHTAG|PLACE|EVENT|OBJECT|"
    r"TEXT_FRAGMENT|EXTERNAL_RESOURCE)-[0-9]{3,}$"
)

# Placeholders are forbidden as factual values unless the bundle is synthetic.
PLACEHOLDER_PATTERNS = [
    r"\bAccount [A-Z]\b",
    r"\bPerson [A-Z]\b",
    r"\bEvent [A-Z]\b",
    r"\bTarget [A-Z]\b",
    r"\[username\]",
    r"\[bio text\]",
    r"\[display name\]",
    r"\[Number\]",
]

# references/evidence-model.md 34: no invented probabilities without a calibrated model.
PERCENT_CONFIDENCE_RE = re.compile(
    r"\b\d{1,3}\s?%\s*(likely|confidence|probability|sure|certain)\b", re.IGNORECASE
)

QUALITY_BANDS = [
    (0, 3, "WEAK"),
    (4, 6, "MODERATE"),
    (7, 9, "STRONG"),
    (10, 99, "HIGH_VALUE"),
]

THRESHOLD = 6  # references/suggestion-surface-analysis.md 16.4

# Mirrors the schema's required arrays so the fallback path (no jsonschema
# installed) still rejects structurally incomplete records.
REQUIRED_FIELDS = {
    "nodes": ("id", "type"),
    "sources": ("id", "type", "access_status"),
    "observations": ("id", "source", "subject", "observation", "type", "reliability"),
    "relationships": ("id", "subject", "relationship", "object", "strength"),
    "hypotheses": ("id", "statement", "status", "confidence"),
    "leads": ("id", "account", "base_signal", "score", "quality", "threshold_met"),
    "unknowns": ("id", "surface", "status", "reason"),
    "conclusions": ("id", "statement", "status", "confidence", "hypotheses"),
}

INVESTIGATION_FIELDS = (
    "id",
    "target",
    "started_at",
    "mode",
    "auth_state",
    "setup_state",
    "final_state",
)


class Report:
    def __init__(self, path: Path) -> None:
        self.path = path
        self.errors: list[str] = []
        self.warnings: list[str] = []

    def error(self, message: str) -> None:
        self.errors.append(message)

    def warn(self, message: str) -> None:
        self.warnings.append(message)

    @property
    def ok(self) -> bool:
        return not self.errors


def load_json(path: Path) -> Any:
    with path.open(encoding="utf-8") as handle:
        return json.load(handle)


def validate_with_jsonschema(bundle: Any, report: Report) -> bool:
    """Return True when jsonschema performed validation, False when unavailable."""
    try:
        import jsonschema  # type: ignore
    except ImportError:
        return False

    schema = load_json(SCHEMA_PATH)
    validator = jsonschema.Draft202012Validator(schema, format_checker=jsonschema.FormatChecker())
    for error in sorted(validator.iter_errors(bundle), key=lambda e: list(e.absolute_path)):
        location = "/".join(str(part) for part in error.absolute_path) or "<root>"
        report.error(f"schema: {location}: {error.message}")
    return True


def collect_ids(bundle: dict[str, Any], report: Report) -> dict[str, str]:
    """Map every declared ID to its collection name; report duplicates."""
    seen: dict[str, str] = {}
    for collection in ID_COLLECTIONS:
        for record in bundle.get(collection) or []:
            record_id = record.get("id")
            if not isinstance(record_id, str):
                report.error(f"{collection}: record without a string id")
                continue
            if record_id in seen:
                report.error(
                    f"duplicate id {record_id}: declared in both "
                    f"{seen[record_id]} and {collection}"
                )
            seen[record_id] = collection
    return seen


def check_required_fields(bundle: dict[str, Any], report: Report) -> None:
    investigation = bundle.get("investigation")
    if not isinstance(investigation, dict):
        report.error("investigation: missing object")
    else:
        for field in INVESTIGATION_FIELDS:
            if field not in investigation:
                report.error(f"investigation: missing required field {field}")

    for collection, fields in REQUIRED_FIELDS.items():
        for record in bundle.get(collection) or []:
            record_id = record.get("id", "<unknown>")
            for field in fields:
                if field not in record:
                    report.error(f"{collection}/{record_id}: missing required field {field}")


def check_refs(
    value: Any,
    field: str,
    ids: dict[str, str],
    report: Report,
    *,
    expected: Iterable[str] | None = None,
) -> None:
    refs = value if isinstance(value, list) else [value]
    expected_set = set(expected) if expected else None
    for ref in refs:
        if not isinstance(ref, str):
            report.error(f"{field}: non-string reference {ref!r}")
            continue
        if ref not in ids:
            report.error(f"{field}: unresolved reference {ref}")
        elif expected_set is not None and ids[ref] not in expected_set:
            report.error(
                f"{field}: {ref} points at {ids[ref]}, expected {sorted(expected_set)}"
            )


def check_entity_ref(value: Any, field: str, node_ids: set[str], report: Report) -> None:
    if value is None:
        return
    if not isinstance(value, str):
        report.error(f"{field}: entity reference must be a string")
        return
    if NODE_ID_RE.match(value) and value not in node_ids:
        report.error(f"{field}: node reference {value} not found in nodes[]")


def check_placeholders(bundle: Any, report: Report) -> None:
    if bundle.get("synthetic") is True:
        return

    def walk(value: Any, path: str) -> None:
        if isinstance(value, dict):
            for key, child in value.items():
                walk(child, f"{path}/{key}")
        elif isinstance(value, list):
            for index, child in enumerate(value):
                walk(child, f"{path}/{index}")
        elif isinstance(value, str):
            for pattern in PLACEHOLDER_PATTERNS:
                if re.search(pattern, value):
                    report.error(
                        f"placeholder {pattern!r} at {path}: mark the bundle synthetic "
                        f"or replace it with UNKNOWN"
                    )
                    return

    walk(bundle, "")


def check_percentages(bundle: dict[str, Any], report: Report) -> None:
    for collection in ("hypotheses", "conclusions"):
        for record in bundle.get(collection) or []:
            for field in ("statement", "notes"):
                text = record.get(field)
                if isinstance(text, str) and PERCENT_CONFIDENCE_RE.search(text):
                    report.error(
                        f"{collection}/{record.get('id')}/{field}: invented percentage "
                        f"confidence; use LOW/MODERATE/HIGH/VERY_HIGH"
                    )


def check_lead_scores(bundle: dict[str, Any], report: Report) -> None:
    for lead in bundle.get("leads") or []:
        lead_id = lead.get("id", "<unknown>")
        score = lead.get("score") or {}
        parts = (
            "recurrence",
            "mutual_count",
            "persistence",
            "multi_surface",
            "bidirectional",
            "corroboration",
        )
        if not all(isinstance(score.get(part), int) for part in parts):
            report.error(f"leads/{lead_id}: score breakdown must be integers")
            continue
        if not isinstance(score.get("total"), int):
            report.error(f"leads/{lead_id}: score.total missing")
            continue
        computed = sum(score[part] for part in parts)
        if computed != score["total"]:
            report.error(
                f"leads/{lead_id}: score.total={score['total']} but breakdown sums "
                f"to {computed}"
            )

        declared = lead.get("quality")
        band = next(
            (name for low, high, name in QUALITY_BANDS if low <= score["total"] <= high),
            None,
        )
        if band and declared != band:
            report.error(
                f"leads/{lead_id}: quality={declared} but total={score['total']} "
                f"falls in {band}"
            )

        expected_threshold = score["total"] >= THRESHOLD
        if lead.get("threshold_met") is not expected_threshold:
            report.error(
                f"leads/{lead_id}: threshold_met={lead.get('threshold_met')} but "
                f"total={score['total']} (threshold {THRESHOLD})"
            )


def check_suggestion_fields(bundle: dict[str, Any], report: Report) -> None:
    required = ("target_account", "position", "mutual_count", "context_label", "timestamp")
    for observation in bundle.get("observations") or []:
        if observation.get("type") != "SUGGESTION_OBSERVATION":
            continue
        obs_id = observation.get("id", "<unknown>")
        suggestion = observation.get("suggestion")
        if not isinstance(suggestion, dict):
            report.error(
                f"observations/{obs_id}: SUGGESTION_OBSERVATION requires a suggestion object"
            )
            continue
        for field in required:
            if field not in suggestion:
                report.error(
                    f"observations/{obs_id}: suggestion.{field} is required "
                    f"(canonical record, references/suggestion-surface-analysis.md 4)"
                )
        context = suggestion.get("context_label")
        if isinstance(context, str) and context.strip() != context:
            report.warn(f"observations/{obs_id}: context_label has surrounding whitespace")


def check_hypothesis_links(bundle: dict[str, Any], report: Report) -> None:
    status = {
        hypothesis.get("id"): hypothesis.get("status")
        for hypothesis in bundle.get("hypotheses") or []
    }
    for hypothesis in bundle.get("hypotheses") or []:
        hyp_id = hypothesis.get("id", "<unknown>")
        if hypothesis.get("status") in ("SUPPORTED", "STRONGLY_SUPPORTED"):
            if not hypothesis.get("supporting"):
                report.error(f"hypotheses/{hyp_id}: {hypothesis['status']} with no supporting evidence")
        if hypothesis.get("status") == "CONTRADICTED" and not hypothesis.get("contradicting"):
            report.error(f"hypotheses/{hyp_id}: CONTRADICTED with no contradicting evidence")

    for conclusion in bundle.get("conclusions") or []:
        con_id = conclusion.get("id", "<unknown>")
        for hyp_ref in conclusion.get("hypotheses") or []:
            if hyp_ref not in status:
                report.error(f"conclusions/{con_id}: unresolved hypothesis {hyp_ref}")
                continue
            if conclusion.get("status") in ("SUPPORTED", "PARTIALLY_SUPPORTED") and status[
                hyp_ref
            ] in ("UNRESOLVED", "CONTRADICTED", "POSSIBLE"):
                report.error(
                    f"conclusions/{con_id}: claims {conclusion['status']} but "
                    f"{hyp_ref} is {status[hyp_ref]}"
                )


def check_relationship_evidence(bundle: dict[str, Any], report: Report) -> None:
    for relationship in bundle.get("relationships") or []:
        rel_id = relationship.get("id", "<unknown>")
        if relationship.get("hypothetical") is not True and not relationship.get("evidence"):
            report.error(
                f"relationships/{rel_id}: edge with no evidence must set hypothetical=true"
            )


def validate_bundle(path: Path) -> Report:
    report = Report(path)
    try:
        bundle = load_json(path)
    except json.JSONDecodeError as exc:
        report.error(f"invalid JSON: {exc}")
        return report
    except OSError as exc:
        report.error(f"cannot read file: {exc}")
        return report

    if not isinstance(bundle, dict):
        report.error("bundle root must be a JSON object")
        return report

    validate_with_jsonschema(bundle, report)
    check_required_fields(bundle, report)

    ids = collect_ids(bundle, report)
    node_ids = {node.get("id") for node in bundle.get("nodes") or [] if node.get("id")}

    for node in bundle.get("nodes") or []:
        if node.get("source"):
            check_refs(node["source"], f"nodes/{node.get('id')}/source", ids, report, expected={"sources"})

    for source in bundle.get("sources") or []:
        artifact = source.get("artifact")
        if isinstance(artifact, str) and artifact.startswith(("/", "~")):
            report.warn(
                f"sources/{source.get('id')}: artifact path should be relative to the bundle"
            )

    for observation in bundle.get("observations") or []:
        obs_id = observation.get("id", "<unknown>")
        if observation.get("source"):
            check_refs(
                observation["source"], f"observations/{obs_id}/source", ids, report, expected={"sources"}
            )
        check_entity_ref(observation.get("subject"), f"observations/{obs_id}/subject", node_ids, report)
        check_entity_ref(observation.get("object"), f"observations/{obs_id}/object", node_ids, report)
        if observation.get("related"):
            check_refs(
                observation["related"],
                f"observations/{obs_id}/related",
                ids,
                report,
                expected={"observations"},
            )

    for relationship in bundle.get("relationships") or []:
        rel_id = relationship.get("id", "<unknown>")
        check_entity_ref(relationship.get("subject"), f"relationships/{rel_id}/subject", node_ids, report)
        check_entity_ref(relationship.get("object"), f"relationships/{rel_id}/object", node_ids, report)
        if relationship.get("evidence"):
            check_refs(
                relationship["evidence"],
                f"relationships/{rel_id}/evidence",
                ids,
                report,
                expected={"observations"},
            )

    for hypothesis in bundle.get("hypotheses") or []:
        hyp_id = hypothesis.get("id", "<unknown>")
        for field in ("supporting", "contradicting"):
            if hypothesis.get(field):
                check_refs(
                    hypothesis[field],
                    f"hypotheses/{hyp_id}/{field}",
                    ids,
                    report,
                    expected={"observations"},
                )

    for lead in bundle.get("leads") or []:
        lead_id = lead.get("id", "<unknown>")
        if lead.get("evidence"):
            check_refs(
                lead["evidence"], f"leads/{lead_id}/evidence", ids, report, expected={"observations"}
            )

    if bundle.get("unknowns"):
        for unknown in bundle["unknowns"]:
            if unknown.get("related"):
                check_refs(
                    unknown["related"],
                    f"unknowns/{unknown.get('id')}/related",
                    ids,
                    report,
                    expected={"observations", "sources"},
                )

    for conclusion in bundle.get("conclusions") or []:
        con_id = conclusion.get("id", "<unknown>")
        if conclusion.get("hypotheses"):
            check_refs(
                conclusion["hypotheses"],
                f"conclusions/{con_id}/hypotheses",
                ids,
                report,
                expected={"hypotheses"},
            )

    check_lead_scores(bundle, report)
    check_suggestion_fields(bundle, report)
    check_hypothesis_links(bundle, report)
    check_relationship_evidence(bundle, report)
    check_percentages(bundle, report)
    check_placeholders(bundle, report)

    return report


def discover(target: Path) -> list[Path]:
    if target.is_file():
        return [target]
    if not target.exists():
        return []
    return sorted(
        path
        for path in target.rglob("*.json")
        if SCHEMA_PATH.name not in path.name and "/schema/" not in path.as_posix()
    )


def main(argv: list[str]) -> int:
    targets = [Path(arg) for arg in argv[1:]] or [REPO_ROOT / "examples"]
    paths: list[Path] = []
    for target in targets:
        found = discover(target.resolve())
        if not found:
            print(f"no JSON bundles found under {target}", file=sys.stderr)
        paths.extend(found)

    if not paths:
        return 2

    failures = 0
    for path in paths:
        report = validate_bundle(path)
        relative = path.relative_to(REPO_ROOT) if path.is_relative_to(REPO_ROOT) else path
        status = "PASS" if report.ok else "FAIL"
        print(f"{status} {relative}")
        for warning in report.warnings:
            print(f"  warning: {warning}")
        for error in report.errors:
            print(f"  error:   {error}")
        if not report.ok:
            failures += 1

    print(f"\n{len(paths) - failures}/{len(paths)} bundles valid")
    return 0 if failures == 0 else 1


if __name__ == "__main__":
    sys.exit(main(sys.argv))
