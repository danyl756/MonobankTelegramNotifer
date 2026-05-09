Запит для встановлення вебхука, X - Токен з api.monobank.ua, X.X.X.X/webhook - адреса веб сервера

curl -X POST -H "X-Token: X" -d "{\"webhookurl\": \"http://X.X.X.X/webhook\"}" https://api.monobank.ua/personal/webhook


Запит для отримання інформації про клієнта(включаючи адресу вебхука), X - Токен з api.monobank.ua

curl -X GET -H "X-Token: X" https://api.monobank.ua/personal/client-info
