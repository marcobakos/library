def username_generator(first_name,last_name):
  return(first_name[:3] + last_name[:4])

#
username=username_generator("Abe","Simpson")
print(username)
#
def password_generator(username):
  return(username[-1] + username[:len(username)-1])

#
print(password_generator(username))
