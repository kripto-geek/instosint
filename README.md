# INSTOSINT

Instagram-focused OSINT investigation skill for OpenCode.

INSTOSINT is designed to help an agent investigate an Instagram account
using publicly observable Instagram information, build an evidence graph,
discover non-obvious connections, and recursively investigate the most
useful leads.

The goal is not simply to collect information.

The goal is to **reason over relationships between publicly observable
Instagram entities**.

---

## What Are We Building?

INSTOSINT is an investigation framework/skill that turns an Instagram
account into the starting point of a graph-based investigation.

Given a target account:

    @target

the agent should be able to examine relevant public Instagram surfaces,
identify accounts, posts, people, places, events, interactions and other
recurring entities, connect them together, generate hypotheses, and decide
what should be investigated next.

Conceptually:

    Target Account
          |
          v
    Public Instagram Data
          |
          v
    Observations
          |
          v
    Evidence Graph
          |
          v
    Relationships
          |
          v
    Hypotheses
          |
          v
    High-value Leads
          |
          v
    Recursive Investigation
          |
          v
    Evidence-backed Conclusions


The important part is the reasoning loop:

    OBSERVE
       ↓
    RECORD
       ↓
    CONNECT
       ↓
    FORM HYPOTHESES
       ↓
    INVESTIGATE
       ↓
    CHALLENGE
       ↓
    UPDATE GRAPH
       ↓
    CHOOSE NEXT BEST LEAD
       ↓
    REPEAT


---

# Core Idea

Instagram is treated as a dynamic relationship graph rather than a
collection of isolated profiles.

For example:

    Target
      |
      | follows
      v
    Account A
      |
      | appears in
      v
    Event X
      |
      +------> Account B
      |
      +------> Account C

There may also be:

    Target
      |
      | interacts with
      v
    Account A

    Target
      |
      | tagged in
      v
    Event X

    Account A
      |
      | posts from
      v
    Event X

These connections can reveal useful investigation leads.

However, a connection is not automatically a conclusion.

The system must distinguish:

    Observation
        ↓
    Derived relationship
        ↓
    Inference
        ↓
    Hypothesis
        ↓
    Supported hypothesis


---

# What INSTOSINT Is NOT

INSTOSINT is NOT intended to be:

- A generic web search tool
- A simple Instagram profile scraper
- A username-search engine
- A follower-list exporter
- A tool that blindly crawls everything
- A system that assumes two accounts are the same person
- A system that treats recommendations as proof
- A relationship-status detector
- A private-account bypass
- A system for accessing restricted information
- A system that invents missing evidence

The objective is **investigation and reasoning**, not indiscriminate
data collection.


---

# Instagram-Only Focus

The primary investigation environment is Instagram.

The agent should reason using publicly observable Instagram surfaces such as:

- Profiles
- Usernames
- Display names
- Bios
- Profile pictures
- Followers
- Following
- Mutual connections
- Public posts
- Captions
- Comments
- Visible likes
- Mentions
- Tags
- Tagged posts
- Hashtags
- Stories/highlights when publicly observable
- Images
- Text contained in images
- Locations
- Events
- Recurring people
- Recurring objects
- Recurring visual contexts
- Posting times
- Interaction patterns
- Recommendation surfaces
- Linked accounts
- Shared networks
- Recurring contexts between accounts

The exact surfaces available depend on the data-access mechanism being
used by the agent.


---

# Images Are First-Class Evidence

Images are not treated as decoration.

They are an important investigation surface.

The agent should examine publicly observable visual information such as:

- People appearing in images
- Repeated appearances of the same person
- Locations
- Venues
- Events
- Objects
- Signs
- Text in images
- Logos
- Clothing or other contextual clues
- Background consistency
- Recurring visual environments
- Shared event/context clues

For example:

    Target Post 1
        |
        +--> Event X

    Target Post 2
        |
        +--> Event X
        |
        +--> Person A

    Account A Post
        |
        +--> Event X

This creates a potentially useful graph:

    Target
      |
      +---- Event X ---- Account A
                         |
                         +---- repeated interaction


Visual information should be recorded as observations first.

The agent must not automatically convert:

    "Two people appear in the same photo"

into:

    "These people have a particular personal relationship."


---

# Recursive Investigation

INSTOSINT should not stop after examining the target account.

The target is the starting point.

If the investigation finds:

    Target → Account A

and Account A provides a strong lead to:

    Event X

