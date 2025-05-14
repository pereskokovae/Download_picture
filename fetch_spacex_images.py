import requests
from pathlib import Path
from helpers import get_spacex_id
from helpers import download_images_to_directory


def fetch_spacex_last_launch(spacex_id):
    if not spacex_id:
        response = requests.get('https://api.spacexdata.com/v5/launches/')
        response.raise_for_status()
        spacex_launches = response.json()
        spacex_id = spacex_launches[-1]['id']

    response = requests.get(f'https://api.spacexdata.com/v5/launches/{spacex_id}')
    response.raise_for_status()
    launch_details = response.json()

    image_links=[]

    for links_jpg in launch_details:
        link_image = links_jpg['links']['flickr']['original']
        if link_image:
            for url in link_image:
                image_links.append(url)

    for image_number, url in enumerate(link_image):
        filename = f'images/spacex{image_number}.jpg'

        download_images_to_directory(url, filename)


if __name__ == "__main__":
    spacex_id = get_spacex_id()

    Path('images/').mkdir(parents=True, exist_ok=True)     
    fetch_spacex_last_launch(spacex_id)
