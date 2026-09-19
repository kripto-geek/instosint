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
    ├── graph-model.md
    └── suggestion-surface-analysis.md
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

## Architecture

```text
Instagram Data Access Layer
  ├── Direct HTTP (raw fetches, web search)
  └── Browser Automation (optional, authorized test-account session)
        ↓
  INSTOSINT
    → Evidence Graph
      → Investigation Report
```

INSTOSINT is the reasoning layer. It operates only on publicly observable or otherwise authorized data. Browser automation is an optional data-access layer for observing JS-rendered public surfaces; it is not an access-control bypass.

---

## Status

INSTOSINT contains the investigation methodology, supporting reference documentation, and an optional browser-access layer. The next engineering step is connecting the reasoning layer to a reliable, authorized Instagram data source so every observation is backed by actual retrieved data.

---

## Disclaimer

INSTOSINT is intended for research, learning, and authorized public-information investigations. It should respect platform rules, privacy boundaries, and applicable laws. Publicly observable information should not automatically be treated as proof of private identity, motives, relationships, or other sensitive attributes. Prefer uncertainty and transparent evidence trails over confident speculation.
