# Investigation Output

## 1. Purpose

The investigator must produce an output that allows another person to understand:

* what was actually observed
* what was derived from those observations
* what relationships were discovered
* which hypotheses were considered
* what evidence supports or contradicts them
* what remains unknown
* how confident the investigator should be

The output must never hide uncertainty behind a confident narrative.

---

# 2. Investigation Summary

Begin with a short summary.

```text
Investigation target:
[Instagram username]

Investigation scope:
Publicly observable Instagram information

Current status:
[Exploring / Partially resolved / No strong leads / Completed]

Main finding:
[Short evidence-based summary]
```

Do not state an interpretation as fact unless the available evidence supports it.

---

# 3. Observations

List important observations separately from interpretations.

Format:

```text
OBS-001
Source: Target profile
Observation: Target follows Account A.
Type: DIRECT_OBSERVATION
Reliability: HIGH
```

Another example:

```text
OBS-002
Source: Target post
Observation: Account A is visibly present in the post.
Type: VISUAL_OBSERVATION
Reliability: HIGH
```

Another:

```text
OBS-003
Source: Recommendation surface
Observation: Account B was shown as a recommended account.
Type: DIRECT_OBSERVATION
Reliability: MEDIUM
```

Observations should describe **what was seen**, not what it supposedly means.

---

# 4. Derived Relationships

After observations, list relationships derived directly from them.

Example:

```text
REL-001

Subject: Target
Relationship: INTERACTS_WITH
Object: Account A

Supporting observations:
OBS-001
OBS-004
OBS-007

Strength: MODERATE
```

Possible relationship types include:

```text
FOLLOWS
INTERACTS_WITH
MENTIONS
TAGGED_WITH
APPEARS_WITH
SHARES_CONTEXT_WITH
SHARES_NETWORK_WITH
POSSIBLE_ALIAS
POSSIBLE_SAME_ENTITY
POSSIBLE_ASSOCIATION
```

Do not use a stronger relationship type than the evidence justifies.

---

# 5. Evidence Table

Important evidence should be summarized in a structured table.

| ID      | Subject | Object    | Relationship         | Evidence                       | Strength |
| ------- | ------- | --------- | -------------------- | ------------------------------ | -------- |
| OBS-001 | Target  | Account A | FOLLOWS              | Visible following relationship | Strong   |
| OBS-002 | Target  | Account A | APPEARS_WITH         | Both visible in post           | Strong   |
| OBS-003 | Target  | Account B | POSSIBLE_ASSOCIATION | Recommendation                 | Weak     |

The table is a summary, not a replacement for the underlying evidence.

---

# 6. Hypotheses

List hypotheses separately.

Format:

```text
HYP-001

Hypothesis:
Target and Account A have a recurring association.

Status:
INVESTIGATING

Supporting evidence:
OBS-001
OBS-002
OBS-006

Contradicting evidence:
OBS-010

Confidence:
MODERATE

Reason:
Multiple independent observations indicate repeated interaction,
but the available evidence does not establish the nature of the association.
```

---

# 7. Hypothesis Status

Use one of:

```text
POSSIBLE
INVESTIGATING
SUPPORTED
STRONGLY_SUPPORTED
CONTRADICTED
UNRESOLVED
```

Definitions:

### POSSIBLE

There is some evidence compatible with the hypothesis, but very little support.

### INVESTIGATING

The hypothesis is plausible and additional evidence is being examined.

### SUPPORTED

Multiple useful observations support the hypothesis.

### STRONGLY_SUPPORTED

Multiple independent and reliable observations support the hypothesis and major alternatives have been weakened.

### CONTRADICTED

Important evidence conflicts with the hypothesis.

### UNRESOLVED

The available evidence cannot distinguish the hypothesis reliably.

---

# 8. Confidence Language

Use qualitative confidence.

Preferred:

```text
Low confidence
Moderate confidence
High confidence
Very high confidence
```

Do not invent percentages such as:

```text
87% probability
93.5% likely
```

unless the system has a properly calibrated statistical model.

Confidence must describe the **evidence**, not the investigator's intuition.

---

# 9. Alternative Explanations

For important hypotheses, explicitly list alternatives.

Example:

```text
Primary hypothesis:
Target and Account A have a recurring association.

Alternative 1:
They belong to the same community.

Alternative 2:
They are ordinary acquaintances.

Alternative 3:
The observed interactions are mostly incidental.

Alternative 4:
Some observed accounts may belong to different people with similar identities.
```

Then explain which observations distinguish these alternatives.

---

# 10. Contradictory Evidence

Never hide evidence that conflicts with the leading hypothesis.

Format:

```text
CONTRADICTION

Hypothesis:
Target and Account A frequently interact.

Evidence:
Account A appears in one context only and there are no other visible
interactions across the examined surfaces.

Effect:
Reduces confidence in the hypothesis.
```

