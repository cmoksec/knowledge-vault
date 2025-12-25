# Detecting TE.CL methodology

We will take 1st payload for the detection purposes

![image.png](image.png)

### Understanding the probing payload

![image.png](Detecting%20CL%20TE%20methodology/image.png)

```xml
POST / HTTP/1.1
Host: 0a03000604f73bd78145459f00ec005e.web-security-academy.net
Content-Type: application/x-www-form-urlencoded
Content-Length: 6
Transfer-Encoding: chunked

3
abc
X
```

1 - HTTP protocol is downgraded to version 1.1 because HTTP 2 is immune to smuggling attacks (except the case when the protocol downgrade is performed)

2 - Both Content-Length and Transfer-Encoding headers are used here, to confuse different systems (more about [Transfer-Encoding](https://ru.hexlet.io/courses/http_protocol/lessons/chunked/theory_unit)). Chunks are built on the following pattern:

```xml
<chunk length in HEX, e.g. 3> <**\r\n** aka CRLF> <chunk content> <\r\n aka CRLF>
```

3 - `\r\n` is a special sequence also known as **CRLF**, that means new line in HTTP protocol. Body must be always separated from the headers by `\r\n` , which is done on line 6

![image.png](Detecting%20CL%20TE%20methodology/image%201.png)

4 - Number `3` in line 7 says “we are sending a chunk of 3 bytes”

5 - Contents of the chunk itself (abc)

6 - `X` is an invalid character, that cannot be interpreted as a HEX byte length, so it immediately causes the frontend (the system that uses TE method) to throw an error out of confusion. This will confirm that the frontend uses Transfer-Encoding

![image.png](Detecting%20TE%20CL%20methodology/image.png)

7 - Next, we need to figure out which header is honored on the backend. For this, we will use the 2nd payload from the scheme:

![image.png](Detecting%20TE%20CL%20methodology/image%201.png)

```xml
POST / HTTP/1.1
Host: 0ab90042048475618004052f004d0095.web-security-academy.net
Content-Type: application/x-www-form-urlencoded
Content-Length: 6
Transfer-Encoding: chunked

0

X
```

What’s happening is:

Frontend, that uses Transfer-Encoding, is cutting off character `X` as he sees a terminating chunk. But the backend, that uses CL, has received a length of 6, but only 5 bytes have came, so it’s confused and it starts to wait for the rest of the message to come. After not receiving the last byte, it’s throwing a timeout error.

![image.png](Detecting%20TE%20CL%20methodology/image%202.png)

With this, it’s enough to state that the system has [TE.CL](http://TE.CL) vulnerability, because we confirmed which methods both of the systems use.

[Lab: HTTP request smuggling, basic TE.CL vulnerability](https://www.youtube.com/watch?v=kIRIV-BwBTE&t=855s)