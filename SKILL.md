---
name: instosint
description: Instagram-focused public-data investigation skill. Use when investigating publicly observable Instagram accounts, connections, interactions, recurring entities, visual context, and relationship hypotheses. Builds a traceable evidence graph, recursively investigates high-value leads, and clearly separates observations from hypotheses and conclusions.
---

# INSTOSINT

INSTOSINT is an Instagram-focused investigation methodology for agents.

Its purpose is to investigate publicly observable Instagram information,
build a traceable evidence graph, discover meaningful connections, generate
and test hypotheses, and determine what investigation step is most useful
next.

INSTOSINT is a reasoning and investigation framework.

It is NOT an Instagram access mechanism.

The agent must only reason over data that it has actually retrieved through
an available authorized/public data source.

---

# 1. Core Objective

Given a target Instagram account, investigate relevant publicly observable
information and construct an evidence-backed explanation of the meaningful
relationships and patterns discovered around that account.

The objective is NOT:

- collecting as much data as possible
- crawling every account
- generating a large report
- finding a predetermined relationship
- confirming the investigator's initial suspicion
- producing a conclusion at any cost

The objective IS:

> Build the strongest defensible explanation supported by the available
> evidence while explicitly preserving uncertainty.

The investigation should answer:

1. What was actually observed?
2. What relationships can be derived from those observations?
3. What hypotheses could explain those relationships?
4. What evidence supports or contradicts each hypothesis?
5. What should be investigated next?
6. What can and cannot be established?

---

# 2. Non-Negotiable Evidence Rule

## NEVER FABRICATE EVIDENCE

The agent MUST NOT invent, assume, simulate, or template an Instagram
observation as if it were real.

An observation may only be recorded when its underlying source data was
actually retrieved.

Never fabricate:

- usernames
- accounts
- followers
- following relationships
- mutual followers
- likes
- comments
- mentions
- tags
- captions
- bios
- display names
- profile information
- recommendations
- posts
- images
- image contents
- locations
- events
- timestamps
- linked accounts
- relationships
- identities
- interaction counts

Never convert a template into a factual finding.

BAD:

    Target follows Account A.

when no following data was retrieved.

BAD:

    Account B appeared in recommendations.

when no recommendation data was retrieved.

BAD:

    Target and Account C have 12 mutual followers.

when no follower data was retrieved or calculated.

BAD:

    Target appears with Account D.

when no image or tagged-post evidence supports this.

---

# 3. No Placeholder Evidence

The following MUST NEVER appear as factual investigation entities:

    Account A
    Account B
    Account C
    Person X
    Event X
    [Number]
    [username]
    [display name]
    [bio text]
    [location]

These may only be used inside explicitly marked synthetic examples.

When required information is unavailable, use:

    UNKNOWN — DATA NOT AVAILABLE

or an equivalent explicit data-availability statement.

Unknown information must remain unknown.

Do NOT replace missing information with a plausible-looking value.

---

# 4. Data Availability Gate

Before creating any observation, the agent MUST establish:

1. What source contains the information?
2. Was that source actually accessed?
3. What exact information was retrieved?
4. Can the observation be traced to the retrieved source?

If the answer to any of these is no, the observation MUST NOT be created.

The investigation should instead record a data limitation when useful.

Example:

    STATUS: BLOCKED_NO_DATA

    Target: @example

    The required Instagram surface was not available through the
    current authorized data source.

    Observations: 0
    Relationships: 0
    Hypotheses: 0

This is a valid investigation result.

---

# 5. Instagram Access Boundary

INSTOSINT does not bypass Instagram privacy or security controls.

Do NOT:

- bypass private-account restrictions
- circumvent authentication
- defeat access controls
- obtain restricted content
- access private information
- use stolen credentials
- attempt to reveal deleted/private content through unauthorized means
- treat unavailable information as available

If the required information cannot be accessed through the available
authorized/public data source, report the limitation.

The absence of retrieved data does NOT prove that the underlying
relationship or information does not exist.

---

# 6. Investigation Loop

The canonical investigation loop is:

```text
    OBSERVE
       ↓
    VALIDATE SOURCE
       ↓
    RECORD
       ↓
    CONNECT
       ↓
    FORM HYPOTHESES
       ↓
    SELECT HIGH-VALUE LEAD
       ↓
    INVESTIGATE
       ↓
    CHALLENGE
       ↓
    UPDATE GRAPH
       ↓
    REASSESS
       ↓
    REPEAT OR STOP
```

Every loop iteration must be grounded in actual available evidence.

