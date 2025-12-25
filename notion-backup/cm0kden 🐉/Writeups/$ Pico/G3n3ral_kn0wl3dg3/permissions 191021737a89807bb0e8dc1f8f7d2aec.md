# permissions

Created: February 5, 2025 10:05 PM

Задача на эскалацию привелегий. Мы появляемся как непривелигированный пользователь, нужно эскалировать привелегии до рута. Сразу видим, что команды листинга не работают.

![image.png](permissions/image.png)

Проверяем, какие права у нас есть. Для этого используем команду

```php
sudo -l
```

Видим, что мы можем выполнять текстовый редактор vim от имени рута.

![image.png](permissions/image%201.png)

Идем на [GTFOBins](https://gtfobins.github.io/gtfobins/vi/#shell) и обнаруживаем, что привелегированный вим может заспавнить рут шелл

![image.png](permissions/image%202.png)

Пробуем. Получили рутовый шелл!

![image.png](permissions/image%203.png)

Дальше без проблем находим файл флага и читаем. Бинго!

![image.png](permissions/image%204.png)