# Investigation Strategy

## 1. Purpose

The investigator should not simply collect every piece of available Instagram data.

Its goal is to determine:

> **What investigation step would provide the most useful new information about the current hypotheses?**

The agent should continuously prioritize leads, investigate them, update the evidence graph, and reconsider its hypotheses.

Core loop:

```text
OBSERVE
  ↓
RECORD EVIDENCE
  ↓
UPDATE GRAPH
  ↓
GENERATE HYPOTHESES
  ↓
RANK POSSIBLE NEXT ACTIONS
  ↓
INVESTIGATE BEST LEAD
  ↓
CHECK FOR CONTRADICTIONS
  ↓
REPEAT
```

---

# 2. Start With the Target

When given an Instagram account, create a target entity.

Record only information that is publicly observable or otherwise explicitly authorized.

Example:

```text
TARGET
├── username
├── display_name
├── bio
├── profile_image
├── followers
├── following
├── visible posts
├── visible interactions
└── other observable surfaces
```

Do not immediately decide what the target's relationships are.

The initial target is simply the starting node of the investigation graph.

---

# 3. Build a Candidate Pool

As observations are collected, create candidate entities.

Examples:

```text
Target
 ├── Account A
 ├── Account B
 ├── Account C
 ├── Location X
 ├── Event Y
 └── Hashtag Z
```

Candidates can originate from:

* followers
* following
* mutual connections
* recommendations
* comments
* mentions
* tags
* visible likes
* captions
* hashtags
* images
* profile pictures
* recurring locations
* recurring events
* linked accounts
* repeated usernames
* repeated aliases

A candidate is **not automatically a meaningful connection**.

---

# 4. Rank Candidates

Every candidate should receive a qualitative priority.

Use:

```text
HIGH
MEDIUM
LOW
IGNORE
```

Priority should consider:

### 4.1 Relevance

How directly is the candidate connected to the current hypothesis?

Example:

```text
Target repeatedly appears with Account A
```

is more relevant than:

```text
Target and Account B follow the same large public account
```

---

### 4.2 Evidence Strength

Prefer candidates supported by multiple independent observations.

For example:

```text
Target follows Account A
Target repeatedly interacts with Account A
Target appears with Account A
```

is more useful than one isolated follow.

---

### 4.3 Novelty

Prefer investigations that could reveal something not already known.

If five observations all originate from the same post, investigating another identical signal has low value.

---

### 4.4 Discriminating Power

Prefer actions that can distinguish between competing hypotheses.

Example:

```text
H1: Account A is simply a mutual connection.
H2: Account A has a stronger recurring association with Target.
```

Finding another mutual follower may not distinguish H1 from H2.

Finding several independent interactions between Target and Account A may.

---

### 4.5 Reliability

Prefer directly observable evidence over speculation.

Rough ordering:

```text
Direct visible observation
        ↓
Repeated observation
        ↓
Independent corroboration
        ↓
Derived relationship
        ↓
Interpretation
        ↓
Speculation
```

---

# 5. Do Not Crawl Everything

The investigator should avoid exhaustive exploration when it has little expected value.

Bad strategy:

```text
Open every follower.
Open every follower's followers.
Open every post.
Open every comment.
Repeat forever.
```

This creates enormous noise.

Instead:

```text
Target
 ↓
Find interesting candidate
 ↓
Investigate candidate
 ↓
Determine whether candidate produces useful evidence
 ↓
Continue or abandon branch
```

---

# 6. Follow Strong Leads Recursively

If Account A becomes important, investigate Account A.

For example:

```text
Target
   ↓
Account A
   ↓
Account B
   ↓
Location X
   ↓
Account C
```

Each newly discovered node can reveal additional evidence.

However, recursion must have limits.

Do not recursively explore an entire Instagram network without a reason.

---

# 7. Bridge Accounts

A particularly useful candidate is a **bridge account**.

A bridge account connects otherwise separate parts of the graph.

Example:

```text
Target
 ├── Network A
 │    ├── Account 1
 │    └── Account 2
 │
 └── Account X
      │
      └── Network B
           ├── Account 3
           └── Account 4
```

If Account X repeatedly connects Target's otherwise separate networks, it deserves investigation.

Bridge accounts can reveal:

* shared communities
* recurring social contexts
* events
* organizations
* friend groups
* shared activities

Do not automatically interpret a bridge as evidence of a personal relationship.

---

# 8. Recurring Contexts

Repeated context can be more informative than a single interaction.

Look for repeated:

* locations
* events
* venues
* activities
* groups
* hashtags
* people
* objects
* dates/time periods
* visual backgrounds
* captions/themes

Example:

```text
Post 1 → Location X
Post 2 → Location X
Post 3 → Account A
Post 4 → Location X + Account A
```

This may justify investigating:

```text
Target ↔ Account A ↔ Location X
```

The system should record the observations separately rather than immediately declaring a relationship.

---

# 9. Image-Based Investigation

Images should be treated as evidence sources, not decoration.

When an image is available, inspect observable features such as:

### People

* number of people
* recurring faces
* apparent same person across images
* clothing patterns
* positioning
* group composition

### Environment

* buildings
* streets
* venues
* landmarks
* interiors
* signs

### Objects

* vehicles
* products
* equipment
* decorations
* distinctive items

### Text

Read visible:

* signs
* usernames
* event names
* logos
* captions embedded in images
* dates
* locations

### Temporal clues

Compare:

