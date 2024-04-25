import json

def write_json_fn(data, track):
    with open(track, "w") as file:
        json.dump(data, file)