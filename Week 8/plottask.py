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

plt.title("Histogram of Normal Distribution")
plt.xlabel("1000 values")
plt.ylabel("Mean 5, standard deviation 2")
plt.legend()

#show the plot  
plt.show()

# x and y axis points
xpoints = np.array(range(0,10))
ypoints = xpoints**3

#plotting the function
plt.plot(xpoints, ypoints, 'r', label = 'y = x cubed')
plt.title("Function")
plt.xlabel("0 - 10")
plt.ylabel("x cubed")
plt.legend()

#show the plot
plt.show()