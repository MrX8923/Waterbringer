import json
from string import ascii_letters
from random import choice


def make_json(dct: dict, file_path: str) -> None:
    json_key = ''.join([choice(ascii_letters) for _ in range(10)])
    try:
        with open(f'{file_path}', 'r') as file:
            temp: dict = json.load(file)

        temp.update({json_key: dct})

        with open(f'{file_path}', 'w') as file:
            json.dump(
                temp,
                file,
                indent=2
            )
    except Exception as exc:
        print(exc)
        with open(f'{file_path}', 'w') as file:
            json.dump(
                {json_key: dct},
                file,
                indent=2
            )
