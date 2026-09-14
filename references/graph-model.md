# Graph Model

## 1. Purpose

The Instagram investigation should be represented as a graph.

The graph allows the investigator to connect observations across different Instagram surfaces and discover relationships that are not obvious from a single profile.

The graph should represent:

```text
Entities
+
Relationships
+
Evidence
+
Uncertainty
+
Time
```

The graph is an investigative model, not proof by itself.

---

# 2. Basic Graph Structure

Use:

```text
NODE ── RELATIONSHIP ── NODE
```

Example:

```text
Target ── FOLLOWS ── Account A
```

Another:

```text
Target ── APPEARS_WITH ── Account A
```

Another:

```text
Target ── SHARES_CONTEXT_WITH ── Event X
```

Every meaningful relationship should have supporting evidence.

---

# 3. Node Types

The graph may contain different node types.

## 3.1 Account

An Instagram account.

```text
ACCOUNT
```

Example:

```text
@account_a
```

---

## 3.2 Person

A person represented by one or more accounts.

This should be used carefully because account-to-person identity may be uncertain.

```text
PERSON
```

Example:

```text
Person X
```

Do not automatically assume:

```text
Account A = Person X
```

---

## 3.3 Post

A visible Instagram post.

```text
POST
```

A post can connect:

```text
Account
Person
Location
Event
Hashtag
Other Account
```

---

## 3.4 Location

A publicly identifiable location.

```text
LOCATION
```

Examples:

```text
Venue X
Campus Y
Public landmark Z
```

Do not infer that a location is someone's home or private residence.

---

## 3.5 Event

A publicly identifiable event or activity.

```text
EVENT
```

Examples:

```text
Concert X
Tournament Y
College Event Z
```

---

## 3.6 Hashtag

A hashtag appearing in visible content.

```text
HASHTAG
```

Example:

```text
#eventX
```

---

## 3.7 Image

A visual artifact associated with a post, profile, story, or highlight.

```text
IMAGE
```

It can contain visual observations.

---

## 3.8 Textual Entity

A meaningful piece of text extracted from visible content.

Examples:

```text
USERNAME
EVENT_NAME
VENUE_NAME
ORGANIZATION
```

---

# 4. Core Relationship Types

Use explicit relationship types.

```text
FOLLOWS
FOLLOWED_BY
INTERACTS_WITH
LIKES
COMMENTS_ON
MENTIONS
TAGGED_WITH
APPEARS_WITH
SHARES_CONTEXT_WITH
SHARES_NETWORK_WITH
USES_HASHTAG
POSTED_BY
LOCATED_AT
ASSOCIATED_WITH_EVENT
POSSIBLE_ALIAS
POSSIBLE_SAME_ENTITY
POSSIBLE_ASSOCIATION
RECOMMENDED_WITH
```

Not every relationship has the same evidentiary strength.

---

# 5. Account Graph

Basic example:

```text
Target
 ├── FOLLOWS ──> Account A
 ├── FOLLOWS ──> Account B
 ├── INTERACTS_WITH ──> Account C
 └── MENTIONS ──> Account D
```

This forms the initial network.

The investigator can then examine high-value neighboring nodes.

---

# 6. Post Graph

Posts connect multiple entities.

Example:

```text
Target
  │
  │ POSTED
  ▼
Post X
 ├── APPEARS_WITH ── Account A
 ├── LOCATED_AT ── Location B
 ├── ASSOCIATED_WITH_EVENT ── Event C
 └── USES_HASHTAG ── #event
```

A single post can therefore produce several graph edges.

---

# 7. Event-Centered Graph

Events can act as bridge nodes.

Example:

```text
Target
   │
   ▼
 Event X
   ▲
   │
Account A
   │
   ▲
Account B
```

This establishes:

```text
Target SHARES_CONTEXT_WITH Event X
Account A SHARES_CONTEXT_WITH Event X
Account B SHARES_CONTEXT_WITH Event X
```

It does **not** automatically establish:

```text
Target ↔ Account A
```

as a personal relationship.

The investigator must distinguish shared context from direct interaction.

---

# 8. Location-Centered Graph

Locations can also connect accounts.

Example:

```text
Target ──────┐
             │
             ▼
         Location X
             ▲
             │
Account A ───┘
```

If the same location appears repeatedly, it may become a useful investigation node.

However:

