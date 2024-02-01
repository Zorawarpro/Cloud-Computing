import math
import numpy as np
from scipy import stats
 
# Math library example
x = 4.0
y = math.sqrt(x)
print("Square root of", x, "is", y)
 
# NumPy library example
arr = np.array([1, 2, 3, 4, 5])
mean = np.mean(arr)
print("Mean of the array is", mean)
 
# SciPy library example
data = np.array([1, 2, 3, 4, 5])
result = stats.describe(data)
print ("Descriptive statistics:", result)
