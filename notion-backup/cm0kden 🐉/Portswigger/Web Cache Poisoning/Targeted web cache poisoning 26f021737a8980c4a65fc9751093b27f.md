# Targeted web cache poisoning

![image.png](Targeted%20web%20cache%20poisoning/image.png)

Going to the lab. Using Param Miner, identify secret header, revealing a vector for Web Cache Poisoning attack

![image.png](Targeted%20web%20cache%20poisoning/image%201.png)

Deploy sample script to the exploit server:

![image.png](Targeted%20web%20cache%20poisoning/image%202.png)

Poison web cache

![image.png](Targeted%20web%20cache%20poisoning/image%203.png)

![image.png](Targeted%20web%20cache%20poisoning/image%204.png)

Then, notice comments section contains posting HTML. It’s using DOM Purify, but we still can post the image with source leading to our Collaborator:

![image.png](Targeted%20web%20cache%20poisoning/image%205.png)

![image.png](Targeted%20web%20cache%20poisoning/image%206.png)

Got the request from the victim:

![image.png](Targeted%20web%20cache%20poisoning/image%207.png)

The task for this lab is to target the exact subset of users where Victim sits. So, we need to understand what differs them from the others.

And we can understand it by `Vary` header on `GET /`  response. `Vary`  specifies additional headers that may be treated as part of cache key. In our case, it’s `User-Agent` . And we just got needed `User-Agent` of our user, meaning we can target him directly.

![image.png](Targeted%20web%20cache%20poisoning/image%208.png)

Fine-tune the script:

![image.png](Targeted%20web%20cache%20poisoning/image%209.png)

Poison the cache:

![image.png](Targeted%20web%20cache%20poisoning/image%2010.png)

Done

![image.png](Targeted%20web%20cache%20poisoning/image%2011.png)