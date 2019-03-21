# Write your sum_values function here:
def sum_values(my_dictionary):
  sum_values=0
  for value in my_dictionary.values():
    sum_values+=value
  return sum_values
#
# Uncomment these function calls to test your sum_values function:
print(sum_values({"milk":5, "eggs":2, "flour": 3}))
# should print 10
print(sum_values({10:1, 100:2, 1000:3}))
# should print 6