from data.data_access.cars_access import CarNotFound, add_car, CarExistsException, find_car_by_plate_nr, get_all_cars
from view.utils import menu_tool


def print_car(car: dict):
    print('Selected car: \n')
    print('Make:', car['make'])
    print('Model:', car['model'])
    print('Plate NR:', car['plate_number'])
    print('VIN:', car['VIN'])
    print('Color:', car['color'])
    print('Produced in:', car['yop'])


def print_car_small(car):
    print(
        f"Car [{car['VIN']}]: PlateNR: {car['plate_number']} , {car['make']} {car['model']}, {car['color']} from {car['yop']}")


def add_car_view():
    print('Adding car, please provide info:')
    car = dict()
    car['make'] = input('Make:')
    car['model'] = input('Model:')
    car['plate_number'] = input('Plate NR:')
    car['VIN'] = input('VIN:')
    car['color'] = input('Color:')
    car['yop'] = input('Produced in:')
    try:
        add_car(car)
    except CarExistsException:
        print('Car already exists, Try Again.')
    print('Succesfully created')
    print_car_small(car)


def list_cars():
    print('Here\'s the list:\n')
    for car in get_all_cars():
        print_car_small(car)


def info_by_plate_number():
    p_nr = input('Plate number:')
    try:
        car = find_car_by_plate_nr(p_nr)
        print_car(car)
    except CarNotFound as ex:
        print(str(ex))


def get_menu_text():
    return """
    1: Add car
    2: List cars
    3: Get car info by plate number
    """


def get_car_menu():
    opt_dict = {
        1: add_car_view,
        2: list_cars,
        3: info_by_plate_number
    }
    menu_tool(menu_text=get_menu_text(), options_dict=opt_dict, stop_word='back')
