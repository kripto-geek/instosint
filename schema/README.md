# INSTOSINT Schema

`evidence-bundle.schema.json` is the machine-readable form of the evidence model.
It is **not** a new source of truth: every field maps to an existing rule in
`references/`. If the schema and a reference document disagree, the reference
document wins and the schema is a bug.

| Definition | Defined in |
|---|---|
| `investigation` | `SKILL.md` §0.3, §5; `references/investigation-output.md` |
| `node` | `references/graph-model.md` §2–4 |
| `source` | `references/evidence-model.md` §3–4, §31 |
| `observation` | `references/evidence-model.md` §5–7, §17 |
| `observation.suggestion` | `references/suggestion-surface-analysis.md` §4–5 |
| `relationship` | `references/graph-model.md` §5–7, §8 |
| `hypothesis` | `references/evidence-model.md` §20–21 |
| `lead` | `references/suggestion-surface-analysis.md` §16 |
| `unknown` | `references/evidence-model.md` §31; `references/graph-model.md` §15 |
| `conclusion` | `references/investigation-output.md` §12–13 |

## Enumerations

Values are closed sets. Adding one is a schema change and must be reflected in
the matching reference document first.

- **Observation types** — `DIRECT_OBSERVATION`, `DERIVED_OBSERVATION`,
  `VISUAL_OBSERVATION`, `TEXTUAL_OBSERVATION`, `INFERENCE`, `HYPOTHESIS`,
  `DATA_AVAILABILITY`, `SUGGESTION_OBSERVATION`,
  `RECURRING_SUGGESTION_SIGNAL`, `BIDIRECTIONAL_SUGGESTION_SIGNAL`,
  `SHARED_SUGGESTION_FINGERPRINT`, `COMMUNITY_CANDIDATE`.
  `HYPOTHESIS`-typed observations are accepted for compatibility with
  `references/evidence-model.md` §7, but new work should use `hypotheses[]`.
- **Reliability** — `LOW`, `MODERATE`, `HIGH`, `UNKNOWN`.
- **Hypothesis status** — `POSSIBLE`, `INVESTIGATING`, `SUPPORTED`,
  `STRONGLY_SUPPORTED`, `CONTRADICTED`, `UNRESOLVED`.
- **Relationship strength** — `UNKNOWN`, `WEAK`, `MODERATE`, `STRONG`.
- **Lead quality** — `WEAK` (0–3), `MODERATE` (4–6), `STRONG` (7–9),
  `HIGH_VALUE` (10+).

## What the schema cannot express

`scripts/validate_bundle.py` adds the semantic checks:

- IDs are unique across every collection and every reference resolves.
- Non-hypothetical relationships carry at least one observation.
- `SUPPORTED` / `STRONGLY_SUPPORTED` hypotheses carry supporting evidence;
  `CONTRADICTED` hypotheses carry contradicting evidence.
- A `SUPPORTED` or `PARTIALLY_SUPPORTED` conclusion cannot rest on an
  `UNRESOLVED`, `CONTRADICTED`, or merely `POSSIBLE` hypothesis.
- Lead score totals equal the sum of the breakdown, and the quality band and
  `threshold_met` flag agree with the total.
- Suggestion observations carry the canonical fields.
- Non-synthetic bundles contain no placeholders and no invented percentages.

## Conventions

- Timestamps are RFC 3339 UTC (`2026-01-15T10:00:00Z`).
- `synthetic: true` is required for any bundle containing invented values, and
  the accompanying report must be marked `[SYNTHETIC EXAMPLE]`.
- `artifact` paths are relative to the bundle directory. Screenshots, cookies,
  session state, and credentials must never be committed. Real evidence lives
  outside version control (`temp/` and `evidence/` are gitignored).
- Node references are either a node ID (`ACCOUNT-001`) or an observed handle
  (`@account`). Node IDs must resolve.
