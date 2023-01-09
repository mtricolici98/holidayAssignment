

def menu_tool(options_dict, stop_word, menu_text):
    while True:
        print(menu_text)
        option = input(f'Select option or type {stop_word}:')
        option = option.lower().strip()
        if option == stop_word:
            break
        if not option.isnumeric():
            print('Invalid option')
            continue
        option = int(option)
        try:
            options_dict[option]() # Calling the function
        except KeyError as ex:
            print('Invalid option', str(ex))
            
def get_date():
    date = input('Day')
    month = input('Month')
    year = input('Year')
    return (date, month, year)