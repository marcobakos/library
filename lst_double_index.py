#Write your function here
def double_index(lst, index):
  if index < len(lst):
  	lst[index] = lst[index] * 2
  return lst

#Uncomment the line below when your function is done
print(double_index([3, 8, -10, 12], 2))