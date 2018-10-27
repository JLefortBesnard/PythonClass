###########################################
### SUM OF THE SECOND PYTHON CLASS 23.10 ##
###########################################

# to clear the screen, write "clear" with a MAC, "cls" with Anaconda prompt


############ BREAK EXERCICES #########
# For the next session, create a list named "my_status". This list includes your age, your name, your job status.
# Your age should be written as an integer, the 2 other elements should be strings.
# print your list

my_status = [30, "Jeremy", "Python fan"]
print(my_status) # this print the raw elements

# print it with sentences but it looks uggly
print("Hi, I am ", my_status[1],", I am ", my_status[0], " years old, and I am a ", my_status[2], "in Aachen")

# Beautiful way to print the sentence
print("Hi, I am %s, I am %s years old, and I am a %s in Aachen") %(my_status[1], my_status[0], my_status[2])

# Best programming way to print something:
print("Hi, I am {}, I am {} years old, and I am a {} in Aachen").format(my_status[1], my_status[0], my_status[2])

# The raw_input function ask for input to the user
my_age = input("Age= ?")
my_name = input("Name= ?")
my_status = input("Status= ?")
print("Hi, I am %s, I am %s years old, and I am a %s in Aachen") %(my_name, my_age, my_status)


"""
### Three ways to run a script ###
1 copy paste the script in the terminal with ipython activated
2 if ipython is activated, write:  run program_name.py (make sure your locaton -pwd- is the same as the python script)
3 if ipython is not activated, write: python program_name.py 

Everything in between 3 inverted commas (3 * ") is considered as commentary in python
like if it was starting with a hashtag (#)
"""

# The len() function
my_list = [0, 2, 4]
len(my_list) # return the number of elements, here 3
my_list = ["a", "b", "c"]
len(my_list) # 3 elements as well
my_string = "hello world"
len(my_string) # return the number of characters


######  OPERATIONS ####
my_list = [3, 2, 1, 4]
my_list.append(8) # add the number 8 to the list
sum(my_list) # return the sum of each element of the list
my_number = 54
print(my_number*3)  #multiplication, return 54*3
print(my_number/3) #division
print(my_number**2) #exponent, here return 54 squared

#Booleans:
my_number = 54
print(my_number == 54) # if my variable is equal to 54, return True
print(my_number != 54)  # if my variable is different from 54, return True 
print(my_number < 100)  # if my variable is inferior to 100, return True
print(my_number**2 > 3000) # if my variable squared is superior 3000, return True

############ BREAK EXERCICES #########
# create a new list called "my_list" with the numbers 34, 23 and 12
# add 7 and 1 to my_list using the append function
# create a variable named "user_choice"that ask the user to type a number
# make sure the entered value is an integer
# hint: int() would do it for you
# print a sentence that tells if it's true or not that the selected number is higher from the square
# of the sum of your list

# Exemple of a solution
my_list = [34, 23, 12]
my_list.append(7)
my_list.append(1)
user_choice = raw_input("enter a number: ")
answer = int(user_choice) > sum(my_list)
print ("Number higher than the sum of the list: %s") %(answer)


########### IF ELIF and ELSE ############
my_list = [1, 2, 3]
if 3 in my_list: # if 3 is in my_list, then return "included", in other words, if the "if" statement is true, then it returns "included"
    print("included")
else: # if the "if" statement is false, then it returns "not included"
    print("not included")

if 1==2:  # this is False so this would return "non ok"
    print("ok")
else:
    print("non ok")


my_number = 54
if my_number == 52:
    print("yes")
elif my_number == 54: # "elif" is a continuity of "if", again it returns the following only if it's true, otherwise, it goes to the next "elif" or the "else"
    print("Congrats!")
elif my_number != 54:
    print("hello")
else:
    print("I don't understand what you mean!")

if my_number > 50 and my_number < 60: # The "if" statement works without the "elif", nor the "else". If it's not true, the computer will just continue to read the rest without printing "It's a good one"
    print("It's a good one")