then the agent may investigate Event X and the accounts associated with
that event.

For example:

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
      +---- Account D


The agent should then decide which of B/C/D is actually worth
investigating.

It should NOT blindly crawl every account.

Each investigation hop should have a reason.


---

# Investigation Strategy

The system should optimize for **information value**, not volume.

For every potential lead, consider:

- Relevance to the current hypothesis
- Strength of existing evidence
- Novel information
- Ability to distinguish competing hypotheses
- Reliability of the source
- Recurrence of the connection
- Whether the lead creates a bridge to another part of the graph
- Whether investigating it is likely to produce useful evidence

A useful mental model is:

    "What investigation step would teach us the most?"


rather than:

    "What else can we scrape?"


---

# Recommendation Signals

Instagram recommendations can be useful as leads.

For example:

    Target
       |
       +--> Account A
       |
       +--> Recommended Account B


Account B may deserve investigation.

But:

    Recommended(B)

does NOT mean:

    Target knows B

and certainly does not mean:

    Target has a specific relationship with B.


Recommendation signals should therefore have lower evidentiary weight
unless independently corroborated.


---

# Evidence Model

Every important claim should have provenance.

The system uses the following conceptual hierarchy:

    DIRECT OBSERVATION
          ↓
    DERIVED OBSERVATION
          ↓
    INFERENCE
          ↓
    HYPOTHESIS
          ↓
    SUPPORTED HYPOTHESIS


### Direct Observation

Something directly visible in the source.

Example:

    Target follows @account_a.


### Derived Observation

Something calculated from observed data.

Example:

    Target and @account_a share 12 visible followers.


### Inference

A reasonable interpretation of multiple observations.

Example:

    Target and @account_a appear to have repeated interaction.


### Hypothesis

A possible explanation that has not yet been established.

Example:

    Account A may be a particularly significant connection for Target.


### Supported Hypothesis

A hypothesis supported by multiple independent pieces of evidence.

It is still not necessarily absolute proof.


---

# Evidence Independence

Repeated observations are not automatically independent evidence.

For example:

    Target likes 10 posts from Account A.

This may represent one underlying relationship pattern rather than ten
independent pieces of evidence.

INSTOSINT should avoid artificially increasing confidence simply because
the same type of signal appears many times.

Stronger evidence often comes from different categories:

    Follow relationship
          +
    Repeated comments
          +
    Shared event
          +
    Recurring visual context
          +
    Independent account interaction


---

# Entity Resolution

The system may encounter accounts that appear to represent the same
person or entity.

For example:

    @john_smith
    @johnsmith_
    @john.smith123


Similarity is only a lead.

The system should represent uncertain identity using concepts such as:

    POSSIBLE_SAME_ENTITY

rather than immediately merging the accounts.

Potential supporting signals can include:

- Similar public identity information
- Recurring visual context
- Shared public links
- Consistent public biography
- Repeated contextual association
- Other independently observable signals

No single weak similarity should establish identity.


---

# Evidence Graph

The investigation is represented as a graph.

### Nodes

Possible node types include:

- Account
- Person
- Post
- Image
- Location
- Event
- Hashtag
- Textual entity


### Edges

Possible relationships include:

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


Every important edge should have supporting evidence.

Conceptually:

    [Target]
       |
       | FOLLOWS
       |
       v
    [Account A]
       |
       | APPEARS_WITH
       |
       v
    [Person X]
       |
       | ASSOCIATED_WITH
       |
       v
    [Event Y]


The graph is a representation of evidence.

The graph itself is NOT the conclusion.


---

# Hypothesis Engine

The agent should be capable of maintaining multiple competing
hypotheses.

For example:

    H1: Account A is a significant recurring connection.

    H2: The observed connection is primarily explained by a shared
        community/event.

    H3: The apparent connection is mostly an artifact of Instagram's
        recommendation or interaction systems.

The investigation should seek evidence that distinguishes these
possibilities.

The agent should actively search for contradictions.

A good investigation asks:

    "What evidence would make this hypothesis less likely?"


not only:

    "What evidence supports it?"


---

# Contradiction Search

A hypothesis should not become strong simply because supporting evidence
was found.

The agent should actively search for:

- Contradictory observations
- Alternative explanations
- Missing expected evidence
- Evidence suggesting a different context
- Evidence that two apparently connected accounts are unrelated
- Evidence that an apparent visual match is coincidental

This helps prevent confirmation bias.


---

# Unknown ≠ False

