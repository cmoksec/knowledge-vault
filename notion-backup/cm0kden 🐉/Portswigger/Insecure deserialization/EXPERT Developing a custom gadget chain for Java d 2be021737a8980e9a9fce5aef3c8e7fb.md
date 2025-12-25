# EXPERT: Developing a custom gadget chain for Java deserialization

![Снимок экрана 2025-12-03 в 14.00.44.png](EXPERT%20Developing%20a%20custom%20gadget%20chain%20for%20Java%20d/%D0%A1%D0%BD%D0%B8%D0%BC%D0%BE%D0%BA_%D1%8D%D0%BA%D1%80%D0%B0%D0%BD%D0%B0_2025-12-03_%D0%B2_14.00.44.png)

![Снимок экрана 2025-12-03 в 13.53.52.png](EXPERT%20Developing%20a%20custom%20gadget%20chain%20for%20Java%20d/%D0%A1%D0%BD%D0%B8%D0%BC%D0%BE%D0%BA_%D1%8D%D0%BA%D1%80%D0%B0%D0%BD%D0%B0_2025-12-03_%D0%B2_13.53.52.png)

Home page:

![Снимок экрана 2025-12-03 в 13.54.08.png](EXPERT%20Developing%20a%20custom%20gadget%20chain%20for%20Java%20d/%D0%A1%D0%BD%D0%B8%D0%BC%D0%BE%D0%BA_%D1%8D%D0%BA%D1%80%D0%B0%D0%BD%D0%B0_2025-12-03_%D0%B2_13.54.08.png)

![Снимок экрана 2025-12-03 в 13.55.38.png](EXPERT%20Developing%20a%20custom%20gadget%20chain%20for%20Java%20d/%D0%A1%D0%BD%D0%B8%D0%BC%D0%BE%D0%BA_%D1%8D%D0%BA%D1%80%D0%B0%D0%BD%D0%B0_2025-12-03_%D0%B2_13.55.38.png)

![Снимок экрана 2025-12-03 в 13.58.13.png](EXPERT%20Developing%20a%20custom%20gadget%20chain%20for%20Java%20d/%D0%A1%D0%BD%D0%B8%D0%BC%D0%BE%D0%BA_%D1%8D%D0%BA%D1%80%D0%B0%D0%BD%D0%B0_2025-12-03_%D0%B2_13.58.13.png)

![Снимок экрана 2025-12-03 в 13.58.28.png](EXPERT%20Developing%20a%20custom%20gadget%20chain%20for%20Java%20d/%D0%A1%D0%BD%D0%B8%D0%BC%D0%BE%D0%BA_%D1%8D%D0%BA%D1%80%D0%B0%D0%BD%D0%B0_2025-12-03_%D0%B2_13.58.28.png)

Here we can spot the SQL injection in readObject method, that gets invoked when the object is deserialized.

To construct a gadget, use:

[https://github.com/PortSwigger/serialization-examples](https://github.com/PortSwigger/serialization-examples)

![Снимок экрана 2025-12-03 в 14.34.34.png](EXPERT%20Developing%20a%20custom%20gadget%20chain%20for%20Java%20d/%D0%A1%D0%BD%D0%B8%D0%BC%D0%BE%D0%BA_%D1%8D%D0%BA%D1%80%D0%B0%D0%BD%D0%B0_2025-12-03_%D0%B2_14.34.34.png)

![Снимок экрана 2025-12-03 в 14.34.56.png](EXPERT%20Developing%20a%20custom%20gadget%20chain%20for%20Java%20d/%D0%A1%D0%BD%D0%B8%D0%BC%D0%BE%D0%BA_%D1%8D%D0%BA%D1%80%D0%B0%D0%BD%D0%B0_2025-12-03_%D0%B2_14.34.56.png)

Logged in as administrator using extracted password

![Снимок экрана 2025-12-03 в 14.35.40.png](EXPERT%20Developing%20a%20custom%20gadget%20chain%20for%20Java%20d/%D0%A1%D0%BD%D0%B8%D0%BC%D0%BE%D0%BA_%D1%8D%D0%BA%D1%80%D0%B0%D0%BD%D0%B0_2025-12-03_%D0%B2_14.35.40.png)