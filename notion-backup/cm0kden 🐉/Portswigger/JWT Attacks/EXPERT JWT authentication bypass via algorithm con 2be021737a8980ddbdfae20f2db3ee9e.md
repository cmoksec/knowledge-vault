# EXPERT: JWT authentication bypass via algorithm confusion

![Снимок экрана 2025-12-03 в 21.13.50.png](EXPERT%20JWT%20authentication%20bypass%20via%20algorithm%20con/%D0%A1%D0%BD%D0%B8%D0%BC%D0%BE%D0%BA_%D1%8D%D0%BA%D1%80%D0%B0%D0%BD%D0%B0_2025-12-03_%D0%B2_21.13.50.png)

![Снимок экрана 2025-12-03 в 21.43.34.png](EXPERT%20JWT%20authentication%20bypass%20via%20algorithm%20con/%D0%A1%D0%BD%D0%B8%D0%BC%D0%BE%D0%BA_%D1%8D%D0%BA%D1%80%D0%B0%D0%BD%D0%B0_2025-12-03_%D0%B2_21.43.34.png)

Public key

![Снимок экрана 2025-12-03 в 21.00.52.png](EXPERT%20JWT%20authentication%20bypass%20via%20algorithm%20con/%D0%A1%D0%BD%D0%B8%D0%BC%D0%BE%D0%BA_%D1%8D%D0%BA%D1%80%D0%B0%D0%BD%D0%B0_2025-12-03_%D0%B2_21.00.52.png)

Copy key

![Снимок экрана 2025-12-03 в 21.02.22.png](EXPERT%20JWT%20authentication%20bypass%20via%20algorithm%20con/%D0%A1%D0%BD%D0%B8%D0%BC%D0%BE%D0%BA_%D1%8D%D0%BA%D1%80%D0%B0%D0%BD%D0%B0_2025-12-03_%D0%B2_21.02.22.png)

New RSA Key

![Снимок экрана 2025-12-03 в 21.02.56.png](EXPERT%20JWT%20authentication%20bypass%20via%20algorithm%20con/%D0%A1%D0%BD%D0%B8%D0%BC%D0%BE%D0%BA_%D1%8D%D0%BA%D1%80%D0%B0%D0%BD%D0%B0_2025-12-03_%D0%B2_21.02.56.png)

Copy as PEM

![Снимок экрана 2025-12-03 в 21.03.58.png](EXPERT%20JWT%20authentication%20bypass%20via%20algorithm%20con/%D0%A1%D0%BD%D0%B8%D0%BC%D0%BE%D0%BA_%D1%8D%D0%BA%D1%80%D0%B0%D0%BD%D0%B0_2025-12-03_%D0%B2_21.03.58.png)

Encode as B64

![Снимок экрана 2025-12-03 в 21.05.09.png](EXPERT%20JWT%20authentication%20bypass%20via%20algorithm%20con/%D0%A1%D0%BD%D0%B8%D0%BC%D0%BE%D0%BA_%D1%8D%D0%BA%D1%80%D0%B0%D0%BD%D0%B0_2025-12-03_%D0%B2_21.05.09.png)

New Symmetric key (replace k with copied PEM)

![Снимок экрана 2025-12-03 в 21.06.06.png](EXPERT%20JWT%20authentication%20bypass%20via%20algorithm%20con/%D0%A1%D0%BD%D0%B8%D0%BC%D0%BE%D0%BA_%D1%8D%D0%BA%D1%80%D0%B0%D0%BD%D0%B0_2025-12-03_%D0%B2_21.06.06.png)

Sign edited JWT with this key without modifying headers

![Снимок экрана 2025-12-03 в 21.08.31.png](EXPERT%20JWT%20authentication%20bypass%20via%20algorithm%20con/%D0%A1%D0%BD%D0%B8%D0%BC%D0%BE%D0%BA_%D1%8D%D0%BA%D1%80%D0%B0%D0%BD%D0%B0_2025-12-03_%D0%B2_21.08.31.png)

Success

![Снимок экрана 2025-12-03 в 21.09.19.png](EXPERT%20JWT%20authentication%20bypass%20via%20algorithm%20con/%D0%A1%D0%BD%D0%B8%D0%BC%D0%BE%D0%BA_%D1%8D%D0%BA%D1%80%D0%B0%D0%BD%D0%B0_2025-12-03_%D0%B2_21.09.19.png)

![Снимок экрана 2025-12-03 в 21.12.34.png](EXPERT%20JWT%20authentication%20bypass%20via%20algorithm%20con/%D0%A1%D0%BD%D0%B8%D0%BC%D0%BE%D0%BA_%D1%8D%D0%BA%D1%80%D0%B0%D0%BD%D0%B0_2025-12-03_%D0%B2_21.12.34.png)

![Снимок экрана 2025-12-03 в 21.12.52.png](EXPERT%20JWT%20authentication%20bypass%20via%20algorithm%20con/%D0%A1%D0%BD%D0%B8%D0%BC%D0%BE%D0%BA_%D1%8D%D0%BA%D1%80%D0%B0%D0%BD%D0%B0_2025-12-03_%D0%B2_21.12.52.png)