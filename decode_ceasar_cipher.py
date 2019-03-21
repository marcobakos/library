# DECODE - Caesar Cipher
letters = "abcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyz"


def decode(word, offset):
    word_decode = ''
    for letter in word:
        if letter in letters:
            word_decode += letters[(letters.find(letter) + offset):(letters.find(letter) + (offset + 1))]
        else:
            word_decode += letter
    return word_decode


#
# print(decode("xuo",10))
#
message = "xuo jxuhu! jxyi yi qd unqcfbu ev q squiqh syfxuh. muhu oek qrbu je tusetu yj? y xefu ie! iudt cu q cuiiqwu rqsa myjx jxu iqcu evviuj!"
message_decode = ''
#
message_split = []
#
message_split = message.split()
# print(message_split)
#
for word_code in message_split:
    #    print(word_code)
    #    print(decode(word_code))
    message_decode += decode(word_code, 10) + ' '
#
print(message_decode)
