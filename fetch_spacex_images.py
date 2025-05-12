import requests
from helpers import path_for_images
from helpers import get_id_spacex


def fetch_spacex_last_launch(id_spacex):
    if not id_spacex:
        response = requests.get('https://api.spacexdata.com/v5/launches/')
        response.raise_for_status()
        data = response.json()
        id_spacex = data[-1]['id']

    response = requests.get(f'https://api.spacexdata.com/v5/launches/{id_spacex}')
    response.raise_for_status()
    data = response.json()

    links_image=[]
    number_image = 0

    for links_jpg in data:
        link_image = links_jpg['links']['flickr']['original']
        if link_image:
            for url in link_image:
                links_image.append(url)

        for link in link_image:
            response = requests.get(link)
            response.raise_for_status()
            filename = f'images/spacex{number_image}.jpg'

            with open(filename, 'wb') as file:
                file.write(response.content)
            number_image += 0


if __name__ == "__main__":
    id_spacex = get_id_spacex()

    path_for_images()       
    fetch_spacex_last_launch(id_spacex)
