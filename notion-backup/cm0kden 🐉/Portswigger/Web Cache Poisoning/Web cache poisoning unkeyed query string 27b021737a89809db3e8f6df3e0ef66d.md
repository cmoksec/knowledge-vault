# Web cache poisoning: unkeyed query string

In this lab, query parameters are not included in cache key, however they influence the response that is saved to the cache, making it possible to target normal users by infecting the cache.

![image.png](Web%20cache%20poisoning%20unkeyed%20query%20string/image.png)

We’ll accept the infection request twice and wait for the user to trigger the payload.

![image.png](Web%20cache%20poisoning%20unkeyed%20query%20string/image%201.png)

![image.png](Web%20cache%20poisoning%20unkeyed%20query%20string/image%202.png)