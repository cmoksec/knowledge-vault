# Reflected XSS into a JavaScript string with angle brackets and double quotes HTML-encoded and single quotes escaped

In this lab, quotes get escaped using backslash `\` 

![image.png](Reflected%20XSS%20into%20a%20JavaScript%20string%20with%20angle%20/image.png)

But guess what? We can escape backslash using backslash, and this way, the quote after it will close the initial one

![image.png](Reflected%20XSS%20into%20a%20JavaScript%20string%20with%20angle%20/image%201.png)

We will also insert `//`  to comment out the rest, add `-` and paste our payload.

Why do we need `-` ? Awesome question. This is because JS syntax must initialize variable in which we are performing an injection, and we are adding `-` so that the whole expression gets:

```xml
var searchTerms = 'somestring' - alert(1) //alert(1) is undefined
```

So any arithmetic sign will also work here!  

![image.png](Reflected%20XSS%20into%20a%20JavaScript%20string%20with%20angle%20/image%202.png)

![image.png](Reflected%20XSS%20into%20a%20JavaScript%20string%20with%20angle%20/image%203.png)

![image.png](Reflected%20XSS%20into%20a%20JavaScript%20string%20with%20angle%20/image%204.png)