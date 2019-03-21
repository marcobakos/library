#extend

#Many times people find the difference between extend and append to be unclear. So note:

# append: appends whole object at end:

x = [1, 2, 3]
x.append([4, 5])
print(x)


# extend: extends list by appending elements from the iterable:
x = [1, 2, 3]

x.extend([4, 5])

print(x)