---

# 7. Investigation State

At all times, the agent should conceptually know the current state:

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

Possible blocked/terminal states:

    BLOCKED_NO_DATA
    BLOCKED_ACCESS
    INSUFFICIENT_EVIDENCE
    STOPPED_LOW_VALUE
    STOPPED_BUDGET
    COMPLETED

Do not claim an investigation is complete merely because a report was
generated.

---

# 8. Target Initialization

When an investigation begins:

1. Create the target account node.
2. Record only information actually retrieved.
3. Record the source for each observation.
4. Identify available Instagram surfaces.
5. Identify potentially useful investigation leads.
6. Do not generate conclusions yet.

Example:

    Target
      |
      +-- profile
      +-- posts
      +-- followers
      +-- following
      +-- interactions
      +-- tags
      +-- mentions
      +-- images

Only surfaces that are actually available should be considered observed.

---

# 9. Instagram Investigation Surfaces

Relevant public/authorized surfaces may include:

## Profile

- username
- display name
- bio
- profile picture
- publicly visible links
- account metadata that is actually available

## Network

- followers
- following
- mutual connections
- recurring accounts
- bridge accounts

## Content

- posts
- captions
- comments
- visible likes
- mentions
- tags
- tagged content
- hashtags

## Visual Content

- people appearing in images
- recurring people
- locations
- venues
- events
- visible text
- objects
- logos
- recurring environments
- other contextual visual information

## Temporal Information

- posting dates
- repeated activity periods
- recurring event periods
- interaction timing

## Recommendation Surface

Recommendations may be recorded when actually observed.

They are leads, not proof of a relationship.

## Linked Information

Only publicly visible and actually retrieved linked accounts or references
should be recorded.

---

# 10. Observation First

The agent must separate what is observed from what it means.

Example:

    OBSERVATION:
    Target publicly follows @account_x.

    DERIVED RELATIONSHIP:
    Target → FOLLOWS → @account_x.

    INFERENCE:
    The two accounts have a public network connection.

    HYPOTHESIS:
    @account_x may be relevant to the investigation.

Do not skip directly from observation to conclusion.

---

# 11. Evidence Hierarchy

Use the following conceptual hierarchy:

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

These levels MUST NOT be treated as interchangeable.

A hypothesis is not an observation.

An inference is not proof.

A graph edge is not automatically a conclusion.

---

# 12. Evidence Provenance

Every factual observation must have provenance.

At minimum, track:

- evidence ID
- source
- subject
- object/property
- observation
- evidence type
- reliability
- timestamp when available
- notes
- independence group when relevant

Example:

    OBS-014

    Source:
        Instagram following surface

    Subject:
        @target

    Relationship:
        FOLLOWS

    Object:
        @actual_account

    Observation:
        @target publicly follows @actual_account.

    Type:
        DIRECT_OBSERVATION

    Reliability:
        HIGH

This observation can then support a graph relationship.

---

# 13. Evidence IDs

Evidence IDs must correspond to real evidence.

Do NOT pre-generate:

    OBS-001
    OBS-002
    OBS-003

unless those observations actually exist.

Each evidence record must be traceable to a retrieved source.

If no source exists:

    No evidence record.

---

# 14. Derived Relationships

A relationship may be derived from one or more observations.

Example:

    Observation:
    Target follows @account_x.

    Relationship:

    Target
       |
       | FOLLOWS
       v
    @account_x

The relationship should reference the observation(s) supporting it.

Do not create unsupported graph edges merely because they appear
plausible.

---

# 15. Evidence Strength

Strength describes the evidence for a particular claim or relationship.

Use:

    UNKNOWN
    WEAK
    MODERATE
    STRONG

Do not assign STRONG merely because several observations exist.

Consider:

- directness
- source reliability
- independence
- recurrence
- specificity
- corroboration
- contradictory evidence

Repeated observations from the same underlying event should not be
counted as independent evidence.

---

# 16. Images Are First-Class Evidence

Images must be investigated when they are relevant and actually available.

Possible visual observations include:

- a person appearing in an image
- repeated appearance of a person
- shared event context
- shared location context
- visible text
- recurring venue
- recurring object
- recurring visual environment

The process should be:

```text
    IMAGE
      ↓
    VISUAL OBSERVATION
      ↓
    CONTEXTUAL RELATIONSHIP
      ↓
    HYPOTHESIS
```

Never:

```text
    IMAGE
      ↓
    ASSUMED IDENTITY
      ↓
    CERTAIN RELATIONSHIP
```

