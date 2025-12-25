# Partial Construction Race Condition

### **Understanding Partial Construction Race Conditions (PortSwigger Academy Explanation)**

This paragraph describes a **race condition vulnerability** that occurs when an application **creates or modifies objects in multiple steps**, leaving a temporary "partially constructed" state that attackers can exploit. Here's a breakdown:

---

### **Key Concepts**

1. **Multi-Step Object Creation**
    - Some apps create objects (e.g., user accounts) in **multiple database operations** (e.g., `INSERT` followed by `UPDATE`).
    - Example:
        
        sql
        
- 
    - `- Step 1: Create user with default/null API key
    INSERT INTO users (username, api_key) VALUES ('alice', NULL);
    -- Step 2: Set API key later
    UPDATE users SET api_key = 'secret123' WHERE username = 'alice';`
    - Between these steps, the `api_key` is **temporarily `NULL` or empty**.
- **Race Condition Exploit**
    - An attacker can **send concurrent requests** to interact with the object **during this temporary state**.
    - Example:
        - If the app checks `api_key == NULL` for permissions, an attacker might:
            1. Register a user (`api_key` is initially `NULL`).
            2. Quickly call a privileged API endpoint **before the key is set**.
            3. Bypass security checks (since `api_key` is still `NULL`).
- **Unexpected Input Handling**
    - Frameworks (e.g., PHP) may parse inputs like `param[]` as **arrays** instead of strings.
    - Example:
        - Sending `api_key[]=` in a request might make the server treat `api_key` as an **empty array `[]`** (equivalent to `NULL` in some contexts).
        - This can trick the app into comparing `api_key == NULL` (returning `true`).