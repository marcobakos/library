drinks = ["espresso", "chai", "decaf", "drip"]
caffeine = [64, 40, 0, 120]
#
zipped_drinks=zip(drinks,caffeine)
#
print(list(zipped_drinks))
#
drinks_to_caffeine={k:v for k,v in zip(drinks,caffeine)}
#
print(drinks_to_caffeine)
#