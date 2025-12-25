# Reflected XSS into HTML context with most tags and attributes blocked

![image.png](Reflected%20XSS%20into%20HTML%20context%20with%20most%20tags%20and/image.png)

Fuzz using XSS Cheatsheet

First, copy tags

![image.png](Reflected%20XSS%20into%20HTML%20context%20with%20most%20tags%20and/image%201.png)

Then simplify initial request

![image.png](Reflected%20XSS%20into%20HTML%20context%20with%20most%20tags%20and/image%202.png)

And run intruder

![image.png](Reflected%20XSS%20into%20HTML%20context%20with%20most%20tags%20and/image%203.png)

`<body>` is not being filtered

Now, run fuzz check for event handlers

![image.png](Reflected%20XSS%20into%20HTML%20context%20with%20most%20tags%20and/image%204.png)

![image.png](Reflected%20XSS%20into%20HTML%20context%20with%20most%20tags%20and/image%205.png)

And we found a bunch of allowed ones

![image.png](Reflected%20XSS%20into%20HTML%20context%20with%20most%20tags%20and/image%206.png)

We will take onresize and construct an attack

![image.png](Reflected%20XSS%20into%20HTML%20context%20with%20most%20tags%20and/image%207.png)

![image.png](Reflected%20XSS%20into%20HTML%20context%20with%20most%20tags%20and/image%208.png)

![image.png](Reflected%20XSS%20into%20HTML%20context%20with%20most%20tags%20and/image%209.png)