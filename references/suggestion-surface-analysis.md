# Suggestion Surface Analysis

This document defines how INSTOSINT extracts, records, and reasons about Instagram's suggestion surfaces — particularly the profile-page suggestion block shown when viewing a private account that is not followed.

---

# 1. Surface Identification

When a private account is viewed without following it, Instagram may expose a suggestion surface on or around the profile page.

Record the exact location and context:

- profile-page suggestion block
- "Suggested accounts" section
- "Accounts you may know" section
- any other suggestion/similarity surface observed

The exact UI labels may vary. Record what is actually visible, not what is expected.

---

# 2. Core Principle

Suggestion surfaces are publicly observable context.

They are not evidence that:
- the target follows the suggested account
- the suggested account follows the target
- the accounts are friends, family, or associates
- the suggestion reason is known

They ARE evidence that:
- Instagram's platform signal associated the two accounts in some observable way
- the suggestion was visible in the documented context at the documented time

Record the observation, not an assumed relationship.

---

# 3. Observable Features

The suggestion block typically exposes multiple features per suggested account.

Record every observable feature.

## 3.1 Account Identity

- username
- display name
- profile category/type if visible
- profile image
- verification status if visible

## 3.2 Mutual Connection Count

Instagram may display a mutual-connection count such as:

```text
Followed by 3 accounts you follow
```

Record:
- the count as an integer if available
- whether mutual connections are shown
- whether the count is exact or approximate

Mutual-connection count is a quantitative signal.

Do not treat:
```text
mutual count = relationship closeness
```

Do treat it as:
```text
NETWORK_PROXIMITY_QUANTIFIER
```

## 3.3 Suggestion Rank / Position

The order of suggested accounts is not random.

Record:
- position in the suggestion list
- whether the target is the first or only suggestion
- any visual grouping or separation

Rank position may correlate with signal strength.

Do not treat rank as proof.
Treat it as:
```text
SUGGESTION_WEIGHT_FEATURE
```

## 3.4 Suggestion Context Labels

Instagram may attach context labels such as:
- "Followed by X accounts you follow"
- "Suggested for you"
- "Similar accounts"
- "Popular"

Record the exact label.

The label may indicate why the platform surfaced the account.

Do not assume the label fully explains the recommendation mechanism.

---

# 4. Canonical Suggestion Observation Record

Each observation of the suggestion surface should be recorded as:

```text
OBS-0XX

Source:
    Profile-page suggestion block (or other observed surface)

Target:
    @target_account

Observation:
    @suggested_account appeared in position N of the
    suggestion block.

Mutual count:
    X (if visible)

Context label:
    "Followed by X accounts you follow" (exact text if present)

Timestamp:
    observed timestamp

Reliability:
    MODERATE
```

This is the canonical observation record. Every suggestion observation must contain these fields.

Reliability rationale:
- The account was directly observed in the documented surface.
- The underlying recommendation reason is opaque.
- The mutual count, when shown, increases directness.

---

# 5. Feature Extraction

Extract structured features from each suggestion observation.

## 5.1 Features

```text
suggested_username
suggested_display_name
position_in_list
mutual_count
context_label
target_account
observation_surface
observation_timestamp
```

## 5.2 Feature Completeness

Record which features were available and which were absent.

If mutual count is not shown:
```text
mutual_count: NOT_VISIBLE
```

If position is ambiguous:
```text
position: UNKNOWN
```

Never invent a feature that was not observed.

---

# 6. Suggestion Set as Fingerprint

The entire set of suggested accounts from one observation is a fingerprint of the target's observable platform context.

## 6.1 Set Comparison

When two observations produce suggestion sets for the same or different targets, compare them:

```text
Observation A: [B, C, D, E]
Observation B: [B, C, F, G]

Intersection: [B, C]
A-only: [D, E]
B-only: [F, G]
```

## 6.2 Overlap as Signal

Persistent accounts across observations (e.g., B and C) are:
- RECURRING_RECOMMENDATION_SIGNAL

