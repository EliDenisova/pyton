# Дана последовательность из N целых чисел и число K.
# Необходимо сдвинуть всю последовательность (сдвиг -
# циклический) на K элементов вправо,  K – положительное число.
# Input:   [1, 2, 3, 4, 5] k = 2
#
# Output:  [4, 5, 1, 2, 3]

K = 2
m = [1, 2, 3, 4, 5]

for i in range(0, K):
    m.insert(0, m[-1])
    print(m)
    m.pop(-1)
print(m)

import random

n = int(input('Введите длину списка >>> '))
l = []
for num in range(0, n):
    random_number = round(random.randint(-10, 10))
    l.append(random_number)
print(l)

k = int(input('Введите на сколько индексов сдвигать >>> '))
for i in range(k):
    p = l.pop(-1)
    l.insert(0, p)

print(l)