Images alone should not establish sensitive personal conclusions.

A visual similarity should remain a possible match until independently
supported.

---

# 17. Entity Resolution

When two accounts or entities may represent the same person/entity:

    POSSIBLE_SAME_ENTITY

may be created as a hypothesis or uncertain relationship.

Do NOT automatically merge them.

Potential supporting signals may include:

- consistent public identity information
- recurring public context
- shared public links
- repeated contextual association
- visual consistency
- other independent evidence

Weak username or profile-picture similarity alone is insufficient.

---

# 18. Recommendations

Recommendation surfaces can produce useful leads.

Example:

    Target
       |
       +---- Recommended with ----> Account X

This means:

    "Account X was observed in a recommendation context."

It does NOT mean:

    "Target knows Account X."

It does NOT mean:

    "Target follows Account X."

It does NOT establish a personal relationship.

Recommendation evidence should generally begin as WEAK evidence and
require independent corroboration before becoming important.

---

# 19. Recursive Investigation

INSTOSINT is recursive.

If a useful relationship is discovered:

    Target → Account A

and Account A reveals:

    Account A → Event X

then Event X may become the next investigation target.

Example:

    Target
       |
       v
    Account A
       |
       v
    Event X
       |
       +---- Account B
       +---- Account C

Do not automatically investigate B and C.

Ask:

    Which lead is most useful for resolving the current uncertainty?

Every recursive hop must have a reason.

Record that reason.

Example:

    LEAD:
    Investigate Event X.

    REASON:
    Event X independently connects Target and Account A and may
    distinguish a recurring association from a one-time interaction.

---

# 20. Lead Prioritization

Rank possible next actions using factors such as:

- relevance
- evidence strength
- novelty
- discriminating power
- source reliability
- recurrence
- graph connectivity
- ability to test a hypothesis
- expected information gain
- investigation cost

Prefer:

    "This action can distinguish H1 from H2."

over:

    "This account looks interesting."

---

# 21. Information Gain

The best next action is usually the one that reduces the most uncertainty.

Suppose:

    H1:
    Target and Account A have a recurring association.

    H2:
    Their connection is explained by a shared event/community.

If investigating another post from the same event cannot distinguish H1
from H2, it may have low information value.

If investigating Account A's independent public interactions outside that
event can distinguish them, it may have higher information value.

The agent should prefer the latter.

---

# 22. Competing Hypotheses

Do not investigate only one explanation.

When meaningful ambiguity exists, maintain alternatives.

Example:

    H1:
    Target and Account A have a recurring public association.

    H2:
    Their observed connection is primarily due to a shared community.

    H3:
    The observed connection is mostly incidental.

The exact wording depends on the evidence.

The point is to avoid confirmation bias.

---

# 23. Contradiction Search

For important hypotheses, actively seek contradictory evidence.

Ask:

- What would make this hypothesis weaker?
- Is there an alternative explanation?
- Is expected evidence missing?
- Is there evidence pointing elsewhere?
- Is the apparent pattern explained by a common event?
- Could the visual match be coincidental?
- Could recommendation behavior explain the apparent connection?

A hypothesis should not become stronger merely because supporting
evidence was repeatedly collected.

---

# 24. Evidence Independence

Do not double-count correlated evidence.

Example:

    Target liked Post 1.
    Target liked Post 2.
    Target liked Post 3.
    Target liked Post 4.

These may represent a recurring interaction pattern.

They should not automatically be treated as four independent confirmations
of a hypothesis.

Likewise:

    Target appears in five photos from the same event.

This may represent one underlying event rather than five independent
relationship signals.

Seek evidence from different categories when possible.

---

# 25. Graph Construction

Build a graph from verified observations.

Possible nodes:

- Account
- Person
- Post
- Image
- Location
- Event
- Hashtag
- Textual Entity

Possible relationships:

- FOLLOWS
- FOLLOWED_BY
- LIKES
- COMMENTS_ON
- INTERACTS_WITH
- MENTIONS
- TAGGED_WITH
- APPEARS_WITH
- SHARES_CONTEXT_WITH
- SHARES_NETWORK_WITH
- USES_HASHTAG
- POSTED_BY
- LOCATED_AT
- ASSOCIATED_WITH_EVENT
- POSSIBLE_ALIAS
- POSSIBLE_SAME_ENTITY
- POSSIBLE_ASSOCIATION
- RECOMMENDED_WITH

Every meaningful edge must have supporting evidence.

---

# 26. Graph Is Not Conclusion

The graph represents known and inferred relationships.

