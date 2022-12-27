from data.data_storage.customers_fs import get_all_customers_from_storage


def get_all_customers():
    return get_all_customers_from_storage()

def add_customer(first_name, last_name, idnp, dob):
    pass #TODO: Implement

# TODO: Implement other methods (Remove/Find/Edit)