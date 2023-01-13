from view.car_views import get_car_menu
from view.customer_view import get_customer_menu
from view.reservations_view import get_reserv_menu
from view.utils import menu_tool

options_dict = {
    1: get_car_menu,
    2: get_customer_menu,
    3: get_reserv_menu,
}


def get_menu_text():
    return """
For car options, press 1
For customer options, press 2
For reservations options, press 3
"""


menu_tool(menu_text=get_menu_text(), options_dict=options_dict, stop_word='stop')
