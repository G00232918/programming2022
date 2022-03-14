# a program that makes a list from salaries
# Author: James Connolly

import numpy as np

minSalary = 20000
maxSalary = 80000
numberOfEntries = 10

np.random.seed(1)
salaries = np.random.randint(minSalary, maxSalary, numberOfEntries)
print (salaries)

salariesPlus = salaries + 5000
print (salariesPlus)

# adding 5% to salaries
salariesMul = salaries * 1.05
print (salariesMul)

# This is a float array, here I convert it to an int 
# array (it does a floor)
newSalaries = salariesMult.astype(int)
print(newSalaries)

salariesPlus = salaries + 5000
print (salariesPlus)

# adding 5% to salaries
salariesMul = salaries * 1.05
print (salariesMul)

# This is a float array, here I convert 
# it to an int array (it does a floor)
newSalaries = salariesMult.astype(int)
print(newSalaries)