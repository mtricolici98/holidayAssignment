from data.data_storage.file_service import load_data_from_json_file, save_data_to_json_file

RESERVATIONS_FILE_NAME = 'reservations.json'

def get_all_reservations_from_storage():
    """Will return all the reservations from file storage

    Returns:
        list: list of all reservations
    """
    data = load_data_from_json_file(RESERVATIONS_FILE_NAME)
    if not data:
        return []
    return data

def save_reservations_to_storage(reservations_list=None):
    """
    Saves all reservations from file storage
    !!WARNING!! Will overwrite all the data.

    Args:
        reservations_list (list, optional): List of reservations to save. Defaults to None.
    """
    if not reservations_list:
        reservations_list = []
    save_data_to_json_file(RESERVATIONS_FILE_NAME, reservations_list)