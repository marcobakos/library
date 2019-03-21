def check_for_name(sentence, name):

    sent_temp = sentence.lower()
    name_temp = name.lower()
    if name_temp in sent_temp:
        return True
    else:
        return False


#
# Uncomment these function calls to test your  function:
print(check_for_name("My name is Jamie", "Jamie"))
# should print True
print(check_for_name("My name is jamie", "Jamie"))
# should print True
print(check_for_name("My name is Samantha", "Jamie"))
# should print False
print(check_for_name("My name is JAMIE", "Jamie"))
# should print true
