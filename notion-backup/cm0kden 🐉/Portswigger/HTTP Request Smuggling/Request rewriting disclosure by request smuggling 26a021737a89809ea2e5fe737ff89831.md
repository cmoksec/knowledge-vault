# Request rewriting disclosure by request smuggling

![image.png](Request%20rewriting%20disclosure%20by%20request%20smuggling/image.png)

![image.png](Request%20rewriting%20disclosure%20by%20request%20smuggling/image%201.png)

![image.png](Request%20rewriting%20disclosure%20by%20request%20smuggling/image%202.png)

---

### Lab solution

Search functionality

![image.png](Request%20rewriting%20disclosure%20by%20request%20smuggling/image%203.png)

The search criterion is reflecting on a response

![image.png](Request%20rewriting%20disclosure%20by%20request%20smuggling/image%204.png)

The application reportedly has CL.TE vulnerability:

![image.png](Request%20rewriting%20disclosure%20by%20request%20smuggling/image%205.png)

We’ll use request smuggling to understand how frontend rewrites the request.

![image.png](Request%20rewriting%20disclosure%20by%20request%20smuggling/image%206.png)

![image.png](Request%20rewriting%20disclosure%20by%20request%20smuggling/image%207.png)

As a result, we found hidden header that may be used to utilize unauthorized access to admin panel.

![image.png](Request%20rewriting%20disclosure%20by%20request%20smuggling/image%208.png)

![image.png](Request%20rewriting%20disclosure%20by%20request%20smuggling/image%209.png)

Solved

![image.png](Request%20rewriting%20disclosure%20by%20request%20smuggling/image%2010.png)