############ BREAK EXERCICES #########    
# create a variable named "user_age" that asks the user to enter his age
# make sure the entered value is an integer
# hint: int() would do it for you
# create an if operation that prints "You're so young!" if his age is between 25 and 30,
# "You're a baby" if it's under 25, otherwise, print "You're so old"

user_age = int(raw_input("What s your age dude? "))
if 24 < user_age < 31:
    print("You're so young!")
elif user_age < 25:
    print("You're a baby")
else:
    print("You're so old")

 

 ### Information: show on white board what an if, or, and, nor functions are on a computer (electricity=> 0/1 switch)
 
 
 ###########################################
 ### SUM OF THE THIRD PYTHON CLASS 23.10 ##
 ###########################################
 
 
 ########### FOR LOOP ############
 
My_string = "Python is awesome"
 # for loop
for letter in My_string:
    print(letter) # Python iterates through each element (here named letter) of the variable My_string
     
 # The name used for the element doesn't matter, the three following for loops will print the same thing
 # for loop 1
for vegetable in My_string:
    print(vegetable) # but don't forget to name it the same way afterwards
 
 # for loop 2    
for tomatoe in My_string:
    print(tomatoe)
 
 # for loop 3
for i in My_string: # it can also be just a letter (this is usually the case)
    print(i)
 
 
 # for loop with fancy printing
for letter in My_string:
    print("letter: %s") %(letter) # print it at each iteration
    print("-" * 20) # print 20 times the "-" at each iteration
 
 # increment
i = 0
for letter in My_string:
    print("letter #%s => %s") %(i, letter)
    i += 1 # += increase at each iteration => basically means: i = i + 1 => read: the new value of i is equal to the old value of i + 1
 
a = 0
for letter in My_string: # we can use a if/else statement in a for loop
    if letter == " ": # at each iteration, the if/else statement will be checked by Python
        print("letter #%s => space") %(a) # if the statement is true then this will be printed
    else:
        print("letter #%s => %s") %(a, letter) # if the statement is wrong then this will be printed
    a += 1
 
 # for loop works with any kind of iterable element
My_list = [2, 3, 4, 5]
My_list_squared = [] # create an empty list to store the new squared numbers in
for number in My_list:
    new_number = number ** 2 # create a variable that square the element in My_list
    My_list_squared.append(new_number) # add the new squared number to the new list
print(My_list_squared)
 
 
 ############ BREAK EXERCICES #########
 # Create a list including:
 #  "I", "got", 99, 88, 77, "ninety-nine", "Problems"
 # Using a for and a if loop to create a new list that include only the words (strings).
 # i.e., ["I" "got" "ninety-nine" "problems"]
 # print it as a fancy sentence
 # Hints:
 # type(element_from_My_list) == str     will return if the element of the list is true or not
 
 # Example of a solution
My_list = ["I", "got", 99, 88, 77, "ninety-nine", "Problems", "the"]
My_new_list = []
for i in My_list:
    if type(i) == str:
        My_new_list.append(i)
 
print("%s %s %s %s") %(My_new_list[0], My_new_list[1], My_new_list[2], My_new_list[3])
print("{} {} {} {}".format(My_new_list[0], My_new_list[1], My_new_list[2], My_new_list[3]))
 
 ############ BREAK EXERCICE #########
 # Create a list including:
 # 9, 9.2, 9.9, 8
 # Using a for and a if loop, create a new list that include only the float.
 # print it as a fancy sentence
 
 # Example of a solution
My_list = [9, 9.2, 9.9, 8]
My_new_list = []
for i in My_list:
    if type(i) == float:
        My_new_list.append(i)
 
print("my floats are : %s %s") %(My_new_list[0], My_new_list[1])
 
 #################################
 ########### FUNCTION ############
 #################################
 
def square_me(number): # def means that it's a function, square_me is the name of the function, what is in bracket is the arguments (the inputs)
    squared_number = number ** 2 # this is actually what the function does, so creating a new variable that is equal to the squared of the argument (the input, here "number")
    return squared_number # return means that it is the end of the function, it returns what it has done 
 
 # We created the function "square_me" but if we want to use it, we have to call it
 # with an actual number as an input (an argument), ex:
