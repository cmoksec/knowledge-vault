# XSS+ via Request smuggling

![image.png](XSS+%20via%20Request%20smuggling/image.png)

---

### Lab Solution

The application is vulnerable to Reflected XSS via User-Agent header:

![image.png](XSS+%20via%20Request%20smuggling/image%201.png)

![image.png](XSS+%20via%20Request%20smuggling/image%202.png)

Also it’s vulnerable to CL.TE:

![image.png](XSS+%20via%20Request%20smuggling/image%203.png)

We’ll smuggle a request to deliver poisoned User-Agent request to the user:

![image.png](XSS+%20via%20Request%20smuggling/image%204.png)

Done - ANY request from a legitimate user causes an XSS. This type of attack is very dangerous because it doesn’t need any interaction with the victim for a payload to be delivered.

![image.png](XSS+%20via%20Request%20smuggling/image%205.png)

![image.png](XSS+%20via%20Request%20smuggling/image%206.png)