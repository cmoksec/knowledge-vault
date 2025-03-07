# KRONOS AI - writeup

На начальном экране SQLi (скрипт выделенный жирным - тупиковый вектор)

![image.png](KRONOS%20AI%20-%20writeup%20185021737a89807a87aff5c6164dbcb5/image.png)

Раскрутил UNION инъекцию, нашел базу с сообщениями

![image.png](KRONOS%20AI%20-%20writeup%20185021737a89807a87aff5c6164dbcb5/image%201.png)

В сообщениях - ссылка на проект и 2 части флага:

![image.png](KRONOS%20AI%20-%20writeup%20185021737a89807a87aff5c6164dbcb5/image%202.png)

Перехожу на проект и сразу начинаю фаззить

![image.png](KRONOS%20AI%20-%20writeup%20185021737a89807a87aff5c6164dbcb5/image%203.png)

Находится директория /admin

![image.png](KRONOS%20AI%20-%20writeup%20185021737a89807a87aff5c6164dbcb5/image%204.png)

Поле для команды уязвимо к PHPi, проверил с помощью phpinfo(); - обязательно кавычки. Развиваем до RCE, в ответе приходит третья часть флага:

![image.png](KRONOS%20AI%20-%20writeup%20185021737a89807a87aff5c6164dbcb5/image%205.png)

С помощью RCE нахожу файл флага, но его охраняет WAF - не дает обратиться по абсолютному пути. Использую wildcard и получаю последнюю часть флага. Профит!

![image.png](KRONOS%20AI%20-%20writeup%20185021737a89807a87aff5c6164dbcb5/image%206.png)