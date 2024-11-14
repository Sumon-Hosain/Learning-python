import numpy as np
import matplotlib.pyplot as plt
var=np.random.uniform(1,11,11)
print(var)
plt.hist(var,4)
plt.show()