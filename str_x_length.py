# Write your x_length_words function here:
def x_length_words(sentence,x):
  list_split=[]
  result=0
  list_split=sentence.split()
  for word in list_split:
    if len(word) >= x:
      result+=1
  if len(list_split) == result:
    return True
  else:
    return False
#
# Uncomment these function calls to test your tip function:
print(x_length_words("i like apples", 2))
# should print False
print(x_length_words("he likes apples", 2))
# should print True