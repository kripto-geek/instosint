# INSTOSINT Evidence Model

This document defines the canonical evidence model used by INSTOSINT.

All other INSTOSINT reference documents should follow these definitions.

The evidence model exists to prevent:

- fabricated observations
- unsupported graph relationships
- accidental overclaiming
- double-counting evidence
- premature conclusions
- identity overreach
- confusion between observation and inference

---

# 1. Fundamental Rule

> Evidence must originate from an actually retrieved source.

No source:

```text
→ No observation.
```

No observation:

```text
→ No derived relationship.
```

No supporting evidence:

```text
→ No evidence-backed hypothesis.
```

The agent must never fill missing information with assumptions.

---

# 2. Evidence Pipeline

INSTOSINT uses the following pipeline:

```text
SOURCE
  ↓
OBSERVATION
  ↓
DERIVED RELATIONSHIP
  ↓
INFERENCE
  ↓
HYPOTHESIS
  ↓
SUPPORTED / CONTRADICTED / UNRESOLVED
  ↓
CONCLUSION
```

Each level has a different meaning.

Do not collapse multiple levels into one.

---

# 3. Source

A source is the actual data origin from which an observation was obtained.

Examples:

- public Instagram profile
- public Instagram post
- public Instagram comment
- public follower surface
- public following surface
- public tagged-post surface
- public recommendation surface
- publicly available image
- other authorized Instagram data source

A source must represent something the agent actually accessed.

A hypothetical source does not count.

---

# 4. Source Record

Conceptually, a source record may contain:

```text
SOURCE-001

type:
    instagram_profile

target:
    @example

retrieved_at:
    timestamp if available

access_status:
    AVAILABLE

data:
    actual retrieved data
```

The exact storage format may vary by implementation.

The important requirement is that observations can be traced back to their source.

---

# 5. Observation

An observation is a statement directly supported by retrieved source data.

Examples:

```text
@target publicly follows @account_x.

@target has a public post containing a visible location tag.

@target commented on a public post by @account_x.

@account_x and @target appear together in a public image.
```

Observations must describe what was observed, not what it supposedly means.

---

# 6. Observation Requirements

Every factual observation should contain:

- id
- source
- subject
- object/property
- observation
- type
- reliability

When useful, also include:

- timestamp
- source location
- independence group
- notes
- related evidence IDs

Example:

```text
ID:
    OBS-001

Source:
    SOURCE-001

Subject:
    @target

Relationship:
    FOLLOWS

Object:
    @account_x

Observation:
    @target publicly follows @account_x.

Type:
    DIRECT_OBSERVATION

Reliability:
    HIGH
```

---

# 7. Evidence Types

Use the following canonical evidence types.

## DIRECT_OBSERVATION

Information directly visible in the retrieved source.

Example:

```text
A profile's visible following list contains @account_x.
```

## DERIVED_OBSERVATION

Information calculated or constructed from multiple direct observations.

Example:

```text
@target and @account_x share several publicly visible followers.
```

The underlying follower observations must exist.

## VISUAL_OBSERVATION

A factual observation obtained from an image.

Example:

```text
@target appears in a public image together with another visible person.
```

Do not automatically infer identity or relationship from this observation.

## TEXTUAL_OBSERVATION

A factual observation derived from visible text.

Example:

```text
A public caption contains the name of Event X.
```

The text must actually be present in the retrieved source.

## INFERENCE

An interpretation derived from one or more observations.

Example:

```text
@target and @account_x show a recurring public interaction pattern.
```

Inference is not direct observation.

## HYPOTHESIS

A possible explanation that is currently being investigated.

Example:

```text
@account_x may represent a particularly relevant recurring
connection for @target.
```

A hypothesis must not be presented as established fact.

## DATA_AVAILABILITY

A record describing whether required data was available.

Example:

```text
The public following surface could not be retrieved.
```

This is not evidence that the following relationship does not exist.

## SUGGESTION_OBSERVATION

A factual observation from a suggestion surface.

Example:

```text
@suggested_account appeared in position 2 of the profile-page
suggestion block for @target, with mutual count = 12.
```

## RECURRING_SUGGESTION_SIGNAL

A derived observation indicating that the same account appeared in multiple suggestion observations.

Example:

```text
@suggested_account appeared in 3 of 4 observations of @target's
suggestion block.
```

## BIDIRECTIONAL_SUGGESTION_SIGNAL

A derived observation indicating that @target appears in @suggested_account's suggestion context and vice versa (when observable).

