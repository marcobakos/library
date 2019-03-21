# Write your every_other_letter function here:
def every_other_letter(word):
  every_word=''
  i=1
  for i in range(len(word)):
    if i % 2 == 0:
      continue
    else:
      every_word+=word[i-1]
  return every_word
#
# Uncomment these function calls to test your function:
print(every_other_letter("Codecademy"))
# should print Cdcdm
print(every_other_letter("Hello world!"))
# should print Hlowrd
print(every_other_letter(""))
# should print