Contradictions should be included even when they make the final conclusion less interesting.

---

# 11. Entity Resolution

When two accounts may represent the same entity:

```text
ENTITY-001

Account A:
@account_a

Account B:
@account_b

Relationship:
POSSIBLE_SAME_ENTITY

Supporting evidence:
- Similar public username
- Similar public profile information
- Consistent public context

Confidence:
Low / Moderate / High
```

Never silently merge accounts.

The final report should make uncertain identity matching visible.

---

# 12. Evidence Graph

For complex investigations, represent the important graph.

Example:

```text
                    ┌──────────────┐
                    │   Account A  │
                    └──────┬───────┘
                           │
                       interacts
                           │
                           ▼
┌──────────┐          ┌──────────┐
│  Target  │─────────▶│Location X│
└────┬─────┘  appears  └────┬─────┘
     │                       │
     │ follows               │ shared
     ▼                       ▼
┌──────────┐            ┌──────────┐
│Account B │            │  Event Y │
└──────────┘            └──────────┘
```

Every important edge should be traceable to evidence.

---

# 13. Investigation Path

Show how important discoveries were reached.

Example:

```text
Target
  ↓
Following surface
  ↓
Account A discovered
  ↓
Account A investigated
  ↓
Recurring interaction discovered
  ↓
Location X discovered
  ↓
Additional accounts discovered
```

This helps distinguish deliberate investigation from accidental discovery.

---

# 14. Next Best Leads

If the investigation is not finished, list the most useful next leads.

Example:

```text
NEXT LEADS

1. Account A
   Reason:
   Multiple independent interactions with Target.

2. Location X
   Reason:
   Appears repeatedly across different posts.

3. Account B
   Reason:
   Bridge between two otherwise separate networks.
```

Do not recommend a lead merely because it is interesting.

Explain **why investigating it could change the current conclusion**.

---

# 15. Dead Ends

Record useful failed investigations.

Example:

```text
DEAD END

Candidate:
Account C

Reason abandoned:
Only shared connection was a large public account.
No additional interaction or contextual evidence found.
```

This prevents the investigator from repeatedly exploring the same weak branch.

---

# 16. Unknowns

Clearly state what cannot currently be determined.

Example:

```text
UNKNOWN

- Nature of the relationship between Target and Account A
- Whether two visually similar accounts represent the same person
- Why Account B appeared in recommendations
- Whether two posts occurred at the same event
```

Unknown information must remain unknown.

Do not fill gaps using assumptions.

---

# 17. Final Conclusion

The conclusion should have three parts.

### What is established

Facts supported directly by evidence.

### What is supported but uncertain

Reasonable interpretations supported by multiple observations.

### What cannot be established

Claims for which sufficient evidence does not exist.

Example:

```text
ESTABLISHED

Target and Account A have multiple observable interactions.

SUPPORTED BUT UNCERTAIN

The accounts appear to have a recurring association.

CANNOT BE ESTABLISHED

The available public evidence does not establish the exact nature
of that association.
```

---

# 18. Evidence Quality Summary

End with:

```text
Evidence quality:
[Low / Moderate / High]

Independent evidence sources:
[Number or qualitative description]

Major limitations:
[List]

Major contradictions:
[List]

Unresolved questions:
[List]
```

---

# 19. Do Not Overclaim

Avoid conclusions such as:

```text
"They are definitely friends."

"They are definitely dating."

"This account definitely belongs to X."

"Instagram recommended this person because they know each other."
```

unless the evidence directly establishes the claim.

Prefer:

```text
"The accounts show repeated interaction."

"The available evidence is consistent with a recurring association."

"The accounts may represent the same entity, but this is not established."

"The recommendation is a lead, not proof of a connection."
```

---

# 20. Evidence Traceability

Every significant conclusion must be traceable.

Use:

```text
Conclusion
    ↓
Hypothesis
    ↓
Relationships
    ↓
Observations
```

Example:

```text
Conclusion:
Recurring association is supported.

        ↓

HYP-001

        ↓

REL-001
REL-004
REL-007

        ↓

OBS-001
OBS-004
OBS-008
OBS-012
```

If a conclusion cannot be traced back to observations, downgrade or remove it.

---

# 21. Core Output Principle

The final report should make it possible for another investigator to reproduce the reasoning.

A good report answers:

```text
What did we see?
        ↓
What relationships can be directly established?
        ↓
What hypotheses were considered?
        ↓
What evidence supports them?
        ↓
What evidence contradicts them?
        ↓
What remains uncertain?
        ↓
What should be investigated next?
```

The investigator should optimize for:

```text
TRACEABILITY
+
EVIDENCE QUALITY
+
UNCERTAINTY
+
REPRODUCIBILITY
```

not for a dramatic or definitive-sounding conclusion.
