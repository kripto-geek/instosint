# INSTOSINT

Instagram-focused OSINT investigation skill for OpenCode.

INSTOSINT investigates publicly observable Instagram information, builds an evidence graph, discovers connections, and recursively pursues the most useful leads.

The goal is **reasoning over relationships**, not indiscriminate data collection.

---

## What It Does

Given a target account, the agent examines public Instagram surfaces, identifies accounts, posts, people, places, events, and interactions — including the profile-page suggestion block shown for private accounts — connects them, generates hypotheses, and decides what to investigate next.

```text
Target Account
  → Public Instagram Data
  → Observations
  → Evidence Graph
  → Relationships
  → Hypotheses
  → High-value Leads
  → Evidence-backed Conclusions
```

### Reasoning Loop

```text
OBSERVE → RECORD → CONNECT → FORM HYPOTHESES → INVESTIGATE
  → CHALLENGE → UPDATE GRAPH → CHOOSE NEXT BEST LEAD → REPEAT
```

---

## Core Idea

Instagram is treated as a dynamic relationship graph, not isolated profiles.

INSTOSINT operates on publicly observable surrounding signals — including the profile-page suggestion block shown for private accounts — and uses suggestion-set fingerprinting, multi-surface triangulation, and community detection to map network relationships without accessing private content.

Examples:

```text
Target (private)
  → SUGGESTED → Account A (mutual count: 12, recurring, multi-surface)
  → Account A's public content → SHARED_EVENT → Event X
  → Event X → Account B (also suggested around Target)
```

```text
Target A → SUGGESTED_SET → [B, C, D]
Target B → SUGGESTED_SET → [C, D, E]
Target C → SUGGESTED_SET → [D, E, F]
Shared cluster → [D, E] → COMMUNITY_CANDIDATE
```

A connection is not automatically a conclusion. The system distinguishes:

```text
Observation → Derived relationship → Inference → Hypothesis → Supported hypothesis
```

The goal is **reasoning over relationships**, not indiscriminate data collection.

---

## What INSTOSINT Is NOT

- A generic web search tool
- A profile scraper or follower exporter
- A private-account bypass
- A system that invents missing evidence
- A relationship-status detector
- A bundled Instagram API client — data acquisition is delegated to the harness

---

## Key Principles

1. **Evidence first** — no evidence, no factual claim
2. **Observation before interpretation** — record what is visible before deciding what it means
3. **Graph before conclusion** — represent connections explicitly before drawing conclusions
4. **Recursion with purpose** — every investigation hop must have a reason
5. **Information gain over data volume** — investigate what reduces uncertainty
6. **Images matter** — visual context reveals relationships text misses
7. **Recommendations are leads** — useful signals, not proof
8. **Similarity is not identity** — similar accounts do not automatically mean the same person
9. **Contradictions matter** — actively seek evidence that challenges hypotheses
10. **Unknown is allowed** — "We don't know" is a valid answer
11. **No fabrication** — never create evidence to make a report look complete
12. **Traceability** — every conclusion must map back to source

---

## Project Structure

```text
instosint/
├── SKILL.md
├── README.md
├── schema/
│   ├── README.md
│   └── evidence-bundle.schema.json
├── examples/
│   └── synthetic-example/
│       ├── bundle.json
│       └── report.md
├── scripts/
│   └── validate_bundle.py
├── tests/
│   └── test_validate_bundle.py
└── references/
    ├── instagram-surfaces.md
    ├── evidence-model.md
    ├── investigation-strategy.md
    ├── investigation-output.md
    ├── image-analysis.md
    ├── graph-model.md
    ├── suggestion-surface-analysis.md
    └── browser-access.md
```

### Reference Files

