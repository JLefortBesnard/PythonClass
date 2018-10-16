###########################################
### SUM OF THE FIRST PYTHON CLASS 16.10 ###
###########################################
# Jeremy Lefort-Besnard

######### Navigate in the TERMINAL #############
# cd my_folder (to go in a specific folder)
# cd .. (to move backward)
# pwd (print the directory in which we are)

# cd Desktop
#  mkdir "python_class" (to create a folder named my_folder)
# cd $_
# touch class1.py
# atom
# open class1.py
# write "ipython" on the terminal to enter python3
# write "quit" on ipython to return to the bash command

# pip instal numpy





######### IN IPYTHON #############
# Hashtag means it is a comment, Python won't read it
# indentation (space) is very important in Python
# Be careful where you put some
# for example:
# my variable = 0 doesn't work but
# my_variable = 0 does work
# my, variable = 1, 2


# type of variable in Python
my_integer = 1
type(my_integer) # return INT
my_float = 1.3
type(my_float) # return FLOAT

# python works with assignment
a = 1
print(a) # return the value 1

b = a
print(b) # return the value 1

a = 2
print(b) # return the value 1 because b was equal to the previous version of a

dir() # Python returns all the variables you used so far
who # same but only the variable you implemented
whos # same but with details

i = 42
type(i) # return INT
i = 42 + 0.11
type(i) # return FLOAT
i = "fourty"
type(i)  # Return STR for String, so Python directly transform the variable type

My_string = "Everything in quotes is a string"
My_string2 = 'whatever the type of quotes'

##############################
## four kinds of container ###
##############################
import numpy # import the package we need to make arrays
# !pip install numpy (to download the package if not done)

a_list = [10, 20, 30] # You can recognize a list as it is between square brackets
a_tupple = (1, 2, 3) # You can recognize a tupple as it is between round brackets
an_array = numpy.array([[1, 2, 3], [2, 3, 4]]) # You can recognize an array "numpy.array" is written before
a_dictionnary = {1:["a", "b"], 2:"b", 3:"c"} # You can recognize a dictionnary as it is between curvy brackets


# Excercice: create an array called "array2" with 3 columns and 5 rows. What is the shape of this array?

# a list is mutable, ex:
my_list = [0, 3, 2, 5, 7]
print(my_list) # return [0, 3, 2, 5, 7]
my_list[3] = 20
print(my_list) # return [0, 3, 2, 20, 7]

# a tupple is immutable
my_tupple = (0, 3, 2, 5, 7)
my_tupple[3] = 20 # return an error

# !!!  The first element of anything in Python is indexed at ZERO and not ONE !!!
my_list = ["a", "b", "c"] # ex: my_list[0] = "a", my_list[1] = "b"

my_list = ["a", "b", "c"] # a list can be made of integer or float
my_list = ["a", 2, "c"] # or a mix of strings and integers

# access to the ith element in a list
my_list = [0, 3, 2, 5, 7]
print(my_list[3]) # return 5
print(my_list[4]) # return 7

# change the 4th element into the integer 2à
my_list[3] = 20 # change the 4th element (indexed as 3) for 20 (so the 5 for 20)

############ BREAK EXERCICES #########
# For the next session, create a list named "my_status". This list includes your age, your name, your job status.
# Your age should be written as an integer, the 2 other elements should be strings.
# print your list
