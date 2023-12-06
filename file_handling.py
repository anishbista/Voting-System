import json


def read_file(file):
    with open(file, "r") as f:
        try:
            return json.load(f)
        except:
            return {}


def write_file(obj, file):
    with open(file, "w") as f:
        json.dump(obj, f,indent=4)
