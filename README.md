# О боте
Бот для реализации полностью анонимного голосования в настолке [Secret Hitler](https://www.secrethitler.com/) при игре вживую
# Как использовать?
1. Создайте групповой чат в Телеграм
2. Добавьте в него @secret_HBot
3. Отправьте `/new_game` в чат, когда все роли разданы
4. Отправьте `/vote @<president_username> @<chancellor_username>` когда пришло время голосования!

**P.S. Бот создан исключительно для проведения голосования, он ничего не знает про ваши роли, кто был прошлым президентом и тд, эта ответственность ложиться на игроков!**

# Запуск собственного бота
1. `poetry install`
2. Создайте свеого Telegram бота при помощи [BotFather](https://t.me/BotFather)
3. Создайте файл `token.txt` с токеном вашего бота
4. `poetry run python bot.py` или `python bot.py` после `poetry shell` 
5. Вернитесь к разделу **Как использовать?** , но вместо @secret_HBot добавьте своего бота