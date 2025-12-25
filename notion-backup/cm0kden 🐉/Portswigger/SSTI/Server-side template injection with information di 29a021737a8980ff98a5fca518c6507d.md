# Server-side template injection with information disclosure via user-supplied objects

To solve the lab, steal and submit the framework's secret key.

Using creds to login as content editor

We can edit templates

![Снимок экрана 2025-10-28 в 15.18.14.png](Server-side%20template%20injection%20with%20information%20di/%D0%A1%D0%BD%D0%B8%D0%BC%D0%BE%D0%BA_%D1%8D%D0%BA%D1%80%D0%B0%D0%BD%D0%B0_2025-10-28_%D0%B2_15.18.14.png)

Quick investigation did not work, lauching fuzz

![Снимок экрана 2025-10-28 в 15.19.49.png](Server-side%20template%20injection%20with%20information%20di/%D0%A1%D0%BD%D0%B8%D0%BC%D0%BE%D0%BA_%D1%8D%D0%BA%D1%80%D0%B0%D0%BD%D0%B0_2025-10-28_%D0%B2_15.19.49.png)

![Снимок экрана 2025-10-28 в 15.19.19.png](Server-side%20template%20injection%20with%20information%20di/%D0%A1%D0%BD%D0%B8%D0%BC%D0%BE%D0%BA_%D1%8D%D0%BA%D1%80%D0%B0%D0%BD%D0%B0_2025-10-28_%D0%B2_15.19.19.png)

![Снимок экрана 2025-10-28 в 15.25.51.png](Server-side%20template%20injection%20with%20information%20di/%D0%A1%D0%BD%D0%B8%D0%BC%D0%BE%D0%BA_%D1%8D%D0%BA%D1%80%D0%B0%D0%BD%D0%B0_2025-10-28_%D0%B2_15.25.51.png)

So we are working with Django template

Use debug tag

![Снимок экрана 2025-10-28 в 15.42.15.png](Server-side%20template%20injection%20with%20information%20di/%D0%A1%D0%BD%D0%B8%D0%BC%D0%BE%D0%BA_%D1%8D%D0%BA%D1%80%D0%B0%D0%BD%D0%B0_2025-10-28_%D0%B2_15.42.15.png)

Read details

![Снимок экрана 2025-10-28 в 15.43.12.png](Server-side%20template%20injection%20with%20information%20di/%D0%A1%D0%BD%D0%B8%D0%BC%D0%BE%D0%BA_%D1%8D%D0%BA%D1%80%D0%B0%D0%BD%D0%B0_2025-10-28_%D0%B2_15.43.12.png)

Notice settings object

![Снимок экрана 2025-10-28 в 15.44.33.png](Server-side%20template%20injection%20with%20information%20di/%D0%A1%D0%BD%D0%B8%D0%BC%D0%BE%D0%BA_%D1%8D%D0%BA%D1%80%D0%B0%D0%BD%D0%B0_2025-10-28_%D0%B2_15.44.33.png)

Invoke it

![Снимок экрана 2025-10-28 в 15.46.15.png](Server-side%20template%20injection%20with%20information%20di/%D0%A1%D0%BD%D0%B8%D0%BC%D0%BE%D0%BA_%D1%8D%D0%BA%D1%80%D0%B0%D0%BD%D0%B0_2025-10-28_%D0%B2_15.46.15.png)

Now access Django docs and find needed field — SECRET KEY

![Снимок экрана 2025-10-28 в 15.48.38.png](Server-side%20template%20injection%20with%20information%20di/%D0%A1%D0%BD%D0%B8%D0%BC%D0%BE%D0%BA_%D1%8D%D0%BA%D1%80%D0%B0%D0%BD%D0%B0_2025-10-28_%D0%B2_15.48.38.png)

![Снимок экрана 2025-10-28 в 15.49.07.png](Server-side%20template%20injection%20with%20information%20di/%D0%A1%D0%BD%D0%B8%D0%BC%D0%BE%D0%BA_%D1%8D%D0%BA%D1%80%D0%B0%D0%BD%D0%B0_2025-10-28_%D0%B2_15.49.07.png)

Done

![Снимок экрана 2025-10-28 в 15.49.24.png](Server-side%20template%20injection%20with%20information%20di/%D0%A1%D0%BD%D0%B8%D0%BC%D0%BE%D0%BA_%D1%8D%D0%BA%D1%80%D0%B0%D0%BD%D0%B0_2025-10-28_%D0%B2_15.49.24.png)