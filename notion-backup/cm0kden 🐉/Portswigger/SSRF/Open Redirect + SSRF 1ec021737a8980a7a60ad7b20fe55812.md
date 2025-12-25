# Open Redirect + SSRF

Take a look at below. The app is carelessly taking path value and putting it into the Location header, triggering a redirect.

![image.png](Open%20Redirect%20+%20SSRF/image.png)

Let’s try some arbitrary website to redirect to.

![image.png](Open%20Redirect%20+%20SSRF/image%201.png)

This is a clear Open Redirect vulnerability.

Paired the SSRF vulnerability, even though the domain is prefixed on backend, we can access internal endpoints.

![image.png](Open%20Redirect%20+%20SSRF/image%202.png)