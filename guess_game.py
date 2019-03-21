# this is a comment
# this is another comment


##########################
# Data types
##########################

# creating an integer data type
# integer are whole numbers
#print(5)


# creating a float data type
# float are any decimal point number

#print(3.2)
#print(458.79)
#print(1.0)

# creating a string
# a string is defined between single or double quotes
#print('Hey there you')
#print('They\'re you are')
#print("they're you are")


# creating a boolean
# boolen are True or False, like switches

#print(True)
#print(False)


# creating a list
# a list is a collection of data types

#print([5, 3.4, 'program', True])

########################
# string manipulation
########################

# replace a exclamation point with a period
#print('Hi there!'.replace('!', '.'))

# using strip to get rid of white space
#print('       John Smith       . '.strip())


# create a list of words from a string using split
#print('This has words in it.'.split(' '))

# find the location of a specific letter

#print('Hi there.'.find('there'))

####################
#  variables
#  variable are used to save data to be used later
#  a value is assigned to a variable name as reference
####################

# storing an integer into a variable

num = 5

#print(num)

# storing a float into a variable

num = 3.2
#print(num)

# storing a boolena into a variable

#flag = True
#print(flag)


# storing a string into a variable

#name = 'Bakos'
#print(name)


# storing a list into a variable

sports = ['Baseball', 'Football', 'Hockey', 'Basketball']

#print(sports)


#####################
# Indexing
#####################

#print(sports[0])
#print(sports[3])

# use indexing to access multiple elements
# otherwise known as slicing

#print(sports[1:3])


# printing out all indexes

#print(sports[0:])
#print(sports[::2])

# using an index on strings
greeting = 'Hello There!'

#print(greeting[0:5])


word = greeting[0:5]
#print(word)


###################################
# string formatting / concatenation
###################################

# attacch two separate strings
first_name = "John"
last_name = "Smith"

#print(first_name + " " + last_name)

sport = sports[0]

#print('I cannot wait for ' + sport)

# a way to inject variables directly into a string
# using the .format() method

#print('Hi {}, do you like {}?'.format("David", sport))


# f string only in Python 3.6+

#print(f'Hi {first_name}, do you like {sport}')



##########################
#   branching statements
#########################

# how to accept user input

#ans = input("Do you like pizza ? ")

#print(ans)

#if ans == 'yes' :
#    print('Take the pizza home then!')
#elif ans == 'no':
#    print('Do not take pizza home then.')
#else:
#    print('Bummer .....')


# assign two variables print lower one

x = 10
y = 10
a = 11

"""
if x < y:
    print('x is less than y')
elif x == y or x > a:
    print('equal')
else:
    print('x is more than y')

"""

######################
# Loops
######################


# create a for loop
"""
for num in range(10):
    print(num)

# using a for loop with a list

for sport in sports:
    print("I like to watch " + sport)

"""

# while loop
"""
x = 0

while x < 5:
    print(x)
    x += 1

"""


# loop until they answer yes
"""
while True:
    ans = input('Would you like to stop ?')
    if ans == 'yes':
        break
"""

###############################
# Guess the computer's number
###############################


import random

# declare game variables

num = random.randint(1, 100)
game_over = False
counter = 0


#print(num)

while not game_over:
    ans = input('What number are you guess ? ')

    counter += 1

    # base case
    if int(ans) == num:
        print("You guessed correctly.")
        print("it took {} tries ".format(counter))
        break
    elif int(ans) < num:
        print("the number is higher")
    elif int(ans) > num:
        print('The number is lower')

