# file_upload_skill_assessment

Given: a website with contact form, that has an option to upload screenshots.

![image.png](file_upload_skill_assessment%201c1021737a89801ba3a8db00a28c1688/image.png)

First, we’ll test for XXE vuln using SVG upload. First, amend frontent script to allow svg upload, then upload PoC file.

![image.png](file_upload_skill_assessment%201c1021737a89801ba3a8db00a28c1688/image%201.png)

```bash
<?xml version="1.0" encoding="UTF-8"?>
<!DOCTYPE svg [ <!ENTITY xxe SYSTEM "file:///etc/passwd"> ]>
<svg>&xxe;</svg>
```

![image.png](file_upload_skill_assessment%201c1021737a89801ba3a8db00a28c1688/image%202.png)

App is vulnerable. As seen from Burp History, there’s upload.php script that handles uploads. Let’s read the source code.

![image.png](file_upload_skill_assessment%201c1021737a89801ba3a8db00a28c1688/image%203.png)

```bash
<?xml version="1.0" encoding="UTF-8"?>
<!DOCTYPE svg [ <!ENTITY xxe SYSTEM "php://filter/convert.base64-encode/resource=/var/www/html/contact/upload.php"> ]>
<svg>&xxe;</svg>
```

Now we can see source and all the validations:

![image.png](file_upload_skill_assessment%201c1021737a89801ba3a8db00a28c1688/image%204.png)

There are several checks in place:

1. Blacklisting for php, phps, phtml
2. Whitelisting image extensions by using regex: `'/^.+\.[a-z]{2,3}g$/’`
3. Type test: `Content Type` header and MIME type to match regex `'/image\/[a-z]{2,3}g/’` (starts with /image and then goes 2-3 chars closed by ‘g’, like `image/png`)
4. Size test

Having this info in place, we are able to bypass all the filters. We will be trying to escalate arbitrary code execution.

But first, it’s needed to understand where the uploaded files are stored. We have upload directory disclosure: `./user_feedback_submissions/`, and it’s clear how file name is mutated: `$fileName = date('ymd') . '_' . basename($_FILES["uploadFile"]["name"]);`, script takes current date (year, month, date), appends `_` and file name. Let’s check the file we used as PoC. With initial name `readpoc.svg`, mutated name will be `250325_readpoc.svg`. Let’s try getting the file directly via URL:

 

![image.png](file_upload_skill_assessment%201c1021737a89801ba3a8db00a28c1688/image%205.png)

Success. Now we can start bypassing filters and uploading a webshell:

1. To bypass blacklisting of php extensions, we can use phar, which is not on the list
2. To bypass whitelisting of image extensions, we can exploit a flaw in regex — it is accepting any input before enclosing image extension. We will use double extension `.phar.png`
3. To bypass MIME & Content Type check, we can mimic a valid image upload by repeating PNG file upload with appended payload
4. File size will be bypassed with no efforts

Final forged request:

 

![forged filename: shell.phar.png](file_upload_skill_assessment%201c1021737a89801ba3a8db00a28c1688/image%206.png)

forged filename: shell.phar.png

…

![minishell appended after the image](file_upload_skill_assessment%201c1021737a89801ba3a8db00a28c1688/image%207.png)

minishell appended after the image

Let’s hit send:

![image.png](file_upload_skill_assessment%201c1021737a89801ba3a8db00a28c1688/image%208.png)

Success, now we’ll access our webshell and get the flag:

![image.png](file_upload_skill_assessment%201c1021737a89801ba3a8db00a28c1688/image%209.png)

![image.png](file_upload_skill_assessment%201c1021737a89801ba3a8db00a28c1688/image%2010.png)

[https://www.notion.so](https://www.notion.so)

PWNed!