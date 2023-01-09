from data.data_storage.cars_fs import get_all_cars_from_storage, save_cars_to_storage

class CarNotFound(Exception):
    pass

class CarExistsException(Exception):
    pass

def get_all_cars():
    return get_all_cars_from_storage()


def find_car_by_vin(vin:str):
    all_cars = get_all_cars()
    for car in all_cars:
        if car['VIN'] == vin:
            return car
    raise CarNotFound('Car with vin ', vin, 'does not exist')


def find_car_by_plate_nr(plate_nr: str):
    all_cars = get_all_cars()
    for car in all_cars:
        if car['plate_number'] == plate_nr:
            return car
    raise CarNotFound('Car with plate number ', plate_nr, 'does not exist')


def add_car(car:dict):
    car_exists = True
    try:
        find_car_by_vin(car['VIN'])
        find_car_by_plate_nr(car['plate_number'])
    except CarNotFound:
        car_exists = False
    if car_exists:
        raise CarExistsException('Cannot add car')
    all_cars = get_all_cars()
    all_cars.append(car)
    save_cars_to_storage(all_cars)

def edit_car_data(plate_nr: str, new_data: dict):
    all_cars = get_all_cars()
    for a in range(len(all_cars)):
        if all_cars[a]['plate_number'] == plate_nr:
            all_cars[a] = new_data
            break
    else:
        raise CarNotFound()

def remove_car_by_plate_number(plate_nr: str):
    all_cars = get_all_cars()
    for idx, car in enumerate(all_cars):
        if car['plate_number'] == plate_nr:
            all_cars.pop(idx)
            break
    else:
        raise CarNotFound()