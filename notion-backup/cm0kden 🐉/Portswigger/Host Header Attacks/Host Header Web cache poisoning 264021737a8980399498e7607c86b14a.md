# Host Header Web cache poisoning

1. In Burp's browser, open the lab and click **Home** to refresh the home page.
2. In **Proxy > HTTP history**, right-click the `GET /` request and select **Send to Repeater**.
3. In Repeater, study the lab's behavior. Notice
that the website validates the Host header. If you modify the Host
header, you can no longer access the home page.

![image.png](Host%20Header%20Web%20cache%20poisoning/image.png)

![image.png](Host%20Header%20Web%20cache%20poisoning/image%201.png)

1. In the original response, notice the verbose
caching headers, which tell you when you get a cache hit and how old the cached response is. Add an arbitrary query parameter to your requests
to serve as a cache buster, for example, `GET /?cb=123`. You can change this parameter each time you want a fresh response from the back-end server.
2. Notice that if you add a second Host header with an arbitrary value, this appears to be ignored when validating and
routing your request. Crucially, notice that the arbitrary value of your second Host header is reflected in an absolute URL used to import a
script from `/resources/js/tracking.js`.
3. Remove the second Host header and send the
request again using the same cache buster. Notice that you still receive the same cached response containing your injected value.
4. Go to the exploit server and create a file at `/resources/js/tracking.js` containing the payload `alert(document.cookie)`. Store the exploit and copy the domain name for your exploit server.

![image.png](Host%20Header%20Web%20cache%20poisoning/image%202.png)

1. Back in Burp Repeater, add a second Host
header containing your exploit server domain name. The request should
look something like this: `GET /?cb=123 HTTP/1.1
Host: YOUR-LAB-ID.web-security-academy.net
Host: YOUR-EXPLOIT-SERVER-ID.exploit-server.net`

![image.png](Host%20Header%20Web%20cache%20poisoning/image%203.png)

1. Send the request a couple of times until you get a cache hit with your exploit server URL reflected in the response. To
simulate the victim, request the page in the browser using the same
cache buster in the URL. Make sure that the `alert()` fires.
2. In Burp Repeater, remove any cache busters and
keep replaying the request until you have re-poisoned the cache. The lab is solved when the victim visits the home page.