# Referer-based access control

App has functionality to upgrade users

![Снимок экрана 2025-10-28 в 16.50.45.png](Referer-based%20access%20control/%D0%A1%D0%BD%D0%B8%D0%BC%D0%BE%D0%BA_%D1%8D%D0%BA%D1%80%D0%B0%D0%BD%D0%B0_2025-10-28_%D0%B2_16.50.45.png)

Using this request

![Снимок экрана 2025-10-28 в 16.51.29.png](Referer-based%20access%20control/%D0%A1%D0%BD%D0%B8%D0%BC%D0%BE%D0%BA_%D1%8D%D0%BA%D1%80%D0%B0%D0%BD%D0%B0_2025-10-28_%D0%B2_16.51.29.png)

Login as wiener and try to do the same

![Снимок экрана 2025-10-28 в 16.53.15.png](Referer-based%20access%20control/%D0%A1%D0%BD%D0%B8%D0%BC%D0%BE%D0%BA_%D1%8D%D0%BA%D1%80%D0%B0%D0%BD%D0%B0_2025-10-28_%D0%B2_16.53.15.png)

It worked, because app’s security control here is totally based on Referer header, which can be easily bypassed

![Снимок экрана 2025-10-28 в 16.55.23.png](Referer-based%20access%20control/%D0%A1%D0%BD%D0%B8%D0%BC%D0%BE%D0%BA_%D1%8D%D0%BA%D1%80%D0%B0%D0%BD%D0%B0_2025-10-28_%D0%B2_16.55.23.png)