```text
Same location ≠ relationship
```

People may independently visit the same public place.

---

# 9. Recommendation Edges

Recommendations should have their own relationship type:

```text
RECOMMENDED_WITH
```

Example:

```text
Target ── RECOMMENDED_WITH ── Account A
```

This edge must carry low or uncertain evidentiary weight unless independently corroborated.

Do not convert:

```text
RECOMMENDED_WITH
```

into:

```text
KNOWS
FRIEND_OF
RELATED_TO
```

without additional evidence.

---

# 10. Interaction Edges

Interactions should retain their specific type.

Prefer:

```text
LIKES
COMMENTS_ON
MENTIONS
```

over collapsing everything into:

```text
INTERACTS_WITH
```

The generic relationship can be derived later.

Example:

```text
Target ── LIKES ──> Post A
Target ── COMMENTS_ON ──> Post A
```

can produce:

```text
Target ── INTERACTS_WITH ──> Account A
```

when Post A belongs to Account A.

The original evidence should still be preserved.

---

# 11. Evidence Attached to Edges

Every important edge should store evidence.

Example:

```text
Target
   │
   │ APPEARS_WITH
   │
   └──────────────> Account A

Evidence:
- Post 14
- Post 27
- Post 31
```

A relationship without supporting evidence should be marked:

```text
UNSUPPORTED
```

or:

```text
HYPOTHETICAL
```

rather than presented as established.

---

# 12. Edge Strength

Use qualitative strength:

```text
UNKNOWN
WEAK
MODERATE
STRONG
```

Example:

```text
Target ── FOLLOWS ── Account A
Strength: STRONG
Evidence: directly visible
```

But:

```text
Target ── POSSIBLE_ASSOCIATION ── Account A
Strength: WEAK
Evidence: indirect contextual clues
```

Relationship strength must describe the **evidence for that relationship**, not the importance of the relationship.

---

# 13. Graph Traversal

The investigator should move through the graph deliberately.

Example:

```text
Target
  ↓
Account A
  ↓
Account A's visible interactions
  ↓
Post X
  ↓
Location Y
  ↓
Account B
```

Each traversal should have a reason.

Bad:

```text
Target
 ↓
Random follower
 ↓
Their follower
 ↓
Random account
 ↓
Another account
```

Good:

```text
Target
 ↓
Account A
 ↓
Repeated interaction
 ↓
Post X
 ↓
Recurring Location Y
 ↓
Other accounts appearing at Location Y
```

---

# 14. One-Hop Investigation

First investigate direct neighbors.

```text
Target
├── Followers
├── Following
├── Mutuals
├── Visible interactions
├── Mentions
├── Tags
└── Recommendations
```

This establishes the local graph.

---

# 15. Two-Hop Investigation

Investigate important neighbors.

Example:

```text
Target
   ↓
Account A
   ↓
Account B
```

Only continue to Account B if Account A is sufficiently relevant.

---

# 16. Deep Traversal

Deep traversal should be reserved for strong leads.

Example:

```text
Target
 ↓
Account A
 ↓
Event X
 ↓
Account B
 ↓
Location Y
 ↓
Account C
```

Before each additional hop, ask:

```text
Does this node have evidence relevant to the current hypothesis?
```

If not, stop the branch.

---

# 17. Bridge Detection

A bridge node connects different parts of the graph.

Example:

```text
Network A
   │
   ▼
Account X
   │
   ▼
Network B
```

Account X may deserve priority if it connects multiple otherwise separate clusters.

Possible bridge types:

```text
ACCOUNT
LOCATION
EVENT
ORGANIZATION
HASHTAG
```

A bridge is an investigative lead, not proof of a personal relationship.

---

# 18. Cluster Detection

Groups of densely connected nodes may represent a common context.

Example:

```text
        Account A
        /       \
       /         \
Target ─────── Account B
   \             /
    \           /
      Account C
```

Possible explanation:

```text
Shared community
```

But the investigator should test alternatives.

A cluster may simply result from:

* a popular event
* a school
* a workplace
* a public community
* a common interest
* platform recommendation behavior

---

# 19. Recurring Node Detection

Nodes that repeatedly appear in different observations should receive higher investigative priority.

Example:

```text
Post 1 → Location X
Post 2 → Location X
Post 3 → Location X

Post 4 → Account A
Post 5 → Account A
```

