import numpy as np
a = np.array([4, 10, 12, 23, -2, -1, 0, 0, 0, -6, 3, -7])
a
#array([ 4, 10, 12, 23, -2, -1,  0,  0,  0, -6,  3, -7])


#How many negative numbers are there
#4
num = a < 0
num
#array([False, False, False, False,  True,  True, False, False, False, True, False,  True])


#How many positive numbers are there?
#5
num = a > 0
num
#array([[ True,  True,  True,  True, False, False, False, False, False, False,  True, False]])

#How many even positive numbers are there?
#8
num = a % 2 == 0
num
#array([ True,  True,  True, False,  True, False,  True,  True,  True, True, False, False])

#If you were to add 3 to each data point, how many positive numbers would there be?
#10
num = (a + 3) > 0
num
#array([ True,  True,  True,  True,  True,  True,  True,  True,  True, False,  True, False])

#If you squared each number, what would the new mean and standard deviation be?
a = np.array([4, 10, 12, 23, -2, -1, 0, 0, 0, -6, 3, -7])
a
#array([ 4, 10, 12, 23, -2, -1,  0,  0,  0, -6,  3, -7])

#squared each value in num
num = a ** 2
num
#array([ 16, 100, 144, 529,   4,   1,   0,   0,   0,  36,   9,  49])

#mean value
np.mean(num)
#74.0

#standard diviation array elements
np.std(num)
std_num = np.std(num)
np.round(std_num, 2)
#144.02

####Centering####
#original array below
a = np.array([4, 10, 12, 23, -2, -1, 0, 0, 0, -6, 3, -7])
a
#array([ 4, 10, 12, 23, -2, -1,  0,  0,  0, -6,  3, -7])
np.mean(a)
#3.0

# created function to center data
center_function = lambda x: x - x.mean()

# apply created center function to numpy array 
data_centered = center_function(a)

#view the updated array
print(data_centered)
#[  1.   7.   9.  20.  -5.  -4.  -3.  -3.  -3.  -9.   0. -10.]

#verify the mean of the centered array is 0
print(data_centered.mean())
#0.0

#Calculate the z-score for each data point. Recall that the z-score is given by: Z = (x - μ) / σ
#Calculate z-score of one dimensional numpy array

import pandas as pd
import numpy as np
import scipy.stats as stats

#create your np array
a = np.array([4, 10, 12, 23, -2, -1, 0, 0, 0, -6, 3, -7])

#puts the array in order asc
a.sort()

#use function stats.zscore(a) by passing in your variable a 
stats.zscore(a)

#each z-score tells us how many standard deviations away an individual value is from the mean.

#array([-1.24034735, -1.11631261, -0.62017367, -0.49613894, -0.3721042 ,-0.3721042 , -0.3721042 ,
# 0.        ,  0.12403473,  0.86824314,1.11631261,  2.48069469])


####Multi-Dimensional Arrays####

#If we have a multi-dimensional array, we can use the axis parameter 
#to specify that we want to calculate each z-score relative to its own array

data = np.array([[5, 6, 7, 7, 8],
                 [8, 8, 8, 9, 9],
                 [2, 2, 4, 4, 5]])


#We can use the following syntax to calculate the z-scores for each array
stats.zscore(data, axis=1)

#The z-scores for each individual value are shown relative to the array they’re in
#array([[-1.56892908, -0.58834841,  0.39223227,  0.39223227,  1.37281295],
#       [-0.81649658, -0.81649658, -0.81649658,  1.22474487,  1.22474487],
#      [-1.16666667, -1.16666667,  0.5       ,  0.5       ,  1.33333333]])











import numpy as np
# Life w/o numpy to life with numpy

## Setup 1
a = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# Use python's built in functionality/operators to determine the following:
# Exercise 1 - Make a variable called sum_of_a to hold the sum of all the numbers in above list

# Exercise 2 - Make a variable named min_of_a to hold the minimum of all the numbers in the above list

# Exercise 3 - Make a variable named max_of_a to hold the max number of all the numbers in the above list

