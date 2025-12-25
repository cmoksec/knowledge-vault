# Infinite money logic flaw

The application has a coupon for customers signed to their newsletter:

![image.png](Infinite%20money%20logic%20flaw/image.png)

![image.png](Infinite%20money%20logic%20flaw/image%201.png)

The shop sells gift cards that can be redeemed to obtain money on the account for 10$.

![image.png](Infinite%20money%20logic%20flaw/image%202.png)

The trick is, if we apply a coupon, buy a card and redeem it, it will deposit 10$ while only 7$ were spent:

![image.png](Infinite%20money%20logic%20flaw/image%203.png)

![image.png](Infinite%20money%20logic%20flaw/image%204.png)

![image.png](Infinite%20money%20logic%20flaw/image%205.png)

![image.png](Infinite%20money%20logic%20flaw/image%206.png)

Let’s craft a macros to perform infinite money deposit. We need to select a sequence with crucial steps for that glitch:

![image.png](Infinite%20money%20logic%20flaw/image%207.png)

![image.png](Infinite%20money%20logic%20flaw/image%208.png)

![image.png](Infinite%20money%20logic%20flaw/image%209.png)

Now let’s configure mapping to gather a coupon code that was purchased to use it in `POST /gift-card` request:

![image.png](Infinite%20money%20logic%20flaw/image%2010.png)

Adding a custom parameter:

![image.png](Infinite%20money%20logic%20flaw/image%2011.png)

Highlight the latest purchased code, it will be automatically configured to be collected using regex patterns:

![image.png](Infinite%20money%20logic%20flaw/image%2012.png)

After OK:

![image.png](Infinite%20money%20logic%20flaw/image%2013.png)

Now, let’s configure auto-redeem of that parameter, select `POST /gift-card` request. Make sure `gift-card` param has the exact same name and is fetched from a needed request.

![image.png](Infinite%20money%20logic%20flaw/image%2014.png)

![image.png](Infinite%20money%20logic%20flaw/image%2015.png)

Done, let’s test this macro. Balance before:

![image.png](Infinite%20money%20logic%20flaw/image%2016.png)

Click Test macro:

![image.png](Infinite%20money%20logic%20flaw/image%2017.png)

Balance after:

![image.png](Infinite%20money%20logic%20flaw/image%2018.png)

We can now launch an attack to gain any amount of money we want. But first, we need to connect a macro to a particular request to activate it. Add a session handling rule:

![image.png](Infinite%20money%20logic%20flaw/image%2019.png)

![image.png](Infinite%20money%20logic%20flaw/image%2020.png)

Connect it to some legit request.

![image.png](Infinite%20money%20logic%20flaw/image%2021.png)

Confirm.

![image.png](Infinite%20money%20logic%20flaw/image%2022.png)

Now, let’s launch an Intruder attack & use a request we tied to with Null payloads. **It’s important to use only 1 thread to run the Intruder, so that the macros won’t get broken**:

![image.png](Infinite%20money%20logic%20flaw/image%2023.png)

Run the attack and wait for it to finish:

![image.png](Infinite%20money%20logic%20flaw/image%2024.png)