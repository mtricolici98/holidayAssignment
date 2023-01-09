from data.data_access.customers_access import  CustomerExistsException, CustomerNotFound, add_customer, find_customer_by_idnp, get_all_customers
from view.utils import get_date, menu_tool


def print_customer(customer: dict):
    print('Selected customer: \n')
    print('IDNP:', customer['idnp'])
    print('First Name:',customer['first_name'])
    print('Last Name:',customer['last_name'])
    print('Date of birth:',customer['dob'])

def print_customer_small(customer):
    print(f"Customer [{customer['idnp']}]: {customer['first_name']} {customer['last_name']}, {customer['dob']}")
    
def add_customer_view():
    print('Adding customer, please provide info:')
    customer = dict()
    customer['idnp'] = input('IDNP:')
    customer['first_name'] = input('First Name:')
    customer['last_name'] = input('Last Name :')
    customer['dob'] = get_date()
    try:
        add_customer(customer)
    except CustomerExistsException:
        print('Customer already exists, Try Again.')
    print('Succesfully created')
    print_customer_small(customer)
    
def list_customers():
    print('Here\'s the list:\n')
    for customer in get_all_customers():
        print_customer_small(customer)


def info_by_idnp():
    idnp = input('Customer IDNP:')
    try:
        customer = find_customer_by_idnp(idnp)
        print_customer(customer)
    except CustomerNotFound as ex:
        print(str(ex))
     
     
def get_menu_text():
    return """
    1: Add customer
    2: List customers
    3: Get customer info by idnp
    """
        
def get_customer_menu():
    opt_dict = {
        1: add_customer_view,
        2: list_customers,
        3: info_by_idnp
    }
    menu_tool(menu_text=get_menu_text(), options_dict=opt_dict, stop_word='back')