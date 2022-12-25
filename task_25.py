string = 'a a a b c a a d c d d'
res = ''
data = {}
array = string.split()
print(array)
for item in array:
    if item in data:
        data[item] += 1
        res += item + '_' + str(data[item]) + ' '
    else:
        data[item] = 0
        res += item + ' '
print(res)

