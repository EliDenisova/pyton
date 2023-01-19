fileName = 'tel.txt'


def writeFile(file_name):
    with open(file_name, 'a') as data:
        data.writelines("Hello world111" + '\n')


def readFile(file_name):
    result = []
    with open(file_name, 'r+') as data:
        for line in data:
            result.append(line.split())
    return result
def findUsers(userList):
 name = 'Ivan'

 for user in userList:
    if user[0] == name:
        print(user[3])



# writeFile(fileName)
print(type(readFile(fileName)))
print(readFile(fileName))

import os
from datetime import time


def clear_screen():
    os.system('cls')


def search_data():
    clear_screen()
    while (True):
        answer = input('Строка поиска(\'\'-выход) :>')
        if answer == "": return
        result = []
        with open('phonebook.txt', 'r', encoding='utf8') as datafile:
            for line in datafile:
                result.append(line.strip('\n'))
            result = list(filter(lambda line: answer in line, result))
        for printdata in result:
            output_data_string(printdata)


def output_data_string(printdata):
    parse_data = printdata.split(',')
    template = 'Фамилия: {0}\nИмя: {1}\nОтчество: {2}\nТелефон: {3}\n'
    print(template.format(parse_data[0], parse_data[1], parse_data[2], parse_data[3]))


def save_data_to_file(data_to_save):
    data_to_save = ",".join(data_to_save) + "\n"
    print(data_to_save)
    with open('phonebook.txt', 'a', encoding='utf8') as datafile:
        datafile.write(data_to_save)


def print_data(enum=False):
    count = 0
    with open('phonebook.txt', 'r', encoding='utf8') as datafile:
        for line in datafile:
            if enum: print(count + 1)
            output_data_string(line)
            count += 1
    return count


def print_all_data():
    count = print_data()
    input('Всего {} Записей.  Enter для выхода'.format(count))


def add_data():
    while (True):
        print('Добавление записи(""-выход)')
        last_name = input("Фамилия: ")
        first_name = input("Имя: ")
        patronymic = input("Отчество: ")
        phone_number = input("Номер Телефона: ")
        data_to_save = [last_name, first_name, patronymic, phone_number]
        if "" in data_to_save: return
        save_data_to_file(data_to_save)

    # def del_data():

    # if __name__ == '__main__':
    # основной длок
menu = '''1 - Вывод данных\n2 - Добавление записи\n3 - Поиск\n4 - Выход'''
while (True):
    clear_screen()
    print(menu)
    answer = input('>:')
    match answer:
        case "1":
            # вывод данных
            print_all_data()

        case "2":
            # добавление данных
            add_data()

        case "3":
            # поиск
            search_data()

        case "4":
            # удаление данных
            pass

        case "5":
            # выход
            exit(0)

        case _:
            print("неверный ввод")
            time.sleep(3)