square_me(3) # here we are calling the function for the input 3, it will returns the square of 3 so 9
 
 
 # a function to multiply 2 numbers
def multiply_me(number1, number2): # this time we have 2 arguments (2 inputs)
    multiplied_number = number1 * number2 # the function create a new variable equals to the multiplication of the two arguments
    return multiplied_number # return the new created variable
 
multiply_me(3, 5) # here we are calling the function with the input 3 and 5 so it will return 15
 
 ############ BREAK EXERCICES #########
 # create a function named extract_integer() that take off every interger
 # from a list and return the new list including everything but the integers
 # hints: use a for loop, type(), and boolean different from is !=
 
 # example of solution
def extract_integer(my_list):
    my_new_list = []
    for element in my_list: # as you can see, you can use a for loop within a function
        if type(element) != int: # this != is a boolean function for "different from"
            my_new_list.append(element)
    return my_new_list
 
 # HOW TO READ IT:
def extract_integer(my_list):  # The name of the function is extract_integer which take one input (my_list)
    my_new_list = [] # create an empty list named my_new_list
    for element in my_list: # for each element of my_list Python will do the following
        if type(element) != int: # it checks if the element is different form an integer
            my_new_list.append(element) # if it's true (if it's not an integer) then the element is added to my_new_list
    return my_new_list # return the new list without any integer
 
 # REMEMEBER that extract_interger is a function that we created but if we want to use it, we have to call it
 # with a list as an input (an argument)
 # different ways:
 
 # I can just put a list in the argument when I call a function
extract_integer(["a", 1]) 
 # or just create a new list
my_fancy_list = [1, 2.2, "3", "hello", 8]
 # and apply (call) the function to the new list
extract_integer(my_fancy_list)
 
 ############ HOME EXERCICES 1 ######### 
 # Create a function named take_off_integer() that take off every integer
 # from a list and return the new list including everything but integers
 # hints: use a for loop, type(), and boolean different from is !=
 # apply your function to my_fancy_list = [1, 2.2, "3", "hello", 8]
 
 
 
 ############ HOME EXERCICES 2 ######### 
 # Create a function named take_off_e() that take off every letter "e"
 # from a list of string and return the new list including everything but the letter "e"
 # hints 1: use a for loop, a if statement and a boolean function
 # hints 2: rememeber that you take off every letter "e"from a list of string AND NOT from a string
 # Once your function created, apply your function to my_string_list = ["e", "r", "o", "e", "a", "r", "e"]
 # it should return ["r", "o", "a", "r"]
 # hints: use a for loop, type(), and boolean different from is !=
 
 
 string = "Hello world this is great exciting blablabla"
 def extract_e(string):
     without_e = []
     for letter in string:
         if letter != "e":
             without_e.append(letter)
     return without_e
 

 
 
 ############ HOME EXERCICES 3 #########  
 # Create a function named my_age_is() without argument that ask for year and month of birth of the user,
 # then year and month of today.
 # This function should return the actual age of the user
 # ex:
 """
 In: my_age_is()
 year birth = ?
 1986
 month birth = ?
 12
 today year = ?
 2017
 Today month = ?
 09
 Out: "You are 30 years old"
 """
 
 # Hint: to obtain the age, you have to substract today year - birth year and then substract 1 if the month of birth is superior to the today month
 # ex: 
 # i was born the in 12/1986, the today date is 09/2017
 # 12 is superior to 9 so i substract 1 to 2017 - 1986
 # which gives 30 years old
 
 
 
def your_age_is():
    birth_month = input("What is your birth month? ")
    birth_year = input("What is your birth year? ")
    current_month = input("What is the current month? ")
    current_year = input("What is the current year? ")
    age = int(current_year) - int(birth_year)
    if birth_month > current_month:
        age - 1
    else:
        age
    print("Your age is: {}".format(age))





