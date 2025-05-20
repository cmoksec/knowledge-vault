# login_brute_forcing

Created: March 29, 2025 1:30 PM

## Customized wordlists

For usernames: `username-anarchy` 

![image.png](login_brute_forcing%201c5021737a898056847aeed438bb00e5/image.png)

```bash
./username-anarchy Jane Smith > jane_smith_usernames.txt
```

For passwords: `CUPP`

![image.png](login_brute_forcing%201c5021737a898056847aeed438bb00e5/image%201.png)

## Password policy filtering

- Minimum Length: 6 characters
- Must Include:
    - At least one uppercase letter
    - At least one lowercase letter
    - At least one number
    - At least two special characters (from the set `!@#$%^&*`)

```bash
grep -E '^.{6,}$' jane.txt | grep -E '[A-Z]' | grep -E '[a-z]' | grep -E '[0-9]' | grep -E '([!@#$%^&*].*){2,}' > jane-filtered.txt
```

---

[Login_Brute_Forcing_Module_Cheat_Sheet.pdf](login_brute_forcing%201c5021737a898056847aeed438bb00e5/Login_Brute_Forcing_Module_Cheat_Sheet.pdf)