Accounts that appear and disappear are:
- TRANSIENT_RECOMMENDATION_SIGNAL

The size of the intersection relative to total set size matters.

```text
intersection_size / union_size = overlap_ratio
```

Record the overlap ratio as a derived observation.

Do not treat overlap ratio as proof of relationship strength.
Treat it as:
```text
NETWORK_PROXIMITY_SIGNAL
```

## 6.3 Set Delta Tracking

Record deltas across observations of the same target:

```text
OBS-0XX:
B, C, D surfaced.

OBS-0XY:
B, C, E surfaced.

DELTA:
D disappeared.
E appeared.
B and C persisted.
```

Persistent accounts justify deeper investigation.
Disappearing accounts may be weaker leads.

---

# 7. Multi-Surface Triangulation

Instagram's suggestion behavior may differ across surfaces.

Possible surfaces:
- profile-page suggestion block
- "Accounts you may know" section
- search suggestions
- "Recommended for you" feed
- post-page related accounts
- story-page suggestions

## 7.1 Cross-Surface Comparison

If the same target or suggested account appears across multiple surfaces, record:

```text
OBS-0XX:
@suggested_account appeared in profile-page suggestion block.

OBS-0XY:
@suggested_account appeared in "Accounts you may know."

Derived:
@suggested_account is surfaced across multiple suggestion surfaces
associated with @target.
```

This is stronger than a single-surface observation.

## 7.2 Surface Weighting

Different surfaces carry different signal weight.

General weighting (adjust based on observed evidence):

```text
profile-page suggestion block: HIGHER (directly attached to target)
"Accounts you may know": MODERATE (broader signal)
search suggestion: MODERATE (query-dependent)
feed recommendation: MODERATE (content-dependent)
```

Weighting is a reasoning tool, not a proof multiplier.

---

# 8. Mutual Connection Feature

The mutual-connection count is the most directly quantitative feature in the suggestion block.

## 8.1 Recording

Record the exact count when available.

```text
OBS-0XX:
@suggested_account surfaced with mutual count = 12
```

## 8.2 Mutual Count as Weight

Higher mutual counts generally indicate stronger network proximity.

Use the count as a weighting factor in lead scoring.

Do not assume:
```text
mutual count = relationship closeness
```

The count reflects shared follows, which may indicate:
- shared community
- shared workplace
- shared location
- actual personal connection
- platform artifact

All of these are possible.

## 8.3 Mutual Count Changes

Track mutual count over repeated observations.

```text
OBS-0XX: mutual count = 8
OBS-0XY: mutual count = 12

DELTA: +4 mutual connections over observation interval
```

An increasing mutual count may indicate:
- the suggested account is becoming more connected to the target's network
- the suggested account is gaining general platform traction
- either is possible; do not assume target-specific meaning

---

# 9. Suggestion Recurrence

If the same account appears in repeated observations of the same target's suggestion block, record recurrence.

## 9.1 Recurrence Recording

```text
OBS-0XX: @account_b appeared in suggestion block.
OBS-0XY: @account_b appeared in suggestion block.
OBS-0XZ: @account_b appeared in suggestion block.

Derived:
REL-00X: @account_b is a recurring recommendation around @target.
```

## 9.2 Recurrence Strength

More observations of recurrence increase the signal.

General guidance:
- 1 observation: WEAK signal
- 2–3 observations: MODERATE signal
- 4+ observations: STRONGER signal (still not proof)

Recurrence must still be combined with other evidence before strong conclusions.

---

# 10. Suggestion Persistence

Some accounts persist in the suggestion block across many observations.
Others appear only once or twice.

Persistence is distinct from recurrence in that it considers:
- how many observations were made
- how many of those observations included the account
- the observation interval

## 10.1 Persistence Ratio

```text
persistence_ratio = observations_including_account / total_observations
```

Record:
- total observations of the target's suggestion block
- observations including each account
- persistence ratio per account

## 10.2 Persistence as Lead Signal

High persistence accounts are generally better leads than low-persistence accounts.

A high-persistence account that also has:
- high mutual count
- independent public corroboration
- recurrence in other suggestion surfaces