It does not automatically determine their meaning.

Example:

    Target
      |
      | APPEARS_WITH
      v
    Account A

does not automatically mean:

    Target and Account A have a particular personal relationship.

The graph records the observable connection.

Interpretation belongs to the hypothesis layer.

---

# 27. Investigation Budget

Recursive investigation must have practical limits.

Avoid:

- unlimited graph expansion
- exhaustive follower crawling
- investigating every recommendation
- repeatedly investigating the same evidence
- following weak leads indefinitely

Stop or deprioritize branches when:

- expected information gain is low
- evidence is repetitive
- the branch is unrelated to current hypotheses
- the evidence becomes increasingly speculative
- available data is exhausted
- investigation budget is exhausted

The objective is:

    useful evidence > data volume

---

# 28. Unknowns

The agent must explicitly maintain unknown information.

Examples:

    Follower relationship:
    UNKNOWN — DATA NOT AVAILABLE

    Identity match:
    UNRESOLVED

    Hypothesis:
    INSUFFICIENT_EVIDENCE

Unknown is not false.

Unobserved is not disproven.

---

# 29. Final Report Requirements

A final investigation should contain, when applicable:

    Investigation Summary

    Data Availability

    Observations

    Derived Relationships

    Evidence Table

    Hypotheses

    Supporting Evidence

    Contradictory Evidence

    Alternative Explanations

    Entity Resolution

    Evidence Graph

    Investigation Path

    Next Best Leads

    Dead Ends

    Unknowns

    Final Conclusion

The report must distinguish:

### Established

Directly supported by available evidence.

### Supported but Uncertain

Supported by meaningful evidence but still interpretive.

### Unresolved

Insufficient evidence to determine.

### Contradicted

Evidence currently weighs against the hypothesis.

---

# 30. Final Conclusion Rules

Never produce a conclusion merely because the report format expects one.

If evidence is insufficient, say so.

Good:

    The available public evidence establishes that the two accounts
    interact and share multiple public contexts. The available data
    does not establish the nature of their private relationship.

Bad:

    They are definitely close friends.

when that conclusion is not directly supported.

---

# 31. Traceability Requirement

Every meaningful final claim must be traceable:

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

If a claim cannot be traced through this chain, downgrade it, remove it,
or explicitly label it as speculation.

---

# 32. Failure Handling

If Instagram data is unavailable:

    Do not fabricate.

If only partial data is available:

    Investigate only within the available evidence.

If a source is unreliable:

    Record the reliability limitation.

If identity cannot be resolved:

    Keep entities separate.

If hypotheses conflict:

    Preserve both and investigate discriminating evidence.

If no useful next lead exists:

    Stop.

If the evidence does not support a conclusion:

    Report that conclusion cannot be established.

---

# 33. Synthetic Examples

Examples in documentation are NOT real observations.

Synthetic examples must be explicitly marked:

    [SYNTHETIC EXAMPLE]

Example:

    [SYNTHETIC EXAMPLE]

    Target: @synthetic_target

    Target follows @synthetic_account.

This example must never be interpreted as data retrieved from Instagram.

---

# 34. Canonical Reference Files

INSTOSINT uses the following reference modules:

    references/instagram-surfaces.md
        Instagram investigation surfaces

    references/evidence-model.md
        Evidence definitions and provenance

    references/investigation-strategy.md
        Lead selection and investigation strategy

    references/investigation-output.md
        Final report structure

    references/image-analysis.md
        Image and visual evidence methodology

    references/graph-model.md
        Graph nodes, edges and traversal

Future state-management rules may be defined in:

    references/investigation-state.md

The canonical definition of evidence belongs in:

    references/evidence-model.md

Do not create conflicting evidence definitions in other files.

---

# 35. Core Principle

INSTOSINT should behave like a careful investigator, not a report
generator.

The agent must prefer:

    verified observation
        over
    plausible assumption

    useful investigation
        over
    exhaustive crawling

    competing hypotheses
        over
    confirmation bias

    uncertainty
        over
    false certainty

    traceability
        over
    impressive-looking reports

    "unknown"
        over
    fabricated evidence

The final objective is:

    PUBLIC/AUTHORIZED DATA
            +
    VERIFIED OBSERVATIONS
            +
    TRACEABLE EVIDENCE
            +
    GRAPH RELATIONSHIPS
            +
    HYPOTHESIS TESTING
            +
    CONTRADICTION SEARCH
            +
    INFORMATION-GUIDED INVESTIGATION
            =
    DEFENSIBLE CONCLUSION