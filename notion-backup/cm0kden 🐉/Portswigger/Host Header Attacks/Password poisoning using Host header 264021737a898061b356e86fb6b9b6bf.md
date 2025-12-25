# Password poisoning using Host header

When sending password reset link, server insecurely using Host header to construct password reset link:

![image.png](Password%20poisoning%20using%20Host%20header/image.png)

![image.png](Password%20poisoning%20using%20Host%20header/image%201.png)

![image.png](Password%20poisoning%20using%20Host%20header/image%202.png)

![image.png](Password%20poisoning%20using%20Host%20header/image%203.png)

With this, we can setup a page that steals password reset token, host it via controllable domain, supply this domain to the /forgot-password endpoint triggering it for the target user. User then will click on malicious link and his token will be stolen.

Evil page:

![image.png](Password%20poisoning%20using%20Host%20header/image%204.png)

Submitting the request:

![image.png](Password%20poisoning%20using%20Host%20header/image%205.png)

Collaborator:

![image.png](Password%20poisoning%20using%20Host%20header/image%206.png)

Using hijacked token, we will reset the password and access target account.

![image.png](Password%20poisoning%20using%20Host%20header/image%207.png)