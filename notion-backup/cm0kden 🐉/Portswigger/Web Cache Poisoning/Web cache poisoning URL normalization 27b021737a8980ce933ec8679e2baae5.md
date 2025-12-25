# Web cache poisoning: URL normalization

**Vulnerability Summary:**

The application reflects the requested path in 404 error messages without 
proper encoding. By poisoning the cache with an XSS payload in the URL 
path, the payload is served to victims when they request the same path.

**Key Steps:**

1. **Identify Reflection Point:**
    - Requesting a non-existent path (e.g., `/random`) reflects the path in the error message.
2. **XSS Payload in Path:**
    - Direct browser requests URL-encode the path, preventing XSS execution.
    - Example payload: `/random</p><script>alert(1)</script><p>foo`
3. **Cache Poisoning:**
    - Send the unencoded XSS payload directly via Repeater to poison the cache.
    - The cache stores the raw HTML response containing the active script.
4. **Exploitation:**
    - When a victim visits the same URL, the cache serves the poisoned response.
    - The victim's browser receives the unencoded payload, executing the XSS.

![image.png](Web%20cache%20poisoning%20URL%20normalization/image.png)

![image.png](Web%20cache%20poisoning%20URL%20normalization/image%201.png)

![image.png](Web%20cache%20poisoning%20URL%20normalization/image%202.png)