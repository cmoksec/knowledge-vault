# Basic server-side template injection

First, we find a reflected input

![Снимок экрана 2025-10-28 в 13.54.01.png](Basic%20server-side%20template%20injection/%D0%A1%D0%BD%D0%B8%D0%BC%D0%BE%D0%BA_%D1%8D%D0%BA%D1%80%D0%B0%D0%BD%D0%B0_2025-10-28_%D0%B2_13.54.01.png)

Then fuzz and quickly find the working payload

![Снимок экрана 2025-10-28 в 13.57.44.png](Basic%20server-side%20template%20injection/%D0%A1%D0%BD%D0%B8%D0%BC%D0%BE%D0%BA_%D1%8D%D0%BA%D1%80%D0%B0%D0%BD%D0%B0_2025-10-28_%D0%B2_13.57.44.png)

Analysis suggests this is ERB Ruby payload, so we seek for the RCE escalation

![Снимок экрана 2025-10-28 в 14.00.26.png](Basic%20server-side%20template%20injection/%D0%A1%D0%BD%D0%B8%D0%BC%D0%BE%D0%BA_%D1%8D%D0%BA%D1%80%D0%B0%D0%BD%D0%B0_2025-10-28_%D0%B2_14.00.26.png)

![Снимок экрана 2025-10-28 в 14.02.30.png](Basic%20server-side%20template%20injection/%D0%A1%D0%BD%D0%B8%D0%BC%D0%BE%D0%BA_%D1%8D%D0%BA%D1%80%D0%B0%D0%BD%D0%B0_2025-10-28_%D0%B2_14.02.30.png)

![Снимок экрана 2025-10-28 в 14.02.43.png](Basic%20server-side%20template%20injection/%D0%A1%D0%BD%D0%B8%D0%BC%D0%BE%D0%BA_%D1%8D%D0%BA%D1%80%D0%B0%D0%BD%D0%B0_2025-10-28_%D0%B2_14.02.43.png)