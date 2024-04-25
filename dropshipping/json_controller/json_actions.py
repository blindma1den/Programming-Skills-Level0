
import json
import os

def read_json_fn(file_path):
    if not os.path.isfile(file_path):
        with open(file_path, 'w') as file:
            json.dump([], file)

    with open(file_path, 'r') as file:
        data = json.load(file)
    
    return data


def write_json_fn(data, file_path):
    with open(file_path, 'w') as file:
        json.dump(data, file)