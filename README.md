# About

Bot for fully anonymous voting in [Secret Hitler](https://www.secrethitler.com/) game, when you are playing offline with your friends!

# How to use?
1. Create group chat with your friends in Telegram
2. Add @secret_HBot to your chat
3. Send `/new_game` in chat when you are ready
4. Send `/vote @<president_username> @<chancellor_username>` when it is an election time!

**P.S. Bot is needed only for voting, it doesn't remember who was the last president etc.**

# Local start
1. `poetry install`
2. Create Telegram Bot using [BotFather](https://t.me/BotFather)
3. Create `token.txt` with your bot token
4. `poetry run python bot.py` or `python bot.py` after `poetry shell` 
5. Read **How to use** section, but instead of @secret_HBot add your own