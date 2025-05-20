# Authentication

Created: May 5, 2025 4:34 PM

![image.png](Authentication%201ea021737a89809ab179f4e16daae478/image.png)

![image.png](Authentication%201ea021737a89809ab179f4e16daae478/image%201.png)

## Username enumeration

1. Different message (Invalid username or password — Invalid password)
2. Different response length
3. Time difference (use very long passwords to spot time diff)

![image.png](Authentication%201ea021737a89809ab179f4e16daae478/image%202.png)

## Bruteforce protection bypass

[Failed login counter bypass](Authentication%201ea021737a89809ab179f4e16daae478/Failed%20login%20counter%20bypass%201ea021737a8980d18109e910aa737e73.md)

![image.png](Authentication%201ea021737a89809ab179f4e16daae478/image%203.png)

![image.png](Authentication%201ea021737a89809ab179f4e16daae478/image%204.png)

[Username enumeration via account lock](Authentication%201ea021737a89809ab179f4e16daae478/Username%20enumeration%20via%20account%20lock%201eb021737a8980f8b2a1fc3dbc2d8d8f.md)

## 2FA

![image.png](Authentication%201ea021737a89809ab179f4e16daae478/image%205.png)

## Other auth vulnerabilities

Weak stay logged in cookie (storing user credentials):

![image.png](Authentication%201ea021737a89809ab179f4e16daae478/image%206.png)

![image.png](Authentication%201ea021737a89809ab179f4e16daae478/image%207.png)

### Middleware reset poisoning (TODO: investigate…)

![image.png](Authentication%201ea021737a89809ab179f4e16daae478/image%208.png)

### Change password: bruteforce using different messages

![image.png](Authentication%201ea021737a89809ab179f4e16daae478/image%209.png)

![image.png](Authentication%201ea021737a89809ab179f4e16daae478/image%2010.png)

## Preventing

1. **Take care with user credentials**
2. **Don't count on users for security**
3. **Prevent username enumeration**
4. **Implement robust brute-force protection**
5. **Triple-check your verification logic**
6. **Don't forget supplementary functionality**