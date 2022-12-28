import random

n = int(input("Введите длину первого массива : "))
m = int(input("Введите длину второго массива : "))

arr_1 = [n]
arr_2 = [m]

for i in range(1, n + 1):
    arr_1.append(random.randint(0, 20))

for i in range(1, m + 1):
    arr_2.append(random.randint(0, 20))

print(arr_1)
print(arr_2)

length = 0

if len(arr_1) > len(arr_2):
    length = arr_1
else:
    length = arr_2

arr_set = set()


for i in length:
    if (i in arr_1) & (i in arr_2):
        arr_set.add(i)

res = []
for i in arr_set:
    res.append(i)

res.sort()
print(res)



