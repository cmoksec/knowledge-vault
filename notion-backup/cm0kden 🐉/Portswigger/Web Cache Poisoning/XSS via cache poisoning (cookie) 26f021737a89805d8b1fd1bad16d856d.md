# XSS via cache poisoning (cookie)

The request we have is:

![image.png](XSS%20via%20cache%20poisoning%20(cookie)/image.png)

Let’s manipulate `fehost` cookie to confirm it’s not changing the cache key:

Send this request twice:

![image.png](XSS%20via%20cache%20poisoning%20(cookie)/image%201.png)

Then change `fehost` and check whether X-Cache-Hit is miss or hit:

![image.png](XSS%20via%20cache%20poisoning%20(cookie)/image%202.png)

Still hit — that’s an unkeyed data. That means we can use it to poison the response. Construct classic XSS following lab’s task.

![image.png](XSS%20via%20cache%20poisoning%20(cookie)/image%203.png)

![image.png](XSS%20via%20cache%20poisoning%20(cookie)/image%204.png)