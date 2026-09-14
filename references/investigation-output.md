# INSTOSINT Investigation Output

The final report must distinguish observed facts from interpretation.

---

# 1. Output Structure

Use:

```text
INVESTIGATION SUMMARY
DATA AVAILABILITY
KEY OBSERVATIONS
DERIVED RELATIONSHIPS
HYPOTHESES
SUPPORTING EVIDENCE
CONTRADICTING EVIDENCE
ALTERNATIVE EXPLANATIONS
HIGH-VALUE LEADS
UNKNOWN / UNAVAILABLE DATA
CONCLUSION
TRACEABILITY
```

# 2. Investigation Summary

Include:

target
scope
investigation state
data availability
investigation depth
major limitations

Do not claim that inaccessible data was investigated.

# 3. Key Observations

Only include actual observations.

Example:

OBS-001
Target publicly follows Account B.

OBS-002
Account B appears in three publicly visible posts associated with the target.

OBS-003
The posts occur within the same publicly observable event context.

Each observation should reference its source.

# 4. Derived Relationships

Example:

REL-001
Target → FOLLOWS → Account B

Evidence:
OBS-001

Another:

REL-002
Target → SHARES_EVENT_CONTEXT → Account B

Evidence:
OBS-002
OBS-003

Do not present unsupported edges.

# 5. Hypotheses

Use:

HYP-001
Statement:
Target and Account B may have a recurring public association.

Status:
INVESTIGATING

Supporting evidence:
REL-001
REL-002

Contradicting evidence:
None currently observed.

Alternative explanations:
They may simply participate in the same public community/event.
# 6. Hypothesis Status

Allowed:

POSSIBLE
INVESTIGATING
SUPPORTED
STRONGLY_SUPPORTED
CONTRADICTED
UNRESOLVED

Use UNRESOLVED when evidence does not distinguish between plausible explanations.

# 7. Evidence Strength

Use:

UNKNOWN
WEAK
MODERATE
STRONG

Strength should reflect:

specificity
source quality
independence
corroboration
consistency
contradictions

Do not make evidence strong merely because there are many weak observations.

# 8. Alternative Explanations

Every important hypothesis should include plausible alternatives.

Example:

Primary hypothesis:
Repeated association between A and B.

Alternative:
Both participate in the same community.

Alternative:
Interactions are driven by public content rather than an offline association.
# 9. Contradicting Evidence

Explicitly record evidence that weakens a hypothesis.

Example:

HYP-001
Contradicting evidence:
OBS-017 indicates the apparently shared event occurred at a different time than initially expected.

Contradicting evidence must not be hidden.

# 10. Unknown Data

List important unanswered questions:

Followers unavailable.
Private posts unavailable.
Timestamp unavailable.
Identity unresolved.
Recommendation mechanism unknown.

Unknown is not equivalent to false.

# 11. High-Value Leads

A lead should contain:

LEAD-ID
target
reason
expected information gain
cost
status

Example:

LEAD-001
Target:
Public event referenced by multiple posts.

Reason:
Could distinguish shared-community explanation from repeated personal association.

Expected information gain:
HIGH

Status:
UNINVESTIGATED
# 12. Conclusions

Conclusions must be proportional to evidence.

Good:

Publicly observable evidence shows repeated interaction between the two accounts.
The available evidence supports a recurring association, but does not establish the nature of that association.

Bad:

They are definitely close friends.

when the evidence only shows follows and likes.

# 13. Traceability

Every conclusion should map:

```text
CONCLUSION
↓
HYPOTHESIS
↓
RELATIONSHIPS
↓
OBSERVATIONS
↓
SOURCES
```

Example:

Conclusion:
Repeated public association is supported.

↓ HYP-001

Hypothesis:
A and B may have a recurring public association.

↓ REL-001
↓ REL-002

Relationships:
A follows B.
A and B repeatedly appear in the same public event context.

↓ OBS-001
↓ OBS-002
↓ OBS-003

Observations:
Actual publicly observed Instagram data.

↓ SRC-001
↓ SRC-002
# 14. Failed Investigations

If no useful evidence was available:

STATUS: INSUFFICIENT_EVIDENCE

Explain:

what was checked
what was unavailable
why no reliable conclusion could be reached

Do not invent findings to make the report look complete.

# 15. Access Restrictions

If investigation is blocked:

STATUS: BLOCKED_ACCESS

Report the limitation.

Do not attempt to bypass it.

# 16. No-Data Rule

If a source was never actually observed:

DO NOT CREATE OBSERVATION
DO NOT CREATE RELATIONSHIP
DO NOT CREATE HYPOTHESIS BASED ON IT

Unknown data remains unknown.

# 17. Synthetic Examples

Any fictional examples must be explicitly marked:

[SYNTHETIC EXAMPLE]

Synthetic entities must never appear in an actual investigation report.

# 18. Final Principle

The report should make it possible for another investigator to ask:

"Why did you reach this conclusion?"

and trace the answer all the way back to the original observed source.