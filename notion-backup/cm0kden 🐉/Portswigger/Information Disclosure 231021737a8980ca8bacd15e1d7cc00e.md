# Information Disclosure

Created: July 15, 2025 3:51 PM

## Common sources of information disclosure

Information disclosure can occur in a wide variety of 
contexts within a website. The following are some common examples of 
places where you can look to see if sensitive information is exposed.

- [Files for web crawlers](https://portswigger.net/web-security/information-disclosure/exploiting#files-for-web-crawlers)
- [Directory listings](https://portswigger.net/web-security/information-disclosure/exploiting#directory-listings)
- [Developer comments](https://portswigger.net/web-security/information-disclosure/exploiting#developer-comments)
- [Error messages](https://portswigger.net/web-security/information-disclosure/exploiting#error-messages)
- [Debugging data](https://portswigger.net/web-security/information-disclosure/exploiting#debugging-data)
- [User account pages](https://portswigger.net/web-security/information-disclosure/exploiting#user-account-pages)
- [Backup files](https://portswigger.net/web-security/information-disclosure/exploiting#source-code-disclosure-via-backup-files)
- [Insecure configuration](https://portswigger.net/web-security/information-disclosure/exploiting#information-disclosure-due-to-insecure-configuration)
- [Version control history](https://portswigger.net/web-security/information-disclosure/exploiting#version-control-history)

---

### Information disclosure in error messages (vulnerable framework used)

![image.png](Information%20Disclosure/image.png)

### Information disclosure on debug page

![image.png](Information%20Disclosure/image%201.png)

### Source code disclosure via backup files

![image.png](Information%20Disclosure/image%202.png)

### **Authentication bypass via information disclosure**

![image.png](Information%20Disclosure/image%203.png)

Profile GET request, let’s switch its HTTP method to TRACE

![image.png](Information%20Disclosure/image%204.png)

Custom authentication header is exposed and can be used by attacker.

![image.png](Information%20Disclosure/image%205.png)

We can authorize like a local user:

![image.png](Information%20Disclosure/image%206.png)

### Information disclosure in version control history

`.git` dir is available

![image.png](Information%20Disclosure/image%207.png)

Use `git-dumper` to dump and see log

![image.png](Information%20Disclosure/image%208.png)

![image.png](Information%20Disclosure/image%209.png)

![image.png](Information%20Disclosure/image%2010.png)

Leaked password is used to access admin panel

![image.png](Information%20Disclosure/image%2011.png)