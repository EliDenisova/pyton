
while True:
    n = int(input("Введите трехзначное число "))
    if 99 < n < 1000:
        sum = n // 100 + n // 10 % 10 + n % 10
        print(f"Сумма цифр числа {n}: {sum}")
        break
    else:
        print("это не трехзначное число")