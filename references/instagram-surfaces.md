# Instagram OSINT — Observable Surfaces

This document defines the categories of publicly observable Instagram information that may be useful during an investigation.

The agent should treat these as possible sources of evidence, not as guaranteed sources of truth.

---

# 1. Profile Surface

Inspect the target profile for observable information.

Potential signals:

* Username
* Display name
* Bio
* Profile picture
* Public account type/category
* Public links
* Website links
* Contact information that is explicitly displayed publicly
* Emoji or symbolic identifiers
* Repeated names or aliases
* Publicly visible profile metadata

Questions to consider:

* Does the username appear to be an alias?
* Does the display name differ from the username?
* Does the bio contain references to organizations, locations, communities, interests, or other accounts?
* Does the profile picture resemble imagery appearing elsewhere in the investigation?
* Does the profile link to another Instagram account?

Do not treat a name or profile picture alone as sufficient identity evidence.

---

# 2. Followers Surface

When follower information is publicly observable, inspect it for relationships and clusters.

Potential signals:

* Mutual followers
* Repeated accounts
* Unusual accounts
* Accounts sharing names or aliases
* Accounts belonging to apparent communities
* Multiple accounts that appear connected to the target
* Accounts repeatedly appearing across related profiles

Important:

The existence of a follower relationship does not establish the nature of the relationship.

Record the observable relationship first.

Example:

TARGET → follows → ACCOUNT_A

Do not automatically convert this into:

TARGET → friend → ACCOUNT_A

---

# 3. Following Surface

Analyze accounts followed by the target.

Look for:

* Friends or acquaintances
* Organizations
* Schools or colleges
* Clubs
* Communities
* Businesses
* Creators
* Sports teams
* Event accounts
* Secondary accounts
* Potential aliases
* Repeated account categories

Look for clusters rather than isolated accounts.

Example:

If the target follows 15 accounts associated with the same university, this may indicate a relevant community connection.

It does not by itself prove enrollment.

---

# 4. Mutual Connection Surface

Mutual connections can provide useful graph evidence.

Potential signals:

* Number of mutual followers
* Specific recurring mutual accounts
* Mutual accounts appearing across multiple related profiles
* Dense clusters of shared connections
* Accounts acting as bridges between otherwise separate groups

A large number of mutual connections may be informative, but should not automatically be interpreted as a personal relationship.

---

# 5. Recommendation Surface

Recommendation exposure is an important but ambiguous signal.

If Instagram visibly recommends or surfaces another account in the context of investigating the target, record:

```text
TARGET
  |
  | recommendation observed
  ↓
ACCOUNT_B
```

Do not assume the reason for the recommendation.

Possible explanations include:

* Shared connections
* Interaction signals
* Social graph overlap
* Shared interests
* Platform ranking behavior
* Contact/network signals
* Other unknown recommendation mechanisms
* Coincidence

Treat recommendation exposure as a **lead generator**.

Recommendation observations become more interesting when independently corroborated by other observable evidence.

For example:

```text
Recommendation
      +
Shared followers
      +
Repeated interaction
      +
Related public content
```

is more informative than the recommendation alone.

---

# 6. Post Surface

Inspect publicly observable posts.

For each relevant post, consider:

* Caption
* Date/time information
* Comments
* Mentions
* Tags
* Hashtags
* Visible location information
* People appearing in the media
* Objects
* Events
* Text visible in the image
* Recurring visual context
* Accounts interacting with the post

Do not inspect every post blindly.

Prioritize posts likely to reveal relationships, communities, locations, events, or recurring entities.

---

# 7. Caption Surface

Captions may contain:

* Names
* Nicknames
* Locations
* Events
* Organizations
* Schools
* Colleges
* Communities
* Dates
* Inside references
* Mentions
* Hashtags
* Links
* Relationship language

Extract entities and relationships rather than simply summarizing captions.

Example:

Caption:

"Back at IITM with the gang"

Potential entities:

* IITM
* People mentioned
* Event/community context

Potential hypothesis:

"The account may have some association with the referenced institution."

Do not treat casual language as definitive evidence.

---

# 8. Comment Surface

Comments may reveal relationships that are not obvious from profiles.

Look for:

* Repeated commenters
* Conversation patterns
* Replies between recurring accounts
* Mentions
* Nicknames
* Inside references
* Event references
* Shared communities
* Accounts repeatedly interacting with the target

Repeated interaction may be more informative than a single comment.

However:

Interaction frequency does not automatically establish the nature of a relationship.

---

# 9. Mention Surface

Mentions can reveal explicit account relationships.

Record:

* Who mentions the target
* Who the target mentions
* Accounts repeatedly mentioned
* Accounts mentioned together
* Context surrounding mentions

Potential patterns:

```text
A mentions B
B mentions A
A and B repeatedly appear in the same posts
```

This may support an association hypothesis.

---

# 10. Tag Surface

Publicly observable tags can reveal additional connections.

Look for:

* Accounts tagging the target
* Accounts tagged by the target
* Recurring co-tagged accounts
* Multiple accounts tagged in the same events
* Accounts appearing repeatedly together

Tags should be treated as observations, not proof of friendship or other relationships.

---

# 11. Hashtag Surface

Hashtags may reveal:

* Communities
* Events
* Organizations
* Locations
* Hobbies
* Interests
* Campaigns
* Recurring activities

Repeated use of a specific hashtag may indicate a contextual connection.

Hashtags are generally weak evidence individually.

Their value increases when combined with other independent signals.

---

