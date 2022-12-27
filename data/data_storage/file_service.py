import json
import os

from config import DATA_STORAGE_PATH

def get_path_for_file_name(file_name):
    return os.path.join(DATA_STORAGE_PATH, file_name)
    

def load_from_file(file_name):
    try:
        return open(get_path_for_file_name(file_name), 'r').read()
    except Exception as ex:
        return None

def save_to_file(file_name, data):
    try:
        return open(get_path_for_file_name(file_name), 'w').write(data)
    except Exception as ex:
        print(f"Failed to save to file {file_name}")
        return None


def load_data_from_json_file(file_name):
    try:
        return json.loads(load_from_file(file_name=file_name))
    except Exception as ex:
        print(ex)
        return None

def save_data_to_json_file(file_name, data):
    return save_to_file(file_name, json.dumps(data))