Example:

```text
@target appeared in @suggested_account's profile-page suggestion block,
and @suggested_account appeared in @target's profile-page suggestion block.
```

## SHARED_SUGGESTION_FINGERPRINT

A derived observation indicating overlap between suggestion sets of two or more targets.

Example:

```text
Target A and Target B share 2 accounts in their suggestion sets
out of 8 total unique accounts.
```

## COMMUNITY_CANDIDATE

A derived observation indicating that an account appears across many targets' suggestion sets, suggesting possible shared network membership.

Example:

```text
@account_x appeared in suggestion sets for 4 of 5 investigated targets.
```

All suggestion evidence types carry MODERATE reliability at most until independent public corroboration is found.

---

# 8. Evidence Status

Evidence records may have statuses such as:

- OBSERVED
- DERIVED
- INFERRED
- HYPOTHETICAL
- CONTRADICTED
- UNRESOLVED

These describe the epistemic status of the record.

---

# 9. Reliability

Reliability describes how trustworthy the underlying observation is.

Use:

- LOW
- MODERATE
- HIGH
- UNKNOWN

Reliability is NOT the same thing as hypothesis confidence.

For example:

```text
A visible public follow relationship
```

may have:

```text
Reliability: HIGH
```

while the hypothesis:

```text
"This account is especially important to the target"
```

may still have:

```text
Confidence: LOW
```

---

# 10. Relationship Strength

Relationship strength describes the support for a graph relationship.

Use:

- UNKNOWN
- WEAK
- MODERATE
- STRONG

Strength should consider:

- directness
- source quality
- corroboration
- recurrence
- specificity
- independence
- contradictions

Do not assign strength merely because the relationship sounds plausible.

---

# 11. Evidence Independence

Evidence independence is critical.

Multiple observations can originate from the same underlying event.

Example:

```text
Target appears in five photographs from Event X.
```

These five observations may all represent:

```text
ONE_EVENT_CONTEXT
```

rather than five independent confirmations.

Similarly:

```text
Target likes ten posts from Account A.
```

This is useful evidence of recurring interaction, but the ten likes should not automatically be treated as ten independent confirmations of every hypothesis involving Account A.

---

# 12. Independence Groups

When evidence is strongly correlated, assign an independence group.

Example:

```text
OBS-021
OBS-022
OBS-023
```

all originate from:

```text
EVENT-X
```

Therefore:

```text
independence_group: EVENT-X
```

Another group might be:

```text
INTERACTION-PATTERN-ACCOUNT-A
```

The investigation should avoid artificially increasing confidence by counting correlated observations multiple times.

---

# 13. Corroboration

Strong conclusions should preferably have evidence from different categories.

For example:

```text
public follow
    +
repeated interaction
    +
shared event
    +
recurring visual context
```

is generally more informative than:

```text
many likes
```

alone.

Cross-category corroboration is valuable because it reduces dependence on one type of signal.

---

# 14. Evidence IDs

Every actual evidence record receives a unique identifier.

Recommended format:

```text
OBS-001
OBS-002
OBS-003
```

for observations.

Other prefixes may be used for other record types:

```text
REL-001
HYP-001
LEAD-001
SRC-001
```

Do not create IDs for evidence that does not exist.

Do not pre-populate fake observations merely to make a table look complete.

---

# 15. No Placeholder Values

The following are forbidden as factual values:

- Account A
- Account B
- Account C
- Person X
- Event X
- [Number]
- [username]
- [bio text]
- [display name]

unless the surrounding section is explicitly marked:

```text
[SYNTHETIC EXAMPLE]
```

For real investigation output, missing values must be represented as:

```text
UNKNOWN
```

or:

```text
UNKNOWN — DATA NOT AVAILABLE
```

---

# 16. Evidence Provenance

Every evidence record should answer:

- Where did this come from?
- What exactly was observed?
- When was it observed?
- What entity does it concern?
- What relationship/property does it establish?
- How reliable is it?

If these questions cannot be answered, the claim should not be treated as verified evidence.

---

# 17. Evidence Object

A conceptual evidence object:

```text
{
    id,
    source,
    subject,
    object,
    relationship,
    observation,
    type,
    reliability,
    independence_group,
    timestamp,
    notes
}
```

Not every field must be populated for every evidence type.

However:

- id
- source
- observation
- type

should normally be present for factual observations.

---

# 18. Direct Observation vs Inference

Consider:

```text
Source:
Public Instagram post.

Observation:
@target and @account_x appear together in the image.
```

