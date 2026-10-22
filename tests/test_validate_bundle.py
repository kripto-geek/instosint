"""Tests for scripts/validate_bundle.py.

Run with:  python -m unittest discover -s tests -v
"""

from __future__ import annotations

import copy
import importlib.util
import json
import sys
import tempfile
import unittest
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parent.parent
EXAMPLE = REPO_ROOT / "examples" / "synthetic-example" / "bundle.json"

spec = importlib.util.spec_from_file_location(
    "validate_bundle", REPO_ROOT / "scripts" / "validate_bundle.py"
)
assert spec and spec.loader
validate_bundle = importlib.util.module_from_spec(spec)
sys.modules["validate_bundle"] = validate_bundle
spec.loader.exec_module(validate_bundle)


def load_example() -> dict:
    with EXAMPLE.open(encoding="utf-8") as handle:
        return json.load(handle)


class ValidatorTest(unittest.TestCase):
    def check(self, bundle: dict) -> list[str]:
        with tempfile.TemporaryDirectory() as tmp:
            path = Path(tmp) / "bundle.json"
            path.write_text(json.dumps(bundle), encoding="utf-8")
            report = validate_bundle.validate_bundle(path)
        return report.errors

    def assert_rejected(self, bundle: dict, needle: str) -> None:
        errors = self.check(bundle)
        self.assertTrue(errors, "bundle should have been rejected")
        joined = "\n".join(errors).lower()
        self.assertIn(needle.lower(), joined, f"expected an error mentioning {needle!r}, got:\n{joined}")

    def test_example_bundle_is_valid(self) -> None:
        self.assertEqual(self.check(load_example()), [])

    def test_dangling_relationship_evidence_is_rejected(self) -> None:
        bundle = load_example()
        bundle["relationships"][0]["evidence"] = ["OBS-999"]
        self.assert_rejected(bundle, "unresolved reference OBS-999")

    def test_relationship_without_evidence_is_rejected(self) -> None:
        bundle = load_example()
        bundle["relationships"][0]["evidence"] = []
        self.assert_rejected(bundle, "hypothetical=true")

    def test_duplicate_ids_are_rejected(self) -> None:
        bundle = load_example()
        bundle["sources"][1]["id"] = bundle["sources"][0]["id"]
        self.assert_rejected(bundle, "duplicate id")

    def test_score_total_must_match_breakdown(self) -> None:
        bundle = load_example()
        bundle["leads"][0]["score"]["total"] = 16
        self.assert_rejected(bundle, "breakdown sums")

    def test_quality_band_must_match_total(self) -> None:
        bundle = load_example()
        bundle["leads"][0]["quality"] = "WEAK"
        self.assert_rejected(bundle, "falls in HIGH_VALUE")

    def test_threshold_flag_must_match_total(self) -> None:
        bundle = load_example()
        bundle["leads"][3]["threshold_met"] = True
        self.assert_rejected(bundle, "threshold")

    def test_supported_hypothesis_needs_supporting_evidence(self) -> None:
        bundle = load_example()
        bundle["hypotheses"][0]["status"] = "SUPPORTED"
        bundle["hypotheses"][0]["supporting"] = []
        self.assert_rejected(bundle, "no supporting evidence")

    def test_conclusion_cannot_upgrade_unresolved_hypothesis(self) -> None:
        bundle = load_example()
        bundle["conclusions"][1]["status"] = "SUPPORTED"
        self.assert_rejected(bundle, "claims SUPPORTED but HYP-002 is POSSIBLE")

    def test_percentage_confidence_is_rejected(self) -> None:
        bundle = load_example()
        bundle["hypotheses"][0]["notes"] = "This is 87% likely to be correct."
        self.assert_rejected(bundle, "invented percentage")

    def test_placeholders_rejected_in_real_bundle(self) -> None:
        bundle = load_example()
        bundle["synthetic"] = False
        bundle["observations"][0]["observation"] = "Account A follows Account B."
        self.assert_rejected(bundle, "placeholder")

    def test_placeholders_allowed_in_synthetic_bundle(self) -> None:
        bundle = load_example()
        bundle["observations"][0]["observation"] = "Account A follows Account B."
        self.assertEqual(self.check(bundle), [])

    def test_suggestion_observation_requires_canonical_fields(self) -> None:
        bundle = load_example()
        del bundle["observations"][1]["suggestion"]["mutual_count"]
        self.assert_rejected(bundle, "suggestion.mutual_count")

    def test_missing_required_field_is_rejected(self) -> None:
        bundle = load_example()
        del bundle["observations"][0]["observation"]
        self.assert_rejected(bundle, "missing required field observation")

    def test_unresolved_node_reference_is_rejected(self) -> None:
        bundle = load_example()
        bundle["observations"][0]["subject"] = "ACCOUNT-999"
        self.assert_rejected(bundle, "ACCOUNT-999")


if __name__ == "__main__":
    unittest.main()
