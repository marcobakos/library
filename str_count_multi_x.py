# Write your count_multi_char_x function here:
def count_multi_char_x(word, x):
  splits = word.split(x)
  return(len(splits)-1)

# Uncomment these function calls to test your  function:
print(count_multi_char_x("mississippiss", "iss"))
# should print 2
print(count_multi_char_x("applepppppp", "pp"))
# should print 1