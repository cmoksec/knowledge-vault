# Modifying serialized data types

![image.png](Modifying%20serialized%20data%20types/image.png)

**Vulnerability Summary:**

The
 application uses insecure PHP object deserialization in session 
cookies, allowing authentication bypass by manipulating serialized 
object properties.

**Attack Flow:**

1. **Intercept Session Cookie:**
    - After login, the session cookie contains a serialized PHP `User` object.
2. **Modify Serialized Object:**
    - Change `username` to "administrator" (length: 13)
    - Change `access_token` from string to integer `0` (replace `s:...` with `i:0`)
3. **Resulting Payload:**
    
    text
    

```
O:4:"User":2:{s:8:"username";s:13:"administrator";s:12:"access_token";i:0;}
```

1. **Exploitation:**
    - Modified cookie grants admin access, revealing `/admin` panel
    - Access `/admin/delete?username=carlos` to delete target user

**Impact:**

Authentication bypass leading to full admin privilege escalation through insecure deserialization.

![image.png](Modifying%20serialized%20data%20types/image%201.png)

![image.png](Modifying%20serialized%20data%20types/image%202.png)

![image.png](Modifying%20serialized%20data%20types/image%203.png)