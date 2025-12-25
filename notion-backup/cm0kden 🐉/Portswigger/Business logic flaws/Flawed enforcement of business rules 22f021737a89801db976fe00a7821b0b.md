# Flawed enforcement of business rules

An application has a coupon applying functionality. One coupon is for new users:

![image.png](Flawed%20enforcement%20of%20business%20rules/image.png)

Another one is for users that signed to the newsletter:

![image.png](Flawed%20enforcement%20of%20business%20rules/image%201.png)

![image.png](Flawed%20enforcement%20of%20business%20rules/image%202.png)

The vulnerability here is, application only checks for a previously applied coupon, and does not check the overall coupon history if there are multiple. Using this flaw, we can re-use coupons and make a huge discount:

![image.png](Flawed%20enforcement%20of%20business%20rules/image%203.png)