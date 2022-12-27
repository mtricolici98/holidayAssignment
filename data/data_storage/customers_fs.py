from data.data_storage.file_service import load_data_from_json_file, save_data_to_json_file

CUSTOMER_FILE_NAME = 'customers.json'

def get_all_customers_from_storage():
    """Will return all customers from storage

    Returns:
        list: List of all customers
    """
    data = load_data_from_json_file(CUSTOMER_FILE_NAME)
    if not data:
        return []
    return data

def save_customers_to_storage(customers_list=None):
    """Will save all data to the file. Warning: Will overwrite the current information in the file.

    Args:
        customers_list (list): List of customers to save. Defaults to None.
    """
    if not customers_list:
        customers_list = []
    save_data_to_json_file(CUSTOMER_FILE_NAME, customers_list)