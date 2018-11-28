#!/usr/bin/env python
# coding: utf-8

# In[9]:


import numpy as np
from mpl_toolkits.mplot3d import Axes3D
import matplotlib.pyplot as plt


# In[22]:


a = 5
b = 3
# plot elipce
x = np.linspace(-5.0,5.0, num=5000)
y=(b**2*(1-(x**2)/(a**2)))**.5
plt.plot(x,y)
plt.plot(x,-y)


# In[ ]:




