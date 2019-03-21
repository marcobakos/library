# Write your make_spoonerism function here:
def make_spoonerism(word1, word2):
    first_word1 = word1[0]
    first_word2 = word2[0]
    word1 = word1.replace(word1[0], first_word2)
    word2 = word2.replace(word2[0], first_word1)
    return (' '.join([word1, word2]))


# Uncomment these function calls to test your function:
print(make_spoonerism("Codecademy", "Learn"))
# should print Lodecademy Cearn
print(make_spoonerism("Hello", "world!"))
# should print wello Horld!
print(make_spoonerism("a", "b"))
# should print b a