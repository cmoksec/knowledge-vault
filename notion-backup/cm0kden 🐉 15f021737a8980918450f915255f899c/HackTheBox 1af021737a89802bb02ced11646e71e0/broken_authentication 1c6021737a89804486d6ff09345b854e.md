# broken_authentication

Created: March 30, 2025 12:19 PM

Authentication factors

![image.png](broken_authentication%201c6021737a89804486d6ff09345b854e/image.png)

Adjusting a wordlist for the password policy

```bash
grep '[[:upper:]]' /opt/useful/seclists/Passwords/Leaked-Databases/rockyou.txt | grep '[[:lower:]]' | grep '[[:digit:]]' | grep -E '.{10}' > custom_wordlist.txt
```

Generate same-length sequence

```bash
seq -w 0 9999 > tokens.txt
```

Default passwords database

[Default Passwords | CIRT.net](https://www.cirt.net/passwords)

## 2FA Bypass

It’s possible to bypass authentication steps like OTP 2FA by tampering responses, and if a server if misconfigured to send a page content even in case of invalid authentication. Example:

![image.png](broken_authentication%201c6021737a89804486d6ff09345b854e/image%201.png)

Redirect to 2fa.php; We already know (from registering non admin user), that after login you should land on profile.php. Tamper the response to redirect to that page

![image.png](broken_authentication%201c6021737a89804486d6ff09345b854e/image%202.png)

![image.png](broken_authentication%201c6021737a89804486d6ff09345b854e/image%203.png)

![image.png](broken_authentication%201c6021737a89804486d6ff09345b854e/image%204.png)

Changing the Location header:

![image.png](broken_authentication%201c6021737a89804486d6ff09345b854e/image%205.png)

For GET profile.php also intercepting the response.

![image.png](broken_authentication%201c6021737a89804486d6ff09345b854e/image%206.png)

![image.png](broken_authentication%201c6021737a89804486d6ff09345b854e/image%207.png)

The response forces redirect to 2fa.php, but **still renders and sends back the content page.** This misconfiguration is basically the reason why the attack is possible.

![image.png](broken_authentication%201c6021737a89804486d6ff09345b854e/image%208.png)

In the code itself, execution is not ending on auth check, but continues to render:

![image.png](broken_authentication%201c6021737a89804486d6ff09345b854e/image%209.png)

Flag is here:

![image.png](broken_authentication%201c6021737a89804486d6ff09345b854e/image%2010.png)

This may be fixed just by adding `exit` to the code when auth fails:

![image.png](broken_authentication%201c6021737a89804486d6ff09345b854e/image%2011.png)

---

[Broken_Authentication_Module_Cheat_Sheet.pdf](broken_authentication%201c6021737a89804486d6ff09345b854e/Broken_Authentication_Module_Cheat_Sheet.pdf)