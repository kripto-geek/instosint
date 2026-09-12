# Instagram OSINT — Evidence Model

This document defines how the investigation agent should represent observations, relationships, hypotheses, confidence, and contradictions.

The purpose of this model is to prevent the agent from turning weak clues into confident claims.

---

# 1. Fundamental Rule

Separate:

```text
WHAT WAS OBSERVED
        ↓
WHAT WAS DERIVED
        ↓
WHAT IS INFERRED
        ↓
WHAT IS HYPOTHESIZED
        ↓
WHAT IS SUPPORTED
```

Never collapse these categories.

An investigation should be explainable backward:

```text
Conclusion
    ↓
Supporting hypothesis
    ↓
Evidence
    ↓
Original observation
```

If the agent cannot explain why it believes something, the conclusion should not be considered reliable.

---

# 2. Evidence Object

Represent every meaningful observation conceptually as:

```text
Evidence
├── id
├── source
├── subject
├── object
├── relationship
├── observation
├── timestamp
├── evidence_type
├── reliability
├── independence_group
└── notes
```

Example:

```text
subject: @lily
object: @hv

relationship: follows

observation:
"Lily's publicly observable following list contains @hv."

evidence_type:
DIRECT_OBSERVATION

reliability:
HIGH
```

The exact storage implementation may vary.

The conceptual distinction must remain.

---

# 3. Evidence Types

Use the following categories.

## DIRECT_OBSERVATION

Something directly visible.

Examples:

* Account A follows Account B.
* Account A mentions Account B.
* Account B appears in a public post.
* A recommendation visibly displays Account B.
* A location is explicitly displayed.

This is the strongest type for establishing that an observable event occurred.

---

## DERIVED_OBSERVATION

A fact calculated from direct observations.

Examples:

* A and B share 12 followers.
* Account X is a bridge between two clusters.
* Person Y appears in 5 investigated posts.
* Account A and B have repeated interaction.

Derived observations should preserve the observations from which they were calculated.

---

## VISUAL_OBSERVATION

Information extracted from an image.

Examples:

* Two people appear together.
* A sign contains a visible name.
* A recognizable building appears.
* A particular object appears repeatedly.
* Two images have similar visual context.

Visual observations should describe what is visible before interpreting what it means.

Bad:

```text
"This is definitely Harshvardhan."
```

Better:

```text
"A person with visually similar characteristics appears in both images."
```

---

## TEXTUAL_OBSERVATION

Information extracted from:

* bio
* caption
* comment
* visible image text
* username
* display name
* hashtag
* mention

The agent should preserve the original context where possible.

---

## INFERENCE

A conclusion derived from one or more observations.

Example:

```text
Observation:
A and B repeatedly interact.

Inference:
A and B have a recurring public interaction pattern.
```

An inference is not automatically a fact.

---

## HYPOTHESIS

A possible explanation for observed evidence.

Example:

```text
Hypothesis:
A and B may belong to the same social group.
```

Hypotheses must remain explicitly labeled.

---

# 4. Relationship Strength

Do not use a single universal confidence score for every relationship.

Instead consider the nature of the relationship.

Useful qualitative levels:

### OBSERVED

The relationship itself is directly visible.

Example:

```text
A follows B
```

### WEAK

There is limited supporting evidence.

Example:

```text
A and B share a small number of connections.
```

### MODERATE

Multiple relevant observations support the relationship.

Example:

```text
A follows B
A repeatedly interacts with B
A and B appear in related public content
```

### STRONG

Multiple relatively independent observations support the same interpretation.

Example:

```text
Explicit interaction
+
Repeated co-occurrence
+
Shared event
+
Additional independent contextual evidence
```

### UNKNOWN

There is insufficient evidence to determine the relationship.

---

# 5. Do Not Treat Confidence as Probability

Unless the system has been statistically calibrated using a suitable dataset, avoid statements such as:

```text
87% chance they are friends.
```

A number can create false precision.

Prefer:

```text
Evidence strength: Moderate
```

or:

```text
Confidence: Low
```

If numerical scoring is eventually implemented, it must be clearly described as an internal prioritization score rather than a literal probability.

---

# 6. Evidence Independence

This is critical.

Multiple observations may originate from the same underlying event.

Example:

```text
A likes B's post
A comments on B's post
A replies to B's comment
```

These may represent one interaction episode rather than three independent pieces of evidence.

Therefore maintain an:

```text
independence_group
```

Example:

```text
Evidence 1 → Event_42
Evidence 2 → Event_42
Evidence 3 → Event_42
```

The agent should avoid treating these as three completely independent confirmations.

---

# 7. Corroboration

Corroboration means different observations support the same hypothesis.

Strong corroboration generally comes from different evidence categories.

Example:

```text
NETWORK
A follows B

CONTENT
A and B appear in related public posts

TEMPORAL
Both appear at the same public event

VISUAL
Recurring contextual similarity
```

This is generally more useful than repeatedly observing the same type of interaction.

---

# 8. Contradictory Evidence

Every important hypothesis must allow contradictory evidence.

Represent:

```text
Hypothesis
├── supporting evidence
└── contradicting evidence
```

Example:

```text
Hypothesis:
Account A and Account B may represent the same entity.

Supporting:
- similar alias
- similar public profile information
- overlapping network

Contradicting:
- incompatible public location
- different age/context information
- independent evidence connecting each account to different entities
```

