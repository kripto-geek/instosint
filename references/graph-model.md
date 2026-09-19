# INSTOSINT Graph Model

The graph represents observed and derived relationships.

The graph itself is not the conclusion.

---

# 1. Graph Layers

Use four conceptual layers:

```text
SOURCE
  ↓
OBSERVATION
  ↓
ENTITY / RELATIONSHIP
  ↓
HYPOTHESIS
```

A conclusion must be traceable back through these layers.

---

# 2. Node Types

Possible node types:

- ACCOUNT
- POST
- COMMENT
- IMAGE
- VIDEO
- HASHTAG
- PLACE
- EVENT
- OBJECT
- TEXT_FRAGMENT
- EXTERNAL_RESOURCE

Only create a node when the corresponding entity was actually observed or legitimately derived.

Do not create fictional factual nodes.

---

# 3. Account Nodes

Example conceptual structure:

```text
id: ACCOUNT-001
type: ACCOUNT
identifier:
  username: observed_username
source: SRC-001
```

Do not store a guessed identity as a confirmed account attribute.

---

# 4. Content Nodes

Example:

```text
id: POST-001
type: POST
source: SRC-002
author: ACCOUNT-001
observed_at: observed_timestamp
```

A post can connect to:

- ACCOUNT
- COMMENT
- IMAGE
- VIDEO
- HASHTAG
- PLACE
- EVENT
- MENTIONED_ACCOUNT
- TAGGED_ACCOUNT

---

# 5. Relationship Types

Common relationships:

- FOLLOWS
- FOLLOWED_BY
- MUTUAL_CONNECTION
- LIKES
- COMMENTS_ON
- MENTIONS
- TAGS
- POSTED
- AUTHORED
- APPEARS_IN
- REFERENCES
- LOCATED_AT
- USES_HASHTAG
- SHARES_CONTEXT
- NETWORK_OVERLAP
- TEMPORAL_OVERLAP
- POSSIBLE_VISUAL_MATCH
- LINKS_TO
- SUGGESTED
- RECURRING_SUGGESTION
- BIDIRECTIONAL_SUGGESTION
- SHARED_SUGGESTION_FINGERPRINT
- COMMUNITY_CANDIDATE
- SUGGESTION_CLUSTER

Relationship names must describe what is actually known.

Avoid relationship names such as:

- LOVES
- DATING
- BOYFRIEND_OF
- GIRLFRIEND_OF
- SECRETLY_MEETS

unless the investigation has genuinely established such a fact through appropriate evidence.

---

# 6. Relationship Structure

Conceptual representation:

```text
id: REL-001
source: ACCOUNT-001
relationship: FOLLOWS
target: ACCOUNT-002

evidence:
  - OBS-001

strength: MODERATE
```

A relationship must point to evidence.

---

# 7. Derived Relationships

A derived relationship is allowed only when it can be calculated from observations.

Example:

```text
OBS-001:
Account A follows Account B.

OBS-002:
Account B follows Account A.

Derived:

REL-001:
Account A and Account B have reciprocal following.
```

The derived relationship must reference both observations.

---

# 8. Unsupported Edges

Never create an edge because:

- it seems likely
- two names look similar
- two profile pictures look similar
- two accounts appear in the same recommendation list
- two people may know each other
- an AI model predicts a connection

Such information may become a hypothesis, not an established graph edge.

---

# 9. Visual Relationships

For images:

```text
IMAGE
  ↓
VISUAL_OBSERVATION
  ↓
POSSIBLE_MATCH
```

Example:

```text
IMAGE-001 contains a person wearing a distinctive jacket.
IMAGE-002 contains a visually similar person.
```

Possible relationship:

```text
IMAGE-001 → POSSIBLE_SAME_PERSON → IMAGE-002
```

Confidence should remain uncertain unless corroborating evidence exists.

---

# 10. Temporal Relationships

Example:

```text
POST-001 → CREATED_AT → time-A
POST-002 → CREATED_AT → time-B
```

Derived:

```text
POST-001 → TEMPORALLY_PRECEDES → POST-002
```

Temporal relationships must not automatically become physical-location claims.

---

# 11. Network Relationships

Example:

```text
A → FOLLOWS → B
C → FOLLOWS → B
```

Possible derived relationship:

```text
A → SHARED_NETWORK_CONNECTION → C
```

This is a network relationship, not proof that A and C personally know each other.

---

# 12. Evidence Independence

Multiple observations from the same underlying source should not automatically count as independent corroboration.

Example:

```text
same_post
same_caption
same_image
same_comment_thread
```

may belong to one independence group.

Independent evidence is stronger than repeated representations of the same evidence.

---

# 13. Graph Confidence

Do not calculate confidence merely by counting edges.

Consider:

- source reliability
- observation quality
- independence
- specificity
- corroboration
- contradictions

A large graph can still have weak evidence.

---

# 14. Graph Updates

When new evidence arrives:

```text
ADD observation
  → UPDATE relationships
  → UPDATE hypotheses
  → CHECK contradictions
  → RECALCULATE lead priorities
```

Existing conclusions must be revisable.

---

# 15. Unknowns

Represent unavailable information explicitly.

Example:

```text
surface: followers
status: NOT_AVAILABLE
reason: public data not observable
```

Do not create:

```text
NO_FOLLOWERS
NO_CONNECTION
NO_INTERACTION
```

from missing data.

---

# 16. Traceability

Every conclusion should be traceable:

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

If this chain cannot be reconstructed, the conclusion should not be presented as established.
