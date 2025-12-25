# Stealing OAuth Access token via Open Redirect

There’s an open redirect vulnerability in the app

![image.png](Stealing%20OAuth%20Access%20token%20via%20Open%20Redirect/image.png)

As for the OAuth flow, app validates the redirect_url param to only lead to the current domain. But with an open redirect, we can route to the evil server and collect the token using JS script.

![image.png](Stealing%20OAuth%20Access%20token%20via%20Open%20Redirect/image%201.png)

Use Open Redirect (with path traversal trailings)

![image.png](Stealing%20OAuth%20Access%20token%20via%20Open%20Redirect/image%202.png)

Now craft CSRF payload and send to the victim

![image.png](Stealing%20OAuth%20Access%20token%20via%20Open%20Redirect/image%203.png)

![image.png](Stealing%20OAuth%20Access%20token%20via%20Open%20Redirect/image%204.png)

![image.png](Stealing%20OAuth%20Access%20token%20via%20Open%20Redirect/image%205.png)