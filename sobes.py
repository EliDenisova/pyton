
# Улитка ползет по столбу высотой 12 м,
# днем на 2м вверх и ночью на 1м вниз.
# На какой день она окажется на вершине"

# postLength = 12
# crawled = 0
# daySpeed = 2
# nightSpeed = 1
# dayNum = 0
#
# while crawled < postLength:
#     crawled = crawled + daySpeed
#     dayNum += 1
#     if crawled >= postLength:
#         break
#     crawled = crawled - nightSpeed
#
# print(dayNum)
#
#
#
# Составить график ДР И выводить количество лет
# 01.12.1980 Маша
# 01.04.1992 Петя
# 05.04.1992 Сергей
# 08.07.1998 Виктор


from datetime import datetime

birthdays = []

todays = datetime.now()
year = todays.year
with open("date.txt", "r", encoding="utf8") as file:
    for line in file:
        days = line.strip("\n").split(" ")
        dd, mm, _ = days[0].split(".")
        birthdays_str = "{}.{}.{}".format(dd, mm, year)
        birthdays_data = datetime.strptime(birthdays_str, "%d.%m.%Y")
        # print(birthdays)
        name = days[1]
        birthdays_real = datetime.strptime(days[0], "%d.%m.%Y")
        # print(birthdays_real)
        age = int((birthdays_data - birthdays_real).days / 365.25)
        birthdays.append((birthdays_real, name, (birthdays_data - todays).days, age))

birthdays_sort = sorted(birthdays, key=lambda x: x[2])
print(todays)
print(birthdays_sort)
for item in birthdays_sort:
    if item[2] > 0:
        print('{} исполняется {} годик, через {} день'.format(item[1], item[3], item[2]))
    elif item[2] == 0:
        print('{} исполняется {} годик, СЕГОДНЯ!!!'.format(item[1], item[3], item[2]))