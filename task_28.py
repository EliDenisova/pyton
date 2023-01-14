a = int(input("Enter the number A "))
b = int(input("Enter the number B "))


def sum(a, b):
        if b == 0:
            return a
        else:
            return sum(a, b - a) + a


print(sum(a, b))
