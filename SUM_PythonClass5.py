# as usual import all the module we will need
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

##### a bit of plotting with PYTHON ####
mean = [0, 0]
cov = [[1, 2], [2, 5]]
data = np.random.multivariate_normal(mean, cov, 50)
# Draw 2 random samples from a multivariate normal distribution.
# the 2 samples will be of size 50, mean 0 for the 1st one and 0 for the second one (mean = [0, 0])
# And Covariance matrix of the distribution of 1, 2 for the first one and 2, 5 for the second one (cov = [[1, 2], [2, 5]])
# See "https://docs.scipy.org/doc/numpy-1.13.0/reference/generated/numpy.random.multivariate_normal.html"
# for more information
# let's create our input and output:
X = data[:, 0] # extract all data ([:] means from the beginning to the end)from the first row (0)
Y = data[:, 1] # extract all data ([:] means from the beginning to the end)from the second row (1)


plt.scatter(X, Y) # Prepare the plot of the data
plt.show()  # display it on the screen, plt.show() is needed any time you need to show the plot

# We are missing x and y labels
plt.scatter(X, Y, color='red')
plt.xlabel("This is the X-axis") # here we go for the x label
plt.ylabel("This is the Y-axis") # here we go for the y label
plt.show()

# Adding a title?
plt.scatter(X, Y, color='yellow')
plt.xlabel("This is the X-axis")
plt.ylabel("This is the Y-axis")
plt.title("My first plot") # here you go for a title
plt.tight_layout() # this is a "magic" fucntion that takes care for you of the disposition of the plot (the windows is well adjusted so
# that we can well see the labels and titles and so on)
# Careful though, it has to be written as the last modiication, if I add "plt.title()" after, then this title won't be
# taken into consideration for the adjustment
plt.show()


# Let's say half of our points are actually from one subject, the other half from another, then we want 2 colors.
# Also, how to save your plot??
plt.scatter(X[25:], Y[25:], color='r') # this one plot suject 1 (the first 25 points from the dataset we generated)
plt.scatter(X[:25], Y[:25], color='b') # this one plot suject 2 (the last 25 points from the dataset we generated)
# color= "b" or "blue" or "r" or "red" or "yellow" or "y" check online for more colors (there are thousands!)
plt.xlabel("This is the X-axis")
plt.ylabel("This is the Y-axis")
plt.title("My first plot")
plt.tight_layout()
plt.savefig("myfirstplot") # save it (be careful where you are on ipython (pwd),
# if you are located in your Desktop, then it will be saved there
plt.show()


# Now you want to modify the scale of the x and y axis?
plt.scatter(X, Y, color='r')
plt.xlim([-2.5, 2]) # here you go, the begining and the end of the x axis
plt.ylim([-7, 4]) # here you go, the begining and the end of the y axis
plt.xlabel("This is the X-axis")
plt.ylabel("This is the Y-axis")
plt.title("My first plot")
plt.tight_layout()
plt.show()

# now let's say that you want to plot subject 1 (25 first datapoints)
# and subject 2 in 2 different plots but on the same windows
fig=plt.subplot(121) # create a subplot with the 121 = 1 row, 2 columns, the last 1 means the position of this subplot
plt.scatter(X[25:], Y[25:], color='r')
fig=plt.subplot(122) # create a subplot with the 122 = 1 row, 2 columns, the last 2 means the position of this subplot
# you can modify it with 221 to 224 meaning 2 rows 2 columns so 4 positions so up to 4 plots
plt.scatter(X[:25], Y[:25], color='b')
plt.xlabel("This is the X-axis")
plt.ylabel("This is the Y-axis")
plt.title("My first plot")
plt.tight_layout()
plt.show()

# We are missing xlabels ylabels and title on the first plotfig=plt.subplot(121)
# Configuring the first plot
fig=plt.subplot(121) # first subplot
plt.scatter(X[25:], Y[25:], color='r')
plt.xlabel("This is the RED X-axis")
plt.ylabel("This is the RED Y-axis")
plt.title("Subject 1")
plt.tight_layout()
# Configuring the second plot
fig=plt.subplot(122) #second subplot
plt.scatter(X[:25], Y[:25], color='b')
plt.xlabel("This is the BLUE X-axis")
plt.ylabel("This is the BLUE Y-axis")
plt.title("Subject 2", fontsize=20, color= "b") # you can modify the fontsize
# Diplaying it
plt.show()


