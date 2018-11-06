###########################################
### SUM OF THE EIGHTH PYTHON CLASS 25.10 ##
###########################################


# Let's say you want to print in color in the terminal (to create a game or something)
# just have to add the "\033[1;31m WRITE WHAT YOU WANNA WRITE \033[1;m"
# you just change the second number to change the COLOR# you can find a more exhaustive list on Google

print('\033[1;31mRed like Radish\033[1;m')
print('\033[1;32mGreen like Grass\033[1;m')
print('\033[1;33mYellow like Yolk\033[1;m')
print('\033[1;34mBlue like Blood\033[1;m')
print('\033[1;35mMagenta like Mimosa\033[1;m')
print('\033[1;36mCyan like Caribbean\033[1;m')
print('\033[1;37mWhite like Whipped Cream\033[1;m')
print('\033[1;38mCrimson like Chianti\033[1;m')
print('\033[1;41mHighlighted Red like Radish\033[1;m')
print('\033[1;42mHighlighted Green like Grass\033[1;m')
print('\033[1;43mHighlighted Brown like Bear\033[1;m')
print('\033[1;44mHighlighted Blue like Blood\033[1;m')
print('\033[1;45mHighlighted Magenta like Mimosa\033[1;m')
print('\033[1;46mHighlighted Cyan like Caribbean\033[1;m')
print('\033[1;47mHighlighted Gray like Ghost\033[1;m')
print('\033[1;48mHighlighted Crimson like Chianti\033[1;m')



import numpy as np
import random
# Standardize your data
# first, let's create an input (X) and an output y
X = np.random.random((10, 5)) # create a 10 rows 5 columns variable
# we can interpret it as an input consisting of 5 parameters for 10 subjects

# and we got 10 outputs, one for each subject
y = np.random.randint(0, 10, 10) # this function randomly picks 10 nbs between 0 and 10


# So you want to standardize your input (mean = 0)
from sklearn.preprocessing import StandardScaler
scaler = StandardScaler().fit(X) # This just call the function on X
standardized_X = scaler.transform(X) # this actually standardizes the data
standardized_X


# then we can fit our linear model
from sklearn.linear_model import LinearRegression
linReg = LinearRegression(normalize=True) # we have to tell Python that our data is already
# standardized so we write normalize=True
sol = linReg.fit(standardized_X, y) # as seen last time, it's a fit function so first we name the function, then we .fit() it
sol.coef_ # return the beta value for each feature
sol.intercept_ # return the intercept of the fitted linear function

# What about fitting a PCA (orthogonal components)
from sklearn.decomposition import PCA
pca = PCA(3) # here we extract 3 components, you can change this number, remember though that it's
# at most as many components as number of parameters
sol = pca.fit(standardized_X) # it's a fit function so first we name, second we fit
sol.components_ # to get the answer, so the value of each weight in the components
sol.explained_variance_ # the explained variance
sol.explained_variance_ratio_ # the expalined variance in %


# A bit of classical statistics:
from scipy import stats
X1 = np.random.random((20)) # let's create 2 variables with 20 observations each
X2 = np.random.random((20))

X1_stand = stats.zscore(X1) # Another way to standardize
X2_stand = stats.zscore(X2)

stats.sem(X1) # standard error of the mean
stats.normaltest(X2) # test for normality


stats.chisquare([12, 14, 16, 18, 10, 10]) # chisquare (each entry represents the category and how many times they appear)
stats.rankdata(X1) # rank the data, useful for non parametric tests

stats.ttest_ind(X1, X2) # independant t test
stats.ttest_rel(X1, X2) # dependant t test

stats.mannwhitneyu(X1, X2) # Mann Whitney U test (non parametric)
stats.wilcoxon(X1, X2) # Wilcoxon test (non parametric)

stats.spearmanr(X1, X2) # spearman correlation

stats.linregress(X1, X2) # linear regression in the classical stats regime (p value)


