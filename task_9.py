n = int(input("введите число "))
res = 1
while n > 1:
    res *= n

    n = int(input('Введите число: '))

    factorial = 1

    while n > 1:
        factorial *= n
        n -= 1
    print(factorial)
