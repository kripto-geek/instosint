---
name: instosint
description: Instagram-focused public-data investigation skill. Investigates publicly observable Instagram accounts, including private-account surrounding signals such as recommendations, mutuals, public network context, interactions, recurring entities, and visual context. Builds a traceable evidence graph, recursively investigates high-value leads, and separates observations from hypotheses and conclusions. Includes advanced suggestion-surface analysis with quantified features, fingerprinting, community detection, and weighted lead scoring.
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

## 12b. Suggestion Evidence Requirements

Every suggestion observation must record:

- target account
- suggested account
- exact surface where observed
- position in suggestion list (if available)
- mutual-connection count (if visible)
- context label text (if present)
- timestamp
- reliability

Do not record a suggestion without identifying the surface and the exact suggested account.

## 12c. Suggestion Graph Layer

Build suggestion relationships as a separate graph layer:

```text
LAYER 1: Direct relationships (FOLLOWS, LIKES, COMMENTS, MENTIONS)
LAYER 2: Suggestion relationships (SUGGESTED, RECURRING_SUGGESTION, BIDIRECTIONAL_SUGGESTION)
```

Suggestion edges carry features:
- recurrence count
- persistence ratio
- mutual count
- surfaces observed
- bidirectional flag

When a SUGGESTED edge coincides with a direct relationship edge, the combined signal is stronger than either alone.

## 12d. Suggestion Lead Scoring

Use the qualitative scoring model from `references/suggestion-surface-analysis.md` to prioritize leads.

Score components:
- recurrence (1-3 points)
- mutual count (1-3 points)
- persistence ratio (1-3 points)
- multi-surface presence (1-3 points)
- bidirectional (0-1 points)
- independent corroboration (0-4 points)

Score ranges:
- 0-3: WEAK lead
- 4-6: MODERATE lead
- 7-9: STRONG lead
- 10+: HIGH-VALUE lead

Score is a prioritization tool, not a proof of relationship.

### Scoring Calibration

- A score of 6 is the minimum threshold for substantive investigation. Leads with score 4-6 may be investigated only if no higher-score leads exist or if budget allows.
- When two leads have the same score, prefer the lead with higher corroboration count.
- When scores and corroboration are equal, prefer the lead with higher mutual-connection count.
- A lead with score 3 that has unique features (e.g., appears in a public post with the target) may be worth a single corroboration check even below threshold.
- A HIGH-VALUE lead with zero corroboration is still a stronger signal than a MODERATE lead with one corroboration — but the MODERATE lead may be faster to validate.

See Step 6 of the Suggestion Investigation Playbook (Section 12f) for community detection methodology.

## 12e. Community Detection via Suggestions

When investigating multiple private targets:
- compare suggestion sets for overlap
- identify accounts that appear across many targets' suggestion sets
- identify strongly connected suggestion clusters
- generate hypotheses about shared network membership

Community detection from suggestions produces:
```text
COMMUNITY_CANDIDATE
```

not:
```text
CONFIRMED_GROUP_MEMBERSHIP
```

## 12f. Suggestion Investigation Playbook

Use this step-by-step procedure when investigating a target with suggestion surfaces available.

### Step 1 — Initial Suggestion Sweep

1. Navigate to the target's profile page (without following, if private).
2. Observe and record the full suggestion block. For each suggested account, capture:
   - username
   - position in list
   - mutual-connection count (if shown)
   - context label (if shown)
3. Use the canonical record format:

```text
OBS-XXX

Source:
    Profile-page suggestion block for @target

Suggested account:
    @suggested_account

Position in list:
    N

Mutual-connection count:
    X (or NOT_VISIBLE)

Context label:
    exact text or NOT_VISIBLE

Surface:
    profile_page_suggestion_block

Timestamp:
    observed timestamp

Reliability:
    MODERATE
```

4. Record the full suggestion set.
5. Do not investigate yet — just record the full set.

### Step 2 — Set Analysis

1. Identify persistent accounts (appearing in multiple observations).
2. Identify transient accounts (appearing once and not again).
3. Calculate overlap if you have multiple observation sessions.
4. Flag the top 3-5 accounts by:
   - recurrence count
   - mutual count
   - persistence ratio

### Step 3 — Lead Scoring

1. For each flagged account, compute the lead score using the model in Section 12d.
2. Prioritize leads with score ≥ 7 (STRONG or HIGH-VALUE).
3. Lower-score leads may still be worth investigating if they have unique features.

### Step 4 — Deep Dive on Top Leads

For each top lead:
1. Inspect the suggested account's public profile.
2. Record public follows, posts, comments, mentions, tags.
3. Look for independent corroboration:
   - does the suggested account publicly follow or mention the target?
   - do they appear in the same public event/place?
   - do they share recurring visual context?
4. Check for bidirectional suggestion if feasible.
5. Update the lead score with corroboration points.
6. Decide: escalate to hypothesis, continue investigation, or stop.

### Step 5 — Multi-Surface Triangulation

If the same target can be observed across multiple surfaces:
1. Check "Accounts you may know" for the same target.
2. Check search suggestions for the target.
3. Compare suggestion sets across surfaces.
4. Accounts appearing on multiple surfaces get the multi-surface bonus.

### Step 6 — Community Detection (Multi-Target)

If investigating multiple private targets:
1. Collect suggestion sets for each target.
2. Compute pairwise overlap between sets.
3. Identify accounts appearing across 2+ targets' sets.
4. Build a suggestion cluster graph.
5. Generate hypotheses about shared network membership.