# ANOVA
# let's create 4 variables for running an ANOVA
X1 = np.random.random((20))
X2 = np.random.random((20))
X3 = np.random.random((20))
X4 = np.random.random((20))
stats.f_oneway(X1, X2, X3, X4) # give us the F stat + p value


# What if we need to run a post hoc test like tukey
# let's import it
from statsmodels.stats.multicomp import pairwise_tukeyhsd
from statsmodels.stats.multicomp import MultiComparison
import pandas as pd

# First I need to rearange the data in that a form of a column of the values and
# a columns of the groups (x1, x1, x1... x2, x2, x2..., etc...)

data = pd.DataFrame(np.concatenate([X1, X2, X3, X4]),
                    index = [np.concatenate([["X1"] * 20,
                                             ["X2"] * 20,
                                             ["X3"] * 20,
                                             ["X4"] * 20])],
                    columns = ["Values"])

# then I can call my post hoc test
mc = MultiComparison(data['Values'], data.index)
result = mc.tukeyhsd()

# then I can print the results:
print(result)
print(mc.groupsunique)


###############################
## DEALING WITH MISSING DATA ##
###############################

# THERE IS NO PERFECT WAY TO DEAL WITH MISSING DATA

# let's first create a dataset with missing data
df = pd.DataFrame(np.random.randn(5, 3), index=['sub 1', 'sub 4', 'sub 5', 'sub 7', 'sub 2'],
                    columns=['size', 'height', 'age'])

# let's add a column:
df['tall'] = df['height'] > 0

# reindexing to add nan
df2 = df.reindex(['sub 1', 'sub 2', 'sub 3', 'sub 4', 'sub 5', 'sub 6', 'sub 7'])

# let's add missing data
df2["size"].iloc[0] = None
df2["age"].iloc[1] = None
df2["height"].iloc[4] = None



# Pandas provides the function isnan() To make detecting missing values easier
pd.isna(df2['size'])
# or notnan() for the opposite
df2['size'].notna()

# let's have an overview on the whole dataset
df2.isna()

###############
# cleaning/filling missing data:
################

# filling nan with 0
df3 = df2.fillna(0)

# filling only a specific column:
df2['size'].fillna('no data')

# fillinf nan with the previous value
df2.fillna(method='ffill')
# or the following value
df2.fillna(method='bfill')

# fill with the column mean
df2.fillna(df2.mean())
# with the median
df2.fillna(df2.median())


# drop the columns with missing data
df2.dropna(axis=1)
# same for rows with missing data
df2.dropna()
# same but just for a specific columns
df2["size"].dropna()

# interpolation (kind of a linear regression on each row to find the value)
df2.interpolate()

# many methods exist, more information there:
# https://pandas.pydata.org/pandas-docs/stable/missing_data.html

# also possible to use knn => look for close neighbor to fill missing data

# dealing with missing data with an array instead of pandas dataframe:
# https://www.dummies.com/programming/big-data/data-science/how-to-create-a-supervised-learning-model-with-logistic-regression/



################################
# EXCERCICE FOR NEXT WEDNESDAY #
################################

"""
A. Create a dataset consisting of 15 rows and 5 columns
Column names: grade, weight, age, number_children, number_hair
row names: subject 1 to subject 15

B. Using a "for" loop, randomly pick 6 value from the dataframe and make it equal to Nan (Not a number)

Hint:
1. your "for" loop should iterate 6 times (6 times transforming a value into Nan)
inside the for loop:
2. create a variable (random_col) that randomly pick an interger between 0 and 4 (columns index) 
3. create a variable (random_sub) that randomly pick an interger between 0 and 14 (rows index)
4. then apply this: df[df.columns[random_col][0]].iloc[random_sub[0]] = None
This should return a df with 6 missing values.

C. then create a second dataframe that replace the missing value by "Empty"
D. then create a third dataframe that take off the row with missing value
E. then create a second dataframe that replace the missing value by the median of the columns

"""





                
    
    
    
    
    
    
    
    