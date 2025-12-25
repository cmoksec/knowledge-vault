# XSS via cache poisoning (multiple headers)

Param finder found 2 headers: `X-Forwarded-Host` and `X-Forwarded-Scheme` . We will use it do direct the victim to the exploit server using cache poisoning.

First, observe this request for the js script.

![image.png](XSS%20via%20cache%20poisoning%20(multiple%20headers)/image.png)

Add `X-Forwarded-Scheme` with an example website and see that we get 302 instead

![image.png](XSS%20via%20cache%20poisoning%20(multiple%20headers)/image%201.png)

Now also add `X-Forwarded-Host` and see that we can direct a user to another URL

![image.png](XSS%20via%20cache%20poisoning%20(multiple%20headers)/image%202.png)

Deploy malicious script to the exploit server, point our request to the exploit server hosting that file.

![image.png](XSS%20via%20cache%20poisoning%20(multiple%20headers)/image%203.png)

![image.png](XSS%20via%20cache%20poisoning%20(multiple%20headers)/image%204.png)

Remove cache buster, poison the cache (X-Cache: hit), wait for the victim

![image.png](XSS%20via%20cache%20poisoning%20(multiple%20headers)/image%205.png)

![image.png](XSS%20via%20cache%20poisoning%20(multiple%20headers)/image%206.png)

![image.png](XSS%20via%20cache%20poisoning%20(multiple%20headers)/image%207.png)