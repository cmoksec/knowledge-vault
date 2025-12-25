# CL.0 Request smuggling

We have a lab, whose frontend has a protection against accessing /admin endpoint. However, seems like backend is blindly accepting any request to admin panel if it came from the frontend. That means, using request smuggling, we can force the backend to issue a response for a smuggled request, so that we can access admin functionality.

![image.png](CL%200%20Request%20smuggling/image.png)

For this lab, we will use an endpoint that ignores Content-Length, basically allowing anything to be transferred in the body.

![image.png](CL%200%20Request%20smuggling/image%201.png)

To successfully exploit that, we will need to follow below scheme:

![image.png](CL%200%20Request%20smuggling/image%202.png)

First, find a request for a static file

![image.png](CL%200%20Request%20smuggling/image%203.png)

Turn it to POST request and remove unnecessary headers

![image.png](CL%200%20Request%20smuggling/image%204.png)

We still get 200 OK, meaning we can proceed

Construct the attack request, don’t forget to downgrade to HTTP 1.1, enable HTTP 1.1 connection reuse:

![image.png](CL%200%20Request%20smuggling/image%205.png)

Add normal request, create group with attack request, make sure both use HTTP/1.1

![image.png](CL%200%20Request%20smuggling/image%206.png)

Send a sequence via the same connection

And we successfully smuggled our request

![image.png](CL%200%20Request%20smuggling/image%207.png)

Now, just amend the smuggled request to access admin page, and delete carlos to solve the lab

![image.png](CL%200%20Request%20smuggling/image%208.png)

![image.png](CL%200%20Request%20smuggling/image%209.png)

Trigger deletion