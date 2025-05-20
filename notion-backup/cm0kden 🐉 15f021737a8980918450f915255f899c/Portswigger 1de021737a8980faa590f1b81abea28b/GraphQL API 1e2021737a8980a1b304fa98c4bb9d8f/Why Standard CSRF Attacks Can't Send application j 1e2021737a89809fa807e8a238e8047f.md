# Why Standard CSRF Attacks Can't Send application/json (But Sometimes Can)

### 

---

### **1. Browser Restrictions (Default Barrier)**

Browsers enforce strict rules for cross-origin requests via HTML forms:

- **HTML forms can only send these `Content-Type` headers by default**:
    - `application/x-www-form-urlencoded` (default)
    - `multipart/form-data` (file uploads)
    - `text/plain` (rarely used)
- **They cannot natively send `application/json`**.

This means a traditional CSRF attack using `<form>` tags **cannot** send JSON data with the correct `Content-Type`.

---

### **2. Workarounds Attackers Use**

Despite the limitation, attackers bypass this in **three ways**:

### **A. `text/plain` Trick (Most Common)**

- **How it works**:
    - Set `enctype="text/plain"` in a `<form>`.
    - Craft input fields to mimic JSON structure.
    
    html
    

`<form action="https://api.example.com/graphql" method="POST" enctype="text/plain"><input name='{"query":"mutation {changeEmail(...)}","variables":{' value='{"email":"attacker@evil.com"}}'}' /></form>`

- Resulting request:
- 
    - `Content-Type: text/plain
    Body: {"query":"mutation {changeEmail(...)}","variables":{="attacker@evil.com"}}'}`
- **Why it sometimes works**:
    - Many servers **ignore** `Content-Type` and parse the body anyway.
    - GraphQL endpoints often use loose parsers (e.g., `express-graphql`).

### **B. Fetch API + CORS Misconfiguration**

- **If the server allows arbitrary origins (`Access-Control-Allow-Origin: *`)**:
    - Attacker can use JavaScript to send JSON:
    
    javascript
    
- `fetch("https://api.example.com/graphql", { method: "POST", headers: { "Content-Type": "application/json" }, body: JSON.stringify({ query: "mutation { ... }" }), credentials: "include" // Sends cookies
});`
- **Prerequisites**:
    - Poor CORS configuration.
    - Session cookies with `SameSite=None` (or no `SameSite`).

### **C. Flash Exploits (Historical)**

- Older browsers allowed Flash to send arbitrary headers (including `application/json`).
- Mostly irrelevant today (Flash is dead).

---

### **3. Why `application/json` CSRF is Still Rare**

1. **Strict Browser Policies**:
    - Modern browsers block cross-origin `application/json` requests unless CORS explicitly allows it.
2. **Server-Side Protections**:
    - Many APIs reject requests without the exact `Content-Type: application/json`.
3. **SameSite Cookies**:
    - Cookies with `SameSite=Lax` (default in modern browsers) block cross-site `POST` requests.

---

### **4. When JSON CSRF Works**

| Scenario | Possible? | Example Target Vulnerabilities |
| --- | --- | --- |
| Server ignores `Content-Type` | ✅ Yes | Legacy APIs, poorly coded GraphQL endpoints |
| CORS misconfigured (`*`) | ✅ Yes | APIs with `Access-Control-Allow-Origin: *` |
| SameSite=None cookies | ✅ Yes | Apps forcing `SameSite=None` for compatibility |
| Default browser behavior | ❌ No | Modern browsers + correct server checks |

---

### **How to Defend Against JSON CSRF**

1. **Require CSRF Tokens**
    - Even for `application/json` endpoints, include a token:
        
        graphql
        
2. 
    - `mutation { changeEmail(input: {email: "new@email.com"}, csrfToken: "RANDOM_STRING")
    }`
3. **Validate `Content-Type`**
    - Reject requests without `application/json`.
4. **Use `SameSite=Strict` Cookies**
    - Prevents cookies from being sent in cross-site requests.
5. **Check `Origin`/`Referer` Headers**
    - Block requests from unexpected domains.
6. **Disable CORS or Whitelist Origins**
    - Never use `Access-Control-Allow-Origin: *`.

---

### **Key Takeaway**

- **Standard CSRF attacks can't send `application/json` via HTML forms** due to browser restrictions.
- **But they can succeed if**:
    - The server ignores `Content-Type`.
    - CORS is misconfigured.
    - Cookies lack `SameSite` protections.
- **Defense is easy**: Use CSRF tokens + strict `Content-Type` validation.