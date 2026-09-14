# INSTOSINT

Instagram-focused OSINT investigation skill for OpenCode.

INSTOSINT investigates publicly observable Instagram information, builds an evidence graph, discovers connections, and recursively pursues the most useful leads.

The goal is **reasoning over relationships**, not indiscriminate data collection.

---

## What It Does

Given a target account, the agent examines public Instagram surfaces, identifies accounts, posts, people, places, events, and interactions, connects them, generates hypotheses, and decides what to investigate next.

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

Example:

```text
Target → FOLLOWS → Account A → APPEARS_WITH → Event X
Event X → Account B
```

A connection is not automatically a conclusion. The system distinguishes:

```text
Observation → Derived relationship → Inference → Hypothesis → Supported hypothesis
```

---

## What INSTOSINT Is NOT

- A generic web search tool
- A profile scraper or follower exporter
- A private-account bypass
- A system that invents missing evidence
- A relationship-status detector

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

```
instosint/
├── SKILL.md
├── README.md
└── references/
    ├── instagram-surfaces.md
    ├── evidence-model.md
    ├── investigation-strategy.md
    ├── investigation-output.md
    ├── image-analysis.md
    └── graph-model.md
```

### Reference Files

- `instagram-surfaces.md` — surfaces that can provide useful observations
- `evidence-model.md` — evidence definitions and provenance
- `investigation-strategy.md` — lead selection and investigation strategy
- `investigation-output.md` — final report structure
- `image-analysis.md` — image and visual evidence methodology
- `graph-model.md` — graph nodes, edges, and traversal

---

## Architecture

```text
Instagram Data Access Layer
  → INSTOSINT
    → Evidence Graph
      → Investigation Report
```

INSTOSINT is the reasoning layer. It operates only on publicly observable or otherwise authorized data.

---

## Status

INSTOSINT contains the investigation methodology and supporting reference documentation. The next engineering step is connecting the reasoning layer to a reliable, authorized Instagram data source so every observation is backed by actual retrieved data.

---

## Disclaimer

INSTOSINT is intended for research, learning, and authorized public-information investigations. It should respect platform rules, privacy boundaries, and applicable laws. Publicly observable information should not automatically be treated as proof of private identity, motives, relationships, or other sensitive attributes. Prefer uncertainty and transparent evidence trails over confident speculation.
