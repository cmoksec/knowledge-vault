# Reflected XSS into a JavaScript string with single quote and backslash escaped

This lab filters characters that may help to escape the output.

![image.png](Reflected%20XSS%20into%20a%20JavaScript%20string%20with%20single/image.png)

But there’s also another tracking script that reflects the value entered on search param.

![image.png](Reflected%20XSS%20into%20a%20JavaScript%20string%20with%20single/image%201.png)

Look at searchTerms var: seems like we can escape the variable, close the script and introduce a new one

![image.png](Reflected%20XSS%20into%20a%20JavaScript%20string%20with%20single/image%202.png)

![image.png](Reflected%20XSS%20into%20a%20JavaScript%20string%20with%20single/image%203.png)

![image.png](Reflected%20XSS%20into%20a%20JavaScript%20string%20with%20single/image%204.png)