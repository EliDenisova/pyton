n = int(input("введите число "))

def fibonache(n):
    if n == 0:
        return 1
    if n == 1:
        return 2
    num0 = 0
    num = 1
    count = 2
    while n >= num:
        if n == num:
            return count
        temp = num
        num += num0
        num0 = temp
        count += 1
    return -1


print(fibonache(n))