# permissions

Created: February 5, 2025 10:05 PM

Задача на эскалацию привелегий. Мы появляемся как непривелигированный пользователь, нужно эскалировать привелегии до рута. Сразу видим, что команды листинга не работают.

![image.png](permissions%20191021737a89807bb0e8dc1f8f7d2aec/image.png)

Проверяем, какие права у нас есть. Для этого используем команду

```php
sudo -l
```

Видим, что мы можем выполнять текстовый редактор vim от имени рута.

![image.png](permissions%20191021737a89807bb0e8dc1f8f7d2aec/image%201.png)

Идем на [GTFOBins](https://gtfobins.github.io/gtfobins/vi/#shell) и обнаруживаем, что привелегированный вим может заспавнить рут шелл

![image.png](permissions%20191021737a89807bb0e8dc1f8f7d2aec/image%202.png)

Пробуем. Получили рутовый шелл!

![image.png](permissions%20191021737a89807bb0e8dc1f8f7d2aec/image%203.png)

Дальше без проблем находим файл флага и читаем. Бинго!

![image.png](permissions%20191021737a89807bb0e8dc1f8f7d2aec/image%204.png)