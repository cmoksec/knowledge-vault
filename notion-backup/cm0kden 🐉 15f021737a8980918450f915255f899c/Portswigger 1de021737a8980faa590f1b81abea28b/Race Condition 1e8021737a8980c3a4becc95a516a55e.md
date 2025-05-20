# Race Condition

Created: May 3, 2025 4:46 PM

Native Parallel attack (applied to a group of requests in repeater)

![image.png](Race%20Condition%201e8021737a8980c3a4becc95a516a55e/image.png)

Turbo Intruder (basic)

![image.png](Race%20Condition%201e8021737a8980c3a4becc95a516a55e/image%201.png)

```bash

def queueRequests(target, wordlists):
    engine = RequestEngine(endpoint=target.endpoint,
                            concurrentConnections=1,
                            engine=Engine.BURP2
                            )
    
    # queue 20 requests in gate '1'
    for i in range(20):
        engine.queue(target.req, gate='1')
    
    # send all requests in gate '1' in parallel
    engine.openGate('1')
```

[Using Turbo Intruder for Race condition fuzzing limit bypass](Race%20Condition%201e8021737a8980c3a4becc95a516a55e/Using%20Turbo%20Intruder%20for%20Race%20condition%20fuzzing%20li%201e8021737a8980fbb757c9afbd8acf16.md)

[Race Condition Detection Methodology](Race%20Condition%201e8021737a8980c3a4becc95a516a55e/Race%20Condition%20Detection%20Methodology%201e8021737a8980e182a8d60d3ef4959c.md)

![image.png](Race%20Condition%201e8021737a8980c3a4becc95a516a55e/image%202.png)

[Multi Endpoint Race Condition](Race%20Condition%201e8021737a8980c3a4becc95a516a55e/Multi%20Endpoint%20Race%20Condition%201e8021737a89807dadcac1c096b4a892.md)

[Single Endpoint Race Condition](Race%20Condition%201e8021737a8980c3a4becc95a516a55e/Single%20Endpoint%20Race%20Condition%201e9021737a89805db1a9e3d25df839b2.md)

[Partial Construction Race Condition](Race%20Condition%201e8021737a8980c3a4becc95a516a55e/Partial%20Construction%20Race%20Condition%201e9021737a89809f864de03d92a53ef0.md)

[Time-sensitive attacks](Race%20Condition%201e8021737a8980c3a4becc95a516a55e/Time-sensitive%20attacks%201e9021737a898061b885cb2938243272.md)

![image.png](Race%20Condition%201e8021737a8980c3a4becc95a516a55e/image%203.png)