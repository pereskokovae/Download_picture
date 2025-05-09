import requests
import os
import dotenv
from pathlib import Path
from urllib.parse import unquote
from datetime import datetime

dotenv.load_dotenv()


def load_pictures():
    filename = 'hubble'
    url = input('Введите url картинки которую хотите скачать: ')

    response = requests.get(url)
    response.raise_for_status()

    with open(f'images/{filename}.jpeg', 'wb') as file:
        file.write(response.content)


def fetch_spacex_last_launch(id_spacex):
    payload={
        'id': id_spacex
    }
    response = requests.get('https://api.spacexdata.com/v5/launches/', params=payload)
    response.raise_for_status()
    data = response.json()

    links_image=[]
    number = 1

    for links_jpg in data:
        link_image = links_jpg['links']['flickr']['original']
        if link_image:
            for url in link_image:
                links_image.append(url)

        for link in link_image:
            response = requests.get(link)
            response.raise_for_status()

            filename = f'images/spacex{number}.jpg'
            with open(filename, 'wb') as file:
                file.write(response.content)
            number += 1


def load_apod_images(api_key):
    payload = {
        'count': '30',
        'api_key': api_key
    }
    response = requests.get('https://api.nasa.gov/planetary/apod', params=payload)
    response.raise_for_status()
    data = response.json()

    images_url = []
    number = 1

    for entry in data:
        if 'url' in entry:
            images_url.append(unquote(entry['url']))

        for nasa_apod in images_url:
            file_format = os.path.splitext(nasa_apod)[1]
            response = requests.get(nasa_apod)
            response.raise_for_status()

            filename = f'images/nasa_apod{number}{file_format}'

        with open(filename, 'wb') as file:
            file.write(response.content)
        number += 1


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
            number = 0
            image_name = str.split(image)[number]

            response_image = requests.get(f'https://api.nasa.gov/EPIC/archive/natural/{formated_date}/png/{image_name}.png?', params=payload)
            response_image.raise_for_status()

            filename = f'images/nasa_epic{number}.png'

            with open(filename, 'wb') as file:
                file.write(response_image.content)
            number += 1
        

if __name__ == "__main__":
    api_key = os.getenv('API_KEY')
    id_spacex = os.getenv('ID_SPACEX')

    Path('images/').mkdir(parents=True, exist_ok=True) 
    load_epic_images(api_key)
