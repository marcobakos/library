# You most likely have already seen pop(), which allows us to "pop" off the last element of a list.
# However, by passing an index position you can remove and return a specific element.

list1 = [1, 2, 3, 4, 5]

ele = list1.pop(1)  # pop the second element

print(ele)

print(list1)


ele1 = list1.pop()  # pop the last element

print(ele1)

print(list1)

