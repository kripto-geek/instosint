---
name: instosint
description: Instagram-focused public-data investigation skill. Investigates publicly observable Instagram accounts, including private-account surrounding signals such as recommendations, mutuals, public network context, interactions, recurring entities, and visual context. Builds a traceable evidence graph, recursively investigates high-value leads, and separates observations from hypotheses and conclusions.
---

# INSTOSINT

INSTOSINT is an Instagram-focused public-data investigation methodology.

It is an investigation and reasoning system, not an access-control bypass mechanism.

The goal is to discover and explain publicly observable connections around an Instagram target, including targets whose own profile content is private or otherwise inaccessible.

---

# 1. Core Principle

INSTOSINT must never fabricate evidence.

If information was not actually observed through an available authorized/public data source:

```text
IT IS NOT EVIDENCE.
```

Unknown information must remain unknown.

However:

```text
TARGET DATA UNAVAILABLE
```

does NOT automatically mean:

```text
INVESTIGATION IMPOSSIBLE
```

A target may have a private profile while Instagram still exposes publicly observable surrounding signals.

## 2. Private Target ≠ No Investigation

A private Instagram account may expose limited direct information while still producing observable platform context.

Examples may include:

- profile metadata
- publicly visible account information
- recommendation surfaces
- mutual connections
- suggested accounts
- accounts surfaced around the target
- public network relationships
- publicly observable interactions involving other accounts

The investigator must distinguish:

```text
TARGET'S PRIVATE CONTENT
```

from:

```text
PUBLICLY OBSERVABLE CONTEXT AROUND THE TARGET
```

The former must not be accessed or bypassed.

The latter may be investigated when genuinely observable.

## 3. Public / Authorized Scope

INSTOSINT may use:

- publicly observable Instagram data
- authorized data supplied by the user/tool
- public account information
- public posts
- public comments
- public likes when visible
- public mentions
- public tags
- public hashtags
- public recommendation/suggestion surfaces
- public network relationships
- public visual information

INSTOSINT must NOT:

- bypass private-account restrictions
- bypass authentication
- bypass access controls
- obtain private posts
- obtain private followers/following through unauthorized means
- use stolen credentials
- exploit vulnerabilities to obtain restricted data
- pretend to be another user to gain access

If the target is private, investigate only what is actually observable.

## 4. Investigation Model

The investigation follows:

```text
TARGET
  ↓
OBSERVABLE SURFACES
  ↓
OBSERVATIONS
  ↓
ENTITIES / RELATIONSHIPS
  ↓
HYPOTHESES
  ↓
HIGH-VALUE LEADS
  ↓
RECURSIVE INVESTIGATION
  ↓
CONTRADICTION CHECK
  ↓
EVIDENCE UPDATE
  ↓
CONCLUSION
```

The target does not need to be fully accessible for this process to operate.

## 5. Investigation States

Use:

```text
INITIALIZED
TARGET_SURFACE_CHECK
DATA_COLLECTION
OBSERVATIONS_AVAILABLE
GRAPH_BUILDING
HYPOTHESIS_GENERATION
LEAD_SELECTION
INVESTIGATING
CONTRADICTION_CHECK
EVIDENCE_UPDATE
COMPLETED
```

Blocked states:

```text
BLOCKED_NO_DATA
BLOCKED_ACCESS
INSUFFICIENT_EVIDENCE
STOPPED_LOW_VALUE
STOPPED_BUDGET
```

## 6. Initial Target Assessment

Before declaring an investigation blocked, determine:

- Is the target profile itself observable?
- Is the target private?
- Are recommendation/suggestion surfaces observable?
- Are mutual/public network signals observable?
- Are other public surfaces surrounding the target observable?

The investigation should continue if useful surrounding signals exist.

Example:

```text
Target profile: PRIVATE
Direct posts: NOT AVAILABLE
Recommendation surface: OBSERVED

Result: INVESTIGATION CAN CONTINUE
```

## 7. Recommendation / Suggestion Surface

Recommendation behavior is a first-class lead source.

When Instagram visibly surfaces accounts around a target, record:

