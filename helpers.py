from pathlib import Path
import argparse


def path_for_images():
    Path('images/').mkdir(parents=True, exist_ok=True)


def get_id_spacex():
    parser = argparse.ArgumentParser(
        description='Программа загрузит фото от SpaceX по указанному ID запуска.'
    )
    parser.add_argument("-i", "--id", help="Введите ID нужного запуска")
    args = parser.parse_args()
    return args.id


def get_count_photo():
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