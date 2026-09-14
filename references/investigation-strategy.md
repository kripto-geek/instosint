# INSTOSINT Investigation Strategy

This document defines how INSTOSINT decides what to investigate next.

---

# 1. Objective

The objective is not to collect the maximum amount of Instagram data.

The objective is to find the strongest useful explanation supported by publicly observable evidence.

---

# 2. Investigation States

```text
INITIALIZED
DATA_COLLECTION
OBSERVATIONS_AVAILABLE
GRAPH_BUILDING
HYPOTHESIS_GENERATION
LEAD_SELECTION
INVESTIGATING
CONTRADICTION_CHECK
EVIDENCE_UPDATE
COMPLETED

Blocked states:

BLOCKED_NO_DATA
BLOCKED_ACCESS
INSUFFICIENT_EVIDENCE
STOPPED_LOW_VALUE
STOPPED_BUDGET
```

---

# 3. Main Loop

```text
OBSERVE
  ↓
VALIDATE SOURCE
  ↓
RECORD OBSERVATION
  ↓
CONNECT OBSERVATION
  ↓
FORM HYPOTHESES
  ↓
SELECT HIGH-VALUE LEAD
  ↓
INVESTIGATE LEAD
  ↓
SEARCH FOR SUPPORTING AND CONTRADICTING EVIDENCE
  ↓
UPDATE GRAPH
  ↓
REASSESS
  ↓
REPEAT OR STOP
```

---

# 4. Phase 1 — Initialization

Input:

```text
one Instagram account
```

Create:

- target account
- investigation state
- source registry
- observation ledger
- relationship graph
- hypothesis list
- lead queue
- investigation budget

Do not assume anything about the target beyond what is actually observed.

---

# 5. Phase 2 — Initial Observation

Inspect available public surfaces:

- profile
- followers/following
- posts
- comments
- likes
- mentions
- tags
- hashtags
- images
- visible timestamps
- locations
- linked resources
- recommendations

Do not exhaustively crawl every available object automatically.

---

# 6. Phase 3 — Observation Recording

For each useful observation record:

- what was observed
- where it was observed
- when it was observed
- source
- reliability
- independence group

Example:

```text
OBS-001
Source: SRC-001
Observation:
Target publicly follows Account B.
Reliability: HIGH
```

---

# 7. Phase 4 — Entity Extraction

Extract potentially useful entities:

- accounts
- people
- places
- events
- hashtags
- objects
- organizations
- recurring visual elements
- recurring interactions

Do not convert uncertain entities into confirmed identities.

---

# 8. Phase 5 — Relationship Discovery

Look for:

- direct interaction
- reciprocal interaction
- repeated interaction
- shared network
- shared content
- shared event
- shared location
- visual recurrence
- temporal recurrence
- cross-post references

Each relationship must be traceable to observations.

---

# 9. Phase 6 — Hypothesis Generation

A hypothesis explains one or more observations.

Example:

```text
HYP-001:
Account A and Account B may have a recurring offline association.

Possible supporting evidence:

- repeated public interactions
- repeated appearance in the same event context
- reciprocal network relationship
- recurring visual context
```

The wording should remain proportional to evidence strength.

---

# 10. Competing Hypotheses

Always consider alternatives.

Example:

```text
H1: A and B have a personal association.

H2: A and B belong to the same social/community network.

H3: A and B repeatedly interact because of a shared activity.

H4: The apparent relationship is an artifact of public platform behavior.
```

Do not investigate only evidence supporting H1.

---

# 11. Lead Selection

Every lead should have:

- lead_id
- target
- reason
- expected_information_gain
- cost
- risk_of_false_inference

Prioritize leads that:

- have high information gain
- have low cost
- are strongly connected to existing evidence
- are capable of distinguishing competing hypotheses

---

# 12. Information Gain

A lead is valuable when its result can significantly change the investigation.

High-value example:

```text
Investigate a recurring public event appearing in multiple posts.
```

Lower-value example:

```text
Collect another generic follower with no connection to the hypothesis.
```

---

# 13. Recursive Investigation

A discovered entity may become the next investigation target.

Example:

```text
Target
  ↓
recurring account
  ↓
public post
  ↓
recurring event
  ↓
other public participants
  ↓
shared visual context
```

Every hop must have a reason.

Record:

- parent entity
- new entity
- reason for traversal
- expected information gain

Avoid uncontrolled graph expansion.

---

# 14. Image-Driven Investigation

Images can create leads.

Example:

```text
Image
  ↓
recognizable venue
  ↓
public event
  ↓
other public posts from event
  ↓
recurring accounts
```

Visual observations must remain separate from identity conclusions.

---

# 15. Recommendation-Driven Investigation

Recommendations can generate leads.

Example:

```text
Target
  ↓
recommended account
  ↓
inspect observable network overlap
  ↓
compare independent evidence
```

Do not conclude:

```text
recommended = close relationship
```

---

# 16. Contradiction Search

For every important hypothesis ask:

```text
What evidence would make this hypothesis less likely?
```

Search for:

- contradictory timestamps
- incompatible locations
- non-reciprocal patterns
- alternative explanations
- inconsistent identities
- unrelated context
- evidence suggesting platform-driven rather than personal interaction

---

# 17. Entity Resolution

Possible identity matches should be treated probabilistically.

Useful signals:

- username similarity
- display-name similarity
- profile-image similarity
- bio similarity
- network overlap
- visual context
- temporal consistency
- cross-references

No single weak signal should establish identity.

Example:

```text
same profile picture
```

means:

```text
POSSIBLE_MATCH
```

not:

```text
CONFIRMED_SAME_PERSON
```

---

# 18. Evidence Independence

Do not double-count evidence.

Example:

```text
Post caption says X.
Screenshot of same caption says X.
Another analysis of same screenshot says X.
```

These are not three independent observations.

---

# 19. Investigation Budget

The investigation should have limits.

Possible limits:

- maximum investigation depth
- maximum inspected accounts
- maximum inspected posts
- maximum recursive hops
- maximum low-value actions
- maximum time/tool budget

If the budget is exhausted:

```text
STOPPED_BUDGET
```

Do not continue indefinitely.

---

# 20. Stop Conditions

Stop when:

- the question is sufficiently answered
- useful public leads are exhausted
- evidence remains insufficient after useful leads are exhausted
- additional investigation has low expected value
- public/authorized data is unavailable
- investigation budget is exhausted

Possible final states:

```text
COMPLETED
INSUFFICIENT_EVIDENCE
STOPPED_LOW_VALUE
STOPPED_BUDGET
BLOCKED_ACCESS
BLOCKED_NO_DATA
```

---

# 21. Confidence

Use qualitative levels:

- UNKNOWN
- WEAK
- MODERATE
- STRONG

Confidence should reflect evidence quality, not the model's intuition.

---

# 22. Sensitive Conclusions

Do not infer sensitive personal characteristics or private relationships from weak signals.

Especially avoid presenting:

- dating
- romantic relationship
- sexual relationship
- family relationship
- private identity

as established merely from:

- likes
- follows
- comments
- visual similarity
- recommendations
- shared location

If such a hypothesis is relevant, keep it explicitly unresolved unless sufficiently supported by appropriate public evidence.

---

# 23. Final Decision

The investigator must distinguish:

- OBSERVED
- DERIVED
- INFERRED
- HYPOTHETICAL
- SUPPORTED
- CONTRADICTED
- UNKNOWN

Never collapse these categories into one.

---

# 24. Core Principle

The next action should be chosen because it can change what we know.

NOT:

```text
"Explore everything."
```

BUT:

```text
"What is the most useful unanswered question right now?"
```