is a stronger lead than any single feature alone.

---

# 11. Reverse Suggestion Check

For each suggested account identified around a target, check whether the same target is visible in that account's suggestion context.

This is not always possible or observable.

When observable, record:

```text
OBS-0XX:
@suggested_account appeared in @target's suggestion block.

OBS-0XY:
@target appeared in @suggested_account's suggestion block (if observable).

Derived:
REL-00X:
Bidirectional suggestion signal between @target and @account_b.
```

## 11.1 Bidirectional Signal Strength

Bidirectional suggestion is generally stronger than unidirectional.

However:
- both accounts may be recommended because they belong to the same network
- this does not establish the nature of the relationship

Record it as:
```text
BIDIRECTIONAL_SUGGESTION_SIGNAL
```

not as:
```text
MUTUAL_CONNECTION
```

---

# 12. Suggestion-Set Fingerprinting

The full suggestion set from one observation functions as a fingerprint of the target's current observable platform neighborhood.

## 12.1 Fingerprint Record

```text
OBS-0XX

Target:
    @target

Surface:
    profile-page suggestion block

Suggestion set (ordered by observed position):
    1. @account_a
    2. @account_b
    3. @account_c
    4. @account_d
    5. @account_e

Mutual counts:
    @account_a: 12
    @account_b: 8
    @account_c: 3
    @account_d: NOT_VISIBLE
    @account_e: 1

Context:
    Observed at timestamp T
```

## 12.2 Fingerprint Comparison

When comparing two targets' suggestion fingerprints:

```text
Target A fingerprint: [B, C, D, E, F]
Target B fingerprint: [C, D, G, H, I]

Overlap: [C, D]
Overlap ratio: 2/8 = 0.25
```

Record:
- overlapping accounts
- overlap ratio
- accounts unique to each target

## 12.3 Overlap as Network Signal

Significant overlap between two targets' suggestion sets may indicate:
- shared network neighborhood
- shared community/context
- direct or indirect association

It does NOT establish:
- direct relationship
- shared location
- shared identity

Record as:
```text
SHARED_SUGGESTION_FINGERPRINT
```

---

# 13. Community Detection via Suggestion Clusters

When multiple private targets have been observed, their suggestion sets can reveal community structure.

## 13.1 Candidate Social Circles

Accounts that repeatedly appear across many targets' suggestion sets may represent:
- a shared community
- a geographic cluster
- a professional or social network
- a content/interest cluster

Record them as:
```text
COMMUNITY_CANDIDATE
```

## 13.2 Strongly Connected Components

Accounts that:
- appear in each other's suggestion sets (if observable)
- are co-suggested across multiple targets
- have high mutual counts across multiple targets

may form a strongly connected component in the suggestion graph.

Record as:
```text
SUGGESTION_CLUSTER
```

## 13.3 Cluster Isolation

A private target whose suggestion set is dominated by a specific cluster may be associated with that cluster.

Example:
```text
Target A's suggestions: 4/5 accounts belong to Cluster X.
Target B's suggestions: 5/5 accounts belong to Cluster X.
Target C's suggestions: 1/5 accounts belong to Cluster X.

Inference:
A and B may have stronger association with Cluster X
than C does.
```

This is a hypothesis, not a conclusion.

---

# 14. Quantified Edge Features

When building the evidence graph, suggestion edges should carry quantified features, not just boolean existence.

## 14.1 Suggestion Edge Structure

```text
REL-00X

Subject:
    @target

Relationship:
    SUGGESTED

Object:
    @account_b

Features:
    recurrence_count: 3
    persistence_ratio: 0.75
    mutual_count: 12
    position_avg: 2.0
    surfaces: [profile_page, accounts_you_may_know]
    bidirectional: NO

Strength:
    MODERATE (recurring, high mutual count, multi-surface)

Evidence:
    OBS-0XX, OBS-0XY, OBS-0XZ
```

## 14.2 Strength Guidelines

Use the features to assign relationship strength:

