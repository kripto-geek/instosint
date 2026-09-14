# INSTOSINT Image Analysis

Images are first-class evidence sources.

Image analysis must remain grounded in what is actually visible.

---

# 1. Image Pipeline

```text
IMAGE SOURCE
↓
VISUAL OBSERVATION
↓
TEXT / OBJECT / CONTEXT EXTRACTION
↓
ENTITY CANDIDATES
↓
RELATIONSHIP CANDIDATES
↓
HYPOTHESES
↓
CORROBORATION
```

# 2. Source Registration

Every image observation must reference the actual source.

Conceptually:

source_id: SRC-IMAGE-001
type: IMAGE
origin: observed Instagram post

Do not create image evidence without a source.

# 3. Visual Categories

Inspect for:

PEOPLE
PLACES
EVENTS
OBJECTS
TEXT
LOGOS
SIGNS
LANDMARKS
VEHICLES
CLOTHING
BACKGROUND
SCREENSHOTS
DATES
USERNAMES

Only record what can actually be observed.

# 4. People in Images

Possible observations:

number of visible people
relative arrangement
visible clothing
visible accessories
visible context
whether a person appears in multiple images

Avoid unnecessary identification.

A visual similarity is:

POSSIBLE_VISUAL_MATCH

not automatic identity confirmation.

# 5. Recurring Visual Elements

Recurring elements can be useful:

same venue
same landmark
same event decoration
same object
same background
same vehicle
same clothing

Example:

Image A contains a distinctive venue interior.

Image B contains a similar venue interior.


Derived hypothesis:

The posts may relate to the same location.

This should be corroborated where possible.

# 6. Text Extraction

Visible text may be extracted from:

signs
posters
screenshots
event banners
menus
public usernames
dates
captions inside images

OCR output should be treated as an observation with possible recognition errors.

If OCR is uncertain:

TEXT_UNCERTAIN

Do not silently correct uncertain text into a different factual value.

# 7. Location Clues

Possible clues:

landmarks
street signs
venue names
event names
geographic references
recognizable architecture

Location clues should not automatically establish where a person currently lives or is physically located.

# 8. Event Detection

Images may contain:

concerts
festivals
sports events
college events
public gatherings
conferences
celebrations

A recurring event can become a useful investigation lead.

Example:

```text
Image
↓
event name
↓
public event context
↓
other public posts
↓
recurring accounts
```

# 9. Visual Similarity

Visual similarity is useful for candidate generation.

Potential match signals:

similar clothing
similar hairstyle
similar accessories
similar background
similar object
similar environment

However:

visual similarity ≠ confirmed identity

Use stronger corroboration before making an identity claim.

# 10. Image Relationships

Possible relationships:

IMAGE → CONTAINS → OBJECT
IMAGE → CONTAINS → TEXT
IMAGE → SHOWS → PLACE
IMAGE → REFERENCES → EVENT
IMAGE → POSSIBLY_MATCHES → IMAGE
IMAGE → POSSIBLY_CONTAINS_SAME_PERSON_AS → IMAGE

Use uncertain relationship names when certainty is unavailable.

# 11. Image + Network Correlation

Example:

Image A:
Account A appears at Event E.

Image B:
Account B appears at Event E.

Network:
A follows B.

This provides multiple related observations.

It does not automatically establish a personal relationship.

The investigation should ask:

Is Event E publicly known to involve both accounts?
Is there independent interaction?
Does the pattern repeat?
Are there alternative explanations?
# 12. Image + Temporal Correlation

Example:

Image A → Event E → date D
Image B → Event E → date D

This may support shared event participation.

Do not infer exact physical presence when timestamps are uncertain.

# 13. Image Evidence Independence

Multiple screenshots of the same image are one underlying source.

Do not count:

original image
screenshot
OCR result
AI description

as independent corroboration.

# 14. Image Limitations

Image analysis may be affected by:

cropping
compression
lighting
angle
occlusion
filters
low resolution
OCR errors
AI perception errors

Record uncertainty when these affect interpretation.

# 15. Forbidden Shortcuts

Do not conclude identity from:

face resemblance alone
similar username alone
similar clothing alone
same location alone
same recommendation alone

These can generate leads only.

# 16. Final Rule

Images should answer:

"What is visibly present?"

before asking:

"What might this mean?"

Observation comes before interpretation.