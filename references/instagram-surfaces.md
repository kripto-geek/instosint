# Instagram Data Surfaces

This document defines the Instagram surfaces that INSTOSINT may use when they are publicly observable or otherwise authorized.

---

# 1. Scope

INSTOSINT investigates observable Instagram data.

It must never:

- bypass private-account restrictions
- bypass authentication
- access deleted/private content through unauthorized means
- exploit access-control weaknesses
- treat inaccessible information as negative evidence
- fabricate unavailable data

If a surface cannot actually be observed, record it as `UNKNOWN` or `DATA_UNAVAILABLE`.

---

# 2. Profile Surface

Potential observations:

- username
- display name
- bio
- profile photo
- account type, when visible
- public follower/following counts
- visible external links
- visible location references
- visible pronouns or self-description
- visible category
- visible profile metadata

Possible derived relationships:

```text
Account → HAS_USERNAME → username
Account → HAS_DISPLAY_NAME → display_name
Account → LINKS_TO → external_resource
Account → REFERENCES → place/topic
```

Do not assume:

```text
display_name = legal_name
username = identity
location_reference = current_location
profile_photo = unique identity proof
```

---

# 3. Followers and Following

When publicly observable:

- followers
- following
- mutual followers
- accounts appearing repeatedly across networks
- unusual overlap between accounts
- reciprocal following
- asymmetric following

Potential relationships:

```text
A → FOLLOWS → B
A ← FOLLOWS ← B
A → MUTUAL_CONNECTION → B
A → NETWORK_OVERLAP → B
```

A follow relationship alone does not establish:

- friendship
- romantic involvement
- family relationship
- offline contact
- current interaction

---

# 4. Posts

Inspect publicly observable posts for:

- caption text
- date/time metadata when available
- comments
- visible likes
- mentions
- tagged accounts
- hashtags
- locations
- recurring people
- recurring places
- recurring objects
- recurring events
- recurring activities
- visual context

Potential observations:

```text
Post → CREATED_BY → Account
Post → MENTIONS → Account
Post → TAGS → Account
Post → USES_HASHTAG → Hashtag
Post → REFERENCES → Place
Post → REFERENCES → Event
```

---

# 5. Comments

Comments may reveal:

- repeated interaction
- conversational context
- mentions
- recurring commenters
- event participation
- shared references
- temporal interaction patterns

Example:

```text
Account A comments on Post P.
Account B repeatedly comments on posts by Account A.
```

This may support:

```text
A → INTERACTS_WITH → B
```

It does not automatically prove a personal relationship.

---

# 6. Likes

Visible likes can provide interaction evidence.

Potential observation:

```text
Account A → LIKES → Post P
```

Derived relationship:

```text
Account A → ENGAGES_WITH_CONTENT_OF → Account B
```

Repeated interaction may increase the usefulness of a relationship hypothesis, but likes should not be treated as proof of relationship type.

Consider:

- frequency
- time distribution
- content context
- whether interaction is reciprocal
- whether interaction is unique or widespread
- whether independent evidence exists

---

# 7. Mentions and Tags

Mentions and tags are generally stronger relationship signals than generic similarity.

Examples:

```text
Post P → MENTIONS → Account B
Post P → TAGS → Account B
```

Potential interpretation:

```text
Account A → PUBLICLY_REFERENCES → Account B
```

Do not automatically infer why the account was mentioned or tagged.

---

# 8. Hashtags

Hashtags can reveal:

- events
- locations
- communities
- activities
- recurring topics
- temporal clusters

Example:

```text
Post A → USES_HASHTAG → #event
Post B → USES_HASHTAG → #event
```

This can support:

```text
Post A → SHARES_TOPIC_WITH → Post B
```

Hashtag overlap alone is weak evidence of a personal connection.

---

# 9. Tagged Content

Public tagged content can reveal:

- recurring people
- recurring events
- locations
- group participation
- cross-account appearance

Visual appearance of the same person should be recorded as:

```text
POSSIBLE_VISUAL_MATCH
```

not:

```text
CONFIRMED_IDENTITY
```

unless stronger evidence exists.

---

# 10. Images

Images are first-class investigation sources.

Inspect for observable:

- people
- groups
- locations
- landmarks
- signs
- text
- clothing
- objects
- vehicles
- event decorations
- recurring backgrounds
- logos
- dates
- screenshots
- visible usernames
- visual similarities

Record the actual observation.

Example:

```text
OBS-001:
Image contains a group of three people near a recognizable location.

OBS-002:
The same visual location appears in another public post.
```

Do not write:

```text
Person X is definitely the same person.
```

unless the available evidence genuinely establishes this.

---

# 11. Text in Images

Visible text may include:

- signs
- posters
- event names
- venue names
- usernames
- dates
- captions shown in screenshots
- addresses when publicly displayed
- product/event branding

