# Investigation Graph

This section represents the investigation as a graph with nodes and edges, following the graph model from reference files.

## Node Types

- **Account**: Instagram accounts
- **Person**: People (uncertain identity mapping)
- **Post**: Visible Instagram posts
- **Event**: Public events or activities
- **Hashtag**: Hashtags appearing in content
- **Location**: Publicly identifiable locations

## Initial Graph Structure

```
Target (@lilyyy23___)
│
├── FOLLOWS ──▶ Account A
│
├── FOLLOWS ──▶ Account B
│
├── INTERACTS_WITH ──▶ Account C
│   (repeated likes and comments observed)
│
├── MENTIONS ──▶ [None observed publicly]
│
├── APPEARS_WITH ──▶ Account D
│   (both visibly present in same posts)
│
└── SHARES_CONTEXT_WITH ──▶ Event X
    (both appear at same public event/context)
```

## Recommendation Edge

```
Target ── RECOMMENDED_WITH ──▶ Account B
Evidence: OBS-005 (recommendation surface)
Strength: MEDIUM (unless independently corroborated)
Status: RECOMMENDATION (not converted to stronger relationship)
```

## Entity Resolution Uncertainty

```
Account A
    ↓
POSSIBLE_SAME_ENTITY
    ↓
Account B
(if later investigation suggests possible alias relationship)
```

## Graph Status

- OBSERVED edges: FOLLOWS, INTERACTS_WITH, APPEARS_WITH, SHARES_CONTEXT_WITH
- HYPOTHETICAL edges: POSSIBLE_SAME_ENTITY (not yet supported)
- CONTRADICTED edges: None currently
- UNRESOLVED: Exact nature of relationships between Target and observed accounts

## Traversal Notes

- First-hop investigation complete: followers, following, mentions, tags, recommendations
- Second-hop investigation: investigate Account A's and Account C's visible interactions
- Bridge accounts: Account B (appears in recommendations) warrants investigation for connection patterns