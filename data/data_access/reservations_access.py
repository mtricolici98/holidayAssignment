from data.data_access.cars_access import find_car_by_plate_nr, CarNotFound
from data.data_access.customers_access import find_customer_by_idnp
from data.data_storage.reservations_fs import get_all_reservations_from_storage, save_reservations_to_storage


class ReservationConflict(Exception):
    pass


def get_all_reservations():
    return get_all_reservations_from_storage()


def get_reservations_for_car(plate_number: str):
    return [reserv for reserv in get_all_reservations() if reserv['car_plate_number'] == plate_number]


def upcoming_reservations_for_car(plate_number, date_to_match: tuple):
    reservations = get_reservations_for_car(plate_number)
    return [reserv for reserv in reservations if date_to_match > tuple(reserv['date'])]


def current_reservations_for_car(plate_number, date_to_match: tuple):
    reservations = get_reservations_for_car(plate_number)
    return [reserv for reserv in reservations if date_to_match == tuple(reserv['date'])]


def past_reservations_for_car(plate_number, date_to_match: tuple):
    reservations = get_reservations_for_car(plate_number)
    return [reserv for reserv in reservations if date_to_match < tuple(reserv['date'])]


def validate_reservation_confilct(reservation):
    try:
        find_car_by_plate_nr(reservation['car_plate_number'])
    except CarNotFound:
        raise ReservationConflict(f"Car with plate number {reservation['car_plate_number']} does not exist")
    try:
        find_customer_by_idnp(reservation['customer_idnp'])
    except CarNotFound:
        raise ReservationConflict(f"Customer with plate number {reservation['customer_idnp']} does not exist")
    for reserv in get_reservations_for_car(reservation['car_plate_number']):
        if tuple(reserv['date']) == reservation['date']:
            raise ReservationConflict('Cannot do that')


def add_reservation(reservation: dict):
    """
    {
        'car_plate_number': str,
        'customer_idnp': str,
        'date': tuple(day, month, year)
    }

    Args:
        reservation (dict): _description_
    """
    validate_reservation_confilct(reservation)
    reservations = get_all_reservations()
    reservations.append(reservation)
    save_reservations_to_storage(reservations)