- target
- suggested account
- whether mutual connections are shown
- whether the suggestion is repeated
- where the suggestion was observed
- timestamp/context if available

Example observation:

```text
OBS-001

Target:
private Instagram account

Observed surface:
Instagram suggestion UI

Observation:
Account B was publicly surfaced as a suggested account around the target.

Status:
OBSERVED
```

Do NOT record:

```text
Account B is the target's boyfriend.
```

That is an inference, not an observation.

## 8. Recommendation Signals Are Leads

A recommendation is not proof of:

- friendship
- romantic relationship
- family relationship
- offline contact
- close relationship
- identity

Treat it as:

```text
NETWORK_PROXIMITY_SIGNAL
```

or:

```text
INVESTIGATION_LEAD
```

The exact recommendation algorithm is unknown unless explicitly documented by an authoritative source.

Do not claim to know why Instagram generated a recommendation.

## 9. Non-Mutual Suggestions

Non-mutual suggested accounts can still be useful.

For example:

```text
Target
  ↓
Suggested Account B
```

even when:

```text
Target ↛ follows B
B ↛ follows Target
```

This may still justify investigating Account B as a lead if the suggestion is actually observable.

But:

```text
suggestion ≠ relationship
```

The purpose is to investigate the suggested account's public context.

## 10. Recommendation Recurrence

If the same account is repeatedly surfaced around the target, record the recurrence.

Example:

```text
OBS-001:
Account B appeared in the suggestion surface.

OBS-002:
Account B appeared again in a later observation.

OBS-003:
Account B remained associated with the same target context.
```

Derived relationship:

```text
REL-001:
Account B is a recurring recommendation lead around the target.
```

This is stronger than a single recommendation signal, but still does not establish the reason for the recommendation.

## 11. Recommendation Delta

When different observations of the same target produce different suggestion sets, record the differences.

Example:

```text
Observation A: B, C, D surfaced.
Observation B: B, C, E surfaced.

Delta:
D disappeared.
E appeared.
B and C persisted.
```

The persistent accounts may be useful leads.

Do NOT assume that persistence means closeness.

Instead:

```text
B → RECURRING_RECOMMENDATION_SIGNAL
C → RECURRING_RECOMMENDATION_SIGNAL
```

## 12. Recommendation Graph

Treat recommendations as a separate graph layer.

```text
TARGET
  │
  ├── SUGGESTED → ACCOUNT A
  ├── SUGGESTED → ACCOUNT B
  └── SUGGESTED → ACCOUNT C
```

Then investigate the public side of those accounts:

```text
ACCOUNT B
  ↓
public profile
  ↓
public network
  ↓
posts
  ↓
comments
  ↓
mentions
  ↓
tags
  ↓
images
  ↓
events
```

The purpose is to determine whether independent public evidence connects the lead back to the target context.

## 13. Lead Escalation

A recommendation lead becomes more interesting when additional independent evidence appears.

Example:

```text
Recommendation signal
        +
shared public network
        +
recurring interaction
        +
shared public event
        +
visual/contextual recurrence
```

This may justify a stronger hypothesis.

But the final conclusion must still reflect what the evidence actually establishes.

## 14. Public-Side Recursive Investigation

When a private target produces a public lead:

```text
PRIVATE TARGET
    ↓
PUBLICLY OBSERVED LEAD
    ↓
PUBLIC ACCOUNT
    ↓
PUBLIC CONTENT
    ↓
PUBLIC NETWORK
    ↓
PUBLIC ENTITIES
```

The investigator may recursively explore the public side.

The recursion must always have a reason.

Example:

```text
Account B was repeatedly surfaced around the target.
Therefore inspect B's public network and content for independent
evidence connecting B to the target's observable context.
```

## 15. Observation Before Interpretation

Always separate:

```text
OBSERVATION
```

from:

```text
INTERPRETATION
```

Example:

```text
OBSERVATION:
Account B appears in Instagram's suggestion surface around Target.

INFERENCE:
Account B may have some platform-level network proximity.

HYPOTHESIS:
Account B may be relevant to the target's broader social context.

CONCLUSION:
Unresolved until independent evidence is found.
```

## 16. Evidence Hierarchy

Use:

