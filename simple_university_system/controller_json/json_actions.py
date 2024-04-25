import json
import os


def read_json_fn(file_name):
    if not os.path.isfile(file_name):
        with open(file_name, "w") as file:
            json.dump([], file)

    with open(file_name, "r") as file:
        data = json.load(file)

    return data


def write_json_fn(data, file_name):
    with open(file_name, "w") as file:
        json.dump(data, file)
