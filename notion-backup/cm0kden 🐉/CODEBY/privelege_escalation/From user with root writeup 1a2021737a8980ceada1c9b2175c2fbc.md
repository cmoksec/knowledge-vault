# From user with root writeup

Дан таргет сайт:

![image.png](From%20user%20with%20root%20writeup/image.png)

Замечаем интересную особенность — если вбить несуществующий путь, вместо 404 будет кастомная страница:

![image.png](From%20user%20with%20root%20writeup/image%201.png)

Это — SSTI, а именно Jinja2.

![image.png](From%20user%20with%20root%20writeup/image%202.png)

Прокинем реверсшелл с помощью RCE (в хинте говорится, что на сервере присутствует netcat):

![image.png](From%20user%20with%20root%20writeup/image%203.png)

![image.png](From%20user%20with%20root%20writeup/image%204.png)

Шелл получен, заспавним tty с помощью python:

![image.png](From%20user%20with%20root%20writeup/image%205.png)

Проверим SUID-бинарки (команда [отсюда](https://swisskyrepo.github.io/InternalAllTheThings/redteam/escalation/linux-privilege-escalation/#find-suid-binaries))

![image.png](From%20user%20with%20root%20writeup/image%206.png)

Как вариант, можно эскалировать привелегии с помощью `cp`

Скопируем в tmp файл `/etc/passwd`

![image.png](From%20user%20with%20root%20writeup/image%207.png)

Идея следующая — склонировать файл паролей, добавить туда пользователя с известным паролем и рут правами, и залогиниться под ним.

Используем рут юзера `evil` с паролем `password`:

```bash
evil:$1$evil$nQuhWDmzDqj5JWJG19JQ0/:0:0:root:/root:/bin/bash
```

Создаем на нашем IPS файл-клон passwd с этим пользователем и копируем его на таргет машину.

![image.png](From%20user%20with%20root%20writeup/image%208.png)

![image.png](From%20user%20with%20root%20writeup/image%209.png)

Подставляем его в `/etc/passwd`

![image.png](From%20user%20with%20root%20writeup/image%2010.png)

Видим что нужный пользователь появился. Пробуем зайти, используя известный заранее пароль `passwd`:

![image.png](From%20user%20with%20root%20writeup/image%2011.png)

Вот и все, теперь мы рут. Читаем флаг в `/root` и сдаем )

![image.png](From%20user%20with%20root%20writeup/image%2012.png)