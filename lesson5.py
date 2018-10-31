#!/usr/bin/env python
# coding: utf-8

# In[ ]:


#define a vectorel function and define it's derivative
#comment them
#drow the derivate for a point in that curve

# sint cost t vektör değerli fonk grafiğini çiziniz

#sint,cost,t
#cost,sint,1
#t=20


# In[5]:


import math
def draw_my_curve():
    theta_current = 8 * np.pi
    x_1 = math.sin(theta_current)
    y_1 = math.cos(theta_current)
    z_1 = 1
    
    x_2 = math.sin(theta_current)
    y_2 = math.cos(theta_current)
    z_2 = theta_current
    
    x_s = [x_1,x_2] 
    y_s = [y_1,y_2]
    z_s = [z_1,z_2]
    
    ax.plot(x_s,y_s,z_s)
    plt.show()


# In[6]:


import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import math

get_ipython().run_line_magic('matplotlib', 'notebook')
n = 1000
fig = plt.figure()
plt.axes(projection="3d")
ax = fig.add_subplot(111,projection="3d")

theta_max = 8 * np.pi
theta = np.linspace(0, theta_max, n)
a = 5
b = 7
z = theta
x = a*np.sin(theta)
y = b*np.cos(theta)

ax.plot(x,y,z,"b",lw=2)

theta_current = 3 * np.pi/2
x_1 = math.cos(theta_current)
y_1 = math.sin(theta_current)
z_1 = 1
    
x_2 = a*math.sin(theta_current)
y_2 = b*(-math.cos(theta_current))
z_2 = theta_current

x_3=x_1+x_2
y_3=y_1+y_2
z_3=z_1+z_2
    
x_s = [x_3,x_2] 
y_s = [y_3,y_2]
z_s = [z_3,z_2]
    
ax.plot(x_s,y_s,z_s)
plt.show()


# In[ ]:


#b 3pi/2 deki teğet doğrusunu çiziniz
#c x=6t y=3t**2 z=t olan eğrinin t=10daki teğetini çiziniz


# In[5]:


import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import math

get_ipython().run_line_magic('matplotlib', 'notebook')
n = 1000
fig = plt.figure()
plt.axes(projection="3d")
ax = fig.add_subplot(111,projection="3d")

theta_max = 8 * np.pi
theta = np.linspace(0, theta_max, n)
z = theta
x = 6*theta
y = 3*(theta*theta)

ax.plot(x,y,z,"b",lw=2)

theta_current = 3 * np.pi/2
x_1 = math.cos(theta_current)
y_1 = math.sin(theta_current)
z_1 = 1
    
x_2 = math.sin(theta_current)
y_2 = math.cos(theta_current)
z_2 = theta_current

x_3=x_1+x_2
y_3=y_1+y_2
z_3=z_1+z_2
    
x_s = [x_3,x_2] 
y_s = [y_3,y_2]
z_s = [z_3,z_2]
    
ax.plot(x_s,y_s,z_s)
plt.show()