# Exercise 4 - Make a variable named mean_of_a to hold the average of all the numbers in the above list

# Exercise 5 - Make a variable named product_of_a to hold the product of multiplying all the numbers in the above list together

# Exercise 6 - Make a variable named squares_of_a. It should hold each number in a squared like [1, 4, 9, 16, 25...]

# Exercise 7 - Make a variable named odds_in_a. It should hold only the odd numbers

# Exercise 8 - Make a variable named evens_in_a. It should hold only the evens.

## What about life in two dimensions? A list of lists is matrix, a table, a spreadsheet, a chessboard...
## Setup 2: Consider what it would take to find the sum, min, max, average, sum, product, and list of squares for this list of two lists.
b = [
    [3, 4, 5],
    [6, 7, 8]
]

# Exercise 1 - refactor the following to use numpy. Use sum_of_b as the variable. **Hint, you'll first need to make sure that the "b" variable is a numpy array**
sum_of_b = 0
for row in b:
    sum_of_b += sum(row)

# Exercise 2 - refactor the following to use numpy. 
min_of_b = min(b[0]) if min(b[0]) <= min(b[1]) else min(b[1])  

# Exercise 3 - refactor the following maximum calculation to find the answer with numpy.
max_of_b = max(b[0]) if max(b[0]) >= max(b[1]) else max(b[1])


# Exercise 4 - refactor the following using numpy to find the mean of b
mean_of_b = (sum(b[0]) + sum(b[1])) / (len(b[0]) + len(b[1]))

# Exercise 5 - refactor the following to use numpy for calculating the product of all numbers multiplied together.
product_of_b = 1
for row in b:
    for number in row:
        product_of_b *= number

# Exercise 6 - refactor the following to use numpy to find the list of squares 
squares_of_b = []
for row in b:
    for number in row:
        squares_of_b.append(number**2)


# Exercise 7 - refactor using numpy to determine the odds_in_b
odds_in_b = []
for row in b:
    for number in row:
        if(number % 2 != 0):
            odds_in_b.append(number)


# Exercise 8 - refactor the following to use numpy to filter only the even numbers
evens_in_b = []
for row in b:
    for number in row:
        if(number % 2 == 0):
            evens_in_b.append(number)

# Exercise 9 - print out the shape of the array b.

# Exercise 10 - transpose the array b.

# Exercise 11 - reshape the array b to be a single list of 6 numbers. (1 x 6)

# Exercise 12 - reshape the array b to be a list of 6 lists, each containing only 1 number (6 x 1)

## Setup 3
c = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

# HINT, you'll first need to make sure that the "c" variable is a numpy array prior to using numpy array methods.
# Exercise 1 - Find the min, max, sum, and product of c.

# Exercise 2 - Determine the standard deviation of c.

# Exercise 3 - Determine the variance of c.

# Exercise 4 - Print out the shape of the array c

# Exercise 5 - Transpose c and print out transposed result.

# Exercise 6 - Get the dot product of the array c with c. 

# Exercise 7 - Write the code necessary to sum up the result of c times c transposed. Answer should be 261

# Exercise 8 - Write the code necessary to determine the product of c times c transposed. Answer should be 131681894400.


## Setup 4
d = [
    [90, 30, 45, 0, 120, 180],
    [45, -90, -30, 270, 90, 0],
    [60, 45, -45, 90, -45, 180]
]

# Exercise 1 - Find the sine of all the numbers in d

# Exercise 2 - Find the cosine of all the numbers in d

# Exercise 3 - Find the tangent of all the numbers in d

# Exercise 4 - Find all the negative numbers in d

# Exercise 5 - Find all the positive numbers in d

# Exercise 6 - Return an array of only the unique numbers in d.

# Exercise 7 - Determine how many unique numbers there are in d.

# Exercise 8 - Print out the shape of d.

# Exercise 9 - Transpose and then print out the shape of d.

# Exercise 10 - Reshape d into an array of 9 x 2