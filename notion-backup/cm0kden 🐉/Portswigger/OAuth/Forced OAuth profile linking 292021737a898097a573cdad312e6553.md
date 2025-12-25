# Forced OAuth profile linking

Given classic password-based auth + OAuth login with account linking

After logging in to the account using password, you can also log in using social media profile and then link it to the profile

![Снимок экрана 2025-10-20 в 12.39.02.png](Forced%20OAuth%20profile%20linking/%D0%A1%D0%BD%D0%B8%D0%BC%D0%BE%D0%BA_%D1%8D%D0%BA%D1%80%D0%B0%D0%BD%D0%B0_2025-10-20_%D0%B2_12.39.02.png)

Attaching a profile is done by sending the following request:

![Снимок экрана 2025-10-20 в 12.39.34.png](Forced%20OAuth%20profile%20linking/%D0%A1%D0%BD%D0%B8%D0%BC%D0%BE%D0%BA_%D1%8D%D0%BA%D1%80%D0%B0%D0%BD%D0%B0_2025-10-20_%D0%B2_12.39.34.png)

We can spot the absence of state param, which acts as the CSRF token. Therefore, CSRF attack is possible to attach our social account to admin website profile. We will intercept attaching request, craft CSRF link and deliver to admin.

![Снимок экрана 2025-10-20 в 14.11.33.png](Forced%20OAuth%20profile%20linking/%D0%A1%D0%BD%D0%B8%D0%BC%D0%BE%D0%BA_%D1%8D%D0%BA%D1%80%D0%B0%D0%BD%D0%B0_2025-10-20_%D0%B2_14.11.33.png)

While intercepting, drop the activation request to use it in the attack

![Снимок экрана 2025-10-20 в 14.12.16.png](Forced%20OAuth%20profile%20linking/%D0%A1%D0%BD%D0%B8%D0%BC%D0%BE%D0%BA_%D1%8D%D0%BA%D1%80%D0%B0%D0%BD%D0%B0_2025-10-20_%D0%B2_14.12.16.png)

![Снимок экрана 2025-10-20 в 14.13.58.png](Forced%20OAuth%20profile%20linking/%D0%A1%D0%BD%D0%B8%D0%BC%D0%BE%D0%BA_%D1%8D%D0%BA%D1%80%D0%B0%D0%BD%D0%B0_2025-10-20_%D0%B2_14.13.58.png)

After sending payload, logout from wiener and login using social media account and gain admin priveleges

![Снимок экрана 2025-10-20 в 14.16.33.png](Forced%20OAuth%20profile%20linking/%D0%A1%D0%BD%D0%B8%D0%BC%D0%BE%D0%BA_%D1%8D%D0%BA%D1%80%D0%B0%D0%BD%D0%B0_2025-10-20_%D0%B2_14.16.33.png)

![Снимок экрана 2025-10-20 в 14.16.54.png](Forced%20OAuth%20profile%20linking/%D0%A1%D0%BD%D0%B8%D0%BC%D0%BE%D0%BA_%D1%8D%D0%BA%D1%80%D0%B0%D0%BD%D0%B0_2025-10-20_%D0%B2_14.16.54.png)