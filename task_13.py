import random

from random import randint
n = int(input())
l = [randint(-50, 50) for i in range(1, n)]
count = 0
maxcount = 0
m = []
for el in l:
    if el >= 0:
        count += 1
        m.append(count)
    else:
        if count > maxcount:
            maxcount = count


print(l)
print(maxcount)