| Feature Profile | Strength |
|---|---|
| Single observation, no mutual count, transient | WEAK |
| Recurring, moderate mutual count, single surface | MODERATE |
| Recurring, high mutual count, multi-surface, bidirectional | MODERATE-STRONG |
| Persistent across many observations, high mutual, independent corroboration | STRONG |

Strength reflects how reliably the suggestion signal indicates network proximity.
It does not establish relationship type.

---

# 15. Independent Corroboration for Suggestion Leads

A suggestion lead becomes more valuable when independent public evidence corroborates it.

## 15.1 Corroboration Types

Look for:
- public follow relationship (either direction)
- public interaction (likes, comments)
- public mention or tag
- shared event/place in public posts
- shared visual context in public images
- shared hashtag usage
- overlapping public network

Each independent corroboration increases lead value.

## 15.2 Corroboration Independence

Corroboration must be from a *different* observation surface than the original suggestion.

Bad corroboration:
- Another observation of the same suggestion block
- A screenshot of the same suggestion block

Good corroboration:
- Public follow observed in the account's profile
- Public comment observed on a post
- Public mention observed in a post caption

## 15.3 Corroboration Stack

Track the corroboration stack for each lead:

```text
LEAD-00X

Base signal:
    SUGGESTED (recurring, 12 mutual, multi-surface)

Corroboration:
    + OBS-0XX: public follow (A follows B)
    + OBS-0XY: public comment (B comments on A's post)
    + OBS-0XZ: shared event context

Corroboration depth: 3 independent surfaces

Lead quality: STRONGER
```

---

# 16. Lead Scoring Model

INSTOSINT uses a qualitative lead-scoring model to prioritize investigation.

The model combines suggestion features with independent corroboration.

## 16.1 Score Components

Base score from suggestion features:

```text
RECURRENCE:
    1 observation: 1 point
    2-3 observations: 2 points
    4+ observations: 3 points

MUTUAL_COUNT:
    0-2: 1 point
    3-10: 2 points
    11+: 3 points

PERSISTENCE:
    persistence_ratio < 0.5: 1 point
    0.5-0.8: 2 points
    > 0.8: 3 points

MULTI_SURFACE:
    single surface: 1 point
    two surfaces: 2 points
    three+ surfaces: 3 points

BIDIRECTIONAL:
    no: 0 points
    yes: 1 point
```

Corroboration bonus:

```text
CORROBORATION:
    0 independent surfaces: 0 points
    1 independent surface: 2 points
    2 independent surfaces: 3 points
    3+ independent surfaces: 4 points
```

## 16.2 Score Ranges

```text
0-3 points:  WEAK lead
4-6 points:  MODERATE lead
7-9 points:  STRONG lead
10+ points:  HIGH-VALUE lead
```

## 16.3 Scoring Caveats

- This is a reasoning framework, not a calibrated probability model.
- Points should not be treated as percentages.
- The score is a prioritization tool, not a proof of relationship.
- Leads with high scores still require investigation before conclusions.
- Low scores do not automatically disqualify a lead.

## 16.4 Scoring Calibration

- A score of 6 is the minimum threshold for substantive investigation. Leads with score 4-6 may be investigated only if no higher-score leads exist or if budget allows.
- When two leads have the same score, prefer the lead with higher corroboration count.
- When scores and corroboration are equal, prefer the lead with higher mutual-connection count.
- A lead with score 3 that has unique features (e.g., appears in a public post with the target) may be worth a single corroboration check even below threshold.
- A HIGH-VALUE lead with zero corroboration is still a stronger signal than a MODERATE lead with one corroboration — but the MODERATE lead may be faster to validate.

## 16.5 Score in Lead Record

```text
LEAD-00X

Target:
    @account_b

Base signal:
    SUGGESTED around @target

Score breakdown:
    recurrence: 3
    mutual_count: 3
    persistence: 2
    multi_surface: 2
    bidirectional: 0
    corroboration: 4
    TOTAL: 14

Lead quality: HIGH-VALUE

Reason:
    Recurring high-mutual suggestion across multiple surfaces,
    corroborated by public follow and shared event context.

Expected information gain:
    HIGH

Cost:
    MODERATE

Status:
    UNINVESTIGATED
```

