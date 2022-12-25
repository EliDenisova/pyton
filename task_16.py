import random

N = int(input('Введите длину массива: '))
x = int(input('Введите число: '))

numbers = [N]

for i in range(N):
    numbers.append(random.randint(0, int(N / 2)))
print(numbers)

print(numbers.count(x))
