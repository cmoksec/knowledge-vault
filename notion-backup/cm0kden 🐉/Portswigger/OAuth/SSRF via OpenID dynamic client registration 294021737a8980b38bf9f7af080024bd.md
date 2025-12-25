# SSRF via OpenID dynamic client registration

OAuth server contains the following config file

![Снимок экрана 2025-10-22 в 09.17.53.png](SSRF%20via%20OpenID%20dynamic%20client%20registration/%D0%A1%D0%BD%D0%B8%D0%BC%D0%BE%D0%BA_%D1%8D%D0%BA%D1%80%D0%B0%D0%BD%D0%B0_2025-10-22_%D0%B2_09.17.53.png)

Including interesting endpoints

![Снимок экрана 2025-10-22 в 09.20.29.png](SSRF%20via%20OpenID%20dynamic%20client%20registration/%D0%A1%D0%BD%D0%B8%D0%BC%D0%BE%D0%BA_%D1%8D%D0%BA%D1%80%D0%B0%D0%BD%D0%B0_2025-10-22_%D0%B2_09.20.29.png)

Try to send registration request without any authentication. Registered successfully

![Снимок экрана 2025-10-22 в 09.22.36.png](SSRF%20via%20OpenID%20dynamic%20client%20registration/%D0%A1%D0%BD%D0%B8%D0%BC%D0%BE%D0%BA_%D1%8D%D0%BA%D1%80%D0%B0%D0%BD%D0%B0_2025-10-22_%D0%B2_09.22.36.png)

![Снимок экрана 2025-10-22 в 09.25.09.png](SSRF%20via%20OpenID%20dynamic%20client%20registration/%D0%A1%D0%BD%D0%B8%D0%BC%D0%BE%D0%BA_%D1%8D%D0%BA%D1%80%D0%B0%D0%BD%D0%B0_2025-10-22_%D0%B2_09.25.09.png)

On the OAuth traffic, spot the logo request when asking to confirm user’s permissions. OIDC specification allows to set the logo URI during the registration, so do this with a collaborator / webhook link.

![Снимок экрана 2025-10-22 в 10.13.32.png](SSRF%20via%20OpenID%20dynamic%20client%20registration/%D0%A1%D0%BD%D0%B8%D0%BC%D0%BE%D0%BA_%D1%8D%D0%BA%D1%80%D0%B0%D0%BD%D0%B0_2025-10-22_%D0%B2_10.13.32.png)

![Снимок экрана 2025-10-22 в 10.14.53.png](SSRF%20via%20OpenID%20dynamic%20client%20registration/%D0%A1%D0%BD%D0%B8%D0%BC%D0%BE%D0%BA_%D1%8D%D0%BA%D1%80%D0%B0%D0%BD%D0%B0_2025-10-22_%D0%B2_10.14.53.png)

Lab description says there’s a cloud security config, and we need to access it.

![Снимок экрана 2025-10-22 в 09.28.26.png](SSRF%20via%20OpenID%20dynamic%20client%20registration/%D0%A1%D0%BD%D0%B8%D0%BC%D0%BE%D0%BA_%D1%8D%D0%BA%D1%80%D0%B0%D0%BD%D0%B0_2025-10-22_%D0%B2_09.28.26.png)

So, just register logo URI for this resource and access the secret

![Снимок экрана 2025-10-22 в 10.16.00.png](SSRF%20via%20OpenID%20dynamic%20client%20registration/%D0%A1%D0%BD%D0%B8%D0%BC%D0%BE%D0%BA_%D1%8D%D0%BA%D1%80%D0%B0%D0%BD%D0%B0_2025-10-22_%D0%B2_10.16.00.png)

![Снимок экрана 2025-10-22 в 10.16.44.png](SSRF%20via%20OpenID%20dynamic%20client%20registration/%D0%A1%D0%BD%D0%B8%D0%BC%D0%BE%D0%BA_%D1%8D%D0%BA%D1%80%D0%B0%D0%BD%D0%B0_2025-10-22_%D0%B2_10.16.44.png)

Done