```text
DIRECT OBSERVATION
        ↓
DERIVED OBSERVATION
        ↓
INFERENCE
        ↓
HYPOTHESIS
        ↓
SUPPORTED HYPOTHESIS
        ↓
CONCLUSION
```

Never silently promote an inference into an observation.

## 17. Evidence Strength

Allowed levels:

```text
UNKNOWN
WEAK
MODERATE
STRONG
```

Do not assign strength merely because:

- many weak signals exist

Consider:

- source reliability
- specificity
- independence
- corroboration
- temporal consistency
- contradictions
- alternative explanations

## 18. Evidence Independence

Do not double-count related signals.

For example:

```text
Target → recommendation of B
B → recommendation of target
```

may not represent two independent underlying signals.

Similarly:

```text
same post
same screenshot
OCR of same screenshot
AI description of same image
```

should not be treated as independent evidence.

## 19. Image Evidence

Images are first-class evidence.

Inspect publicly observable images for:

- people
- places
- events
- objects
- text
- signs
- landmarks
- logos
- backgrounds
- recurring visual elements
- screenshots
- visible usernames

Image observations may generate leads.

Example:

```text
Image A contains a distinctive event setting.
Account B's public post contains the same event setting.
```

This may produce:

```text
POSSIBLE_SHARED_EVENT_CONTEXT
```

not:

```text
CONFIRMED_PERSONAL_RELATIONSHIP
```

## 20. Entity Resolution

Do not identify a person from weak similarity.

Possible signals:

- username similarity
- display-name similarity
- profile image similarity
- network overlap
- visual context
- temporal consistency
- public cross-reference

A single weak signal should produce:

```text
POSSIBLE_MATCH
```

not:

```text
CONFIRMED_IDENTITY
```

## 21. Relationship Types

Useful relationships include:

- FOLLOWS
- FOLLOWED_BY
- SUGGESTED
- RECURRING_RECOMMENDATION
- MUTUAL_CONNECTION
- LIKES
- COMMENTS_ON
- MENTIONS
- TAGS
- APPEARS_IN
- POSTED
- AUTHORED
- REFERENCES
- SHARES_EVENT_CONTEXT
- SHARES_LOCATION_CONTEXT
- SHARES_NETWORK_CONTEXT
- POSSIBLE_VISUAL_MATCH
- TEMPORAL_OVERLAP

Avoid inventing relationship types such as:

- BOYFRIEND_OF
- GIRLFRIEND_OF
- SECRET_PARTNER_OF

unless genuinely established by sufficient evidence.

## 22. Relationship Graph

The graph should distinguish recommendation edges from actual observable relationships.

Example:

```text
TARGET
  │
  ├── SUGGESTED → ACCOUNT B
  │
  └── MUTUAL_CONNECTION → ACCOUNT C
```

Then:

```text
ACCOUNT B
  ├── FOLLOWS → ACCOUNT D
  ├── COMMENTS_ON → POST E
  └── APPEARS_IN → EVENT F
```

The graph represents evidence and leads.

It is not itself proof of the final hypothesis.

## 23. Hypothesis Generation

Generate hypotheses only from actual observations.

Example:

```text
HYP-001

Statement:
Account B may have a recurring association with the target's
observable Instagram network.

Supporting evidence:
REL-001
REL-002

Contradicting evidence:
None currently observed.

Alternative:
B may simply be algorithmically connected through shared public
network/context.
```

## 24. Competing Hypotheses

Always consider alternatives.

Example:

```text
H1: B has a meaningful personal association with the target.

H2: B belongs to the same broader social/community network.

H3: B is surfaced because of shared public content/activity.

H4: The recommendation is primarily a platform recommendation artifact.
```

Investigate evidence that distinguishes these possibilities.

## 25. Contradiction Search

For every important hypothesis ask:

```text
What evidence would make this explanation less likely?
```

Search for:

- contradictory timestamps
- incompatible locations
- unrelated contexts
- lack of reciprocal interaction
- alternative event explanations
- identity inconsistencies
- network patterns inconsistent with the hypothesis

## 26. Lead Prioritization

Each lead should have:

