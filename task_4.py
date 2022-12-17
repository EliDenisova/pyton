number = int(input("сколько журавликов сделали дети? "))

if number % 6 == 0:
    cranes = number // 6
    Kate = cranes * 4
    print(f"Мальчики сделали по {cranes}, Катя сделала по {Kate} журавликов")
else:
    print("число корабликов не соответствует условию задачи")