import telegram
import os
import dotenv

dotenv.load_dotenv()


def send_message(token_tg_bot):
    bot = telegram.Bot(token=token_tg_bot)
    updates = bot.get_updates()
    chat_id = updates[0]['message']['chat']['id']

    bot.send_message(text='Hello!', chat_id=chat_id)


if __name__ == "__main__":
    token_tg_bot = os.getenv('TOKEN_TG_BOT')
    send_message(token_tg_bot)