* clothing
* weather
* event decorations
* venue appearance
* visible dates

Visual observations must remain separate from identity claims.

For example:

```text
OBSERVED:
A person with similar visible characteristics appears in two images.

NOT:
These are definitely the same person.
```

---

# 10. Recommendation Signals

Recommendations can be used to generate candidates.

Example:

```text
Target
   ↓
Recommended Account A
```

Record:

```text
Recommendation observed
```

Do not record:

```text
Target knows Account A
```

The recommendation mechanism is not fully observable.

Possible explanations include:

* mutual connections
* interaction signals
* shared interests
* network proximity
* platform ranking
* contact/network signals
* coincidence

Therefore:

```text
Recommendation = LEAD
Recommendation ≠ PROOF
```

---

# 11. Interaction Patterns

Prioritize repeated interactions over isolated interactions.

Example:

```text
One like
    → weak signal

Several likes across different posts
    → stronger signal

Repeated comments
    → stronger signal

Comments + likes + mentions
    → potentially strong association evidence
```

But interaction frequency alone should not be converted into a sensitive relationship claim.

The correct conclusion may simply be:

```text
"These accounts show repeated interaction."
```

---

# 12. Temporal Analysis

Time can reveal patterns.

Compare:

```text
Account A posts
Target interacts
Account B posts
Target appears
```

Look for repeated timing patterns.

Example:

```text
Event 1
Target + Account A

Event 2
Target + Account A

Event 3
Target + Account A
```

Repeated co-occurrence is more informative than one coincidence.

However:

```text
Same date ≠ same event
```

and:

```text
Same location ≠ same group
```

unless additional evidence supports that conclusion.

---

# 13. Generate Competing Hypotheses

Never maintain only one explanation.

Suppose:

```text
Target interacts frequently with Account A.
```

Possible hypotheses:

```text
H1: They are ordinary acquaintances.
H2: They belong to the same social group.
H3: They share a recurring activity/community.
H4: The interaction is mostly one-sided.
H5: The observed pattern is coincidental.
```

The investigator should actively look for evidence that separates these possibilities.

---

# 14. Choose the Next Best Investigation

For every possible next action, ask:

```text
1. What hypothesis does this investigate?
2. What new evidence could it produce?
3. Would that evidence distinguish competing hypotheses?
4. How reliable would the evidence be?
5. Is the evidence independent of what we already know?
6. How much effort does this investigation require?
```

Prefer investigations with:

```text
High relevance
+
High information value
+
Independent evidence
+
Reasonable effort
```

---

# 15. Information Gain

The best next action is often the one that could change the current conclusion.

Example:

```text
H1: Account A is just a mutual.
H2: Account A has a recurring association with Target.
```

Possible actions:

```text
A. Find another mutual follower
B. Inspect another Target post involving Account A
C. Check whether Account A repeatedly appears in Target's visible content
D. Search unrelated hashtags
```

Prefer:

```text
C
```

because it can directly distinguish the hypotheses.

---

# 16. Evidence Independence

Do not count the same underlying event multiple times.

Example:

```text
Target likes Account A's post.
Target's like appears in a list.
Another observation confirms the same like.
```

This is effectively one event:

```text
Target liked Account A's post.
```

It should not become three independent pieces of evidence.

---

# 17. Contradiction Search

For every strong hypothesis, deliberately search for contradictory evidence.

Example:

```text
Hypothesis:
Target and Account A have a recurring association.
```

Search for:

```text
- evidence showing no recurring interaction
- different contexts
- conflicting identity clues
- different locations
- evidence suggesting another Account A
- observations that explain the pattern more simply
```

A good investigator should be able to say:

```text
"What evidence would prove my current hypothesis wrong?"
```

---

# 18. Entity Resolution

Similar usernames, names, profile pictures, or appearances do not automatically indicate the same person.

Represent uncertain identity as:

```text
Account A
   ↓
POSSIBLE_SAME_ENTITY
   ↓
Account B
```

Only strengthen the relationship when independent evidence supports it.

Useful signals may include:

* matching public username patterns
* matching public profile information
* consistent public images
* recurring links
* overlapping public contexts
* explicit public mentions

Avoid relying on one visual similarity.

---

# 19. Stop Investigating a Branch

Abandon a branch when:

```text
Evidence is weak
AND
No new useful information is appearing
```

or:

```text
The candidate is clearly unrelated
```

or:

```text
The branch requires speculation rather than observable evidence
```

Do not continue simply because more data can technically be collected.

---

# 20. Investigation Budget

The investigator should maintain a practical exploration budget.

Possible limits:

```text
Maximum recursion depth
Maximum accounts investigated
Maximum posts per account
Maximum low-value branches
Maximum repeated observations
```

When the budget is exhausted:

```text
Summarize current evidence
Identify unresolved hypotheses
Stop
```

The exact limits should depend on the available tools and task.

---

# 21. Final Investigation Decision

At every stage, the agent should be able to answer:

```text
What do I currently know?

What am I uncertain about?

What are my competing hypotheses?

What evidence supports each?

What evidence contradicts each?

What is the most useful next investigation?

Why?
```

If there is no high-value next investigation, stop.

---

# 22. Core Rule

The investigator is not trying to discover the most interesting story.

It is trying to discover the **most defensible explanation supported by observable evidence**.

```text
More data ≠ better investigation

Better evidence
+
better reasoning
+
better uncertainty handling
=
better investigation
```

