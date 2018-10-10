#!/usr/bin/env python
# coding: utf-8

# In[5]:


import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D


# In[6]:


point1 = np.array([0,0,0])
normal1 = np.array([1,-2,1])

point2 = np.array([0,-4,0])
normal2 = np.array([0,2,-8])

point3 = np.array([0,0,1])
normal3 = np.array([-4,5,9])


# In[7]:


d1 = -np.sum(point1*normal1)
xx,yy = np.meshgrid(range(5),range(5))


# In[8]:


z1 = (-normal1[0]*xx - normal1[1]*yy - d1)*1./normal1[2]
get_ipython().run_line_magic('matplotlib', 'inline')
plt3d = plt.figure().gca(projection="3d")
plt3d.plot_surface(xx,yy,z1,color="blue")


# In[9]:



fig = plt.figure()
ax = fig.add_subplot(111,projection="3d")

n = 1000
theta_max = 8 * np.pi
theta = np.linspace(0, theta_max, n)
z = theta
x =  np.sin(theta)
y =  np.cos(theta)
ax.plot(x, y, z, 'b', lw=2)


# In[ ]:




