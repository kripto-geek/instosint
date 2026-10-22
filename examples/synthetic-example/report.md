# [SYNTHETIC EXAMPLE] INSTOSINT Investigation Report

> **Everything in this file is fictional.** Handles, counts, timestamps, and
> observations were invented to exercise the report structure and the evidence
> bundle at `bundle.json`. No real account is described. Placeholder-style
> values are permitted here only because this example is marked synthetic
> (`references/evidence-model.md` §15).

- **Target**: `@demo.target` (fictional, user ID 000000000)
- **Investigation ID**: `INV-SYNTHETIC-001`
- **Window**: 2026-01-15T10:00Z – 2026-01-15T10:22Z
- **Mode**: FULL — dedicated observer session `instosint-demo.target`
- **Setup**: READY · **Auth**: AUTHENTICATED (observer test account)
- **Interaction policy**: observe only. No follows, likes, comments, or messages.
- **Final state**: STOPPED_BUDGET (profile API returned HTTP 429)

---

## 1. Investigation Summary

The target is a private account showing 12 posts, 40 followers, and 35 following.
Its own posts and connection lists were not observable. The profile-page
suggestion block was observed twice (40 seconds apart) and produced four leads;
one lead (`@demo.lead_b`) was independently corroborated by a direct public
follow edge. Two sweeps is weak recurrence evidence and is treated as such.
Entity resolution against two near-identical handles returned by search remains
unresolved.

---

## 2. Data Availability

| Surface | Status | Notes |
|---|---|---|
| Target profile header | OBSERVED | `SRC-001`, `OBS-001` |
| Target posts | NOT_AVAILABLE | private account |
| Target follower list | NOT_AVAILABLE | `UNK-001` |
| Target following list | NOT_AVAILABLE | `UNK-002` |
| Profile-page suggestion block | OBSERVED | two sweeps, `SRC-002` / `SRC-003` |
| `web_profile_info` API | RATE_LIMITED | HTTP 429, `UNK-003` |
| Handle search | OBSERVED | `SRC-006` |
| Accounts you may know | NOT_OBSERVED | deprioritized, `UNK-004` |

Unavailable surfaces are unknown, not empty. In particular, no claim is made
that the target follows nobody or has no other connections.

---

## 3. Key Observations

| ID | Observation | Type | Reliability | Group |
|---|---|---|---|---|
| OBS-001 | Profile shows 12 posts, 40 followers, 35 following, private notice. | DIRECT | HIGH | PROFILE-HEADER |
| OBS-002 | `@demo.lead_a` at position 1, mutual count 4, sweep A. | SUGGESTION | MODERATE | SWEEP-A |
| OBS-003 | `@demo.lead_b` at position 2, mutual count not visible, sweep A. | SUGGESTION | MODERATE | SWEEP-A |
| OBS-004 | `@demo.lead_c` at position 3, mutual count 1, sweep A. | SUGGESTION | MODERATE | SWEEP-A |
| OBS-005 | `@demo.lead_d` at position 4, mutual count 0, sweep A. | SUGGESTION | MODERATE | SWEEP-A |
| OBS-006–008 | Same three leads recur in sweep B. | SUGGESTION | MODERATE | SWEEP-B |
| OBS-009–011 | Leads A, B, C appear in 2 of 2 sweeps. | DERIVED | MODERATE | SWEEP-COMPARISON |
| OBS-012 | `@demo.target` appears in `@demo.lead_a`'s suggestion block, position 1. | SUGGESTION | MODERATE | LEAD-A-SURFACE |
| OBS-014 | `@demo.target` appears in `@demo.lead_b`'s public followers list. | DIRECT | HIGH | LEAD-B-FOLLOWERS |
| OBS-015 | `@demo.lead_b` appears in `@demo.lead_a`'s suggestion block, position 3. | SUGGESTION | MODERATE | LEAD-A-SURFACE |
| OBS-017 | Search returns two near-identical handles; identity unconfirmed. | DIRECT | MODERATE | SEARCH-NEAR-MISS |
| OBS-018 | `web_profile_info` returned HTTP 429. | DATA_AVAILABILITY | HIGH | API-RATE-LIMIT |

Sweeps A and B were taken 40 seconds apart in one session. They are recorded
under separate independence groups, but the investigation does **not** treat
them as independent confirmation of a stable recommendation; a multi-session
spacing of hours was not performed because of the rate-limit guardrail.

---

## 4. Derived Relationships

| ID | Subject | Relationship | Object | Evidence | Strength |
|---|---|---|---|---|---|
| REL-001 | `@demo.target` | FOLLOWS | `@demo.lead_b` | OBS-014 | STRONG |
| REL-002 | `@demo.target` | SUGGESTED | `@demo.lead_a` | OBS-002, OBS-006 | MODERATE |
| REL-003 | `@demo.target` | SUGGESTED | `@demo.lead_b` | OBS-003, OBS-007 | MODERATE |
| REL-004 | `@demo.target` | SUGGESTED | `@demo.lead_c` | OBS-004, OBS-008 | MODERATE |
| REL-005 | `@demo.target` | SUGGESTED | `@demo.lead_d` | OBS-005 | WEAK |
| REL-006 | `@demo.lead_a` | SUGGESTED | `@demo.target` | OBS-012 | MODERATE |
| REL-007 | `@demo.target` | BIDIRECTIONAL_SUGGESTION | `@demo.lead_a` | OBS-013 | MODERATE |
| REL-008 | `@demo.lead_b` | NETWORK_OVERLAP | `@demo.lead_a` | OBS-015, OBS-016 | WEAK |

