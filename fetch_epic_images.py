import requests
import os
import dotenv
from datetime import datetime
from pathlib import Path
from helpers import download_images_to_directory


def load_epic_images(api_key):
    payload = {
        'api_key': api_key
    }
    response = requests.get('https://api.nasa.gov/EPIC/api/natural/images?', params=payload)
    response.raise_for_status()
    epic_images = response.json()

    all_dates = []
    all_images = []

    for epic_image in epic_images[:5]:
        all_dates.append(epic_image['date'])
        all_images.append(epic_image['image'])

    for date in all_dates:
        formated_date = datetime.fromisoformat(date).strftime("%Y/%m/%d")

        for number_image, image in enumerate(all_images):
            image_name = str.split(image)[number_image]
            url = f'https://api.nasa.gov/EPIC/archive/natural/{formated_date}/png/{image_name}.png?'
            filename = f'images/nasa_epic{number_image}.png'
            
            download_images_to_directory(url, filename, api_key)


if __name__ == "__main__":
    dotenv.load_dotenv()

    api_key = os.getenv('NASA_API_KEY')

    Path('images/').mkdir(parents=True, exist_ok=True)    
    load_epic_images(api_key)
