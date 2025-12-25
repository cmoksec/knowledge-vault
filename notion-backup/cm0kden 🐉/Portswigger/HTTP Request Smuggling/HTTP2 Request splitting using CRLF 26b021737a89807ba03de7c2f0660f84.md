# HTTP2 Request splitting using CRLF

Use GET / request, remove everything unnecessary, add custom header that will have CRLF and a separate request that also goes to nonexistent location

![image.png](HTTP2%20Request%20splitting%20using%20CRLF/image.png)

Send smuggled request a few times to cause response query confusion, and get access to admin account:

![image.png](HTTP2%20Request%20splitting%20using%20CRLF/image%201.png)

![image.png](HTTP2%20Request%20splitting%20using%20CRLF/image%202.png)