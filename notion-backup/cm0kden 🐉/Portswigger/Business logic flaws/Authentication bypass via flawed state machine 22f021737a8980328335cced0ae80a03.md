# Authentication bypass via flawed state machine

Example: an application has a functionality that asks what’s your role once you’re logged in.

![image.png](Authentication%20bypass%20via%20flawed%20state%20machine/image.png)

This happens by doing such call

![image.png](Authentication%20bypass%20via%20flawed%20state%20machine/image%201.png)

But if the request is **dropped** (using Drop button in Burp) and not executed, user’s role gets defaulted to the administrator:

![image.png](Authentication%20bypass%20via%20flawed%20state%20machine/image%202.png)