values = [0, 2, 10, 6]


def same_by(characteristic, objects):
    return len(set(list(map(characteristic, objects)))) == 1


if same_by(lambda x: x % 2, values):
    print('same')
else:
    print('different')
