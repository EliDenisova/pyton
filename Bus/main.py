from datetime import time

from menu import Menu
import function as fn

if __name__ == "__main__":
    # основной блок
    menuitems = [
        ("1", "Вывод автобусов"),
        ("2", "Добавление автобусов"),
        ("3", "вывод водителей"),
        ("4", "добавление водителя"),
        ("5", "вывод маршрута"),
        ("6", "добавление маршрута"),
        ("7", "Выход", lambda: exit())]

    menu = Menu(menuitems)

    for i in menuitems:
        print(i[0], i[1])

    # print(menuitems)
    #
    # text = input("Введите запрос")
    #
    # if text == '1':
    #     print(fn.print_bus())
    # elif text == '3':
    #     print(fn.print_driver())
    # elif text == '5':
    #     print(fn.print_rout())
    while True:
        print(menu)
        answer = input(">:").upper()
        match answer:
            case "1":
                print(fn.print_bus())
            case "2":
                fn.add_bus()
            case "3":
                print(fn.print_driver())
            case "4":
                fn.add_driver()
            case "5":
                print(fn.print_rout())
            case "6":
                fn.add_rout()
            case "7":
                exit()
            case _:
                print("неверный ввод")
                time.sleep(1)
