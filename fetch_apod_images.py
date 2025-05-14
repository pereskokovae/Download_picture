import requests
import os
from urllib.parse import unquote
from pathlib import Path
from helpers import get_photo_count
from helpers import download_images_to_directory


def load_apod_images(api_key, photo_count):
    payload = {
        'count': photo_count,
        'api_key': api_key
    }
    response = requests.get('https://api.nasa.gov/planetary/apod', params=payload)
    response.raise_for_status()
    apod_picture_details = response.json()

    image_urls = []

    for apod_url in apod_picture_details:
        if 'url' in apod_url:
            image_urls.append(unquote(apod_url['url']))

    for image_number, nasa_apod in enumerate(image_urls):
        file_format = os.path.splitext(nasa_apod)[1]
        filename = f'images/nasa_apod{image_number}{file_format}'

        download_images_to_directory(filename, api_key)



if __name__ == "__main__":
    api_key = os.getenv('NASA_API_KEY')
    photo_count = get_photo_count()
    
    Path('images/').mkdir(parents=True, exist_ok=True)
    load_apod_images(api_key, photo_count)
