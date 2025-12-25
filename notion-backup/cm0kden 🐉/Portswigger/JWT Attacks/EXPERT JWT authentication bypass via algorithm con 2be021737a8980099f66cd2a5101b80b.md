# EXPERT: JWT authentication bypass via algorithm confusion with no exposed key

![Снимок экрана 2025-12-03 в 21.43.06.png](EXPERT%20JWT%20authentication%20bypass%20via%20algorithm%20con%202be0-b80b/%D0%A1%D0%BD%D0%B8%D0%BC%D0%BE%D0%BA_%D1%8D%D0%BA%D1%80%D0%B0%D0%BD%D0%B0_2025-12-03_%D0%B2_21.43.06.png)

![Снимок экрана 2025-12-03 в 21.41.00.png](EXPERT%20JWT%20authentication%20bypass%20via%20algorithm%20con%202be0-b80b/%D0%A1%D0%BD%D0%B8%D0%BC%D0%BE%D0%BA_%D1%8D%D0%BA%D1%80%D0%B0%D0%BD%D0%B0_2025-12-03_%D0%B2_21.41.00.png)

First, obtain 2 valid JWT tokens by logging in twice, save them

Run command

```python
docker run --rm -it portswigger/sig2n <token1> <token2>
```

Try each of the tampered JWTs to see which one worked

![Снимок экрана 2025-12-03 в 21.27.19.png](EXPERT%20JWT%20authentication%20bypass%20via%20algorithm%20con%202be0-b80b/%D0%A1%D0%BD%D0%B8%D0%BC%D0%BE%D0%BA_%D1%8D%D0%BA%D1%80%D0%B0%D0%BD%D0%B0_2025-12-03_%D0%B2_21.27.19.png)

1st one worked

![Снимок экрана 2025-12-03 в 21.28.33.png](EXPERT%20JWT%20authentication%20bypass%20via%20algorithm%20con%202be0-b80b/%D0%A1%D0%BD%D0%B8%D0%BC%D0%BE%D0%BA_%D1%8D%D0%BA%D1%80%D0%B0%D0%BD%D0%B0_2025-12-03_%D0%B2_21.28.33.png)

Use associated key from the console output to sign:

![Снимок экрана 2025-12-03 в 21.29.31.png](EXPERT%20JWT%20authentication%20bypass%20via%20algorithm%20con%202be0-b80b/%D0%A1%D0%BD%D0%B8%D0%BC%D0%BE%D0%BA_%D1%8D%D0%BA%D1%80%D0%B0%D0%BD%D0%B0_2025-12-03_%D0%B2_21.29.31.png)

![Снимок экрана 2025-12-03 в 21.30.35.png](EXPERT%20JWT%20authentication%20bypass%20via%20algorithm%20con%202be0-b80b/%D0%A1%D0%BD%D0%B8%D0%BC%D0%BE%D0%BA_%D1%8D%D0%BA%D1%80%D0%B0%D0%BD%D0%B0_2025-12-03_%D0%B2_21.30.35.png)

Craft the token and sign using symmetric key

![Снимок экрана 2025-12-03 в 21.39.34.png](EXPERT%20JWT%20authentication%20bypass%20via%20algorithm%20con%202be0-b80b/%D0%A1%D0%BD%D0%B8%D0%BC%D0%BE%D0%BA_%D1%8D%D0%BA%D1%80%D0%B0%D0%BD%D0%B0_2025-12-03_%D0%B2_21.39.34.png)

Success

![Снимок экрана 2025-12-03 в 21.39.57.png](EXPERT%20JWT%20authentication%20bypass%20via%20algorithm%20con%202be0-b80b/%D0%A1%D0%BD%D0%B8%D0%BC%D0%BE%D0%BA_%D1%8D%D0%BA%D1%80%D0%B0%D0%BD%D0%B0_2025-12-03_%D0%B2_21.39.57.png)