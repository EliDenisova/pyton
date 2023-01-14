A = int(input("Enter the number A "))
B = int(input("Enter the number B "))


def exponentiation(A, B):
    if B == 1:
        return A
    else:
        return exponentiation(A, B - 1) * A


print(exponentiation(A, B))
