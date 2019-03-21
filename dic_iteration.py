# Iteration over keys, values, and items

# Key
d = {'k1': 1, 'k2': 2}

for k in d.keys():
    print(k)

# Value
for v in d.values():
    print(v)

# Items
for item in d.items():
    print(item)


# add items in the dic
key_view = d.keys()

print(key_view)

d['k3'] = 3

print(d)

