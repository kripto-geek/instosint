# Image Analysis

## 1. Purpose

Images are a first-class information source in an Instagram investigation.

An image may contain useful evidence that is not represented in:

* captions
* usernames
* followers
* following
* comments
* tags

The investigator should inspect publicly observable visual information when available.

The goal is not to identify people from appearance alone.

The goal is to extract **observable contextual evidence** and connect it with other evidence.

---

# 2. Image Analysis Pipeline

For every useful image:

```text
IMAGE
  ↓
VISUAL OBSERVATION
  ↓
EXTRACT ENTITIES
  ↓
EXTRACT CONTEXT
  ↓
COMPARE WITH EXISTING GRAPH
  ↓
GENERATE POSSIBLE CONNECTIONS
  ↓
LOOK FOR INDEPENDENT CORROBORATION
```

Do not jump directly from image → conclusion.

---

# 3. What to Inspect

Analyze the image for several categories.

## 3.1 People

Record observable information such as:

* number of people
* whether people appear repeatedly across posts
* approximate positioning
* group composition
* clothing that may provide contextual clues
* visible accessories
* whether someone is explicitly tagged
* whether someone is mentioned in the surrounding post context

Example:

```text
VIS-001

Observation:
Two people are visibly present in the image.

Additional context:
One person is identified by an Instagram tag.

Do not conclude:
The two people have a particular personal relationship.
```

---

# 4. Repeated People

Repeated appearance can be useful.

Example:

```text
Post A → Target + Person X
Post B → Target + Person X
Post C → Target + Person X
```

This produces:

```text
Target
   │
   └── REPEATED_APPEARANCE_WITH
            │
         Person X
```

This may justify further investigation.

However:

```text
Repeated appearance ≠ specific relationship
```

Possible explanations include:

* friends
* classmates
* coworkers
* teammates
* relatives
* event participants
* members of the same community
* repeated coincidence

The investigator should avoid assigning a specific relationship without sufficient evidence.

---

# 5. Locations

Images can contain location clues.

Look for:

* landmarks
* buildings
* signs
* street names
* shop names
* restaurant names
* campus/building identifiers
* recognizable public venues
* geographic features
* event banners

Example:

```text
VIS-010

Observation:
A sign containing a venue name is visible.

Derived entity:
Venue X

Possible relationship:
Target SHARES_CONTEXT_WITH Venue X
```

A location should not be treated as proof that the target lives there.

---

# 6. Text in Images

Text embedded in images can be highly useful.

Inspect:

* signs
* posters
* event names
* usernames
* handles
* dates
* organization names
* venue names
* public contact information
* hashtags
* slogans
* visible labels

Represent extracted text separately:

```text
VIS-TEXT-001

Image:
Target post 14

Observed text:
"Event X — 12 August"

Confidence:
High
```

If text is unclear, mark it as uncertain rather than inventing missing characters.

---

# 7. Objects

Objects can reveal context.

Examples:

* sports equipment
* musical instruments
* uniforms
* event badges
* books
* trophies
* artwork
* vehicles
* distinctive public objects

Example:

```text
VIS-OBJ-001

Observation:
A cricket tournament banner and team uniform are visible.

Possible context:
Sports event.

Confidence:
Moderate
```

Do not infer ownership merely because an object appears near a person.

---

# 8. Events

Images may provide evidence that multiple accounts participated in the same event.

Look for:

* event banners
* venue decorations
* stage/background
* event hashtags
* dates
* organization logos
* matching event imagery

Example:

```text
Target post → Event X
Account A post → Event X
Account B post → Event X
```

This can create:

```text
Target
  │
  └── SHARES_CONTEXT_WITH
          │
       Event X
          │
     ┌────┴────┐
     ▼         ▼
 Account A   Account B
```

This establishes shared context, not a specific personal relationship.

---

# 9. Background Consistency

Background details can sometimes connect otherwise separate posts.

Compare:

* buildings
* walls
* signs
* furniture
* stage layouts
* landscapes
* decorations
* venue interiors
* distinctive objects

Example:

```text
Image A → distinctive stage
Image B → same distinctive stage
```

Possible conclusion:

```text
The images may have been taken at the same venue or event.
```

Do not claim exact identity unless the evidence is strong enough.

---

# 10. Profile Pictures

Profile pictures may help generate entity-resolution hypotheses.

For example:

```text
Account A
      ↓
Profile image appears visually similar
      ↓
Account B
```

Record:

```text
POSSIBLE_SAME_ENTITY
```

Do not automatically conclude:

```text
Account A = Account B
```

Visual similarity can produce false matches.

Use additional public evidence whenever possible.

---

