# XSS via cache poisoning (header)

The lab is given. First, we run Param Miner, it will report findings to Issues tab (Burp Pro) or to Output (Community)

![image.png](XSS%20via%20cache%20poisoning%20(header)/image.png)

![image.png](XSS%20via%20cache%20poisoning%20(header)/image%201.png)

![image.png](XSS%20via%20cache%20poisoning%20(header)/image%202.png)

We found a secret input: X-Forwarded-Host header. Let’s try it to see if it’s reflected on a page:

![image.png](XSS%20via%20cache%20poisoning%20(header)/image%203.png)

Confirmed. Now, using simple escapes, we will perform XSS:

![image.png](XSS%20via%20cache%20poisoning%20(header)/image%204.png)

![image.png](XSS%20via%20cache%20poisoning%20(header)/image%205.png)

Amend the script to show alert(document.cookie)

![image.png](XSS%20via%20cache%20poisoning%20(header)/image%206.png)

Replay the request to poison the cache, wait until bot triggers the payload:

![image.png](XSS%20via%20cache%20poisoning%20(header)/image%207.png)

![image.png](XSS%20via%20cache%20poisoning%20(header)/image%208.png)