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
