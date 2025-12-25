# Connection state attack

### Connection state attacks

For performance reasons, many websites reuse connections for
 multiple request/response cycles with the same client. Poorly 
implemented HTTP servers sometimes work on the dangerous assumption that
 certain properties, such as the Host header, are identical for all 
HTTP/1.1 requests sent over the same connection. This may be true of 
requests sent by a browser, but isn't necessarily the case for a 
sequence of requests sent from Burp Repeater. This can lead to a number 
of potential issues.

For example, you may occasionally encounter servers that 
only perform thorough validation on the first request they receive over a
 new connection. In this case, you can potentially bypass this 
validation by sending an innocent-looking initial request then following
 up with your malicious one down the same connection.

---

### Solution

1. Send the `GET /` request to Burp Repeater.
2. Make the following adjustments:
    - Change the path to `/admin`.
    - Change `Host` header to `192.168.0.1`.
3. Send the request. Observe that you are simply redirected to the homepage.

![image.png](Connection%20state%20attack/image.png)

1. Duplicate the tab, then add both tabs to a new group.

![image.png](Connection%20state%20attack/image%201.png)

1. Select the first tab and make the following adjustments:
    - Change the path back to `/`.
    - Change the `Host` header back to `YOUR-LAB-ID.h1-web-security-academy.net`.
    
    ![image.png](Connection%20state%20attack/image%202.png)
    
2. Using the drop-down menu next to the **Send** button, change the send mode to **Send group in sequence (single connection)**.
3. Change the `Connection` header to `keep-alive`.
4. Send the sequence and check the responses.

![image.png](Connection%20state%20attack/image%203.png)

1. Observe that the second request has successfully accessed the admin
panel.

![image.png](Connection%20state%20attack/image%204.png)

1. Study the response and observe that the
admin panel contains an HTML form for deleting a given user. Make a note of the following details:
    - The action attribute (`/admin/delete`)
    - The name of the input (`username`)
    - The `csrf` token.
2. On the second tab in your group, use these
details to replicate the request that would be issued when submitting
the form. The result should look something like this: `POST /admin/delete HTTP/1.1
Host: 192.168.0.1
Cookie: _lab=YOUR-LAB-COOKIE; session=YOUR-SESSION-COOKIE
Content-Type: x-www-form-urlencoded
Content-Length: CORRECT
csrf=YOUR-CSRF-TOKEN&username=carlos`
3. Send the requests in sequence down a single connection to solve the lab.

![image.png](Connection%20state%20attack/image%205.png)

![image.png](Connection%20state%20attack/image%206.png)