A critical rule:

    No evidence found
        ≠
    Evidence that something does not exist


For example:

If the agent cannot retrieve a follower relationship, it must not say:

    "Target does not follow Account A."

Instead:

    "The follower relationship could not be established from the
    available data."


Unknown information must remain unknown.


---

# No Fabricated Evidence

INSTOSINT must never invent investigation results.

It must never create fictional:

- Accounts
- Usernames
- Followers
- Following relationships
- Likes
- Comments
- Mentions
- Tags
- Captions
- Bios
- Locations
- Events
- Images
- Recommendation results
- Timestamps
- Relationships

Placeholders such as:

    Account A
    Account B
    [Number]
    [display name]
    [bio text]

must NEVER appear as factual investigation findings.

If information was not retrieved:

    UNKNOWN — DATA NOT AVAILABLE


The skill describes the investigation methodology.

It does not magically provide Instagram access.


---

# Data Access Boundary

INSTOSINT operates only on data that the agent is authorized to access.

It must not:

- Bypass private accounts
- Circumvent authentication
- Defeat access controls
- Access restricted content
- Attempt to reveal private information
- Pretend unavailable data was retrieved

If the required data is unavailable, the investigation should report the
limitation rather than fabricate an answer.


---

# Investigation Lifecycle

A typical investigation follows this process:

## 1. Initialize Target

Create the target account node.

Example:

    @target


## 2. Collect Observable Data

Inspect relevant public Instagram surfaces.


## 3. Record Observations

Record factual observations with provenance.


## 4. Build Initial Graph

Connect accounts, posts, interactions, images, events and other entities.


## 5. Identify Interesting Relationships

Find:

- Recurring accounts
- Strong interactions
- Shared contexts
- Bridge accounts
- Recurring locations
- Recurring events
- Visual recurrence
- Unusual clusters


## 6. Generate Hypotheses

Create multiple plausible explanations.


## 7. Rank Leads

Determine which lead is most valuable to investigate next.


## 8. Investigate Recursively

Follow the strongest useful leads.


## 9. Challenge Hypotheses

Search for contradictory evidence and alternative explanations.


## 10. Update Graph

Add new observations and modify hypothesis status.


## 11. Repeat

Continue while investigation provides meaningful information.


## 12. Produce Final Report

Return a traceable evidence-backed investigation.


---

# Investigation Budget

The system should avoid unlimited crawling.

Investigation should stop when:

- Important hypotheses are sufficiently supported
- Additional branches have low information value
- Evidence becomes repetitive
- Remaining leads are weak
- Available public data is exhausted
- Further investigation would mostly produce noise

The goal is:

    Maximum useful evidence
    with
    Minimum unnecessary exploration


---

# Output

A completed investigation should contain sections such as:

    Investigation Summary

    Observations

    Derived Relationships

    Evidence Table

    Hypotheses

    Contradictory Evidence

    Alternative Explanations

    Entity Resolution

    Evidence Graph

    Investigation Path

    Next Best Leads

    Dead Ends

    Unknowns

    Final Conclusion


The final conclusion should distinguish:

### Established

What is directly supported by observable evidence.

### Supported but Uncertain

What has meaningful supporting evidence but is still an inference.

### Cannot Be Established

What the available evidence is insufficient to determine.


---

# Example Investigation

Suppose the agent observes:

    Target follows Account A.

    Target repeatedly comments on Account A's posts.

    Target appears with Account A in two public posts.

    Both accounts appear at Event X.

    Account A independently posts from Event X.

The graph may become:

    Target
       |
       | follows
       v
    Account A
       |
       +---- comments/interactions
       |
       +---- shared visual context
       |
       +---- Event X
                 |
                 +---- Account A
                 |
                 +---- Target


This may support the hypothesis:

    "Target and Account A have a recurring public association."


It does NOT automatically establish any specific private or personal
relationship.

The system should then ask:

    What additional public evidence would distinguish this association
    from a shared community, event, workplace, school, friendship,
    creator/fan relationship, or other explanation?


That is the type of reasoning INSTOSINT is intended to perform.


---

# Project Structure

Current project structure:

    instosint/
    ├── SKILL.md
    ├── README.md
    │
    └── references/
        ├── instagram-surfaces.md
        ├── evidence-model.md
        ├── investigation-strategy.md
        ├── investigation-output.md
        ├── image-analysis.md
        └── graph-model.md


### SKILL.md

The main OpenCode skill.

