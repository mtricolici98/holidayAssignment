from data.data_storage.file_service import load_data_from_json_file, save_data_to_json_file

CARS_FILE_NAME = 'cars.json'

def get_all_cars_from_storage():
    """Will load all cars from file storage

    Returns:
        list: list of all cars
    """
    data = load_data_from_json_file(CARS_FILE_NAME)
    if not data:
        return []
    return data

def save_cars_to_storage(cars_list=None):
    """Will save all cars to storage. Warning: Will overwrite all data.

    Args:
        cars_list (list, optional): List of cars to save. Defaults to None.
    """
    
    if not cars_list:
        cars_list = []
    save_data_to_json_file(CARS_FILE_NAME, cars_list)