# SSRF via flawed request parsing

When you try to amend Host header to a controlled resource, it gets forbidden by some sort of network security solution:

![image.png](SSRF%20via%20flawed%20request%20parsing/image.png)

![image.png](SSRF%20via%20flawed%20request%20parsing/image%201.png)

But when we supply absolute URL on the requested domain, this security solution thinks this is a legitimate target, and allows the request to come through, even with a malicious Host header. And later on, after passing this secure perimeter, another system gets the request (most probably some kind of reverse proxy that can resolve DNS records), and treats is differently — it considers Host header as a priority and forwards the request to the location specified in a Host header.

![image.png](SSRF%20via%20flawed%20request%20parsing/image%202.png)

This gives us the opportunity to run SSRF attack.

![image.png](SSRF%20via%20flawed%20request%20parsing/image%203.png)

![image.png](SSRF%20via%20flawed%20request%20parsing/image%204.png)

Local admin panel successfully accessed:

![image.png](SSRF%20via%20flawed%20request%20parsing/image%205.png)

Delete the user by supplying username and csrf token:

![image.png](SSRF%20via%20flawed%20request%20parsing/image%206.png)

![image.png](SSRF%20via%20flawed%20request%20parsing/image%207.png)