---

# 17. Rate-Aware Observation Protocol

Repeated observation of Instagram surfaces must account for rate limits, anti-abuse mechanisms, and result variability.

## 17.1 Rate Awareness

Instagram may:
- rate-limit repeated requests
- alter suggestion results based on request patterns
- temporarily block or challenge access
- change UI between observations

The observation protocol must be rate-aware.

## 17.2 Spacing

Space repeated observations apart:
- minimum interval between observations of the same surface/target
- longer intervals for deeper observations
- randomize intervals where feasible

Do not fire rapid repeated requests.

## 17.3 Observation Budget

For each investigation, set observation limits:

```text
max_suggestion_observations_per_target: 10
max_targets_in_suggestion_session: 20
min_observation_interval: 1 hour
```

These are example values. Adjust based on actual constraints.

## 17.4 Result Variability

Suggestion results may vary between observations even without rate limiting.

Record:
- each observation separately
- do not merge observations into a single "true" result
- the delta between observations is itself informative

## 17.5 Suggestion Block Changes on Reload

Instagram may show different suggestion sets on successive page reloads within the same session.

If results change between reloads:
1. Record each observation separately with timestamp.
2. Assign each observation to the same session/independence group.
3. Do not merge observations into a single "true" set.
4. Use delta analysis to identify persistent vs. transient accounts.
5. Persistent accounts are stronger leads; transient accounts may be algorithmic noise.

---

# 18. Suggestion Graph Construction

Build a separate graph layer for suggestion relationships.

## 18.1 Suggestion Graph Structure

```text
TARGET
    |
    | SUGGESTED (with features)
    |
ACCOUNT_A
    |
    | SUGGESTED (with features)
    |
ACCOUNT_B
    |
    | SUGGESTED (with features)
    |
ACCOUNT_C
```

The suggestion graph may be built for:
- a single target and its suggestions
- multiple targets and their suggestion sets
- suggested accounts and their own suggestion sets (if observable)

## 18.2 Graph Layers

The suggestion graph is a separate layer from the relationship graph.

```text
LAYER 1: Relationship graph (follows, comments, mentions, tags)
LAYER 2: Suggestion graph (SUGGESTED edges with features)
```

Both layers may coexist.

## 18.3 Cross-Layer Correlation

When a SUGGESTED edge coincides with a FOLLOWS edge:

```text
@target → FOLLOWS → @account_b
@target → SUGGESTED → @account_b
```

This is a meaningful signal.
It may indicate:
- the suggestion reflects an existing follow (if target is public)
- the account is strongly associated with the target's network

For a private target, the FOLLOWS edge would typically not be observable.
The SUGGESTED edge may still be observable.

---

# 19. Multi-Target Investigation

When investigating multiple private targets, use suggestion-set analysis to connect them.

## 19.1 Cross-Target Suggestion Overlap

```text
Target A suggestion set: [B, C, D, E]
Target B suggestion set: [C, D, F, G]
Target C suggestion set: [D, E, G, H]

Shared across all three: [D]
Shared between A and B: [C]
Shared between B and C: [G]
```

These overlaps may indicate shared network membership.

## 19.2 Candidate Cluster Identification

Accounts that appear across many targets' suggestion sets are cluster candidates.

```text
@account_d appears in 3/3 targets' suggestion sets.
@account_c appears in 2/3 targets' suggestion sets.
```

This does not mean they are part of the same organization or group.
It means they share platform-level network proximity.

## 19.3 Cluster Hypothesis

A cluster of accounts that:
- are co-suggested across multiple targets
- show bidirectional suggestions where observable
- have high mutual counts
- have independent public corroboration

may represent:
```text
POSSIBLE_SHARED_NETWORK
```

not:
```text
CONFIRMED_ORGANIZATION
```

---

# 20. Investigation Strategy for Suggestions

## 20.1 Initial Suggestion Sweep

