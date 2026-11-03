# Browser-Based Instagram Access Layer

This document defines how INSTOSINT can use Hermes browser automation to
access publicly observable Instagram surfaces when raw HTTP access is blocked.

This is an optional data-access layer. INSTOSINT's reasoning methodology
works without it. It is provided to make the skill executable against
Instagram's JS-heavy, anti-bot frontend.

The implementation uses, when the harness provides them:
- `browser_exec` for navigation, observation, and screenshots (Hermes helper)
- `browser_vault_list`, `browser_vault_fill`, `browser_vault_save_login`,
  and `browser_vault_enter_code` for credential access via the Hermes vault
- Named browser sessions to isolate investigation state

None of these are bundled with INSTOSINT. Detect them at runtime (SKILL.md 0.1
and 0.2). When they are absent, the investigation continues in public-only mode
with the absence recorded.

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
- the surface is behind a login wall the session is not authorized to pass; record that surface as NOT_AVAILABLE and continue with the remaining public surfaces

---



# 3. Prerequisites

## 3.1 Authorized Test Account

The user must:
1. Create a dedicated test Instagram account
2. Not follow the target or any related accounts
3. Not interact with the target's content
4. Provide session cookies or login credentials via the Hermes vault

The test account should be:
- empty of personal data
- empty of follows/following where possible
- used only for observation

## 3.2 Session Credentials via Vault

When the Hermes vault tools are available, INSTOSINT uses one of:
- a vault login item bound to `https://www.instagram.com` containing the
  test account identifier and password
- credentials saved through the Hermes vault UI

When the vault tools are not available, the user authenticates manually in an
isolated browser session. Either way, the user is responsible for:
- creating the test account
- providing credentials
- understanding Instagram's Terms of Service

INSTOSINT does not create, manage, or verify accounts.

The vault is the only supported programmatic credential store. Manual login in
an isolated harness session is the fallback. Credentials are never typed by the
agent, and session cookies are sensitive credentials that must not be committed
to version control, logged in investigation output, or stored outside the
harness session mechanism.

---



# 4. Authentication & Session Binding Protocol

## 4.0 CDP Session Auto-Detection (Primary)

Before checking vault tools or prompting for manual login:
1. Probe for an existing CDP browser daemon (e.g., `http://127.0.0.1:9222`).
2. If reachable, inspect current cookies/tabs for `instagram.com`.
3. If an authenticated session exists, bind immediately.
4. This allows the investigator to run a browser in the background (`chromium --remote-debugging-port=9222`) logged into their zero-signal test account, and the agent attaches seamlessly.

## 4.1 Vault Discovery (Hermes / Harness MCP)

```text
1. If no active CDP session is bound, detect whether browser_vault_* tools are exposed.
2. If absent: proceed to 4.2a (Interactive Manual Login).
3. If present: call browser_vault_list.
4. Identify an Instagram login item bound to https://www.instagram.com.
5. If found, use browser_vault_fill to authenticate automatically.
```

## 4.2a Manual Login & Private Target Gate

When neither an active CDP session nor vault tooling is available:

```text
1. Open the login page in an isolated session (e.g. chromium with --remote-debugging-port=9222).
2. Prompt the user to log into their test/sock account.
3. Wait for the user to complete login.
4. Validate session state.
5. IF TARGET IS PRIVATE:
   - An authenticated session is MANDATORY to observe suggestion surfaces.
   - Do NOT fall back to public-only mode and declare an empty investigation.
   - Halt with BLOCKED_AUTH_REQUIRED if the user declines or fails to log in.
```

Never request, type, log, or store the password yourself.

## 4.3 Session Validation

Before investigation:
- verify the test account is logged in
- check for login challenges / 2FA requirements
- record session state

If the session becomes invalid during investigation:
- record partial observations
- stop and report session failure

## 4.4 Vault Guardrails

- never log or expose vault secret values
- never commit vault state to version control
- session cookies remain within the isolated Hermes browser session
- the vault handle is the authoritative credential reference

---



# 5. Browser Configuration

## 5.1 Required Setup

```text
browser: chromium or firefox via Hermes browser_exec
mode: headless or visible (user preference)
session: named isolated session per investigation
user_agent: standard desktop browser user agent
viewport: 1280x800 or larger
cookies: loaded from Hermes browser session after vault-backed login
```

## 5.2 Session Isolation

Use a named browser session for each investigation:

```python
browser_exec(
    code="...",
    session="instosint-<target_username>",
    timeout_s=240
)
```

This isolates tab state, cookies, and navigation from other work.

## 5.3 Anti-Detection

Instagram may detect automation. Use standard anti-detection:
- realistic user agent
- standard viewport size
- respect rate limits

Do NOT attempt to hide automation from Instagram if it violates
Instagram's Terms of Service.

## 5.4 Rate Limits

Respect Instagram's rate limits:
- minimum delay between page loads: 2-5 seconds
- minimum delay between profile observations: 1 hour
- randomize intervals where feasible
- stop immediately if blocked/challenged

---



# 6. Navigation Patterns

## 6.1 Profile Page

```python
new_tab("https://www.instagram.com/<target_username>/")
wait_for_load()
page = page_info()
print(page)
capture_screenshot()
```

Check for:
- login wall / private account notice
- suggestion block visibility
- public posts visibility
- blocked/challenged state

## 6.2 Suggestion Block Observation

