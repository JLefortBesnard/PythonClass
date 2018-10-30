###########################################
### SUM OF THE SECOND PYTHON CLASS 30.10 ##
###########################################

# Create a function that tells how many vowels are in a string

def number_vowels(my_string): # function named number_vowels with one input (argument)
    number_vowels = 0 # count the number of vowel, so far 0
    vowels = ["a","e", "i", "o", "u", "y"] # tells Python what the vowels are
    for letter in my_string: # iterate through each letter of my input
        for vowel in vowels: # iterate through each vowel
            if letter == vowel: #check if any of the letter from my_string is actually a vowel from vowels
                number_vowels += 1 # increase the number of vowel only if the letter is indeed a vowel
    return number_vowels # tells the user how many vowels there are in the input

# let's try it!
sentence = "Nous sommes fous, we are crazy, wir sind verruckt" # this is gonna be our input
number_vowels(sentence) # We call the function with our input. This should return 15

# slicing
My_string = "Nous sommes fous, we are crazy, wir sind verruckt"
print(My_string[:16]) # this will return the letter from the beginning to the 15th (remeberPython starts at index=0) so Nous sommes fous
print(My_string[16:30]) # this will return the letter from the 16th to the 29th so we are crazy
print(My_string[30:]) # this will return the letter from the 30th to the end so wir sind verruckt
print(My_string[-12:]) # alternative





#### Challenge ####

# Create a rock paper scissors game against a computer that choose
# randomly the answer

# hint1: to randomly select an interger:
# type this:
# from random import randint
# print(randint(0, 2)) # return an int between 0 and 2

# hint 2: a while loop works like a for loop, it stops only once you reach a certain points# ex
# a = 0
# while a < 6:
#    print"hello"
#    a += 1

# this will print "hello" 6 times and Python will stop automatically
# be careful though, this would end up into an infinite loop
# ex:

# while 10 < 100:
#   print "hello"
# this will print "hello" foreeeeever!!! (press ctrl + c in python to manually stop it, or cmd + c with a MAC)


import os
os.system('clear')  # cls for windows
import time


def chifumi():
    from random import randint # import the module we need for an random choice
    computer_score = 0
    Player_score = 0
    lap = 0
    while Player_score < 3 and computer_score < 3: # we want to play a game till the first player reachs 3 points
        # this part is just to make the game more beautiful on the python screen
        print(" ") # print a space to ease the reading
        print("Game {}".format(lap)) # print which turn it is
        print("  ") # print a space to ease the reading

        # This part ask for the choice of the player and compute the answer for the computer (the bot)
        player_choice = int(input("Rock(Enter 1), Paper(Enter 2), Scissors(Enter 3) ??")) # ask for an answer looking like 1, 2 or 3 and transform it into an integer
        computer_choice = randint(1, 3) # select randomly an integer between 1 and 3
        print("  ") # print a space to ease the reading
        print("  ") # print a space to ease the reading
        # This part checks for the results
        if player_choice == 1 and computer_choice == 2: # rock against paper, paper win
            computer_score += 1 # add a point to the bot
            print("\033[93m You:rock -- Bots:paper \033[0m")
            print("=> bot win! {}/{}".format(Player_score, computer_score))
            time.sleep(3)

        elif player_choice == 1 and computer_choice == 3:
            Player_score += 1 # add a point to the user
            print("\033[93m You:rock -- Bots:scissors \033[0m")
            print("=> you win! {}/{}".format(Player_score, computer_score))
            time.sleep(3)

        elif player_choice == 2 and computer_choice == 1:
            Player_score += 1
            print("\033[93m You:paper -- Bots:rock \033[0m")
            print("=> you win! {}/{}".format(Player_score, computer_score))
            time.sleep(3)

        elif player_choice == 2 and computer_choice == 3:
            computer_score += 1
            print("\033[93m You:paper -- Bots:scissors \033[0m")
            print("=> bot win! {}/{}".format(Player_score, computer_score))
            time.sleep(3)

        elif player_choice == 3 and computer_choice == 2:
            computer_score += 1
            print("\033[93m You:scissors -- Bots:paper \033[0m")
            print("=> you win! {}/{}".format(Player_score, computer_score))
            time.sleep(3)

        elif player_choice == 3 and computer_choice == 1:
            Player_score += 1
            print("\033[93m You:scissors -- Bots:rock \033[0m")
            print("=> bot win! {}/{}".format(Player_score, computer_score))
            time.sleep(3)

        else:
            print("\033[93m Equality\033[0m")
            print("You both took {}".format(player_choice))
            time.sleep(3)

        lap += 1
        print("   ") # print a space to ease the reading
        print("--"*30) # print - 30 times
        print("   ") # print a space to ease the reading

    if Player_score < Player_score:
        print("SCORE you:{} vs bot:{}, YOU WON! YOU ARE AWESOME!!".format(Player_score, computer_score))
    else:
        print("SCORE you:{} vs bot:{}, YOU ARE THE BIGGEST LOSER EVER!!".format(Player_score, computer_score))



chifumi() # call the function to play the game, try it!



#####################
# DATA MANIPULATION #
#####################


# So far we've seen what a list is:
my_list = [[10, 2, 1, 4, 2], [20, 35, 40, 70, 37], [43, 34, 24, 38, 54]]
# Problem is, when it's multidimensional, it's not the best way to display data
my_list.shape # Also the (useful) shape Ufunc doesnt work
len(my_list) # and the len function does not give how many element per list we have

