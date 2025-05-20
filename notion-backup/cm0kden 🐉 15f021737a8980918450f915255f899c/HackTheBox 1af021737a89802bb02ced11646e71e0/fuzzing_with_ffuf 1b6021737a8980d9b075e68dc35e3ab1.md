# fuzzing_with_ffuf

Created: March 14, 2025 3:46 PM

![image.png](fuzzing_with_ffuf%201b6021737a8980d9b075e68dc35e3ab1/image.png)

```bash
ffuf -w /opt/useful/seclists/Discovery/Web-Content/web-extensions.txt:FUZZ <SNIP>
```

FFuF recursion fuzzing

![image.png](fuzzing_with_ffuf%201b6021737a8980d9b075e68dc35e3ab1/image%201.png)

```bash
ffuf -w /opt/useful/seclists/Discovery/Web-Content/directory-list-2.3-small.txt:FUZZ -u http://SERVER_IP:PORT/FUZZ -recursion -recursion-depth 1 -e .php -v
```

---

[Attacking_Web_Applications_With_Ffuf_Module_Cheat_Sheet.pdf](fuzzing_with_ffuf%201b6021737a8980d9b075e68dc35e3ab1/Attacking_Web_Applications_With_Ffuf_Module_Cheat_Sheet.pdf)