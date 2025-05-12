import requests
import os
from urllib.parse import unquote
from helpers import path_for_images
from helpers import get_count_photo


def load_apod_images(api_key, count_photo):
    payload = {
        'count': count_photo,
        'api_key': api_key
    }
    response = requests.get('https://api.nasa.gov/planetary/apod', params=payload)
    response.raise_for_status()
    data = response.json()

    images_url = []
    number_image = 0

    for entry in data:
        if 'url' in entry:
            images_url.append(unquote(entry['url']))

        for nasa_apod in images_url:
            file_format = os.path.splitext(nasa_apod)[1]
            response = requests.get(nasa_apod)
            response.raise_for_status()

            filename = f'images/nasa_apod{number_image}{file_format}'

        with open(filename, 'wb') as file:
            file.write(response.content)
        number_image += 1


if __name__ == "__main__":
    api_key = os.getenv('API_KEY')
    count_photo = get_count_photo()
    
    path_for_images()
    load_apod_images(api_key, count_photo)
