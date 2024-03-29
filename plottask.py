# Author : Michael Allen
# Plotting a function and histogram

# import numpy and matplotlib modules
import numpy as np
import matplotlib.pyplot as plt

font_for_histogram = {'family': 'cambria',
        'color':  'darkblue',
        'weight': 'normal',
        'size': 18,
        }

font_for_plot = {'family': 'calibri',
        'color':  'darkred',
        'weight': 'bold',
        'size': 20,
        }
  
# Generating random data with 1000 values, mean of 5 and standard deviation of 2 
# normal distribution
data = np.random.normal(5, 2, 1000)
  
# Plotting the histogram.
#plt.style.use("seaborn-darkgrid")
plt.style.use("dark_background")
#https://stackoverflow.com/questions/25451294/best-way-to-display-seaborn-matplotlib-plots-with-a-dark-ipython-notebook-profil
plt.hist(data, bins=25, density=True, alpha=0.6, color='b')
#https://matplotlib.org/stable/gallery/text_labels_and_annotations/text_fontdict.html
plt.title("Normal Distribution", color='blue', fontdict=font_for_histogram)
plt.xlabel("Mean 5, St Dev 2", color='blue', fontdict=font_for_histogram)
plt.ylabel("1000 Random values", color='blue', fontdict=font_for_histogram)

plt.legend()
plt.savefig('histogram.png')
#show the plot  
plt.show()

# x and y axis points
xpoints = np.array(range(0,10))
ypoints = xpoints**3

#plotting the function
plt.style.use("seaborn-darkgrid")
plt.plot(xpoints, ypoints, 'r', label = 'h(x)=x3')
plt.title("Function h(x)=x3", color='red', fontdict=font_for_plot)
plt.xlabel("x = 0 - 10", color='red', fontdict=font_for_plot)
plt.ylabel("y = x-cubed", color='red', fontdict=font_for_plot)
plt.legend()

#show the plot
plt.savefig('function_plot.png')
plt.show()