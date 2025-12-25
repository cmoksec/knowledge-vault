# Web cache poisoning: param cloacking

**Key Steps:**

1. **Parameter Cloaking:**
    - The `utm_content` parameter is not included in the cache key.
    - Appending a semicolon (e.g., `utm_content=foo;callback=malicious`) allows arbitrary parameters to be smuggled without affecting the cache key.
2. **XSS via JavaScript Callback:**
    - The page imports `/js/geolocate.js`, which uses a `callback` parameter to execute a function (e.g., `setCountryCookie`).
    - Normally, `callback` is cache-keyed, but cloaking it via `utm_content` bypasses this.
3. **Cache Poisoning:**
    - Request:
        
        `GET /js/geolocate.js?callback=setCountryCookie&utm_content=foo;callback=alert(1)`
        
    - Cache Key: `/js/geolocate.js?callback=setCountryCookie` (ignores `utm_content`).
    - Response: Executes `alert(1)` instead of `setCountryCookie`.
4. **Impact:**
    - Poisoned cache serves the XSS payload to all users visiting the page, triggering the alert.
    - Requires continuous re-poisoning until the victim visits the page.

![image.png](Web%20cache%20poisoning%20param%20cloacking/image.png)

![image.png](Web%20cache%20poisoning%20param%20cloacking/image%201.png)

![image.png](Web%20cache%20poisoning%20param%20cloacking/image%202.png)