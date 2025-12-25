# EXPERT: Internal cache poisoning

Check: https://siunam321.github.io/ctf/portswigger-labs/Web-Cache-Poisoning/cache-13/

X-Forwarded-Host gets reflected on canonical link and analytics.js:

![Снимок экрана 2025-12-02 в 16.59.50.png](EXPERT%20Internal%20cache%20poisoning/%D0%A1%D0%BD%D0%B8%D0%BC%D0%BE%D0%BA_%D1%8D%D0%BA%D1%80%D0%B0%D0%BD%D0%B0_2025-12-02_%D0%B2_16.59.50.png)

Strangely, this isn’t a case with geolocate.js. If we keep sending poison:

(the lab was reloaded here)

![Снимок экрана 2025-12-02 в 17.30.40.png](EXPERT%20Internal%20cache%20poisoning/%D0%A1%D0%BD%D0%B8%D0%BC%D0%BE%D0%BA_%D1%8D%D0%BA%D1%80%D0%B0%D0%BD%D0%B0_2025-12-02_%D0%B2_17.30.40.png)

That means there’s an internal caching only applied for geolocate.js

Now just use exploit server and store a malicious script:

![Снимок экрана 2025-12-02 в 17.32.12.png](EXPERT%20Internal%20cache%20poisoning/%D0%A1%D0%BD%D0%B8%D0%BC%D0%BE%D0%BA_%D1%8D%D0%BA%D1%80%D0%B0%D0%BD%D0%B0_2025-12-02_%D0%B2_17.32.12.png)