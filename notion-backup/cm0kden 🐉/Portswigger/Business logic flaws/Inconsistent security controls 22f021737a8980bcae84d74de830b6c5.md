# Inconsistent security controls

Example: an application provides administrative functionality for the company employees, that have their email address on a company email domain — `@dontwannacry.com` 

After the account registration, email change functionality is available

![image.png](Inconsistent%20security%20controls/image.png)

But the application does not validate the input, and there are no validation measures to check if the user owns the email (unlike it’s done on registration stage), meaning that any value could be submitted.

![image.png](Inconsistent%20security%20controls/image%201.png)

![image.png](Inconsistent%20security%20controls/image%202.png)