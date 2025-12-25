# Reflected XSS in canonical link tag

On this lab, the hypothetical attack is shown, with the canonical link — an element that is located in a head of html page, therefore not accessible physically for a user. However, there’s a way in Chrome to interact with certain elements by providing accesskeys attribute. With the provided information that the victim always presses ‘X’, We will inject accesskeys=’x’ with the payload itself to get triggered.

Obscure and unlikely vector, but anyways.

```jsx
https://0a4600fe03e98484817ba7b900b500e2.web-security-academy.net/?'accesskey='x'onclick='alert(1)
```

![Снимок экрана 2025-11-14 в 16.24.33.png](Reflected%20XSS%20in%20canonical%20link%20tag/%D0%A1%D0%BD%D0%B8%D0%BC%D0%BE%D0%BA_%D1%8D%D0%BA%D1%80%D0%B0%D0%BD%D0%B0_2025-11-14_%D0%B2_16.24.33.png)