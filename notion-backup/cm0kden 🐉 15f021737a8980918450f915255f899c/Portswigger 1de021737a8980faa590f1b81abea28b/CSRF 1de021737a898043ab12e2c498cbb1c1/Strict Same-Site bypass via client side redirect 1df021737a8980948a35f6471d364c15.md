# Strict Same-Site bypass via client side redirect

To bypass Strict Same-site policy, the website must have a redirection vulnerability that will allow to make an arbitrary secondary request from a same-site scope (the website itself will send a request), thus a session cookie will be included into the request. Example from lab **SameSite Strict bypass via client-side redirect**

A website has a vulnerability in post comment confirmation page. It redirects using costId parameter (it’s used to construct a redirection URL). Using it, we can tamper a postId parameter to redirect to any page in a same site scope.

![image.png](Strict%20Same-Site%20bypass%20via%20client%20side%20redirect%201df021737a8980948a35f6471d364c15/image.png)

As far as sensitive functionality works on GET method, we can redirect to the sensitive URL triggering the logic.

![image.png](Strict%20Same-Site%20bypass%20via%20client%20side%20redirect%201df021737a8980948a35f6471d364c15/image%201.png)

CSRF payload:

```jsx
<script>
    document.location = "https://0ab4007a04bcaff48299d806006f004b.web-security-academy.net/post/comment/confirmation?postId=1/../../my-account/change-email?email=pwned%40policia.zx%26submit=1";
</script>
```