The final assessment must consider both sides.

---

# 9. Entity Resolution

When multiple accounts may represent the same person/entity, do not immediately merge them.

Create a candidate relationship:

```text
ACCOUNT_A
    |
    | possible_same_entity
    ↓
ACCOUNT_B
```

Then collect evidence.

Potential evidence categories:

* username similarity
* display-name similarity
* alias similarity
* profile-image similarity
* bio/context similarity
* social-graph overlap
* recurring visual context
* explicit public linkage
* temporal consistency
* contradictory evidence

---

# 10. Entity Resolution Example

Suppose:

```text
@hv
display name: HV
```

and another candidate:

```text
@harshvardhanm
display name: Harshvardhan Mishra
```

Possible observations:

```text
O1:
"HV" is compatible with the candidate's name.

O2:
The public profile imagery appears visually consistent.

O3:
The two accounts share several relevant connections.

O4:
The target interacts with both.

O5:
There is contradictory information suggesting different entities.
```

The agent should conclude something like:

```text
Possible same-entity relationship.

Evidence:
- alias compatibility
- network overlap
- contextual consistency

Counter-evidence:
- none currently observed

Assessment:
Moderate support

Further useful investigation:
Look for explicit public linkage or additional independent context.
```

It must NOT automatically state:

```text
@hv = Harshvardhan Mishra
```

unless sufficiently strong evidence exists.

---

# 11. Relationship Classification

Different relationships require different evidence.

Possible relationship categories include:

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

Avoid inventing stronger semantic relationships from weaker observations.

For example:

```text
A follows B
```

does not automatically become:

```text
A is B's friend
```

Similarly:

```text
A and B appear in the same image
```

does not automatically become:

```text
A and B are romantically involved
```

---

# 12. Hypothesis Lifecycle

A hypothesis should move through explicit stages.

```text
UNPROPOSED
    ↓
POSSIBLE
    ↓
INVESTIGATING
    ↓
SUPPORTED
    ↓
STRONGLY_SUPPORTED
```

It may also move to:

```text
CONTRADICTED
```

or:

```text
UNRESOLVED
```

Example:

```text
Possible:
"Account B may be meaningfully connected to Target."

↓

Investigating:
Collect network, interaction, content and visual evidence.

↓

Supported:
Multiple independent observations support the relationship.

↓

Strongly supported:
Additional independent evidence confirms the same pattern.
```

Do not skip directly from POSSIBLE to STRONGLY_SUPPORTED.

---

# 13. Alternative Hypotheses

For important observations, consider multiple explanations.

Example:

```text
Observation:
Account B repeatedly appears in recommendations around Target.
```

Possible explanations:

```text
H1:
Meaningful network overlap.

H2:
Shared broader community.

H3:
Shared interaction signals.

H4:
Recommendation algorithm behavior unrelated to a meaningful relationship.

H5:
Coincidental recommendation.
```

The agent should seek observations that distinguish these possibilities.

This prevents confirmation bias.

---

# 14. Information Gain

When choosing the next investigation step, prefer actions that could distinguish between competing hypotheses.

Example:

```text
H1:
A and B belong to the same community.

H2:
A and B are unrelated.

Useful next evidence:
Look for independent public community/event connections.
```

A low-value action would be:

```text
Check the same weak signal repeatedly.
```

A high-value action would be:

```text
Find a different evidence category that could support or contradict H1.
```

---

# 15. Evidence Graph

Conceptually maintain:

```text
                    ┌───────────────┐
                    │   Target A    │
                    └───────┬───────┘
                            │
                         follows
                            │
                            ▼
                    ┌───────────────┐
                    │   Account B   │
                    └───────┬───────┘
                            │
                      appears_with
                            │
                            ▼
                    ┌───────────────┐
                    │   Account C   │
                    └───────────────┘
```

Every edge should have evidence attached.

Example:

```text
Target A
   |
   | follows
   | evidence: E001
   ↓
Account B
```

The graph should distinguish:

```text
OBSERVED EDGE
```

from:

```text
INFERRED EDGE
```

---

# 16. Evidence Ledger

Maintain an evidence ledger for important investigations.

Example:

```text
E001
Observation:
Target follows Account B.

Type:
DIRECT_OBSERVATION

Strength:
High for the fact that the follow exists.

Meaning:
Limited.

---

E002
Observation:
Target repeatedly comments on Account B's public posts.

Type:
DIRECT_OBSERVATION

Strength:
Moderate.

Meaning:
Recurring public interaction.

---

E003
Observation:
Account B and Target appear in the same public event context.

Type:
VISUAL_OBSERVATION

Strength:
Moderate.

Meaning:
Possible shared event/context.

---

H001
Hypothesis:
Target and B have a meaningful social association.

Supporting:
E001
E002
E003

Contradicting:
None currently observed.

Assessment:
Moderate support.
```

This ledger makes the investigation auditable.

---

# 17. Stop Conditions

Do not investigate indefinitely.

Stop or pause when:

* additional evidence is repetitive
* new observations provide little information
* the remaining uncertainty cannot be resolved from observable information
* the investigation begins relying primarily on speculation
* the evidence graph has stabilized
* a hypothesis has sufficient evidence for the intended objective

Report remaining uncertainty.

---

# 18. Final Rule

The strongest investigation is not the one that produces the most relationships.

It is the one that produces the most **well-supported relationships while clearly separating observation from interpretation**.