This is a:

```text
VISUAL_OBSERVATION
```

Possible inference:

```text
The two accounts have a public association.
```

This is:

```text
INFERENCE
```

Possible hypothesis:

```text
Their recurring public association may indicate a meaningful
connection.
```

This is:

```text
HYPOTHESIS
```

Do not report the hypothesis as though it were the observation.

---

# 19. Relationship Evidence

Graph relationships must reference evidence.

Example:

```text
REL-001

Subject:
    @target

Relationship:
    FOLLOWS

Object:
    @account_x

Strength:
    STRONG

Supporting evidence:
    OBS-001
```

The graph edge should not exist independently of its supporting evidence unless explicitly marked as hypothetical.

---

# 20. Hypothesis Evidence

A hypothesis should contain:

- id
- statement
- status
- supporting evidence
- contradicting evidence
- alternative explanations
- notes

Example:

```text
HYP-001

Statement:
    @target and @account_x have a recurring public association.

Status:
    INVESTIGATING

Supporting:
    OBS-001
    OBS-008
    OBS-014

Contradicting:
    OBS-021

Alternatives:
    Shared event/community may explain the observed pattern.
```

---

# 21. Hypothesis Status

Use the following lifecycle:

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

Alternative terminal states:

```text
CONTRADICTED
UNRESOLVED
```

A hypothesis should not become SUPPORTED merely because multiple similar observations exist.

---

# 22. Supporting Evidence

Evidence supports a hypothesis when it makes the hypothesis more plausible than it was before.

Supporting evidence should be evaluated for:

- directness
- reliability
- independence
- specificity
- consistency
- alternative explanations

---

# 23. Contradicting Evidence

Evidence is contradictory when it makes the hypothesis less plausible.

Examples:

- evidence suggesting a different explanation
- evidence showing an apparent association was isolated
- evidence showing the visual match is likely incorrect
- evidence showing the connection exists only within a common event
- evidence inconsistent with the proposed interpretation

Contradictory evidence must remain visible in the final reasoning.

Do not silently discard it.

---

# 24. Alternative Explanations

When evidence supports multiple interpretations, record alternatives.

Example:

```text
Observation:
Two accounts repeatedly appear at Event X.

Possible explanations:

H1:
They have a recurring personal association.

H2:
They belong to the same public community.

H3:
They repeatedly attend the same event series.
```

The investigation should seek evidence that distinguishes these hypotheses.

---

# 25. Information Gain

Evidence should be evaluated not only by strength but also by usefulness.

An observation can be true but low-value.

For example:

```text
Another like from Account A
```

may provide little new information if many similar likes already exist.

A new independent observation that distinguishes competing hypotheses may be significantly more valuable.

The investigation should prioritize evidence that reduces uncertainty.

---

# 26. Entity Resolution

Entity resolution concerns whether two observed entities may represent the same real-world entity.

Possible relationship:

```text
POSSIBLE_SAME_ENTITY
```

This should remain uncertain until adequately supported.

Potential signals:

- consistent public identity information
- recurring public context
- shared public links
- recurring visual context
- compatible publicly observable activity
- independent corroboration

Weak similarity alone does not establish identity.

---

# 27. Entity Resolution States

Possible states:

- UNKNOWN
- POSSIBLE
- LIKELY
- RESOLVED
- CONTRADICTED
- UNRESOLVED

"RESOLVED" should only be used when the available evidence justifies treating the entities as the same for the investigation.

---

# 28. Visual Evidence

Visual evidence should contain a distinction between:

```text
WHAT IS VISIBLE
```

and:

```text
WHAT IT MAY MEAN
```

Example:

```text
Visual observation:
The same visually distinctive person appears in two public posts.

Possible inference:
The person may be a recurring participant in the target's public
activity.

Identity claim:
"This is definitely Person X."

The final claim requires additional evidence.
```

---

# 29. Images and Sensitive Conclusions

Images should not be used alone to establish sensitive personal claims.

Do not infer with certainty from appearance alone:

- private identity
- sensitive personal characteristics
- private relationships
- motives
- private activities
- exact home location

Visual observations should remain grounded in what is actually visible.

---

# 30. Recommendation Evidence

Recommendation observations should have their own provenance.

Example:

```text
OBS-030

Source:
    Recommendation surface

Subject:
    @target

Object:
    @account_x

Relationship:
    RECOMMENDED_WITH

Observation:
    @account_x appeared in the recommendation context observed
    while investigating @target.

Type:
    DIRECT_OBSERVATION

Reliability:
    MODERATE
```

