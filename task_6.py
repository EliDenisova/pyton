
while True:
    ticket_number = input("Введите номер билет - 6 цифр: ")
    first_half = int(ticket_number[0]) + int(ticket_number[1]) + int(ticket_number[2])
    second_half = int(ticket_number[3]) + int(ticket_number[4]) + int(ticket_number[5])
    if len(ticket_number) == 6:
        if first_half == second_half:
            print("Ого, Вы счастливчик! Это счастливый билет!")
        else:
            print("Повезет в другой раз.")
            break
    else:
        print("Введите номер билет - 6 цифр: ")
