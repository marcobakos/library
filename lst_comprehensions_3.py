single_digits = range(10)
squares = []

for item in single_digits:
    print(item)
    squares.append(item ** 2)

cubes = [item ** 3 for item in single_digits]
print(cubes)