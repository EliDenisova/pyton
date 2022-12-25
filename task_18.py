import random

N = int(input('Введите длину массива: '))
x = int(input('Введите число: '))

numbers = [N]

for i in range(N):
    if 0 < N < 10:
        numbers.append(random.randint(0, N))
print(numbers)

res = numbers[0]
for i in numbers:
    if abs(i - x) < abs(res - x):
        res = i

print(res)