`SUGGESTED` means the account appeared in a recommendation surface. It does not
mean follow, mutual connection, or known relationship.

---

## 5. Hypotheses

| ID | Statement | Status | Confidence | Supporting | Contradicting |
|---|---|---|---|---|---|
| HYP-001 | The target has a recurring, publicly observable association with `@demo.lead_b`. | INVESTIGATING | MODERATE | OBS-003, OBS-007, OBS-010, OBS-014, OBS-016 | — |
| HYP-002 | A near-identical handle from search is the same real-world entity as the target. | POSSIBLE | LOW | OBS-017 | — |
| HYP-003 | `@demo.lead_d` belongs to the same suggestion cluster as leads A–C. | UNRESOLVED | LOW | OBS-005 | — |

### Alternative explanations

- **HYP-001**: shared school/community cohort rather than a personal association;
  shared audience overlap rather than a direct link.
- **HYP-002**: handle collision between unrelated accounts; fan or impersonation
  account reusing the base handle.
- **HYP-003**: single-sweep appearance may be positional noise.

---

## 6. Supporting and Contradicting Evidence

**Supporting HYP-001**

- `OBS-014` — verified public follow edge (independent surface, HIGH reliability).
- `OBS-003` / `OBS-007` — recurring suggestion exposure.
- `OBS-016` — `@demo.lead_b` also appears in `@demo.lead_a`'s suggestion set,
  consistent with a shared cluster rather than an isolated pairing.

**Contradicting HYP-001**

- None observed. Absence of contradicting evidence is not confirmation, and no
  search for contradicting evidence beyond the surfaces above was possible
  within budget.

**Supporting HYP-002**

- `OBS-017` — near-identical handle. This is similarity, not identity
  (`references/evidence-model.md` §26).

**Contradicting HYP-002**

- None observed; the search surface does not expose enough to distinguish a
  collision from a true match.

---

## 7. High-Value Leads

| ID | Account | Score breakdown (R/M/P/MS/B/C) | Total | Quality | Investigated |
|---|---|---|---|---|---|
| LEAD-001 | `@demo.lead_a` | 2 / 2 / 3 / 2 / 1 / 3 | 13 | HIGH_VALUE | yes |
| LEAD-002 | `@demo.lead_b` | 2 / 1 / 3 / 2 / 0 / 3 | 11 | HIGH_VALUE | yes |
| LEAD-003 | `@demo.lead_c` | 2 / 1 / 3 / 1 / 0 / 0 | 7 | STRONG | yes |
| LEAD-004 | `@demo.lead_d` | 1 / 1 / 2 / 1 / 0 / 0 | 5 | MODERATE | yes |

`LEAD-004` falls below the threshold of 6 and was investigated only because no
higher-value work remained in budget. Scores are prioritization aids, not proof.

---

## 8. Unknown / Unavailable Data

| ID | Surface | Status | Reason |
|---|---|---|---|
| UNK-001 | target followers | NOT_AVAILABLE | private account |
| UNK-002 | target following | NOT_AVAILABLE | private account |
| UNK-003 | `web_profile_info` external URL | RATE_LIMITED | HTTP 429 |
| UNK-004 | Accounts you may know | NOT_OBSERVED | deprioritized |

---

## 9. Conclusion

**CON-001 — PARTIALLY_SUPPORTED, MODERATE confidence.** A publicly observable
association between `@demo.target` and `@demo.lead_b` is supported by one
independent direct observation (public follow edge) plus recurring suggestion
exposure. The nature of that association remains unknown.

**CON-002 — UNRESOLVED, LOW confidence.** Entity resolution against the
near-identical handle is not established.

**CON-003 — UNRESOLVED, LOW confidence.** Cluster membership of `@demo.lead_d`
is not established.

No claim is made about the target's real-world identity, private relationships,
location, or motives.

---

## 10. Limitations

- Two suggestion sweeps 40 seconds apart are weak recurrence evidence.
- Mutual-connection counts were not visible for `@demo.lead_b`.
- The profile API was rate-limited, so the external URL and any linked identity
  signals were unavailable.
- No multi-session spacing was attempted, by design, to respect rate limits.
- This is a synthetic exercise; none of the observations correspond to a real
  account.

---

## 11. Traceability

```text
CON-001 (PARTIALLY_SUPPORTED)
  ↓ HYP-001 (INVESTIGATING)
  ↓ REL-001, REL-003, REL-007
  ↓ OBS-014, OBS-003/007, OBS-013
  ↓ SRC-005, SRC-002/003, SRC-004
```

Machine-readable form: `bundle.json` in this directory. Every ID above resolves
against it, and `scripts/validate_bundle.py` checks that the chain cannot be
broken silently.
