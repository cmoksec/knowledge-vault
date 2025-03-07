# $authbypass

Created: January 31, 2025 12:15 AM

## PHP Insecure Serialization

Было:

```bash
Cookie: Access=YTozOntzOjU6ImxvZ2luIjtzOjQ6InVzZXIiO3M6NjoicGFzc3dkIjtzOjg6InBhc3N3b3JkIjtzOjQ6ImF1dGgiO3M6MTA6InNpbXBsZVVzZXIiO30lM0QlM0Q=
```

Или же, если перевести в плейнтекст:

```bash
Cookie: Access=a:3:{s:5:"login";s:4:"user";s:6:"passwd";s:8:"password";s:4:"auth";s:10:"simpleUser";}%3D%3D
```

Как видно, это небезопасная сериализация PHP. По структуре можно предположить, что сервер обрабатывает права пользователя исходя из значения поля **auth.** Возможно, проверка такого рода:

```php
$data['auth'] == "superMegaAdmin"
```

Однако мы не знаем, с какой именно строкой сравнивается переменная. Но это можно легко обойти. Вот такое значение всегда истинно:

```php
0 == "superMegaAdmin"
```

Строка “superMegaAdmin” неявно привелась к числу 0, и выражение вернуло истину. [Здесь](https://portswigger.net/web-security/deserialization/exploiting) можно почитать подробнее.

В остальном тема перекликается с предыдущими, методичку прикрепляю.

---

[6.7 Обход авторизации.pdf]($authbypass%2018b021737a89803fa6d8e2ebfd10ff79/6.7_%D0%9E%D0%B1%D1%85%D0%BE%D0%B4_%D0%B0%D0%B2%D1%82%D0%BE%D1%80%D0%B8%D0%B7%D0%B0%D1%86%D0%B8%D0%B8.pdf)