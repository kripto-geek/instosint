# Browser-Based Instagram Access Layer

This document defines how INSTOSINT can use browser automation to access
publicly observable Instagram surfaces when raw HTTP access is blocked.

This is an optional data-access layer. INSTOSINT's reasoning methodology
works without it. It is provided to make the skill executable against
Instagram's JS-heavy, anti-bot frontend.

---

# 1. Core Principle

Browser automation is for **observation of publicly available surfaces only**.

It is NOT for:
- accessing private content the user's account is not authorized to see
- following targets, liking posts, or any interaction
- bypassing access controls
- impersonating other users
- automating actions that would not be taken manually

The test account must be created by the user. It should contain no personal
data, no follows, and no activity. It exists solely to observe public surfaces.

---

# 2. When to Use Browser Access

Use browser access when:
- direct HTTP requests are blocked (e.g., error 1357055, login walls)
- the target surface is rendered by JavaScript
- screenshots of visual content are needed
- session state is required to observe suggestion surfaces

Do NOT use browser access when:
- the target is public and raw HTTP already works
- the investigation can proceed without it
- the user has not provided authorized session credentials

---

# 3. Prerequisites

## 3.1 Authorized Test Account

The user must:
1. Create a dedicated test Instagram account
2. Not follow the target or any related accounts
3. Not interact with the target's content
4. Provide session cookies or login credentials

The test account should be:
- empty of personal data
- empty of follows/following where possible
- used only for observation

## 3.2 Session Credentials

INSTOSINT requires one of:
- session cookies from an authenticated browser session
- username/password for automated login
- exported session state from browser DevTools

The user is responsible for:
- creating the test account
- providing credentials
- understanding Instagram's Terms of Service

INSTOSINT does not create, manage, or verify accounts.

---

# 4. Browser Configuration

## 4.1 Recommended Setup

```text
browser: chromium or firefox
mode: headless or visible (user preference)
user_agent: standard desktop browser user agent
viewport: 1280x800 or larger
cookies: loaded from user-provided session file
```

## 4.2 Anti-Detection

Instagram may detect automation. Use standard anti-detection:
- realistic user agent
- standard viewport size
- avoid headless-specific signals where possible
- respect rate limits

Do NOT attempt to hide automation from Instagram if it violates
Instagram's Terms of Service.

## 4.3 Rate Limits

Respect Instagram's rate limits:
- minimum delay between page loads: 2-5 seconds
- minimum delay between profile observations: 1 hour
- randomize intervals where feasible
- stop immediately if blocked/challenged

---

# 5. Navigation Patterns

## 5.1 Profile Page

```text
1. Navigate to https://www.instagram.com/<target_username>/
2. Wait for page load
3. Check for login wall / private account notice
4. If suggestion block is visible, record it
5. If blocked, record state and stop
```

## 5.2 Suggestion Block Observation

```text
1. Scroll to suggestion block section
2. Record all visible suggested accounts
3. For each: username, position, mutual count, context label
4. Take screenshot for evidence
5. Record timestamp
```

## 5.3 "Accounts You May Know" Surface

```text
1. Navigate to Instagram home/explore with test account
2. Locate "Accounts you may know" section
3. Check if target appears in suggestions
4. Record same features as profile-page suggestions
```

---

# 6. Observation Protocol

## 6.1 Canonical Observation Record

```text
OBS-XXX

Source:
    Browser-automated Instagram session (test account)

Surface:
    profile_page_suggestion_block

Target:
    @target_account

Suggested account:
    @suggested_account

Position in list:
    N

Mutual-connection count:
    X (or NOT_VISIBLE)

Context label:
    exact text or NOT_VISIBLE

Screenshot:
    path/to/screenshot.png (if taken)

Timestamp:
    observed timestamp

Access method:
    browser_automation

Reliability:
    MODERATE
```

## 6.2 Screenshot Evidence

When a screenshot is taken:
- save with timestamp and target in filename
- reference in the observation record
- treat as VISUAL_OBSERVATION evidence

Screenshots are evidence of what was visible at the time.
They are not evidence of what the content means.

---

# 7. Session Management

## 7.1 Session Loading

```text
1. User provides session cookies or login credentials
2. Load cookies into browser context
3. Navigate to instagram.com to verify session
4. If session is valid, proceed
5. If session is invalid, report and stop
```

## 7.2 Session Validation

Before each investigation:
- verify the test account is logged in
- check for login challenges / 2FA requirements
- record session state

If the session becomes invalid during investigation:
- record partial observations
- stop and report session failure

## 7.3 Session Storage

Session cookies may be stored locally for reuse.
- store in a secure location
- do not commit to version control
- treat as sensitive credentials

---

# 8. Guardrails

## 8.1 Interaction Prohibitions

Do NOT:
- follow the target
- follow suggested accounts
- like posts
- comment on posts
- send DMs
- report accounts
- block accounts
- modify any account settings

## 8.2 Content Access Limits

Only access content that would be visible to the test account
without any special authorization:
- public profiles
- public posts
- public suggestion surfaces
- public comments on public posts

Do NOT access:
- private posts
- private stories
- DMs
- any content gated by follow/friend relationship

## 8.3 Test Account Integrity

- do not follow the target during investigation
- do not interact with suggested accounts
- if accidental interaction occurs, record it and discard session
- create a fresh test account if the session is compromised

---

# 9. Fallback Behavior

If browser automation fails:
1. Record the failure mode
2. Fall back to raw HTTP if available
3. Fall back to web search if available
4. If all access methods fail, mark as BLOCKED_ACCESS

Do not retry failed browser sessions in a loop.
Increase wait time between retries.

---

# 10. Evidence Handling

## 10.1 Screenshot Evidence

```text
SRC-IMAGE-001

Type:
    screenshot

Source:
    Browser-automated session

Target:
    @target profile page

Content:
    Profile-page suggestion block showing accounts X, Y, Z

Observed at:
    timestamp

File:
    screenshots/2026-09-19_target_suggestion_block.png
```

## 10.2 Browser Session Evidence

```text
SRC-BROWSER-001

Type:
    browser_session

Session:
    test_account_01

Login status:
    authenticated at timestamp

Cookies source:
    user-provided session file
```

---

# 11. Investigation Flow with Browser Access

```text
TARGET
  ↓
BROWSER NAVIGATION (profile page)
  ↓
SUGGESTION BLOCK OBSERVED?
  ├── YES → record features, score leads, investigate
  └── NO → record NOT_AVAILABLE, pivot to other surfaces
  ↓
PUBLIC POSTS OBSERVED?
  ├── YES → record posts, comments, mentions, tags
  └── NO → record NOT_AVAILABLE
  ↓
EVIDENCE UPDATE
  ↓
CONCLUSION
```

---

# 12. Security Considerations

## 12.1 Credential Safety

- session cookies are sensitive credentials
- store them outside the repository
- never log or expose cookies in investigation output
- never commit session files to version control

## 12.2 Test Account Isolation

- the test account should have no real personal data
- do not use a personal Instagram account
- if the test account is compromised, discard it

## 12.3 Legal and Terms of Service

- the user is responsible for complying with Instagram's Terms of Service
- INSTOSINT is a methodology; the user controls execution
- automated access may violate Instagram's ToS
- use at your own risk
