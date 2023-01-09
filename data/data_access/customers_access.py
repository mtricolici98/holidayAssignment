from data.data_storage.customers_fs import get_all_customers_from_storage, save_customers_to_storage

class CustomerNotFound(Exception):
    pass

class CustomerExistsException(Exception):
    pass

def get_all_customers():
    return get_all_customers_from_storage()

def find_customer_by_idnp(idnp:str):
    all_customers = get_all_customers()
    for customer in all_customers:
        if customer['idnp'] == idnp:
            return customer
    raise CustomerNotFound('Customer with idnp ', idnp, 'does not exist')

def add_customer(customer:dict):
    customer_exists = True
    try:
        find_customer_by_idnp(customer['idnp'])
    except CustomerNotFound:
        customer_exists = False
    if customer_exists:
        raise CustomerExistsException('Cannot add customer')
    all_customers = get_all_customers()
    all_customers.append(customer)
    save_customers_to_storage(all_customers)

def edit_customer_data(idnp: str, new_data: dict):
    all_customers = get_all_customers()
    for a in range(len(all_customers)):
        if all_customers[a]['idnp'] == idnp:
            all_customers[a] = new_data
            break
    else:
        raise CustomerNotFound()

def remove_customer_by_idnp(idnp: str):
    all_customers = get_all_customers()
    for idx, customer in enumerate(all_customers):
        if customer['idnp'] == idnp:
            all_customers.pop(idx)
            break
    else:
        raise CustomerNotFound()