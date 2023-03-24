# Author : Michael Allen
# Plotting a function and histogram

# import numpy and matplotlib modules
import numpy as np
import matplotlib.pyplot as plt
  
# Generating random data with 1000 values, mean of 5 and standard deviation of 2 
# normal distribution
data = np.random.normal(5, 2, 1000)
  
# Plotting the histogram.
plt.hist(data, bins=25, density=True, alpha=0.6, color='b')

#show the plot  
plt.show()

# x and y axis points
xpoints = np.array(range(0,10))
ypoints = xpoints**3

#plotting the function
plt.plot(xpoints,ypoints, 'r')

#show the plot
plt.show()