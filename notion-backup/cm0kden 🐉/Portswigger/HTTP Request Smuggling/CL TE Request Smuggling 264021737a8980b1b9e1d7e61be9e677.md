# CL.TE Request Smuggling

Below is the vulnerability payload

```yaml
Content-Length: 6
Transfer-Encoding: chunked

0

G
```

Frontend uses Content Length to understand method length, while backend uses chunks via Transfer-Encoding header.  When 1st request is sent, frontend sends full message as-is, but backend reads chunking and separates “G” symbol as part of the next package. When the next package comes, “G” gets appended to the 1st row, resulting in a “GPOST” method, which causes the error on backend.

NOTE: HTTP protocol must be downgraded in Burp Inspector:

![image.png](CL%20TE%20Request%20Smuggling/image.png)

![image.png](CL%20TE%20Request%20Smuggling/image%201.png)

![image.png](CL%20TE%20Request%20Smuggling/image%202.png)