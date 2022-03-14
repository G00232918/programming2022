# testing with matplotlib
# Author: James Connolly

import numpy as np
import matplotlib.pyplot as plt

xpoints = np.array(range(1,101))
ypoints = xpoints * xpoints 

plt.plot(xpoints, ypoints, label = "xsquared")
plt.plot(xpoints, ypoints, label ="straight", color="blue")
plt.legend()

randompoints = np.random.randint(1,1000,100)
plt.scatter(xpoints, randompoints, label = "random")

# show the plots on graph
plt.show()
# save 
# plt.savefig("test.png")