- LEAD-ID
- target
- reason
- expected_information_gain
- cost
- confidence
- status

Prioritize leads that:

- could distinguish competing hypotheses
- have independent evidence potential
- are strongly connected to current observations
- require relatively little investigation

## 27. Investigation Budget

Do not recursively investigate everything.

Possible limits:

- maximum depth
- maximum accounts
- maximum posts
- maximum recommendation leads
- maximum recursive hops
- maximum low-value actions

Stop when additional exploration is unlikely to materially improve the result.

## 28. Stop Conditions

Stop when:

- question sufficiently answered
- useful public leads exhausted
- evidence remains insufficient
- additional investigation has low information gain
- authorized/public data is unavailable
- budget exhausted

Possible result:

```text
COMPLETED
INSUFFICIENT_EVIDENCE
STOPPED_LOW_VALUE
STOPPED_BUDGET
BLOCKED_ACCESS
BLOCKED_NO_DATA
```

## 29. Sensitive Relationship Claims

Do not confidently infer sensitive personal relationships from weak public signals.

For example:

- likes
- follows
- recommendations
- visual similarity
- shared events
- comments

do not independently establish:

- romantic relationship
- sexual relationship
- family relationship
- private identity

If such a hypothesis is investigated, clearly label it as unresolved unless sufficient appropriate evidence exists.

## 30. No Fabrication

Never invent:

- accounts
- usernames
- posts
- likes
- followers
- comments
- events
- locations
- relationships
- images
- timestamps
- recommendations

Do not use placeholders such as:

```text
Account A
Account B
Person X
Event X
[Number]
[username]
```

as factual investigation data.

These are allowed only inside explicitly marked:

```text
[SYNTHETIC EXAMPLE]
```

## 31. Data Availability

Use:

```text
OBSERVED
PARTIALLY_OBSERVED
NOT_AVAILABLE
UNKNOWN
```

For a private target:

```text
private posts = NOT_AVAILABLE
public recommendation surface = OBSERVED
public lead account = OBSERVED
```

This means investigation can continue through the public lead.

## 32. Final Report

The final report must contain:

```text
INVESTIGATION SUMMARY
TARGET ACCESS STATUS
OBSERVABLE SURFACES
KEY OBSERVATIONS
RECOMMENDATION SIGNALS
DERIVED RELATIONSHIPS
HYPOTHESES
SUPPORTING EVIDENCE
CONTRADICTING EVIDENCE
ALTERNATIVE EXPLANATIONS
HIGH-VALUE LEADS
UNKNOWN DATA
LIMITATIONS
CONCLUSION
TRACEABILITY
```

## 33. Traceability

Every conclusion must be traceable:

```text
CONCLUSION
    ↓
HYPOTHESIS
    ↓
RELATIONSHIPS
    ↓
OBSERVATIONS
    ↓
SOURCE
```

For recommendation-driven investigations:

```text
CONCLUSION
    ↓
HYPOTHESIS
    ↓
PUBLIC-SIDE RELATIONSHIPS
    ↓
PUBLIC ACCOUNT OBSERVATIONS
    ↓
RECOMMENDATION OBSERVATION
    ↓
TARGET SURFACE SOURCE
```

## 34. Example Investigation Pattern

```text
[SYNTHETIC EXAMPLE]

Target account is private.
Direct posts: NOT AVAILABLE
Recommendation surface: OBSERVED
Account B: Repeatedly surfaced around target.

↓
LEAD-001

Inspect Account B's public profile.

↓
Account B has public posts.

↓
A recurring event appears in B's posts.

↓
Another public account associated with the same event
also interacts publicly with the target's observable network.

↓
Build relationships.
Generate competing hypotheses.
Search for contradictions.
Determine whether evidence supports a recurring association.

The example demonstrates methodology only.
It is not factual evidence about any real account.
```

## 35. Core Principle

INSTOSINT should not ask only:

```text
"Can I access the target's profile?"
```

It should ask:

```text
"What publicly observable signals exist around this target,
and which of those signals can generate high-value leads?"
```

A private target may have little directly observable content while still being surrounded by useful public signals.

The investigation must exploit those signals without bypassing privacy controls.
