def read_data_from_file(name):
    result = []
    with open(name, 'r', encoding='utf8') as datafile:
        for line in datafile:
            result.append(line.strip('\n').split(','))
        return result

def save_data_to_file(name, data_list):
    with open(name, 'w', encoding='utf8') as datafile:
        for rawdata in data_list:
            datafile.write(','.join(rawdata) + '\n')


def add_item_to_file(name, rawdata):
    with open(name, 'a', encoding='utf8') as datafile:
        datafile.write('\n' + ','.join(rawdata))

def print_bus():
    return read_data_from_file('bus.txt')

def add_bus():
    print('Добавим автобус')
    name, number = input('автобус '), input('гос. номер ')
    add_item_to_file('bus.txt', [name, number])

def print_driver():
    return read_data_from_file('driver.txt')

def add_driver():
    print('Добавим водителя')
    surname, name, patronymic = input('фамилия '), input('имя '), input('отчество ')
    add_item_to_file('driver.txt', [surname, name, patronymic])

def print_rout():
    return read_data_from_file('rout.txt')

def add_rout():
    print('Добавим маршрут')
    rout_number, namedriver, brand_bus = input('номер маршрута '), input('водитель - ФИО '), input('марка автобуса ')
    add_item_to_file('rout.txt', [rout_number, namedriver, brand_bus])
