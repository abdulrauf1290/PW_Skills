#!/usr/bin/env python
# coding: utf-8
Q1: What is Matplotlib? Why is it used? Name five plots that can be plotted using the Pyplot module of
Matplotlib.--->    

Matplotlib is a popular Python library used for creating static, animated, and interactive visualizations in Python. It provides a wide range of plotting functionalities and is widely used in data analysis, scientific research, and data visualization tasks. 

Here are five plots that can be created using the Pyplot module of Matplotlib:

1)Line Plot: A line plot is a basic plot that shows a series of data points connected by straight line segments. It is commonly used to visualize the trend or relationship between two variables over a continuous range.

2)Bar Plot: A bar plot, also known as a bar chart, represents categorical data using rectangular bars. It is useful for comparing the values of different categories or displaying the distribution of a single categorical variable.

3)Histogram: A histogram is used to visualize the distribution of a continuous variable. It consists of a series of adjacent rectangular bars, where the width represents the range of values and the height represents the frequency or count of values within each range.

4)Scatter Plot: A scatter plot displays the relationship between two continuous variables. Each data point is represented as a marker on the plot, with the x-coordinate representing one variable and the y-coordinate representing the other variable. Scatter plots are useful for identifying patterns or trends in the data.Q2: What is a scatter plot? Use the following code to generate data for x and y. Using this generated data
plot a scatter plot.
import numpy as np
np.random.seed(3)
x = 3 + np.random.normal(0, 2, 50)
y = 3 + np.random.normal(0, 2, len(x))
Note: Also add title, xlabel, and ylabel to the plot.
# In[1]:


import matplotlib.pyplot as plt
import numpy as np
np.random.seed(3)
x = 3 + np.random.normal(0, 2, 50)
y = 3 + np.random.normal(0, 2, len(x))


# In[2]:


plt.scatter(x,y)
plt.xlabel("x axis")
plt.ylabel("y axis")
plt.title("This is my scatter plot")
plt.show()  

Q3: Why is the subplot() function used? Draw four line plots using the subplot() function.
Use the following data:
import numpy as np
For line 1: x = np.array([0, 1, 2, 3, 4, 5]) and y = np.array([0, 100, 200, 300, 400, 500])
For line 2: x = np.array([0, 1, 2, 3, 4, 5]) and y = np.array([50, 20, 40, 20, 60, 70])
For line 3: x = np.array([0, 1, 2, 3, 4, 5]) and y = np.array([10, 20, 30, 40, 50, 60])
For line 4: x = np.array([0, 1, 2, 3, 4, 5]) and y = np.array([200, 350, 250, 550, 450, 150])
# In[3]:


import matplotlib.pyplot as plt
import numpy as np

x = np.array([0, 1, 2, 3, 4, 5])


y1 = np.array([0, 100, 200, 300, 400, 500])
plt.subplot(2, 2, 1)
plt.plot(x, y1)
plt.title('Line 1')

y2 = np.array([50, 20, 40, 20, 60, 70])
plt.subplot(2, 2, 2)
plt.plot(x, y2)
plt.title('Line 2')


y3 = np.array([10, 20, 30, 40, 50, 60])
plt.subplot(2, 2, 3)
plt.plot(x, y3)
plt.title('Line 3')

#
y4 = np.array([200, 350, 250, 550, 450, 150])
plt.subplot(2, 2, 4)
plt.plot(x, y4)
plt.title('Line 4')

plt.tight_layout()
plt.show()

Q4: What is a bar plot? Why is it used? Using the following data plot a bar plot and a horizontal bar plot.

import numpy as np
company = np.array(["Apple", "Microsoft", "Google", "AMD"])
profit = np.array([3000, 8000, 1000, 10000])A bar plot, also known as a bar chart, is a graphical representation of categorical data using rectangular bars. Each bar represents a category, and the length or height of the bar corresponds to the quantity or frequency of that category. Bar plots are commonly used to compare different categories or display the distribution of a single categorical variable.
# In[4]:


import numpy as np
company = np.array(["Apple", "Microsoft", "Google", "AMD"])
profit = np.array([3000, 8000, 1000, 10000])

plt.bar(company,profit)
plt.show()


# In[5]:


plt.barh(company,profit)


# In[ ]:





# In[ ]:




