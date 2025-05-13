import telegram
import os
import random
import time
from helpers import break_between_sending
from pathlib import Path


def send_messages(token_tg_bot, path_to_pictures, breaktime):
    bot = telegram.Bot(token=token_tg_bot)
    updates = bot.get_updates()
    chat_id = updates[0]['message']['chat']['id']

    while True:
        images_for_publish = os.listdir(path_to_pictures)
        random_image = random.choice(images_for_publish)
        with open(f'images/{random_image}', 'rb') as photos:
            bot.send_photo(chat_id=chat_id,  photo=photos)

        time.sleep(breaktime)


if __name__ == "__main__":
    token_tg_bot = os.getenv('TOKEN_TG_BOT')
    path_to_pictures = Path('images/').resolve()

    breaktime = break_between_sending()
    send_messages(token_tg_bot, path_to_pictures, breaktime)