# В некоторой школе решили набрать три новых
# математических класса и оборудовать кабинеты для
# них новыми партами. За каждой партой может сидеть два
# учащихся. Известно количество учащихся в каждом из трех
# классов. Выведите наименьшее число парт, которое нужно
# приобрести для них.
# Input: 20 21 22(ввод чисел НЕ в одну строку)
# Output: 32

first = int(input('Первый класс '))
second = int(input('Второй класс '))
three = int(input('Третий класс '))
sum = (first+1)//2
sum2 = (second+1)//2
sum3 = (three+1)//2
print(sum, sum2, sum3)