- `instagram-surfaces.md` — surfaces that can provide useful observations
- `evidence-model.md` — evidence definitions and provenance
- `investigation-strategy.md` — lead selection and investigation strategy
- `investigation-output.md` — final report structure
- `image-analysis.md` — image and visual evidence methodology
- `graph-model.md` — graph nodes, edges, and traversal
- `suggestion-surface-analysis.md` — advanced suggestion-surface methodology including quantified features, fingerprinting, community detection, and weighted lead scoring
- `browser-access.md` — optional browser-based data-access layer for observing JS-rendered Instagram surfaces with authorized test-account sessions

---

## Evidence Bundle and Validation

The prose model is mirrored by a JSON Schema so a graph can be checked instead
of merely described:

```bash
# Validate the shipped example (no dependencies required)
python3 scripts/validate_bundle.py

# Validate a real investigation bundle
python3 scripts/validate_bundle.py path/to/bundle.json

# Full validation, including JSON Schema constraints
pip install jsonschema
python3 scripts/validate_bundle.py examples

# Semantic tests
python3 -m unittest discover -s tests -v
```

The validator checks schema conformance plus the rules a schema cannot express:
unique and resolvable IDs, evidence-backed edges, hypotheses and conclusions
that cannot upgrade themselves, lead-score arithmetic, canonical suggestion
fields, and rejection of placeholders or invented percentages in non-synthetic
bundles.

Start from `examples/synthetic-example/bundle.json` (and its matching
`report.md`) when producing a new investigation. The example is entirely
fictional and marked as such; real investigation artifacts stay out of git.

---

## Data Access and Degraded Mode

INSTOSINT is a reasoning layer. It does not ship a scraper.

| Layer | Status |
|---|---|
| Reasoning methodology and references | included |
| Evidence schema, validator, tests, synthetic example | included |
| Browser automation (`browser-use` / `browser-harness`) | optional, detected at runtime |
| Vault-backed authentication (`browser_vault_*`, Hermes-only) | optional, detected at runtime |
| Direct HTTP / web search | harness-dependent |

`SKILL.md` §0 requires capability detection before any investigation. When the
browser layer or vault tools are absent, the skill records `DEGRADED` (or
`FAILED`) and continues in public-only mode. It never asserts that an
unavailable surface was observed.

A visual observation is recorded as an observation. It does not become an
identity claim.

---

## Scope and Platform Rules

- Observation is limited to public surfaces plus content the user's authorized
  session may legitimately see.
- No follow, like, comment, message, or other interaction with the target.
- No access-control bypass, credential stuffing, or impersonation.
- Rate limits and login challenges stop the surface, not the whole
  investigation: the affected surface is recorded as `RATE_LIMITED`, and the
  rest of the plan continues.
- Aggressive means persistent across *allowed* surfaces. It never means
  evading detection or ignoring a block.

---

## Status

Current state:

- **Included** — investigation methodology (`SKILL.md` plus eight references),
  a JSON Schema for the evidence bundle, a dependency-free validator with 15
  semantic tests, and a synthetic end-to-end example.
- **Optional** — the browser-access layer. It requires `browser-use` /
  `browser-harness`, a Chromium-family browser, and (for authenticated
  surfaces) a user-provided test account. Vault tooling is specific to the
  Hermes harness and is treated as an optional capability, not a prerequisite.
- **Not included** — a bundled Instagram client, a calibrated probability
  model, and an automated report renderer. Scores are prioritization aids, not
  probabilities.

Real evidence (`temp/`, `evidence/`) is gitignored on purpose: reports contain
third-party personal data and screenshots. Publish sanitized or synthetic
material only.

---

## Requirements

- Python 3.10+ for `scripts/validate_bundle.py` (stdlib only)
- `jsonschema` for full schema validation (optional)
- `browser-use`, `browser-harness`, and Chromium for the optional browser layer
- No network access is required to validate bundles or run the tests

---

## Disclaimer

INSTOSINT is intended for research, learning, and authorized public-information investigations. It should respect platform rules, privacy boundaries, and applicable laws. Publicly observable information should not automatically be treated as proof of private identity, motives, relationships, or other sensitive attributes. Prefer uncertainty and transparent evidence trails over confident speculation.
