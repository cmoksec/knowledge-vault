# Web cache poisoning: fat GET request

Fat GET request — get request with body

**Vulnerability Summary:**

The application caches responses based on the first `callback`
 parameter in the URL, but executes the last occurrence when duplicate 
parameters are provided via the request body. This discrepancy allows 
cache poisoning and XSS.

**Key Steps:**

1. **Identify Vulnerable Endpoint:**
    - The page imports `/js/geolocate.js`, which uses a `callback` parameter (default: `setCountryCookie`).
2. **Parameter Override via Request Body:**
    - The cache key is derived from the URL parameter (`callback=setCountryCookie`).
    - Duplicate `callback` parameters in the request body override the function in the response but are ignored in the cache key.
3. **Cache Poisoning:**
    - Request:
        
        `GET /js/geolocate.js?callback=setCountryCookie`
        
        with body (fat GET request): `callback=alert(1)`
        
    - Cache Key: `/js/geolocate.js?callback=setCountryCookie`
    - Response: Executes `alert(1)` instead of `setCountryCookie`.
4. **Impact:**
    - Poisoned cache serves the XSS payload to all users requesting the resource.
    - Victim triggers the alert when visiting any page importing the script.

![image.png](Web%20cache%20poisoning%20fat%20GET%20request/image.png)

![image.png](Web%20cache%20poisoning%20fat%20GET%20request/image%201.png)

![image.png](Web%20cache%20poisoning%20fat%20GET%20request/image%202.png)