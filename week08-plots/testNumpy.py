# Testing numpy
# Author: James Connolly

import numpy as np

listOfNumbers = (1,2,3,6)
#numpy prints without commas
numbers = np.array([1,2,4,5])

# listOfNumbers = listOfNumbers + 3
numbers = numbers * 3
numbers = numbers * np.array([1,4,5,6])
numbers = numbers + 3

print (listOfNumbers)
print (numbers)

# print random nmbers between 1st and 2nd call, 5 is the amount
# numbers printed out
randomNumbers =np.random.randint(100,200,5)
print (randomNumbers)

randomNumbers= np.random.normal(size=100)
print (randomNumbers)