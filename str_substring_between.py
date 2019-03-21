# Write your substring_between_letters function here:
def substring_between_letters(word,start,end):
  index_start=0
  index_end=0
  if start in word and index_start==0:
    index_start=word.find(start)
  if end in word:
    index_end=word.find(end)
  if index_end != 0:
    return word[index_start+1:index_end]
  else:
    return word
#
# Uncomment these function calls to test your function:
print(substring_between_letters("apple", "p", "e"))
# should print "pl"
print(substring_between_letters("apple", "p", "c"))
# should print "apple"
