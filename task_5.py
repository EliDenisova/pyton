i = int(input('порядковый номер вагоня '))
j = int(input('номер вагона '))

if i - j == 0:
    c = 0
else:
    c = i + j - 1
print(c)