Defines:

- When INSTOSINT should be used
- Investigation lifecycle
- Core reasoning loop
- Evidence discipline
- Recursive investigation
- Hypothesis handling
- Lead prioritization
- Output requirements


### instagram-surfaces.md

Defines the Instagram surfaces that can provide useful observations.


### evidence-model.md

Defines:

- Evidence types
- Observation hierarchy
- Evidence strength
- Evidence independence
- Entity resolution
- Hypothesis lifecycle


### investigation-strategy.md

Defines how the agent decides:

    "What should I investigate next?"


### investigation-output.md

Defines the structure and language of the final investigation report.


### image-analysis.md

Defines how images are treated as first-class investigation evidence.


### graph-model.md

Defines the graph representation of accounts, posts, people,
locations, events and relationships.


---

# Intended Architecture

INSTOSINT is the reasoning layer.

A complete system consists of:

    ┌──────────────────────────────┐
    │ Instagram Data Access Layer  │
    │                              │
    │ Public / Authorized Data     │
    └──────────────┬───────────────┘
                   │
                   v
    ┌──────────────────────────────┐
    │          INSTOSINT            │
    │                              │
    │ Observation Engine           │
    │ Evidence Model               │
    │ Graph Model                  │
    │ Hypothesis Engine            │
    │ Investigation Strategy       │
    │ Image Analysis               │
    │ Contradiction Search         │
    └──────────────┬───────────────┘
                   │
                   v
    ┌──────────────────────────────┐
    │ Evidence Graph               │
    │                              │
    │ Accounts                     │
    │ Posts                        │
    │ People                       │
    │ Events                       │
    │ Locations                    │
    │ Interactions                 │
    │ Visual Context               │
    └──────────────┬───────────────┘
                   │
                   v
    ┌──────────────────────────────┐
    │ Investigation Report         │
    │                              │
    │ Findings                     │
    │ Evidence                     │
    │ Hypotheses                   │
    │ Contradictions               │
    │ Uncertainty                  │
    │ Next Leads                   │
    └──────────────────────────────┘


The data-access layer and reasoning layer should remain conceptually
separate.


---

# Design Principles

## 1. Evidence First

No evidence → no factual claim.


## 2. Observation Before Interpretation

Record what is visible before deciding what it means.


## 3. Graph Before Conclusion

Connections should be represented explicitly before drawing conclusions.


## 4. Recursion With Purpose

Every investigation hop should have a reason.


## 5. Information Gain Over Data Volume

Investigate what is most likely to reduce uncertainty.


## 6. Images Matter

Visual context can reveal relationships that text alone misses.


## 7. Recommendations Are Leads

Recommendation systems are useful signals, not proof.


## 8. Similarity Is Not Identity

Similar usernames, names or images do not automatically establish that
two accounts represent the same person.


## 9. Contradictions Matter

Actively search for evidence that challenges the current hypothesis.


## 10. Unknown Is Allowed

The system must be comfortable saying:

    "We don't know."


## 11. No Fabrication

Never create evidence to make an investigation look complete.


## 12. Traceability

Every meaningful conclusion should be traceable:

    Conclusion
        ↓
    Hypothesis
        ↓
    Relationships
        ↓
    Observations
        ↓
    Source


---

# Development Goal

The long-term goal of INSTOSINT is to create an agent that behaves less
like a traditional scraper and more like a human investigator who can:

1. Observe
2. Remember
3. Connect
4. Reason
5. Prioritize
6. Investigate
7. Challenge its own assumptions
8. Update its model
9. Explain how it reached a conclusion


The defining feature is therefore not:

    "How much Instagram data can we collect?"

It is:

    **"Given the public evidence available, what is the most useful
    next thing to investigate, and why?"**


---

# Status

INSTOSINT currently contains the investigation methodology and supporting
reference documentation.

The next major engineering problem is connecting the reasoning layer to
a reliable, authorized Instagram data source and ensuring that every
observation produced by the agent is backed by actual retrieved data.

Until then, the skill should be tested using synthetic investigation
scenarios rather than treating fabricated/template data as real evidence.


---

# Disclaimer

INSTOSINT is intended for research, learning, and authorized
public-information investigations.

It should respect platform rules, privacy boundaries, and applicable
laws.

Publicly observable information should not automatically be treated as
proof of someone's private identity, motives, personal relationships, or
other sensitive attributes.

The system should prefer uncertainty and transparent evidence trails over
confident speculation.