For each new target:
1. Record the full suggestion set with all observable features.
2. Identify the top 3-5 leads by score.
3. Investigate leads with highest expected information gain.

## 20.2 Deep Dive on High-Value Leads

For each high-value suggestion lead:
1. Inspect the suggested account's public profile.
2. Record public follows, posts, comments, mentions, tags.
3. Look for independent corroboration of the suggestion signal.
4. Check for bidirectional suggestion if feasible.
5. Update lead score with corroboration.
6. Decide whether to escalate to hypothesis or stop.

## 20.3 Recursive Suggestion Investigation

For a high-value lead with its own public content:
1. Extract entities from the public content.
2. Check whether any extracted entities overlap with the original target's network.
3. If overlap is found, record as independent corroboration.
4. If new entities are found, decide whether to investigate them.

## 20.4 Stop Conditions for Suggestion-Driven Investigation

Stop when:
- all high-value leads have been investigated
- corroboration is exhausted
- additional investigation has low expected information gain
- budget is exhausted

## 20.5 Fallback Decision Tree

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

---

# 21. Evidence Model for Suggestions

## 21.1 Suggestion Evidence Types

```text
DIRECT_SUGGESTION_OBSERVATION:
    The account was directly observed in the suggestion surface.

DERIVED_SUGGESTION_SET:
    Calculated from multiple direct suggestion observations.

RECURRING_SUGGESTION_SIGNAL:
    The account appeared in multiple observations.

BIDIRECTIONAL_SUGGESTION_SIGNAL:
    The account appears in suggestion sets associated with both directions.

SHARED_SUGGESTION_FINGERPRINT:
    Overlap between suggestion sets of two or more targets.

COMMUNITY_CANDIDATE:
    Account that appears across many targets' suggestion sets.
```

## 21.2 Suggestion Evidence Reliability

```text
DIRECT_SUGGESTION_OBSERVATION: MODERATE
RECURRING_SUGGESTION_SIGNAL: MODERATE (recurrence increases confidence)
BIDIRECTIONAL_SUGGESTION_SIGNAL: MODERATE-STRONG (when observable)
SHARED_SUGGESTION_FINGERPRINT: MODERATE (depends on set size and overlap)
COMMUNITY_CANDIDATE: MODERATE (depends on observation count)
```

All suggestion evidence remains MODERATE at best until independent corroboration is found.

## 21.3 Independence Groups for Suggestions

Assign independence groups to avoid double-counting:

```text
OBS-0XX, OBS-0XY, OBS-0XZ: independence_group = SUGGESTION_SESSION_A
OBS-0YA, OBS-0YB: independence_group = SUGGESTION_SESSION_B
```

Observations from the same session are not independent.
Observations from different sessions are more independent.

---

# 22. Output Format for Suggestion Investigation

## 22.1 Suggestion Summary

```text
SUGGESTION INVESTIGATION SUMMARY

Target: @target
Surface: profile-page suggestion block
Observations: N
Suggested accounts identified: N
High-value leads: N
Investigations completed: N

Suggestion set fingerprint (first observation):
    [ordered list with mutual counts]

Persistent accounts:
    [accounts appearing in >50% of observations]

High-value leads:
    [lead IDs with scores]
```

## 22.2 Suggestion Graph

When outputting the graph, include suggestion edges with features:

```text
@target
    |-- SUGGESTED --> @account_a [recurrence: 3, mutual: 12, surfaces: 2]
    |-- SUGGESTED --> @account_b [recurrence: 1, mutual: 1, surfaces: 1]
    |-- SUGGESTED --> @account_c [recurrence: 4, mutual: 25, surfaces: 3]
```

## 22.3 Suggestion Hypotheses

```text
HYP-00X

Statement:
    @account_c may have a strong network association with @target.

Evidence:
    REL-00X: recurring SUGGESTED edge, high mutual count,
             multi-surface, corroborated by public follow and
             shared event context.

Confidence:
    MODERATE (suggestion + corroboration)

Alternative:
    The association may be primarily platform/algorithmic.
```
