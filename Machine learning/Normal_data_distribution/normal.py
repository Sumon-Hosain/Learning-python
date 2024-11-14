import numpy as np
import matplotlib.pyplot as plt
var=np.random.normal(5,1,100000)
plt.hist(var,100)
plt.show()