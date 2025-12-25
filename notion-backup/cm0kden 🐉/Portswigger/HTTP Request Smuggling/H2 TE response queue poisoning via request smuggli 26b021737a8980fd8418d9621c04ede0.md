# H2.TE response queue poisoning via request smuggling

![image.png](H2%20TE%20response%20queue%20poisoning%20via%20request%20smuggli/image.png)

This time, we’ll trick the server to mess up response order. But first, let’s confirm desync:

![image.png](H2%20TE%20response%20queue%20poisoning%20via%20request%20smuggli/image%201.png)

Every second request you send receives a 404 response, confirming that you have caused the back-end to append the subsequent request to the smuggled prefix. 

In Burp Repeater, create the following request, which smuggles a complete request to the back-end server. Note that the path in both requests points to a non-existent endpoint. This means that your request will always get a 404 response. Once you have poisoned the response queue, this will make it easier to recognize any other users' responses that you have successfully captured.

Let’s utilize Intruder to automate an attack. The admin bot is simulating login each 15 secs, when we’ll receive 200 instead of 404, it means server was confused by the smuggled request, and returned the admin response instead of 404 page.

Also NOTE that two \r\n after the smuggled request are very important, because they make a smuggled request RFC-compliant and it’s treated as finished on the backend, and because of that we have 2 reponses. We also made each main request line to try for the nonexistent page, which will always result in 404 error, making it easier to spot any deviation.

```xml
POST /nonexistent HTTP/2
Host: YOUR-LAB-ID.web-security-academy.net
Transfer-Encoding: chunked

0

GET /nonexistent HTTP/1.1
Host: YOUR-LAB-ID.web-security-academy.net
```

![image.png](H2%20TE%20response%20queue%20poisoning%20via%20request%20smuggli/image%202.png)

We stole the admin session successfully:

![image.png](H2%20TE%20response%20queue%20poisoning%20via%20request%20smuggli/image%203.png)

Now just login and delete carlos.

![image.png](H2%20TE%20response%20queue%20poisoning%20via%20request%20smuggli/image%204.png)

[Lab: Response Queue Poisoning via H2.TE request smuggling](https://www.youtube.com/watch?v=PeYdUHME7e8)