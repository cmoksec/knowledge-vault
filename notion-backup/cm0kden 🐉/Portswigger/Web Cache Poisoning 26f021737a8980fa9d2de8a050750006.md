# Web Cache Poisoning

Created: September 15, 2025 2:02 PM

To refresh the understanding of how this vulnerability works, visit Portswigger Academy (it’d be a challenge to explain it better then it was done there).

The one main thing to remember is what cache key is: it’s basically a set of data fields / headers etc, anything incorporated in a response and that is used to calculate cache key (similar to hashcode). We are mostly interested in unkeyed data - something we can manipulate and that won’t change the cache key, so that when a legit user requests the page, he will receive the same poisoned request saved on cache.

![image.png](Web%20Cache%20Poisoning/image.png)

![image.png](Web%20Cache%20Poisoning/image%201.png)

---

Design flaws

[XSS via cache poisoning (header)](Web%20Cache%20Poisoning/XSS%20via%20cache%20poisoning%20(header)%2026f021737a8980249805fce59bc6df72.md)

[XSS via cache poisoning (cookie)](Web%20Cache%20Poisoning/XSS%20via%20cache%20poisoning%20(cookie)%2026f021737a89805d8b1fd1bad16d856d.md)

[XSS via cache poisoning (multiple headers)](Web%20Cache%20Poisoning/XSS%20via%20cache%20poisoning%20(multiple%20headers)%2026f021737a898046b934df6e18774878.md)

[Targeted web cache poisoning](Web%20Cache%20Poisoning/Targeted%20web%20cache%20poisoning%2026f021737a8980c4a65fc9751093b27f.md)

Implementation flaws

[Web cache poisoning: unkeyed query string](Web%20Cache%20Poisoning/Web%20cache%20poisoning%20unkeyed%20query%20string%2027b021737a89809db3e8f6df3e0ef66d.md)

[Web cache poisoning: unkeyed query params](Web%20Cache%20Poisoning/Web%20cache%20poisoning%20unkeyed%20query%20params%2027b021737a8980fd903bc50d94347775.md)

[Web cache poisoning: param cloacking](Web%20Cache%20Poisoning/Web%20cache%20poisoning%20param%20cloacking%2027b021737a89809ab798d2c00d06203a.md)

[Web cache poisoning: fat GET request](Web%20Cache%20Poisoning/Web%20cache%20poisoning%20fat%20GET%20request%2027b021737a8980919bf3e95348064fe6.md)

[Web cache poisoning: URL normalization](Web%20Cache%20Poisoning/Web%20cache%20poisoning%20URL%20normalization%2027b021737a8980ce933ec8679e2baae5.md)

---

[EXPERT: **Web cache poisoning to exploit a DOM vulnerability via a cache with strict cacheability criteria**](Web%20Cache%20Poisoning/EXPERT%20Web%20cache%20poisoning%20to%20exploit%20a%20DOM%20vulner%202bd021737a898069b065febbce186f83.md)

[EXPERT: **Combining web cache poisoning vulnerabilities**](Web%20Cache%20Poisoning/EXPERT%20Combining%20web%20cache%20poisoning%20vulnerabiliti%202bd021737a8980788395cd1f70a8ef7a.md)

[EXPERT: **Cache key injection**](Web%20Cache%20Poisoning/EXPERT%20Cache%20key%20injection%202bd021737a8980fd806bc514fb50e7d6.md)

[**EXPERT: Internal cache poisoning**](Web%20Cache%20Poisoning/EXPERT%20Internal%20cache%20poisoning%202bd021737a898011839effbb52be122a.md)