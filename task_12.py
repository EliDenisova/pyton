s = int(input('Введите сумму чисел: '))
p = int(input('Введите произведение чисел: '))

solution_exists = 0
for i in range(s):
    if i * (s - i) == p:
        print(f'Петя загадал числа {i} и {s-i}')
        solution_exists = 1
        break
    if solution_exists == 0:
        print('Таких натуральных чисел нет!')
        break