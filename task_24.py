import random

n = int(input("Сколько кустов на грядке? "))

garden = []
for i in range(n):
    garden.append(random.randint(0, 10))
max_sum = 0

for i in range(n):
    cur_sum = sum(garden[i:i + 3])
    if cur_sum > max_sum:
        max_sum = cur_sum
if garden[0] + garden[-1] + garden[-2] > max_sum:
    max_sum = garden[0] + garden[-1] + garden[-2]
if garden[0] + garden[1] + garden[-1] > max_sum:
    max_sum = garden[0] + garden[1] + garden[-1]
print(garden)
print(max_sum)
