import argparse
import requests


def get_spacex_id():
    parser = argparse.ArgumentParser(
        description='Программа загрузит фото от SpaceX по указанному ID запуска.'
    )
    parser.add_argument("-i", "--id", help="Введите ID нужного запуска")
    args = parser.parse_args()
    return args.id


def get_photo_count():
    parser = argparse.ArgumentParser(
        description='Программа загрузит столько фотографий-сколько вы укажите.'
    )
    parser.add_argument("-c", "--count", help="Введите число фотографий которых хотите скачать.")
    args = parser.parse_args()
    return args.count


def break_between_sending():
    parser = argparse.ArgumentParser(
        description='Программа запустит таймер, по окончанию которого, будут высылаться новые фотографии.'
    )
    parser.add_argument("-t", "--time", help="Введите время перерыва в секундах, которое должно пройти перед отправкой новой фотографии.")
    args = parser.parse_args()
    return args.time


def downloads_images_to_directory(url, filepath, api_key):
    payload = {
        'api_key': api_key
    }
    response_image = requests.get(url, params=payload)
    response_image.raise_for_status()

    with open(filepath, 'wb') as file:
        file.write(response_image.content)