# Let's say we have such a data set:
import numpy as np
x1 = [10, 2, 1, 4, 2] # X1 is the amount of Keuros in bank
x2 = [20, 35, 40, 70, 37] # X2 is the number of hour of work per week
x3 = [43, 34, 24, 38, 54] # X3 is the age of the subject

# We could create a multidimensional array of these elements
X = np.array([x1, x2, x3])

#It's still not really readable, we don't know what is what when we print X on the terminal
# One way would be to add a labels row to specify what is in each column +
# the name of each row at the begining of the row
# so that we know what we are talking about:
labels_col = ["S1", "S2", "S3", "S4", "S5"]
x1 = ["Amount", 10, 2, 1, 4, 2] # Keuros in bank
x2 = ["Hour_work", 20, 35, 40, 70, 37] # the number of hour of work per week
x3 = ["Age", 43, 34, 24, 38, 54] # age

X = np.array([labels_col, x1, x2, x3])
# But still it's not really readable.
# A solution for this problem is to use Pandas DataFrame which will print
# our data in a beautiful and readable way

import pandas as pd # we need to import the package (as pd to write shorter scripts)

# We need to create the dataframe
df_1 = pd.DataFrame({"Amount": [10, 2, 1, 4, 2],
                    "test_before_drug": [20, 35, 40, 70, 37],
                    "test_under_drug": [43, 34, 24, 38, 54]},
                    index = ["Sub 1", "Sub 2", "Sub 3", "Sub 4", "Sub 5"])
df_1
# This indeed looks beautiful and readable! It's like an excel document!

# We will save this df as excel document:
writer = pd.ExcelWriter('My_ExcelFile.xlsx')
df_1.to_excel(writer,'Sheet1')
writer.save()
# We could also create an Excel document and save the Excel file as "My_ExcelFile" on our Desktop for example
# then you directly import in in Python:


import os
os.chdir("/Users/Desktop/") # We need to go to our terminal (os.chdir does it for us)
# you might need to change the path. this one "/Users/Desktop/" is specific to my computer
df = pd.read_excel("My_ExcelFile.xlsx") # import the excel file I created before
df
# As you can see, pandas also print the implicit index
# Implicit index is an index from 0 to N-1, whereas explicit index is the one you decided to use
# here the explicit index is "Sub 1", "Sub 2", "Sub 3", "Sub 4", and "Sub 5"
# Meaning that index 0 = index "Sub 1"

df_1.iloc[:3, :2] # iloc is useful for implicit index
df_1.loc[:"Sub 4", :"test_before_drug"] # loc is useful for explicit index
df.info() # basics computer informations about the dataframe
df.describe() # basics stats about the dataframe
df_1.max()  # display max value of each column
df_1.max(axis=1) # disply the max value of each row
df_1['test_before_drug'].max() # max value of a specific columns
df_1["Amount"] # display the values of that specific columns
df_1['Amount'].values
df.index # display the index
df_1.get_values() # display all values of the dataframe
# I won't describre these function since it's pretty explicit
df_1.min()
df_1.sum()
df_1.count()
df_1.median()
df_1.quantile([0.25, 0.75])
df_1.mean()
df_1.var() #variance
df_1.std() # standart deviation
df_1.abs() # absolute values
df_1.rank()
df_1.cumsum() # cummulative sum
df_1.cumprod()
df_1.cummax()
df_1.cummin()

df_1.drop(columns=df_1.columns[0]) # drop a columns, carefull though it's a copy
df_1 # still has the first column
df_1_colcut = df_1.drop(df_1.columns[0], axis=1) # or df_1_colcut = df_1.drop(columns=df_1.columns[0])
df_1_colcut

df_1_rowcut = df_1.drop(df_1.index[0])
# print specific row and column
df_1["test_before_drug"]["Sub 2"]

# What about a dependant t-test between X1 and X2?
from scipy import stats
stats.ttest_rel(df_1['test_before_drug'].values, df_1['test_under_drug'].values)

# What about plotting our data to see if there is a correlation?
import seaborn as sns
import matplotlib.pyplot as plt
sns.pairplot(df_1)
plt.show()

# What about plotting a specific relationship?
g = sns.lmplot(x= "test_under_drug", y="Amount", data = df_1)
g.set_axis_labels("test_under_drug", "Amount")
plt.show()


### excercise for next session ###
"""
EX 1: 

open an excel document that you previously created using pandas DataFrame with
five input (X1 to X5 and 30 random values in each column)

keep only X1 and X3
print only row 10 to 20
rename them as:
X1 = "age"
X3 = "salary"
"""


"""
EX 2:

Create a function that solve an equation with 2 unknown (https://en.wikipedia.org/wiki/Quadratic_equation)
ax**2 + bx + c = 0     with a, b, c as argument (input known) of the function with a different from 0!

remember high school? if you want to solve a quadratic equation:
first compute the discriminant: discriminant = b**2 - 4*a*c
it has been shown that there is 2 solutions if discriminant is positive
x1 = (-b + square_root(b**2 - 4*a*c))/(2*a)
and
x2 = (-b + square_root(b**2 - 4*a*c))/(2*a)
only one solution if discriminant is equal to 0:
x = -b / (2*a)
No solution in R if discriminant is negative (so just print("no solution") if this is the case)


Once you defined your function:
call it to solve the equations
3x**2 + 5x + 2 = 0
and
-6x**2 + 2x + 3 = 0

!!!!!
hint
!!!!!
The function square root is defined this way:
1: import math
2: math.sqrt(25)
this would return 5

"""