

from data.data_storage.cars_fs import get_all_cars_from_storage, save_cars_to_storage
from data.data_storage.customers_fs import get_all_customers_from_storage, save_customers_to_storage
from data.data_storage.reservations_fs import get_all_reservations_from_storage, save_reservations_to_storage


def test_cars_fs():
    data = [dict(make=1, model=2)]
    save_cars_to_storage(data)
    new_data = get_all_cars_from_storage()
    assert len(new_data) == 1
    for index, el in enumerate(new_data):
        for key, val in el.items():
            assert data[index][key] == val 
            

def test_cust_fs():
    data = [dict(fisrt_name=1, last_name=2)]
    save_customers_to_storage(data)
    new_data = get_all_customers_from_storage()
    assert len(new_data) == 1
    for index, el in enumerate(new_data):
        for key, val in el.items():
            assert data[index][key] == val 
        

def test_res_fs():
    data = [dict(car_vin=1, cust_idnp=2)]
    save_reservations_to_storage(data)
    new_data = get_all_reservations_from_storage()
    assert len(new_data) == 1
    for index, el in enumerate(new_data):
        for key, val in el.items():
            assert data[index][key] == val 
            
if __name__ == '__main__':
    test_cars_fs()
    test_cust_fs()
    test_res_fs()