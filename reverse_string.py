# Write your reverse_string function here:
def reverse_string(word):
    word_inv = ''
    for i in range(len(word)):
        if i == 0:
            index = -1
        else:
            index = (i + 1) * (-1)
        word_inv += word[index]
    return word_inv


# Uncomment these function calls to test your  function:
print(reverse_string("Codecademy"))
# should print ymedacedoC
print(reverse_string("Hello world!"))
# should print !dlrow olleH
print(reverse_string("bakos"))
# should print
