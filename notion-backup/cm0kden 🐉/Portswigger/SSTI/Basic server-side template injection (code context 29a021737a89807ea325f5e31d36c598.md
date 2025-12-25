# Basic server-side template injection (code context)

Spot suspicious function

![Снимок экрана 2025-10-28 в 14.06.06.png](Basic%20server-side%20template%20injection%20(code%20context/%D0%A1%D0%BD%D0%B8%D0%BC%D0%BE%D0%BA_%D1%8D%D0%BA%D1%80%D0%B0%D0%BD%D0%B0_2025-10-28_%D0%B2_14.06.06.png)

blog-post-author-display looks promising, investigate

![Снимок экрана 2025-10-28 в 14.06.42.png](Basic%20server-side%20template%20injection%20(code%20context/%D0%A1%D0%BD%D0%B8%D0%BC%D0%BE%D0%BA_%D1%8D%D0%BA%D1%80%D0%B0%D0%BD%D0%B0_2025-10-28_%D0%B2_14.06.42.png)

When commenting posts being authorized, we can spot our name being rendered

![Снимок экрана 2025-10-28 в 14.08.31.png](Basic%20server-side%20template%20injection%20(code%20context/%D0%A1%D0%BD%D0%B8%D0%BC%D0%BE%D0%BA_%D1%8D%D0%BA%D1%80%D0%B0%D0%BD%D0%B0_2025-10-28_%D0%B2_14.08.31.png)

And this is after changing blog-post-author-display to nickname. Clearly a server side template rendering

![Снимок экрана 2025-10-28 в 14.09.17.png](Basic%20server-side%20template%20injection%20(code%20context/%D0%A1%D0%BD%D0%B8%D0%BC%D0%BE%D0%BA_%D1%8D%D0%BA%D1%80%D0%B0%D0%BD%D0%B0_2025-10-28_%D0%B2_14.09.17.png)

Research manually using polyglot, spot error disclosure

![Снимок экрана 2025-10-28 в 14.13.51.png](Basic%20server-side%20template%20injection%20(code%20context/%D0%A1%D0%BD%D0%B8%D0%BC%D0%BE%D0%BA_%D1%8D%D0%BA%D1%80%D0%B0%D0%BD%D0%B0_2025-10-28_%D0%B2_14.13.51.png)

![Снимок экрана 2025-10-28 в 14.14.38.png](Basic%20server-side%20template%20injection%20(code%20context/%D0%A1%D0%BD%D0%B8%D0%BC%D0%BE%D0%BA_%D1%8D%D0%BA%D1%80%D0%B0%D0%BD%D0%B0_2025-10-28_%D0%B2_14.14.38.png)

Engine is tornado, search for payload

![Снимок экрана 2025-10-28 в 14.17.00.png](Basic%20server-side%20template%20injection%20(code%20context/%D0%A1%D0%BD%D0%B8%D0%BC%D0%BE%D0%BA_%D1%8D%D0%BA%D1%80%D0%B0%D0%BD%D0%B0_2025-10-28_%D0%B2_14.17.00.png)

![Снимок экрана 2025-10-28 в 14.17.11.png](Basic%20server-side%20template%20injection%20(code%20context/%D0%A1%D0%BD%D0%B8%D0%BC%D0%BE%D0%BA_%D1%8D%D0%BA%D1%80%D0%B0%D0%BD%D0%B0_2025-10-28_%D0%B2_14.17.11.png)

This is code context, search for Object through mro

![Снимок экрана 2025-10-28 в 14.23.17.png](Basic%20server-side%20template%20injection%20(code%20context/%D0%A1%D0%BD%D0%B8%D0%BC%D0%BE%D0%BA_%D1%8D%D0%BA%D1%80%D0%B0%D0%BD%D0%B0_2025-10-28_%D0%B2_14.23.17.png)

![Снимок экрана 2025-10-28 в 14.23.56.png](Basic%20server-side%20template%20injection%20(code%20context/%D0%A1%D0%BD%D0%B8%D0%BC%D0%BE%D0%BA_%D1%8D%D0%BA%D1%80%D0%B0%D0%BD%D0%B0_2025-10-28_%D0%B2_14.23.56.png)

Goes 2nd

![Снимок экрана 2025-10-28 в 14.25.25.png](Basic%20server-side%20template%20injection%20(code%20context/%D0%A1%D0%BD%D0%B8%D0%BC%D0%BE%D0%BA_%D1%8D%D0%BA%D1%80%D0%B0%D0%BD%D0%B0_2025-10-28_%D0%B2_14.25.25.png)

![Снимок экрана 2025-10-28 в 14.25.53.png](Basic%20server-side%20template%20injection%20(code%20context/%D0%A1%D0%BD%D0%B8%D0%BC%D0%BE%D0%BA_%D1%8D%D0%BA%D1%80%D0%B0%D0%BD%D0%B0_2025-10-28_%D0%B2_14.25.53.png)

We will use file gadget

![Снимок экрана 2025-10-28 в 14.27.43.png](Basic%20server-side%20template%20injection%20(code%20context/%D0%A1%D0%BD%D0%B8%D0%BC%D0%BE%D0%BA_%D1%8D%D0%BA%D1%80%D0%B0%D0%BD%D0%B0_2025-10-28_%D0%B2_14.27.43.png)

![Снимок экрана 2025-10-28 в 14.29.43.png](Basic%20server-side%20template%20injection%20(code%20context/%D0%A1%D0%BD%D0%B8%D0%BC%D0%BE%D0%BA_%D1%8D%D0%BA%D1%80%D0%B0%D0%BD%D0%B0_2025-10-28_%D0%B2_14.29.43.png)

It is working now, so just execute file deletion as per lab description. Super cool project for finding payload https://github.com/p0dalirius/objectwalker

---

Actually, I got no luck with file, so I just escaped the context and gained RCE

![Снимок экрана 2025-10-28 в 14.50.13.png](Basic%20server-side%20template%20injection%20(code%20context/%D0%A1%D0%BD%D0%B8%D0%BC%D0%BE%D0%BA_%D1%8D%D0%BA%D1%80%D0%B0%D0%BD%D0%B0_2025-10-28_%D0%B2_14.50.13.png)

![Снимок экрана 2025-10-28 в 14.50.34.png](Basic%20server-side%20template%20injection%20(code%20context/%D0%A1%D0%BD%D0%B8%D0%BC%D0%BE%D0%BA_%D1%8D%D0%BA%D1%80%D0%B0%D0%BD%D0%B0_2025-10-28_%D0%B2_14.50.34.png)

![Снимок экрана 2025-10-28 в 14.51.37.png](Basic%20server-side%20template%20injection%20(code%20context/%D0%A1%D0%BD%D0%B8%D0%BC%D0%BE%D0%BA_%D1%8D%D0%BA%D1%80%D0%B0%D0%BD%D0%B0_2025-10-28_%D0%B2_14.51.37.png)

![Снимок экрана 2025-10-28 в 14.51.49.png](Basic%20server-side%20template%20injection%20(code%20context/%D0%A1%D0%BD%D0%B8%D0%BC%D0%BE%D0%BA_%D1%8D%D0%BA%D1%80%D0%B0%D0%BD%D0%B0_2025-10-28_%D0%B2_14.51.49.png)