Both:

```text
Location X
Account A
```

become recurring nodes.

Recurring nodes may reveal useful structure.

---

# 20. Temporal Graph

Relationships can change over time.

Represent important relationships with timestamps.

Example:

```text
Target ── FOLLOWS ── Account A
Date observed: 2026-08-10
```

Another:

```text
Target ── APPEARS_WITH ── Account A
Date: 2026-08-15
```

This allows the investigator to distinguish:

```text
old connection
```

from:

```text
recent recurring connection
```

Do not assume an old relationship still exists today.

---

# 21. Graph Evidence vs Graph Inference

The graph can contain both observed and inferred edges.

Example:

```text
OBSERVED EDGE:

Target ── FOLLOWS ── Account A
```

Then:

```text
DERIVED EDGE:

Target ── INTERACTS_WITH ── Account A
```

Then:

```text
HYPOTHETICAL EDGE:

Target ── POSSIBLE_ASSOCIATION ── Account A
```

These must remain distinguishable.

---

# 22. Graph Confidence

Confidence should propagate carefully.

Do not assume:

```text
Strong edge + Strong edge = Certain conclusion
```

For example:

```text
Target follows A
A follows B
```

does not establish:

```text
Target knows B
```

Graph paths create **possible leads**, not automatic facts.

Longer paths generally require more corroboration.

---

# 23. Path Analysis

A path can reveal how two nodes are connected.

Example:

```text
Target
 ↓
Account A
 ↓
Event X
 ↓
Account B
```

This means:

```text
Target and Account B may share an event-related context through A.
```

It does not necessarily mean:

```text
Target knows Account B personally.
```

The investigator should describe the exact path.

---

# 24. Shortest Path vs Strongest Path

The shortest graph path is not necessarily the best explanation.

Example:

```text
Target
 ↓
Popular Account
 ↓
Account A
```

may be a short path but weak evidence.

Another path:

```text
Target
 ↓
Event X
 ↓
Account A
```

may contain stronger contextual evidence.

Prefer the **strongest evidentiary path**, not merely the shortest path.

---

# 25. Graph Pruning

Remove or deprioritize nodes that produce no useful evidence.

Examples:

```text
Large celebrity account
Huge public hashtag
Generic location
Unrelated follower
Repeatedly uninformative recommendation
```

The graph should remain focused on the current investigation.

---

# 26. Graph Expansion Rules

Expand a node when:

```text
- It has multiple relevant edges.
- It connects separate clusters.
- It repeatedly appears in observations.
- It directly relates to an active hypothesis.
- It may provide independent corroboration.
- It can distinguish competing hypotheses.
```

Do not expand simply because the node exists.

---

# 27. Graph Storage Concept

A conceptual node can contain:

```text
NODE

id:
type:
name:
source:
first_seen:
last_seen:
attributes:
confidence:
evidence_ids:
```

A conceptual edge can contain:

```text
EDGE

source_node:
relationship:
target_node:
observed_at:
evidence_ids:
strength:
status:
confidence:
notes:
```

This structure should be adapted to the actual implementation.

---

# 28. Graph Status

Nodes and edges may have:

```text
OBSERVED
DERIVED
HYPOTHETICAL
CONFIRMED
CONTRADICTED
UNRESOLVED
```

Do not mix these states.

---

# 29. Core Graph Questions

At every stage ask:

```text
1. What nodes do I currently have?

2. Which nodes are directly connected to the target?

3. Which nodes repeatedly appear?

4. Which nodes connect separate clusters?

5. Which edges are directly observed?

6. Which edges are derived?

7. Which edges are only hypotheses?

8. Which nodes could provide independent evidence?

9. Which branch has the highest information value?

10. Which branches should be pruned?
```

---

# 30. Core Principle

The graph is not the conclusion.

It is a representation of:

```text
What was observed
+
How observations are connected
+
How strong those connections are
+
What remains uncertain
```

The investigator should use the graph to discover useful paths while continuously checking whether each path is actually supported by evidence.

```text
GRAPH
  ↓
DISCOVER STRUCTURE
  ↓
TEST RELATIONSHIPS
  ↓
CORROBORATE
  ↓
FORM CONCLUSIONS
```

Never:

```text
GRAPH
  ↓
ASSUME RELATIONSHIPS
  ↓
DECLARE CONCLUSION
```
