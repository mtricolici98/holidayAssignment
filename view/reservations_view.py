from data.data_access.cars_access import find_car_by_plate_nr
from data.data_access.customers_access import CustomerExistsException, CustomerNotFound, find_customer_by_idnp, \
    get_all_customers
from data.data_access.reservations_access import add_reservation, get_reservations_for_car, get_all_reservations, \
    ReservationConflict
from view.car_views import print_car_small, list_cars
from view.customer_view import print_customer_small, list_customers
from view.utils import get_date, menu_tool


def print_reservation(reservation: dict):
    print('Selected reservation: \n')
    print_customer_small(find_customer_by_idnp(reservation['customer_idnp']))
    print('FOR')
    print_car_small(find_car_by_plate_nr(reservation['car_plate_number']))
    print('AT:', reservation['date'])


def print_reservation_small(reservation):
    print(
        f"Reservation for [{reservation['customer_idnp']}] "
        f"of {reservation['car_plate_number']} on [{reservation['date']}]"
    )


def add_reservation_view():
    print('Adding reservation, please provide info:')
    print('Cars list:')
    list_cars()
    print('Customer list:')
    list_customers()
    print("Make your choises")
    reservation = dict()
    reservation['car_plate_number'] = input('Plate NR:')
    reservation['customer_idnp'] = input('Customer IDNP:')
    reservation['date'] = get_date()
    created = False
    while not created:
        try:
            add_reservation(reservation)
            break
        except ReservationConflict as ex:
            print(ex)
            reservation['car_plate_number'] = input('Plate NR:')
            reservation['customer_idnp'] = input('Customer IDNP:')
            reservation['date'] = get_date()
    print('Succesfully created')
    print_reservation(reservation)


def list_reserv():
    print('Here\'s the list:\n')
    for customer in get_all_reservations():
        print_reservation_small(customer)


def info_by_plate_nr():
    plate_nr = input('Car Plate Number:')
    reservations = get_reservations_for_car(plate_nr)
    if not reservations:
        print('No reservations for the car at all')
    for reserv in reservations:
        print_reservation_small(reserv)


def get_menu_text():
    return """
    1: Add reserv
    2: List reserv
    3: Get reserv info by plate nr
    4: Get upcoming for car
    5: Get past for car
    6: Get current for car
    """


def get_reserv_menu():
    opt_dict = {
        1: add_reservation_view,
        2: list_reserv,
        3: info_by_plate_nr
    }
    menu_tool(menu_text=get_menu_text(), options_dict=opt_dict, stop_word='back')
