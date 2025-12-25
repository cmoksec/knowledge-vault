# Arbitrary object injection in PHP

**Vulnerability Summary:**

Insecure deserialization of a `CustomTemplate` object triggers the `__destruct()` method, which deletes files specified in the `lock_file_path` attribute.

**Attack Flow:**

1. **Discover Class Source:**
    - Found `/libs/CustomTemplate.php~` containing class with `__destruct()` method
    - `__destruct()` calls `unlink()` on `lock_file_path`
2. **Craft Malicious Object:**
    - Serialized payload:
        
        `O:14:"CustomTemplate":1:{s:14:"lock_file_path";s:23:"/home/carlos/morale.txt";}`
        
3. **Execute Attack:**
    - Base64 and URL-encode the payload
    - Replace session cookie with malicious object
    - Sending request triggers `__destruct()`, deleting target file

![image.png](Arbitrary%20object%20injection%20in%20PHP/image.png)

![image.png](Arbitrary%20object%20injection%20in%20PHP/image%201.png)

![image.png](Arbitrary%20object%20injection%20in%20PHP/image%202.png)

![image.png](Arbitrary%20object%20injection%20in%20PHP/image%203.png)