### Step 7 — Stop Conditions

Stop suggestion-driven investigation when:
- all top leads have been investigated
- corroboration is exhausted
- additional observations have low expected information gain
- budget is exhausted

Final state may be:
```text
COMPLETED (sufficient evidence)
INSUFFICIENT_EVIDENCE (leads exhausted without strong corroboration)
STOPPED_LOW_VALUE (remaining leads are weak)
```

## 12g. Edge Cases

### No suggestions visible

If the profile page shows no suggestion block:
1. Record: `SUGGESTION_SURFACE = NOT_AVAILABLE`
2. Do not infer that the target has no network connections.
3. Proceed to other observable surfaces: public posts, comments, tagged content, search results.
4. If no public surfaces exist, mark as `INSUFFICIENT_EVIDENCE`.

### Rate-limited or altered results

Instagram may alter suggestions based on request patterns.

If results appear inconsistent:
1. Record each observation separately with timestamp.
2. Do not merge inconsistent observations.
3. Note variability in the report.
4. Increase observation intervals.

### Suggestion block changes on reload

Instagram may show different suggestion sets on successive page reloads within the same session.

If results change between reloads:
1. Record each observation separately with timestamp.
2. Assign each observation to the same session/independence group.
3. Do not merge observations into a single "true" set.
4. Use delta analysis to identify persistent vs. transient accounts.
5. Persistent accounts are stronger leads; transient accounts may be algorithmic noise.

### Empty suggestion set

If the block is present but empty:
1. Record: `SUGGESTION_SET = EMPTY`
2. This may indicate: new account, low activity, or algorithmic suppression.
3. Proceed to other surfaces.

### Single suggestion

If only one account is suggested:
1. Record the single suggestion.
2. A single suggestion is a WEAK lead without corroboration.
3. Do not treat it as more reliable than a multi-account set.

### Fallback decision tree

When suggestion-driven investigation stalls, use this decision tree:

```text
Are there any suggestion leads with score ≥ 7?
├── YES → Investigate them first.
│   └── After investigation: is corroboration sufficient for conclusion?
│       ├── YES → COMPLETED
│       └── NO → are there remaining MODERATE leads (score 4-6)?
│           ├── YES → investigate them if budget allows
│           └── NO → pivot to other public surfaces
└── NO → pivot immediately to other public surfaces:
    ├── public posts
    ├── comments
    ├── tagged content
    ├── public mentions
    └── search results
```

After pivoting:
- If other surfaces yield useful evidence, return to suggestion leads with updated context.
- If other surfaces are also unavailable, mark as `INSUFFICIENT_EVIDENCE`.
- Do not continue investigating suggestion leads that have already been exhausted.

## 12h. "Accounts You May Know" Surface

The "Accounts you may know" surface is distinct from the profile-page suggestion block.

### Observable Features

Record the same features as profile-page suggestions:
- suggested account username
- mutual-connection count
- connection reason label
- position/order in the list

### Difference from Profile-Page Suggestions

Profile-page suggestions are directly attached to the target and may be more target-specific.

"Accounts you may know" is a broader algorithmic surface that may include the target's context but is not exclusively about the target.

Weight profile-page suggestions slightly higher in lead scoring.

### Cross-Surface Corroboration

If the same account appears in both surfaces:
- Record both observations separately.
- This counts as multi-surface presence.
- Increase the lead's multi-surface score.

## 12i. End-to-End Walkthrough

```text
[SYNTHETIC EXAMPLE]

Target: @private_target
Surface: profile-page suggestion block
Observation count: 4 (spaced 2 hours apart)

OBS-001 (Session A):
Suggestion set: [@acc_a (mutual: 12), @acc_b (mutual: 3), @acc_c (mutual: 1)]

OBS-002 (Session B):
Suggestion set: [@acc_a (mutual: 15), @acc_b (mutual: 3), @acc_d]

OBS-003 (Session C):
Suggestion set: [@acc_a (mutual: 12), @acc_b (mutual: 4), @acc_c (mutual: 1)]

OBS-004 (Session D):
Suggestion set: [@acc_a (mutual: 18), @acc_b (mutual: 5), @acc_c (mutual: 2)]

Derived:
- @acc_a: persistent (4/4), high mutual count, increasing trend
- @acc_b: persistent (4/4), low-moderate mutual, stable
- @acc_c: recurring (3/4), low mutual
- @acc_d: transient (1/4)

Lead scores:
- @acc_a: 10 (HIGH-VALUE) — high recurrence, high mutual, full persistence
- @acc_b: 9 (STRONG) — high recurrence, moderate mutual, full persistence

Deep dive on @acc_a:
- Public profile found.
- @acc_a's public posts contain recurring event context.
- Another public account in the same event context interacts with target's network.

Corroboration:
- + shared event context (independent surface)
- + public mention of target's network (independent surface)

Updated @acc_a score: 13 (HIGH-VALUE)

Community detection:
- @acc_a and @acc_b are co-suggested across all sessions.
- They form a SUGGESTION_CLUSTER.
- Target's suggestion set is 2/3 dominated by this cluster.

Hypothesis:
- Target may have a strong network association with the @acc_a/@acc_b cluster.
- The cluster may represent a shared community, workplace, or social circle.

Conclusion:
- Publicly observable suggestion evidence supports a recurring network
  association between the target and the @acc_a/@acc_b cluster.
- The nature of the association is unresolved without further evidence.
```

This is a synthetic example. Real investigations must use actual observed data.

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
