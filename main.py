import requests
import os
import dotenv
from datetime import datetime
from helpers import path_for_images

dotenv.load_dotenv()


def load_pictures():
    filename = 'hubble'
    url = input('Введите url картинки которую хотите скачать: ')

    response = requests.get(url)
    response.raise_for_status()

    with open(f'images/{filename}.jpeg', 'wb') as file:
        file.write(response.content)


def load_epic_images(api_key):
    payload = {
        'api_key': api_key
    }
    response = requests.get('https://api.nasa.gov/EPIC/api/natural/images?', params=payload)
    response.raise_for_status()
    data = response.json()

    all_dates = []
    all_images = []

    for entry in data[:5]:
        all_dates.append(entry['date'])
        all_images.append(entry['image'])

    for date in all_dates:
        formated_date = datetime.fromisoformat(date).strftime("%Y/%m/%d")

        for image in all_images:
            number_image = 0
            image_name = str.split(image)[number_image]

            response_image = requests.get(f'https://api.nasa.gov/EPIC/archive/natural/{formated_date}/png/{image_name}.png?', params=payload)
            response_image.raise_for_status()

            filename = f'images/nasa_epic{number_image}.png'

            with open(filename, 'wb') as file:
                file.write(response_image.content)
            number_image += 1
        

if __name__ == "__main__":
    path_for_images()

    api_key = os.getenv('API_KEY')

    load_epic_images(api_key)
