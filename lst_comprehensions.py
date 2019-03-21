heights = [161, 164, 156, 144, 158, 170, 163, 163, 157]

can_ride_coaster = [height for height in heights if height > 161]

print(can_ride_coaster)

#
lst = [x for x in 'word']

print(lst)

#
lst = [ x**2 for x in [x**2 for x in range(11)]]
print(lst)


