a = [0, -1, 5, 2, 3]

count = 0
for i in range(0, len(a) - 1):
    if a[i - 1] < a[i]:
        count += 1
print(a)
print(count)
