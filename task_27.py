n = int(input())

max_number = n
while n != 0:
    n = int(input())
    if max_number < n:
        max_number = n
print(max_number)
