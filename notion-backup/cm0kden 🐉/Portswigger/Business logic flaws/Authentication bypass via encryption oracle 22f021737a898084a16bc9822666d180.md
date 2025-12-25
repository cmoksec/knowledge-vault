# Authentication bypass via encryption oracle

Example: A sample blogging application.

The first interesting sight is a stay-logged-in cookie:

![image.png](Authentication%20bypass%20via%20encryption%20oracle/image.png)

![image.png](Authentication%20bypass%20via%20encryption%20oracle/image%201.png)

But the main subject here is a following flaw: when we are trying to leave a comment under one of the posts, there’s a message from the server saying that the email we provided is incorrect.

![image.png](Authentication%20bypass%20via%20encryption%20oracle/image%202.png)

![image.png](Authentication%20bypass%20via%20encryption%20oracle/image%203.png)

And it’s done in a very clunky way. Let’s observe the corresponding request & response:

![image.png](Authentication%20bypass%20via%20encryption%20oracle/image%204.png)

The response is redirecting us back to the post page, setting a cookie called `notification` . This cookie is then sent as part of GET /post request, where it gets decrypted and sent back as an HTML page. Meaning, this cookie is exactly what server uses to understand what message should be displayed. This is called an encryption oracle — the communication channel that freely accepts arbitrary inputs and provides a bidirectional cryptographic translations. Let’s swap the value of the `notification` cookie with a `stay-logged-in` cookie. This way, we will decrypt `stay-logged-in` cookie and possibly will be able to bypass authentication.

![image.png](Authentication%20bypass%20via%20encryption%20oracle/image%205.png)

![image.png](Authentication%20bypass%20via%20encryption%20oracle/image%206.png)

We can see that the cookie is decrypted successfully. Knowing an admin username `carlos` , we can craft a `stay-logged-in` for an admin user.

But first, there’s a 23-char prefix `Invalid email address:` that is automatically applied to any value within email field. We’ll take the encrypted cookie, go to Decoder, and URL + Base64 decode.

![image.png](Authentication%20bypass%20via%20encryption%20oracle/image%207.png)

![image.png](Authentication%20bypass%20via%20encryption%20oracle/image%208.png)

Take the first 23 bytes representing the prefix and delete them.

![image.png](Authentication%20bypass%20via%20encryption%20oracle/image%209.png)

![image.png](Authentication%20bypass%20via%20encryption%20oracle/image%2010.png)

Now we’ll take this byte sequence without a prefix and apply a Base64 encryption:

![image.png](Authentication%20bypass%20via%20encryption%20oracle/image%2011.png)

When trying to submit this chopped cookie to the encryption oracle, we receive an internal server error.

![image.png](Authentication%20bypass%20via%20encryption%20oracle/image%2012.png)

Now we can observe that an error message indicates that a block-based encryption algorithm is used and that the input length must be a multiple of 16. We will need to pad the "`Invalid email address:` " prefix with enough bytes so that the number of bytes we will remove is a multiple of 16. `Invalid email address:`  is 23 chars longs, the nearest multiple of 16 is 32, so we will pad 9 more chars.

![image.png](Authentication%20bypass%20via%20encryption%20oracle/image%2013.png)

```yaml
xxxxxxxxxcarlos:1752435823153
```

![image.png](Authentication%20bypass%20via%20encryption%20oracle/image%2014.png)

Now, when we remove 32 bytes from that cookie, we will get the exact value we need — a `stay-signed-in` cookie of the administrator without no prefixes.

![image.png](Authentication%20bypass%20via%20encryption%20oracle/image%2015.png)

Removed and Base64-encoded:

![image.png](Authentication%20bypass%20via%20encryption%20oracle/image%2016.png)

WARNING!!!!! ALWAYS URL-ENCODE THE FINAL RESULT HERE, YOU MIGHT EXPERIENCE CRYPTO ERRORS ON BACKEND IF BASE64 STRING CONTAINS SPECIAL CHARS LIKE +

Finally, our cookie is valid and ready:

![image.png](Authentication%20bypass%20via%20encryption%20oracle/image%2017.png)

We’ll copy and paste the cipher we crafted to the `stay-logged-in` cookie, and delete `session` entirely, to obtain an admin access:

![image.png](Authentication%20bypass%20via%20encryption%20oracle/image%2018.png)

Oops, I just realized I was crafting the cookie for `carlos`, but he’s not an admin. So, just repeat the same instructions for `administrator` , then go to `GET /` , request in Proxy history, and add `stay-logged-in` cookie. I did the same steps **and** URL-encoded the final cookie to avoid discrepancies. 

![image.png](Authentication%20bypass%20via%20encryption%20oracle/image%2019.png)

![image.png](Authentication%20bypass%20via%20encryption%20oracle/image%2020.png)

Finally, the admin panel is accessed:

![image.png](Authentication%20bypass%20via%20encryption%20oracle/image%2021.png)