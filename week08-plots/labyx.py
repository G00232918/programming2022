# a program that plots y = x2

import matplotlib .pyplot as plt
import numpy

xpoints = np.array(0,101)
ypoints = xpoints * xpoints

plt.plot(xpoints, ypoints)
plt.show()