# Stored XSS into onclick event with angle brackets and double quotes HTML-encoded and single quotes and backslash escaped

This lab reflects the URL we paste as a author’s website when leaving a comment.

![Снимок экрана 2025-11-18 в 10.59.05.png](Stored%20XSS%20into%20onclick%20event%20with%20angle%20brackets%20/%D0%A1%D0%BD%D0%B8%D0%BC%D0%BE%D0%BA_%D1%8D%D0%BA%D1%80%D0%B0%D0%BD%D0%B0_2025-11-18_%D0%B2_10.59.05.png)

![Снимок экрана 2025-11-18 в 10.59.18.png](Stored%20XSS%20into%20onclick%20event%20with%20angle%20brackets%20/%D0%A1%D0%BD%D0%B8%D0%BC%D0%BE%D0%BA_%D1%8D%D0%BA%D1%80%D0%B0%D0%BD%D0%B0_2025-11-18_%D0%B2_10.59.18.png)

So we basically need to escape single quote in var tracker initialization and perform JS injection. The problem is, backend handles payloads pretty well, single quotes get escaped, as well as double quotes HTML-encoded etc.

![Снимок экрана 2025-11-18 в 11.02.46.png](Stored%20XSS%20into%20onclick%20event%20with%20angle%20brackets%20/%D0%A1%D0%BD%D0%B8%D0%BC%D0%BE%D0%BA_%D1%8D%D0%BA%D1%80%D0%B0%D0%BD%D0%B0_2025-11-18_%D0%B2_11.02.46.png)

The thing is, escaping is done manually, and there’s a big chance that the developer missed some specific case. And in this lab, this case is obfuscating the payload by performing HTML-encoding.

![Снимок экрана 2025-11-18 в 11.07.05.png](Stored%20XSS%20into%20onclick%20event%20with%20angle%20brackets%20/%D0%A1%D0%BD%D0%B8%D0%BC%D0%BE%D0%BA_%D1%8D%D0%BA%D1%80%D0%B0%D0%BD%D0%B0_2025-11-18_%D0%B2_11.07.05.png)

![Снимок экрана 2025-11-18 в 11.06.55.png](Stored%20XSS%20into%20onclick%20event%20with%20angle%20brackets%20/%D0%A1%D0%BD%D0%B8%D0%BC%D0%BE%D0%BA_%D1%8D%D0%BA%D1%80%D0%B0%D0%BD%D0%B0_2025-11-18_%D0%B2_11.06.55.png)

![Снимок экрана 2025-11-18 в 11.07.47.png](Stored%20XSS%20into%20onclick%20event%20with%20angle%20brackets%20/%D0%A1%D0%BD%D0%B8%D0%BC%D0%BE%D0%BA_%D1%8D%D0%BA%D1%80%D0%B0%D0%BD%D0%B0_2025-11-18_%D0%B2_11.07.47.png)

![Снимок экрана 2025-11-18 в 11.08.05.png](Stored%20XSS%20into%20onclick%20event%20with%20angle%20brackets%20/%D0%A1%D0%BD%D0%B8%D0%BC%D0%BE%D0%BA_%D1%8D%D0%BA%D1%80%D0%B0%D0%BD%D0%B0_2025-11-18_%D0%B2_11.08.05.png)

![Снимок экрана 2025-11-18 в 11.08.19.png](Stored%20XSS%20into%20onclick%20event%20with%20angle%20brackets%20/%D0%A1%D0%BD%D0%B8%D0%BC%D0%BE%D0%BA_%D1%8D%D0%BA%D1%80%D0%B0%D0%BD%D0%B0_2025-11-18_%D0%B2_11.08.19.png)

Solved