from data.data_storage.reservations_fs import get_all_reservations_from_storage


def get_all_reservations():
    return get_all_reservations_from_storage()

def get_reservations_for_car(plate_number):
    # Retunr all reservations for car
    pass

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
    for reserv in get_reservations_for_car(reservation['car_plate_number']):
        if reserv['date'] == reservation['date']:
            raise Exception('Cannot do that')

# TODO: Implement other methods (Remove/Find/Edit)