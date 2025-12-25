# Stealing other users requests using request smuggling

![image.png](Stealing%20other%20users%20requests%20using%20request%20smuggl/image.png)

![image.png](Stealing%20other%20users%20requests%20using%20request%20smuggl/image%201.png)

![image.png](Stealing%20other%20users%20requests%20using%20request%20smuggl/image%202.png)

---

### Lab solution

Confirming CL.TE vulnerability:

![image.png](Stealing%20other%20users%20requests%20using%20request%20smuggl/image%203.png)

Search functionality:

![image.png](Stealing%20other%20users%20requests%20using%20request%20smuggl/image%204.png)

![image.png](Stealing%20other%20users%20requests%20using%20request%20smuggl/image%205.png)

Making it a bit simplier

![image.png](Stealing%20other%20users%20requests%20using%20request%20smuggl/image%206.png)

Now let’s smuggle! Note: I’ve reordered the params so that comment comes at the end and no other params are missing

![image.png](Stealing%20other%20users%20requests%20using%20request%20smuggl/image%207.png)

Sent normal one

![image.png](Stealing%20other%20users%20requests%20using%20request%20smuggl/image%208.png)

What’s on a comment page:

![image.png](Stealing%20other%20users%20requests%20using%20request%20smuggl/image%209.png)

Now just adjust content length to gather more data:

![image.png](Stealing%20other%20users%20requests%20using%20request%20smuggl/image%2010.png)

Send a smuggle a few time and wait for the victim:

![image.png](Stealing%20other%20users%20requests%20using%20request%20smuggl/image%2011.png)

Solved

![image.png](Stealing%20other%20users%20requests%20using%20request%20smuggl/image%2012.png)