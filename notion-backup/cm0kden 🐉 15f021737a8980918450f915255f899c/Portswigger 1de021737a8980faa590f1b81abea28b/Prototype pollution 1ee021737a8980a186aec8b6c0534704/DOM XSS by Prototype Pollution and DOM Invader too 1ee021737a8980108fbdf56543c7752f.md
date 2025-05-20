# DOM XSS by Prototype Pollution and DOM Invader tool

A script in a website is dynamically appending a script, if transport_url property is set. It is a prototype pollution vulnerability.

![image.png](DOM%20XSS%20by%20Prototype%20Pollution%20and%20DOM%20Invader%20too%201ee021737a8980108fbdf56543c7752f/image.png)

With DOM Invader enabled, browse through the website and notice a sink identified.

![image.png](DOM%20XSS%20by%20Prototype%20Pollution%20and%20DOM%20Invader%20too%201ee021737a8980108fbdf56543c7752f/image%201.png)

Then, click Scan for gadgets to automatically probe for malicious gadget payloads to take effect.

![image.png](DOM%20XSS%20by%20Prototype%20Pollution%20and%20DOM%20Invader%20too%201ee021737a8980108fbdf56543c7752f/image%202.png)

By injecting a property using URL parameter, we achieved the XSS.