############ BREAK EXERCICE #########
# Generate 100 data points from a normal distribution with mean 0 for X and 2 for Y
# with cov [2, 1], [3, 7]
# Plot it the best beautiful way (color, labels on x and y axis, title)
# plot three subplot
# 1 with 30 first data points
# 2 with 30:70 (from 30 to 69)
# 3 from 70 till the end

# Solution
mean = [0, 2]
cov = [[2,1], [3, 7]]
data = np.random.multivariate_normal(mean, cov, 100)
X = data[:, 0]
Y = data[:, 1]

fig = plt.subplot(131)
plt.scatter(X[:30], Y[:30], color='blue')
plt.xlabel("x axis")
plt.ylabel("y axis")
plt.title("This is my first graph")
fig = plt.subplot(132)
plt.scatter(X[30:70], Y[30:70], color='red')
plt.xlabel("x axis")
plt.ylabel("y axis")
plt.title("This is my second graph")
fig = plt.subplot(133)
plt.scatter(X[70:], Y[70:], color='green')
plt.xlabel("x axis")
plt.ylabel("y axis")
plt.title("This is my third graph")
plt.tight_layout()
plt.show()



################################
##### Histograms ###############
################################

# Data
# Let's say our data are the answers of a questionnaire
# so we got 1 always, 2 often, 5 sometimes and 3 never:
Y = np.array([1, 2, 5, 3]) # the scores
X = ['always', 'often', 'sometimes', 'never'] # the values

plt.figure(figsize=(7 ,5)) # this creates an empty window where we will put our histogram in, with a certain size (play with it to understand it)
ax1 = sns.barplot(X, Y) # this creates the histogram
# so we call seaborn (as sns) and the function barplot of seaborn with X and Y as argument
plt.show() # this display the histogram

# Again we miss labels, titles and so on, guess what? it's is exactly the same, Python is so E.A.S.Y :D
plt.figure(figsize=(7 ,5))
ax1 = sns.barplot(X, Y, color='b') # we just need one color
plt.title("How often? Subject 1")
plt.xticks(rotation=35) # this tilts the X labels, play with it, it could be up to 360 or -360!
plt.tight_layout()
plt.show()


plt.figure(figsize=(7 ,5))
ax1 = sns.barplot(X, Y, color='b')
plt.title("How often? Subject 1")
plt.xticks(rotation=35)
plt.ylim([min(Y)-1, max(Y)+1]) # this again limits the X and Y axis to the minimum (min() function) and maximum (max() function of our Y data
plt.xlabel("How often?")
plt.ylabel("Numbers of answers")
plt.tight_layout()
plt.show()

# What if we want to plot the scores of several Subject?
# we could use the plt.subplot(221) and plt.subplot(222) see above
# We could also plot both of them on the same histogram:
Y1 = np.array([1, 2, 5, 3]) #subject 1
Y2 = np.array([2, 2, 2, 0]) #subject 2
plt.figure(figsize=(7 ,5))
ax1 = sns.barplot(X, Y1+Y2, color="green") # this will plot the histogram of the scores of subject 1 + subject 2
plt.title("How often? Subject 1 and 2 together")
plt.xticks(rotation=35)
plt.ylim([0, 8])
plt.xlabel("How often?")
plt.ylabel("Numbers of answers")
plt.tight_layout()
plt.show()

# the problem here is that we cannot differentiate if subject 1 got more or less scores than subject 2, better it is to add
# color + legend
import matplotlib.patches as mpatches # we need this thing for a pretty legend

