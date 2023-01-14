values = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29]
transformation = lambda x: x**2
transformed_values = list(map(transformation, values))

print(values)
print(transformed_values)
