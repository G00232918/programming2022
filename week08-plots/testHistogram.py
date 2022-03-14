# testing Histograms
# Author: James Connolly

import numpy as np
import matplotlib.pyplot as plt

# use for debugging as data stays the same
# np.random.seed(1)
normData = np.random.normal(size=10000)

plt.hist(normData)
plt.show()