# 12. Tagged-Content Surface

If publicly observable, inspect content where the target appears.

Look for:

* Recurring people
* Recurring locations
* Events
* Organizations
* Communities
* Repeated account combinations
* Temporal patterns

This can reveal relationships that are not directly visible through the target's own posts.

---

# 13. Image Surface

Images are first-class evidence.

When visual content is available, inspect it systematically.

### People

Look for:

* Recurring individuals
* Multiple appearances of the same individual
* Co-appearance patterns
* Clothing or accessories
* Contextual similarities

Visual resemblance alone is insufficient for identity confirmation.

Use language such as:

* "visually similar"
* "possibly the same individual"
* "appears consistent with"
* "insufficient evidence for identity"

### Locations

Look for:

* Landmarks
* Buildings
* Schools
* Colleges
* Restaurants
* Cafés
* Venues
* Streets
* Signs
* Geographic indicators

### Objects

Look for recurring:

* Cars
* Motorcycles
* Pets
* Instruments
* Sports equipment
* Clothing
* Accessories
* Distinctive objects

### Text inside images

Extract visible:

* Names
* Usernames
* Event names
* Organization names
* Dates
* Locations
* Signs
* Posters
* Screenshots
* Hashtags

### Events

Look for evidence that multiple accounts may have participated in the same event.

Potential signals:

* Same venue
* Same event
* Similar timestamps
* Same background/environment
* Same event branding
* Multiple accounts posting related images

Do not automatically conclude that people appearing at the same event know each other.

---

# 14. Profile Picture Surface

Profile pictures may provide weak identity or continuity clues.

Consider:

* Similar imagery across accounts
* Recurring photographs
* Same artwork/avatar
* Shared visual themes
* Publicly observable changes over time

Do not identify a person solely from profile-picture similarity.

---

# 15. Story / Highlight Surface

When publicly observable, consider:

* Recurring people
* Locations
* Events
* Mentions
* Tagged accounts
* Text
* Visible dates
* Recurring activities
* Highlight titles and organization

Highlights may preserve contextual information that is not obvious from recent posts.

---

# 16. Linked Account Surface

Inspect explicitly visible links between Instagram accounts.

Examples:

* Main account ↔ secondary account
* Personal account ↔ creator account
* Organization ↔ individual
* Publicly linked project/account

Explicitly visible links are generally stronger evidence than inferred similarities.

---

# 17. Temporal Surface

Time can create relationships that are invisible when examining individual posts.

Look for:

* Multiple accounts posting around the same time
* Repeated event dates
* Recurring locations over time
* Accounts becoming connected after a particular event
* Changes in interaction patterns
* Appearance of new accounts
* Repeated yearly events

Temporal correlation is supporting evidence, not proof of causation.

---

# 18. Cross-Account Pattern Surface

Once multiple accounts are discovered, compare them.

Look for:

* Shared followers
* Shared following
* Shared commenters
* Shared tags
* Shared mentions
* Shared hashtags
* Shared locations
* Shared events
* Shared visual contexts
* Recurring people
* Recurring objects
* Recurring organizations

This is where the investigation should begin moving from individual-account analysis toward graph analysis.

---

# 19. Recurring Entity Surface

An entity appearing repeatedly across independent observations is potentially important.

Examples:

```text
Account X
appears in:
    target's followers
    target's comments
    target's tagged content
    related account's followers
    event photographs
```

This recurring entity may deserve prioritization.

The agent should record:

* Number of appearances
* Types of appearances
* Accounts connected through the entity
* Context of each appearance
* Whether evidence is independent or duplicated

---

# 20. Bridge Account Surface

Some accounts connect otherwise separate clusters.

Example:

```text
Cluster A ─── Account X ─── Cluster B
```

A bridge account may be especially useful because investigating it may reveal why two clusters are connected.

Prioritize bridge accounts when:

* They connect multiple relevant clusters
* They repeatedly appear across unrelated observations
* They have meaningful public content
* Investigating them may explain an unresolved relationship

---

# 21. Evidence Independence

Do not count duplicated evidence as independent evidence.

For example:

If ten posts all copy the same event photograph, that is not ten independent confirmations.

Likewise:

```text
A follows B
A likes B's post
A comments on B's post
```

may all represent the same underlying interaction.

The agent should distinguish:

* number of observations
* number of independent evidence sources

---

# 22. Investigation Priority

Not every signal deserves equal investigation.

Prioritize observations that are:

### High value

* Explicit public relationships
* Recurring entities
* Bridge accounts
* Multiple independent corroborating signals
* Unique contextual clues
* Strongly connected clusters
* Previously unexplained relationships

### Medium value

* Mutual connections
* Repeated interactions
* Shared events
* Recurring hashtags
* Recommendation signals with supporting evidence

### Low value

* Generic usernames
* Common names
* Generic hashtags
* Single likes
* Single comments
* Weak visual similarities
* Coincidental similarities

---

# 23. Unknowns Must Remain Unknown

If Instagram does not provide enough observable evidence to determine something, state:

"Unknown."

Do not fill gaps using assumptions.

The objective is not maximum information.

The objective is maximum **defensible information**.

---

# 24. Core Principle

Instagram should be treated as a dynamic relationship graph rather than a collection of isolated profiles.

Every useful observation can potentially:

1. create a new entity,
2. create a new relationship,
3. strengthen an existing relationship,
4. weaken an existing hypothesis,
5. reveal a new investigation path,
6. or explain an existing unexplained connection.

The investigation should continuously update its graph as new evidence appears.

