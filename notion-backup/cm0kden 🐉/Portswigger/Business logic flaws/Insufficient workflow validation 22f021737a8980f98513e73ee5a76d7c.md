# Insufficient workflow validation

An application has an order placement functionality, that has key stages like:

1. POST /cart — used to add new products to the cart
2. POST /cart/checkout — making a payment to checkout the order
3. GET /cart/order-confirmation?order-confirmed=true — get a page that says the order is submitted

![image.png](Insufficient%20workflow%20validation/image.png)

The vulnerability is, in this scenario, the app is not enforcing 2nd step, and using web proxies, we can replicate a sequence of 1nd and 3rd steps only, not making a payment, but confirming the order.

![image.png](Insufficient%20workflow%20validation/image%201.png)

![image.png](Insufficient%20workflow%20validation/image%202.png)

No payment was made, but product was purchased.

![image.png](Insufficient%20workflow%20validation/image%203.png)