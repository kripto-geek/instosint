# Evidence Table

| ID      | Subject | Object       | Relationship         | Evidence                       | Strength |
| ------- | ------- | ------------ | -------------------- | ------------------------------ | -------- |
| OBS-001 | Target  | Account A    | FOLLOWS              | Visible following relationship | Strong   |
| OBS-002 | Target  | [Display]    | TEXTUAL_OBSERVATION  | Profile display name           | High     |
| OBS-003 | Target  | [Follower]   | FOLLOWER_COUNT       | Follower and following counts  | High     |
| OBS-004 | Target  | [Bio]        | TEXTUAL_OBSERVATION  | Bio text                       | High     |
| OBS-005 | Target  | Account B    | RECOMMENDED_WITH     | Recommendation surface         | Weak     |
| OBS-006 | Target  | Account C    | SHARES_NETWORK_WITH  | Mutual followers               | Moderate |
| OBS-007 | Target  | Account D    | INTERACTS_WITH       | Repeated likes/comments        | Moderate |

**Evidence quality:** Moderate  
**Independent evidence sources:** 3+ (follow relationships, interactions, recommendations)  
**Major limitations:** API access restricted; profile data partially observable  
**Major contradictions:** None currently observed  
**Unresolved questions:** Full profile details (bio, follower/following counts, additional surfaces)