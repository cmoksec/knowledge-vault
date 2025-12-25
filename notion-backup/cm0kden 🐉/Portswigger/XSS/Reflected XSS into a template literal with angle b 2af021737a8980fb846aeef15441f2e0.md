# Reflected XSS into a template literal with angle brackets, single, double quotes, backslash and backticks Unicode-escaped

This lab uses something called ‘backticks’, which we can spot if we search for a canary string: 

![Снимок экрана 2025-11-18 в 11.41.38.png](Reflected%20XSS%20into%20a%20template%20literal%20with%20angle%20b/%D0%A1%D0%BD%D0%B8%D0%BC%D0%BE%D0%BA_%D1%8D%D0%BA%D1%80%D0%B0%D0%BD%D0%B0_2025-11-18_%D0%B2_11.41.38.png)

![Снимок экрана 2025-11-18 в 11.43.25.png](Reflected%20XSS%20into%20a%20template%20literal%20with%20angle%20b/%D0%A1%D0%BD%D0%B8%D0%BC%D0%BE%D0%BA_%D1%8D%D0%BA%D1%80%D0%B0%D0%BD%D0%B0_2025-11-18_%D0%B2_11.43.25.png)

![Снимок экрана 2025-11-18 в 11.44.26.png](Reflected%20XSS%20into%20a%20template%20literal%20with%20angle%20b/%D0%A1%D0%BD%D0%B8%D0%BC%D0%BE%D0%BA_%D1%8D%D0%BA%D1%80%D0%B0%D0%BD%D0%B0_2025-11-18_%D0%B2_11.44.26.png)

https://popalltheshells.medium.com/xss-escape-backticks-strings-template-literals-92b3f31b37a8

So all we need to do is repeat the same thing mentioned on this article:

```jsx
${alert(1)}
```

![Снимок экрана 2025-11-18 в 11.45.33.png](Reflected%20XSS%20into%20a%20template%20literal%20with%20angle%20b/%D0%A1%D0%BD%D0%B8%D0%BC%D0%BE%D0%BA_%D1%8D%D0%BA%D1%80%D0%B0%D0%BD%D0%B0_2025-11-18_%D0%B2_11.45.33.png)