```python
# After loading the profile page:
# 1. Scroll to suggestion block if needed
js('window.scrollTo(0, document.body.scrollHeight)')
wait_for_load()

# 2. Extract suggestion block content via JS
suggestions = js('''() => {
  // Inspect the actual DOM structure; adjust selectors to observed UI
  const results = [];
  const items = document.querySelectorAll('...suggestion selector...');
  items.forEach((item, index) => {
    const username = item.querySelector('...')?.textContent || '';
    const mutual = item.querySelector('...')?.textContent || '';
    const label = item.querySelector('...')?.textContent || '';
    results.push({ position: index + 1, username, mutual, label });
  });
  return results;
}''')
print(suggestions)
capture_screenshot()
```

Record:
- each suggested account username
- position in list
- mutual-connection count or NOT_VISIBLE
- context label or NOT_VISIBLE
- screenshot path

## 6.3 "Accounts You May Know" Surface

```python
new_tab("https://www.instagram.com/explore/")
wait_for_load()
page = page_info()
print(page)
capture_screenshot()
```

Locate the "Accounts you may know" section and extract the same features
as profile-page suggestions.

## 6.4 Public Post Inspection

```python
# Navigate to a specific public post if surfaced
new_tab("https://www.instagram.com/p/<post_shortcode>/")
wait_for_load()
page = page_info()
print(page)
capture_screenshot()

# Extract caption, comments, likes, mentions, tags
caption = js('''() => {
  const el = document.querySelector('...caption selector...');
  return el ? el.textContent : '';
}''')
comments = js('''() => {
  // Extract visible comment usernames and text
  const results = [];
  document.querySelectorAll('...comment selector...').forEach(c => {
    results.push(c.textContent.trim());
  });
  return results;
}''')
print({"caption": caption, "comments": comments})
```

---



# 7. Observation Protocol

## 7.1 Canonical Observation Record

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

## 7.2 Screenshot Evidence

When a screenshot is taken:
- save with timestamp and target in filename
- reference in the observation record
- treat as VISUAL_OBSERVATION evidence

Screenshots are evidence of what was visible at the time.
They are not evidence of what the content means.

---



# 8. Session Management

## 8.1 Session Loading via Vault

```text
1. Detect whether browser_vault_* tools are exposed.
2. If absent, record vault_tools: ABSENT and use manual login (8.1a).
3. Call browser_vault_list and identify the Instagram login handle.
4. If not found, request user action (save the login item) and continue in
   public-only mode if the user declines.
5. Navigate to the Instagram login page.
6. Fill the username field from the vault item.
7. Fill the password via browser_vault_fill.
8. Submit and wait for redirect.
9. Validate session state.
```

## 8.1a Manual Login Fallback

```text
1. Open the login page in an isolated session.
2. Ask the user to log in and complete 2FA in that session.
3. Wait a bounded time.
4. Validate session state.
5. If unauthenticated, record NOT_AUTHENTICATED and continue in public-only mode.
```

## 8.2 Session Validation

Before each investigation phase:
- verify the test account is logged in
- check for login challenges / 2FA requirements
- record session state

If the session becomes invalid during investigation:
- record partial observations
- stop and report session failure

## 8.3 Session Termination

When investigation is complete:
- do not manually log out unless requested
- close the browser session or navigate away
- session cookies remain in the isolated browser session until the
  session is terminated by Hermes or the user

---



# 9. Guardrails

## 9.1 Interaction Prohibitions

Do NOT:
- follow the target
- follow suggested accounts
- like posts
- comment on posts
- send DMs
- report accounts
- block accounts
- modify any account settings

## 9.2 Content Access Limits

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

## 9.3 Test Account Integrity

- do not follow the target during investigation
- do not interact with suggested accounts
- if accidental interaction occurs, record it and discard session
- create a fresh test account if the session is compromised

---



# 10. Fallback Behavior

If browser automation fails:
1. Record the failure mode
2. Fall back to raw HTTP if available
3. Fall back to web search if available
4. If all access methods fail, mark as BLOCKED_ACCESS

Do not retry failed browser sessions in a loop.
Increase wait time between retries.

Failure modes to record:
- vault item not found
- login failure
- 2FA challenge not completable
- session validation failure
- page load timeout
- Instagram block/challenge
- suggestion surface not visible

---



# 11. Evidence Handling

## 11.1 Screenshot Evidence

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
    screenshots/2026-10-02_target_suggestion_block.png
```

## 11.2 Browser Session Evidence

```text
SRC-BROWSER-001

Type:
    browser_session

Session:
    instosint-<target_username>

Login status:
    authenticated at timestamp

Vault-backed authentication:
    YES

Access method:
    browser_automation + vault_authentication
```

---



# 12. Investigation Flow with Browser Access

```text
TARGET
  ↓
VAULT CHECK (browser_vault_list)
  ├── NO ITEM → STOP, request user save/login
  └── ITEM FOUND → proceed
  ↓
BROWSER NAVIGATION (profile page)
  ↓
LOGIN IF NEEDED (vault fill + validation)
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



# 13. Security Considerations

## 13.1 Credential Safety

- session cookies and vault handles are sensitive credentials
- never log or expose passwords, cookies, or vault secret values
- never commit session files to version control
- the vault is the only authorized credential store

## 13.2 Test Account Isolation

- the test account should have no real personal data
- do not use a personal Instagram account
- if the test account is compromised, discard it

## 13.3 Legal and Terms of Service

- the user is responsible for complying with Instagram's Terms of Service
- INSTOSINT is a methodology; the user controls execution
- automated access may violate Instagram's ToS
- use at your own risk
