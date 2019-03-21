# Write your values_that_are_keys function here:
def values_that_are_keys(my_dictionary):
    lst = []
    for k in my_dictionary:
        for v in my_dictionary.values():
            if v == k:
                lst.append(k)
    return lst


# Uncomment these function calls to test your  function:
print(values_that_are_keys({1: 100, 2: 1, 3: 4, 4: 10}))
# should print [1, 4]
print(values_that_are_keys({"a": "apple", "b": "a", "c": 100}))
# should print ["a"]