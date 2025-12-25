# Basic Web cache deception attack

The Web cache agent sits between a user and a server.

The target server has a custom rule for a `.js` files. They are cached, and moreover, when arbitrary `file.js` extension is added to `/my-account` page, it gets abstracted from `/my-account/file.js` to `/my-account` . With this, we are able to craft a custom exploit to store victim’s profile page, send the request using XSS, and then view the cached page on our side.

![image.png](Basic%20Web%20cache%20deception%20attack/image.png)

![image.png](Basic%20Web%20cache%20deception%20attack/image%201.png)

![image.png](Basic%20Web%20cache%20deception%20attack/image%202.png)

```bash
<script>document.location="https://0aba0076043490ed853969e800720073.web-security-academy.net/my-account/exploit.js"</script>
```

After exploit delivery, we need to request this cached page on our side and receive a secret:

```jsx
https://0aba0076043490ed853969e800720073.web-security-academy.net/my-account/exploit.js
```

![image.png](Basic%20Web%20cache%20deception%20attack/image%203.png)