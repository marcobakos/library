# CODE - Caesar Cipher
letters = "zyxwvutsrqponmlkjihgfedcbazyxwvutsrqponmlkjihgfedcba"


def code(word, offset):
    word_code = ''
    for letter in word:
        if letter in letters:
            word_code += letters[(letters.find(letter) + offset):(letters.find(letter) + (offset + 1))]
        else:
            word_code += letter
    return word_code


#
# print(decode("hey",10))
#
message = "hey there! this is an example of a caesar cipher. were you able to decode it? i hope so! send me a message back with the same offset!"
message_decode = ''
#
#
#
message_split = message.split()
# print(message_split)
#
for word_code in message_split:
    #    print(word_code)
    #    print(decode(word_code))
    message_decode += code(word_code, 10) + ' '
#
print(message_decode)