Y1 = np.array([1, 2, 5, 3])
Y2 = np.array([2, 2, 2, 0])
plt.figure(figsize=(7 ,5))
ax2 = sns.barplot(X, Y1+Y2, color='r') # this will plot the histogram of the scores of subject 1 + subject 2 in red
ax1 = sns.barplot(X, Y1, color='b') # this will plot the histogram of the scores of subject 1 in blue on top of the first histogram
# so that we can see the differences
plt.title("How often? Subject 1 and 2 together")
plt.xticks(rotation=35)
plt.ylim([0, 8])
plt.xlabel("How often?")
plt.ylabel("Numbers of answers")
blue_patch = mpatches.Patch(color='b', label='subject 1') # create a variable with all information for the legend of subject 1
r_patch = mpatches.Patch(color='r', label='subject 2') # create a variable with all information for the legend of subject 2
plt.legend(handles=[blue_patch, r_patch,], loc=1) # actually plot the legend, loc stands for the position where the legend will appear
# play with it to understand, try loc=2 or 3 or "best"
plt.tight_layout()
plt.show()

"""
You can make very pretty figures, the codes are already made, 
You just have to modify it a little bit to make it appropriate
in your setting. The main python plotting libraries:

Seaborn:
https://seaborn.pydata.org/examples/index.html

matplotlib:
https://matplotlib.org/gallery/index.html

Altair:
https://altair-viz.github.io/gallery/index.html
"""


############ BREAK EXERCICES #########
"""
Create an array including panss items and scores:
positive: 7
negative: 4
general_part1: 3
general_part2: 4
Plot it with a pretty histogram
"""
X = ['pos', 'neg', 'gen_1', 'gen_2']
Y = np.array([7, 4, 3, 4])
plt.figure(figsize=(7, 5))
ax = sns.barplot(X, Y, color='b')
plt.xlabel("scores")
plt.ylabel("questionnaire items")
plt.title("whatever")
plt.xticks(rotation=90)
plt.tight_layout()
plt.show()



# exercice to handle Pandas dataframe and plotting even more:

# Let's download a dataset
tips = sns.load_dataset("tips")
tips.head()

"""
# excercise:
delete the time column
set the tip of the first 10 subjects as 0
set it as the median of the tip column
set the total bill of the subject 8 to 14 equals to the mean total bill of the subject 14 till the last subject
plot the total bill per sex
plot the total bill per day
"""
del tips["time"] # delete the column time
tips["tip"][0:10] = 0 # set the tip of the first 10 subjects as 0
tips["tip"][0:10] = np.median(tips["tip"][10:]) # set it as the median of the tip column
# tips["tip"][0:10] selects the first 10 subjects
# np.median(tips["tip"][10:]) is made of np.median() which extract the median from what is inside
# and tips["tip"][10:] which display the tip values from the subjects 10 till the last subject


tips["total_bill"][8:14] = np.mean(tips["total_bill"][14:]) # same reasonning as before
# set the total bill of the subject 8 to 14 equals to the mean total bill of the subject 14 till the last subject

# from the original dataset, we want to plot the mean total_tip per gender
# first: let's reload the original dataset
tips = sns.load_dataset("tips")
# let's check by looking at the first 5 rows
tips.head(5) 
# let's extract the index where the subject is a female
female_index = tips[tips["sex"]=="Female"].index
# then let's extract the index where the subject is a male
male_index = tips[tips["sex"]=="Male"].index

# let's now compute the mean of the total_bill for the female 
# first let's have the female total_bill as a Pandas.Series (i.e., kind of an array)
tot_tips_female = tips["total_bill"][female_index]
# And then we compute the mean of these values
f_bill = np.mean(tot_tips_female)
print(f_bill) # yeah it works!
# let's now compute the mean of the total_bill for the male 
# first let's have the male total_bill as a Pandas.Series (i.e., kind of an array)
tot_tips_male = tips["total_bill"][male_index]
# And then we compute the mean of these values
m_bill = np.mean(tot_tips_male)
print(m_bill) # yeah it works!

# now we got everything we need, we can plot it
# let's define X and Y
X = ["Female", "Male"]
Y = [f_bill, m_bill]
plt.figure(figsize=(7, 5))
ax = sns.barplot(X, Y, color='b')
plt.xticks(rotation=90)
plt.tight_layout()
plt.show()

"""
Exercise for next time:
plot the total_bill per day
hint: your X should now be Monday, Tuesday, Wednesday, etc... instead of Female and Male
"""




                
    
    
    
    
    
    
    
    
