import random

print("Сколько монеток бросим?")
number = int(input())
coins = []
# heads = 0
for i in range(number):
    coins.append(random.randint(0, 1))
print(f"Монетки на столе - {coins}")
heads = sum(coins)
print(heads)
tails = number - heads
if heads == 0 or heads == number:
    print("Все монетки лежат одинаковой стороной вверх или монеток нет! Переворачивать ничего не требуется!")
elif heads == tails:
    print(f"Можно перевернуть любые монетки! Их выпало равное количество! Превернуть придется {heads}")
elif heads < tails:
    print(f"Необходимо перевернуть монетки, которые лежат решкой вверх - {heads}")
else:
    print(f"Необходимо перевернуть монетки, которые лежат орлом вверх - {tails}")