# EXPERT: Exfiltrating sensitive data via server-side prototype pollution

Identify using BApp extension:

![Снимок экрана 2025-12-03 в 21.51.24.png](EXPERT%20Exfiltrating%20sensitive%20data%20via%20server-side/%D0%A1%D0%BD%D0%B8%D0%BC%D0%BE%D0%BA_%D1%8D%D0%BA%D1%80%D0%B0%D0%BD%D0%B0_2025-12-03_%D0%B2_21.51.24.png)

On the Admin panel

![Снимок экрана 2025-12-03 в 21.53.05.png](EXPERT%20Exfiltrating%20sensitive%20data%20via%20server-side/%D0%A1%D0%BD%D0%B8%D0%BC%D0%BE%D0%BA_%D1%8D%D0%BA%D1%80%D0%B0%D0%BD%D0%B0_2025-12-03_%D0%B2_21.53.05.png)

![Снимок экрана 2025-12-03 в 21.53.25.png](EXPERT%20Exfiltrating%20sensitive%20data%20via%20server-side/%D0%A1%D0%BD%D0%B8%D0%BC%D0%BE%D0%BA_%D1%8D%D0%BA%D1%80%D0%B0%D0%BD%D0%B0_2025-12-03_%D0%B2_21.53.25.png)

![Снимок экрана 2025-12-03 в 21.53.49.png](EXPERT%20Exfiltrating%20sensitive%20data%20via%20server-side/%D0%A1%D0%BD%D0%B8%D0%BC%D0%BE%D0%BA_%D1%8D%D0%BA%D1%80%D0%B0%D0%BD%D0%B0_2025-12-03_%D0%B2_21.53.49.png)

![Снимок экрана 2025-12-03 в 21.54.09.png](EXPERT%20Exfiltrating%20sensitive%20data%20via%20server-side/%D0%A1%D0%BD%D0%B8%D0%BC%D0%BE%D0%BA_%D1%8D%D0%BA%D1%80%D0%B0%D0%BD%D0%B0_2025-12-03_%D0%B2_21.54.09.png)

![Снимок экрана 2025-12-03 в 21.56.08.png](EXPERT%20Exfiltrating%20sensitive%20data%20via%20server-side/%D0%A1%D0%BD%D0%B8%D0%BC%D0%BE%D0%BA_%D1%8D%D0%BA%D1%80%D0%B0%D0%BD%D0%B0_2025-12-03_%D0%B2_21.56.08.png)

![Снимок экрана 2025-12-03 в 21.56.24.png](EXPERT%20Exfiltrating%20sensitive%20data%20via%20server-side/%D0%A1%D0%BD%D0%B8%D0%BC%D0%BE%D0%BA_%D1%8D%D0%BA%D1%80%D0%B0%D0%BD%D0%B0_2025-12-03_%D0%B2_21.56.24.png)

Got some DNS interactions:

![Снимок экрана 2025-12-03 в 22.00.55.png](EXPERT%20Exfiltrating%20sensitive%20data%20via%20server-side/%D0%A1%D0%BD%D0%B8%D0%BC%D0%BE%D0%BA_%D1%8D%D0%BA%D1%80%D0%B0%D0%BD%D0%B0_2025-12-03_%D0%B2_22.00.55.png)

Next step:

![Снимок экрана 2025-12-03 в 21.59.24.png](EXPERT%20Exfiltrating%20sensitive%20data%20via%20server-side/%D0%A1%D0%BD%D0%B8%D0%BC%D0%BE%D0%BA_%D1%8D%D0%BA%D1%80%D0%B0%D0%BD%D0%B0_2025-12-03_%D0%B2_21.59.24.png)

Also changed https to http to evade curl error:

![Снимок экрана 2025-12-03 в 22.01.45.png](EXPERT%20Exfiltrating%20sensitive%20data%20via%20server-side/%D0%A1%D0%BD%D0%B8%D0%BC%D0%BE%D0%BA_%D1%8D%D0%BA%D1%80%D0%B0%D0%BD%D0%B0_2025-12-03_%D0%B2_22.01.45.png)

![Снимок экрана 2025-12-03 в 22.01.59.png](EXPERT%20Exfiltrating%20sensitive%20data%20via%20server-side/%D0%A1%D0%BD%D0%B8%D0%BC%D0%BE%D0%BA_%D1%8D%D0%BA%D1%80%D0%B0%D0%BD%D0%B0_2025-12-03_%D0%B2_22.01.59.png)

![Снимок экрана 2025-12-03 в 22.02.21.png](EXPERT%20Exfiltrating%20sensitive%20data%20via%20server-side/%D0%A1%D0%BD%D0%B8%D0%BC%D0%BE%D0%BA_%D1%8D%D0%BA%D1%80%D0%B0%D0%BD%D0%B0_2025-12-03_%D0%B2_22.02.21.png)

![Снимок экрана 2025-12-03 в 22.02.36.png](EXPERT%20Exfiltrating%20sensitive%20data%20via%20server-side/%D0%A1%D0%BD%D0%B8%D0%BC%D0%BE%D0%BA_%D1%8D%D0%BA%D1%80%D0%B0%D0%BD%D0%B0_2025-12-03_%D0%B2_22.02.36.png)

Finally, get the data

![Снимок экрана 2025-12-03 в 22.03.15.png](EXPERT%20Exfiltrating%20sensitive%20data%20via%20server-side/%D0%A1%D0%BD%D0%B8%D0%BC%D0%BE%D0%BA_%D1%8D%D0%BA%D1%80%D0%B0%D0%BD%D0%B0_2025-12-03_%D0%B2_22.03.15.png)

![Снимок экрана 2025-12-03 в 22.03.44.png](EXPERT%20Exfiltrating%20sensitive%20data%20via%20server-side/%D0%A1%D0%BD%D0%B8%D0%BC%D0%BE%D0%BA_%D1%8D%D0%BA%D1%80%D0%B0%D0%BD%D0%B0_2025-12-03_%D0%B2_22.03.44.png)

![Снимок экрана 2025-12-03 в 22.03.59.png](EXPERT%20Exfiltrating%20sensitive%20data%20via%20server-side/%D0%A1%D0%BD%D0%B8%D0%BC%D0%BE%D0%BA_%D1%8D%D0%BA%D1%80%D0%B0%D0%BD%D0%B0_2025-12-03_%D0%B2_22.03.59.png)

![Снимок экрана 2025-12-03 в 22.06.08.png](EXPERT%20Exfiltrating%20sensitive%20data%20via%20server-side/%D0%A1%D0%BD%D0%B8%D0%BC%D0%BE%D0%BA_%D1%8D%D0%BA%D1%80%D0%B0%D0%BD%D0%B0_2025-12-03_%D0%B2_22.06.08.png)