OCR-derived text should retain a reference to the image source.

```text
Image → CONTAINS_TEXT → "observed text"
```

OCR output may contain errors and should be treated accordingly.

---

# 12. Temporal Surface

When timestamps are publicly available, examine:

- posting periods
- repeated interaction windows
- event dates
- recurring activity
- chronological ordering
- before/after relationships

Temporal overlap is useful only when the relevant timestamps are actually available.

Do not infer location or physical presence solely from posting time.

---

# 13. Recommendations

Recommendations may be observed when the platform exposes them.

Possible signals:

- suggested accounts
- mutual connections
- recurring suggestions
- network proximity

Recommendation systems are opaque.

Therefore:

```text
Recommendation = LEAD
```

not:

```text
Recommendation = RELATIONSHIP PROOF
```

Do not claim to know the exact algorithmic reason for a recommendation.

---

# 14. External Links

Public profiles may contain:

- websites
- public project links
- public contact pages
- public social links

INSTOSINT remains Instagram-focused.

External resources may be recorded as linked context, but unrestricted cross-platform identity hunting is not a default investigation strategy.

---

# 14a. Profile-Page Suggestion Block (Private Accounts)

When viewing a private account without following it, Instagram may display a suggestion block on or near the profile page.

## 14a.1 Surface Identification

Record the exact surface location:
- profile-page suggestion block
- "Suggested accounts" section
- "Accounts you may know" section
- any other suggestion surface observed

The exact UI labels may vary. Record what is actually visible.

## 14a.2 Observable Features

For each suggested account, record all visible features:

- username
- display name
- profile category if visible
- profile image / verification status
- mutual-connection count (e.g., "Followed by 12 accounts you follow")
- suggestion context label (e.g., "Suggested for you", "Similar accounts")
- position in the suggestion list
- whether mutual connections are shown

## 14a.3 Mutual Connection Count

The mutual-connection count is the most directly quantitative feature.

Record the exact count when available.

```text
@suggested_account — mutual count: 12
```

If the count is not shown:
```text
@suggested_account — mutual count: NOT_VISIBLE
```

Do not treat mutual count as relationship closeness.
Treat it as a network-proximity quantifier.

## 14a.4 Suggestion Set as Observation

Record the full suggestion set from each observation:

```text
OBS-0XX

Source:
    Profile-page suggestion block for @target

Suggestion set (ordered by observed position):
    1. @account_a (mutual: 12, label: "Followed by 12 accounts you follow")
    2. @account_b (mutual: 3, label: NOT_VISIBLE)
    3. @account_c (mutual: 1, label: "Suggested for you")

Timestamp:
    observed timestamp
```

## 14a.5 Suggestion Set Delta

When multiple observations of the same target's suggestion set are made, record the delta:

```text
OBS-0XX: [B, C, D]
OBS-0XY: [B, C, E]

DELTA:
Persistent: [B, C]
Disappeared: [D]
Appeared: [E]
```

Persistent accounts are stronger leads than transient accounts.

## 14a.6 Cross-Surface Triangulation

The same account may appear across multiple suggestion surfaces.

Record cross-surface appearances:

```text
OBS-0XX: @account_b appeared in profile-page suggestion block.
OBS-0XY: @account_b appeared in "Accounts you may know."

Derived: @account_b is surfaced across multiple surfaces associated with @target.
```

Multi-surface appearance increases signal reliability.

## 14a.7 Suggestion Reliability

Profile-page suggestions have the following general reliability characteristics:

- DIRECT_OBSERVATION of the suggestion block: MODERATE
- Mutual count shown: increases directness
- Recurrence across observations: increases confidence
- Multi-surface appearance: increases confidence
- Independent public corroboration: required for stronger conclusions

All suggestion evidence is at most MODERATE until independent public corroboration is found.

---

# 15. Surface Reliability

Use the following general hierarchy:

```text
DIRECT_VISIBLE_CONTENT
    ↓
VISIBLE_INTERACTION
    ↓
DERIVED_NETWORK_RELATIONSHIP
    ↓
TEMPORAL/CONTEXTUAL_PATTERN
    ↓
RECOMMENDATION_SIGNAL
```

This is not an absolute ranking.

Context and corroboration always matter.

---

# 16. Data Availability

For every attempted surface record one of:

- OBSERVED
- PARTIALLY_OBSERVED
- NOT_AVAILABLE
- NOT_APPLICABLE
- UNKNOWN

Never convert:

```text
NOT_AVAILABLE
```

into:

```text
NO_RELATIONSHIP
```

---

# 17. Investigation Principle

INSTOSINT should not attempt to collect everything.

Instead:

```text
OBSERVE
→ IDENTIFY HIGH-VALUE SIGNAL
→ RECORD
→ CONNECT
→ FORM HYPOTHESIS
→ INVESTIGATE
```

The goal is useful evidence, not maximum collection.