# 11. Cross-Image Comparison

When comparing images, separate:

### Direct visual observation

```text
"The same-looking jacket appears in both images."
```

from:

### Interpretation

```text
"The images may have been taken during the same event."
```

from:

### Identity claim

```text
"The person is definitely the same individual."
```

These are different confidence levels.

The investigator should not collapse them into one statement.

---

# 12. Image + Text + Account Context

Images become much more useful when combined with surrounding Instagram data.

Example:

```text
Image:
Target and Person X appear together.

Caption:
Event X

Tag:
Person X

Date:
August 12

Account X:
Also posted Event X.
```

This produces several independent evidence categories:

```text
VISUAL
TEXTUAL
TEMPORAL
ACCOUNT
```

Together they may substantially strengthen the **shared event/context** hypothesis.

---

# 13. Image + Recurring Entity

Suppose:

```text
Post 1:
Target + Location X

Post 2:
Target + Location X

Post 3:
Account A + Location X

Post 4:
Target + Account A + Location X
```

The investigation should recognize the recurring entity:

```text
Location X
```

and connect it to the graph.

Possible graph:

```text
Target ─────── Location X ─────── Account A
   │                                  │
   └──────── appears with ───────────┘
```

The system should then investigate whether additional evidence supports the association.

---

# 14. Visual Evidence Independence

Do not double-count multiple images from the same event.

Example:

```text
Image 1
Image 2
Image 3
```

If all three are from the same event, they may represent one underlying event rather than three independent relationship signals.

Record:

```text
EVENT-001
```

and associate the images with that event.

This prevents artificial inflation of evidence strength.

---

# 15. Image Confidence

Use qualitative confidence.

### High

The visual observation is clear and directly visible.

Example:

```text
A readable event name is visible.
```

### Moderate

The observation is reasonably clear but has some ambiguity.

Example:

```text
The venue appears consistent with another image.
```

### Low

The observation depends heavily on visual interpretation.

Example:

```text
A person may be the same person seen in another image.
```

---

# 16. What Images Must Not Establish Alone

An image alone should generally not be used to establish:

* exact personal relationships
* romantic relationships
* family relationships
* private identity
* home address
* sensitive personal characteristics
* motives
* private activities

Instead, record the observable fact.

For example:

```text
GOOD:
"Two accounts appear together in three public posts."

BAD:
"They are definitely dating."
```

---

# 17. Visual False Positives

The investigator must consider:

### Similar-looking people

Two people may look similar.

### Similar locations

Two venues may have similar interiors.

### Reused images

The same image may be reposted.

### Old images

A post may not represent the current situation.

### Edited images

Images may be cropped, filtered, or modified.

### Group events

People appearing together may have no close relationship.

### Coincidental objects

Similar objects do not necessarily indicate shared ownership.

These possibilities should be considered before strengthening a hypothesis.

---

# 18. Image Investigation Priority

Prioritize images that have:

```text
Multiple identifiable entities
+
Clear contextual information
+
Potential connection to an existing hypothesis
```

High-value example:

```text
Target image
+
Account A visibly present
+
Recognizable event
+
Date
+
Account A independently posted same event
```

Low-value example:

```text
Generic landscape
with no identifiable context.
```

---

# 19. Image Evidence Record

Use this structure:

```text
IMAGE-001

Source:
Instagram post/profile/story/highlight

Subject:
Target / Account A / Other entity

Visual observations:
- ...
- ...
- ...

Text extracted:
- ...

Entities identified:
- Person X
- Location Y
- Event Z

Possible relationships:
- APPEARS_WITH
- SHARES_CONTEXT_WITH
- POSSIBLE_SAME_ENTITY

Confidence:
Low / Moderate / High

Supporting evidence:
OBS-001
OBS-004

Limitations:
...
```

---

# 20. Image Investigation Questions

When inspecting an image, ask:

```text
1. What can I directly see?

2. Is there readable text?

3. Are there identifiable public entities?

4. Is there a recognizable location or event?

5. Does someone or something recur elsewhere?

6. Does this image connect two existing graph nodes?

7. Is there a temporal clue?

8. Could this observation have an innocent alternative explanation?

9. Is this evidence independent of evidence already collected?

10. What hypothesis would this evidence actually help distinguish?
```

---

# 21. Image Analysis Rule

The investigator should treat an image as:

```text
A source of observations
        ↓
not
A source of automatic conclusions
```

The strongest image-based reasoning combines:

```text
Visual evidence
+
Textual evidence
+
Temporal evidence
+
Account relationships
+
Independent corroboration
```

The objective is to extract **defensible contextual relationships**, while preserving uncertainty around anything that cannot be directly established.
