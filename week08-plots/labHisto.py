# a program that plots a histogram for salaries
# Author: James Connolly

import numpy as np
import matplotlib.pyplot as plt


minSalary = 20000
maxSalary = 80000
numberOfEntries = 10

np.random.seed(1)
salaries = np.random.randint(minSalary, maxSalary, numberOfEntries)

plt.hist(salaries)
plt.show()