The interpretation must remain limited.

```text
Recommendation:
    ≠ follow
    ≠ mutual connection
    ≠ known relationship
    ≠ proof of association
```

---

# 31. Unknown Data

If data cannot be retrieved:

```text
DATA_AVAILABILITY
```

should be used where appropriate.

Example:

```text
DATA-001

Source:
    Following surface

Status:
    UNAVAILABLE

Observation:
    The following list could not be retrieved from the available
    authorized source.
```

This must NOT become:

```text
"Target does not follow Account X."
```

The correct state is:

```text
UNKNOWN
```

---

# 32. Missing Evidence

Missing evidence should never be silently converted into negative evidence.

Bad:

```text
No public interaction was retrieved,
therefore the accounts do not interact.
```

Good:

```text
No public interaction was identified in the available retrieved
data.
```

Better:

```text
No public interaction was identified in the retrieved data;
this does not establish that no interaction exists.
```

---

# 33. Evidence Quality

Evidence quality should consider:

- Source reliability
- Directness
- Specificity
- Independence
- Recurrence
- Corroboration
- Temporal relevance
- Contradiction

A useful conceptual model is:

```text
Evidence Quality
    =
Source Quality
    +
Directness
    +
Independence
    +
Specificity
    +
Corroboration
    -
Contradiction
    -
Ambiguity
```

This is a reasoning framework, not a mathematical scoring formula.

Do not invent numerical probabilities unless the system has a properly calibrated statistical model.

---

# 34. Confidence Language

Use qualitative confidence:

- LOW
- MODERATE
- HIGH
- VERY HIGH

Avoid invented percentages such as:

```text
87% likely
```

unless the system has a validated basis for calculating that probability.

Prefer:

```text
"Moderate confidence"
```

over:

```text
"73% confidence"
```

when no calibrated probability model exists.

---

# 35. Evidence Ledger

The evidence ledger should allow the investigator to answer:

- What did we observe?
- Where did we observe it?
- What relationship did it create?
- Which hypotheses does it support?
- Which hypotheses does it contradict?
- Is the evidence independent?

Conceptual structure:

```text
| ID | Source | Subject | Object | Type | Reliability | Status |
|----|--------|---------|--------|------|-------------|--------|
```

The ledger should contain actual evidence only.

---

# 36. Evidence Graph

The evidence graph is a structured representation of:

- entities
- relationships
- evidence
- hypotheses
- uncertainty

Example:

```text
@target
   |
   | FOLLOWS
   | supported by OBS-001
   v
@account_x
   |
   | APPEARS_AT
   | supported by OBS-014
   v
Event X
```

The graph is not itself proof of the interpretation.

---

# 37. Graph Evidence vs Graph Inference

These are different.

Graph evidence:

```text
Target → FOLLOWS → Account X
```

Graph inference:

```text
Target and Account X may have a recurring public association.
```

The second must reference evidence supporting the first and any additional observations required.

---

# 38. Contradiction Handling

If new evidence contradicts an existing claim:

1. Do not delete the old evidence.
2. Record the contradictory evidence.
3. Update the hypothesis state.
4. Re-evaluate alternative explanations.
5. Update the graph status where appropriate.
6. Preserve the investigation history.

Evidence should be append-only conceptually.

The interpretation can change.

The historical observation should remain traceable.

---

# 39. Evidence Revision

If an earlier observation is discovered to be incorrect:

```text
mark it as corrected/invalidated
```

Do not silently rewrite history.

Example:

```text
OBS-014

Status:
    INVALIDATED

Reason:
    Original image was incorrectly associated with the target.
```

Any relationship or hypothesis depending exclusively on OBS-014 must then be reassessed.

---

# 40. Stop Conditions

Evidence collection should stop when:

- major hypotheses are sufficiently resolved
- remaining leads have low information value
- available data is exhausted
- further investigation is repetitive
- investigation budget is exhausted
- the remaining uncertainty cannot be reduced using available sources

Stopping is preferable to generating speculative conclusions.

---

# 41. Final Evidence Rule

The final report must always distinguish:

- OBSERVED
- DERIVED
- INFERRED
- HYPOTHESIZED
- SUPPORTED
- CONTRADICTED
- UNKNOWN

The investigator must never present one category as another.

The fundamental rule is:

> If the source was not actually observed, it is not evidence.

And:

> If the evidence does not establish the conclusion, the conclusion remains unresolved.
