#!/usr/bin/env python
# coding: utf-8

# In[1]:


from mpl_toolkits import mplot3d ## imports the mplot3d toolkit


# In[3]:


get_ipython().run_line_magic('matplotlib', 'inline')
import numpy as np
import matplotlib.pyplot as plt

## imports the necessary packaged


# In[4]:


fig = plt.figure()
ax = plt.axes(projection='3d') ## First, we create the axes using this projection
### projection='3d' creates the 3d axes


# In[ ]:


## after creating the 3D axes, we can create multiple 3D plot types


# In[8]:


ax = plt.axes(projection='3d') ## we have to pass the projection='3d' toolkit
## we have to put data for the 3D line
zline = np.linspace(0, 25, 1000)
xline = np.sin(zline)
yline = np.cos(zline)
ax.plot3D(xline, yline, zline, 'gray')

## Let's put data for 3D scatter plots
zdata = 15 * np.random.random(100)
xdata = np.sin(zdata) + 0.1 * np.random.randn(100)
ydata = np.cos(zdata) + 0.1 * np.random.randn(100)
ax.scatter3D(xdata, ydata, zdata, c=zdata, cmap='Reds');


# In[10]:


def f(x, y):
    return np.sin(np.sqrt(x ** 2 + y ** 2))

x = np.linspace(-6, 6, 30)
y = np.linspace(-6, 6, 30)

X, Y = np.meshgrid(x, y)
Z = f(X, Y)


# In[11]:


fig = plt.figure()
ax = plt.axes(projection='3d')
ax.contour3D(X, Y, Z, 50, cmap='binary')
ax.set_xlabel('x')
ax.set_ylabel('y')
ax.set_zlabel('z');  ## Z data is evaluated at each point


# In[ ]:


#### View_init sets azithmuthal and evaluation angels
# Let's elevate the angle to 60 degrees
### x-y plane is elevated to 60 degrees
##### lets set the azimuth to 35 degrees
# azimuth is rotated 35 degrees counter-clockwise about z-axis 


# In[12]:


ax.view_init(60, 35)
fig


# In[13]:


#### View_init sets azithmuthal and evaluation angels
# Let's elevate the angle to 50 degrees
### x-y plane is elevated to 50 degrees
##### lets set the azimuth to 25 degrees
# azimuth is rotated 35 degrees counter-clockwise about z-axis 


# In[14]:


ax.view_init(50, 25)
fig


# In[15]:


ax.view_init(70, 15)
fig


# In[16]:


ax.view_init(10, 75)
fig


# In[18]:


#### Wireframes and surface plots
fig = plt.figure()
ax = plt.axes(projection='3d')
ax.plot_wireframe(X, Y, Z, color='red')
ax.set_title('Wireframe');


# In[19]:


ax = plt.axes(projection='3d')
ax.plot_surface(X, Y, Z, rstride=1, cstride=1,
               cmap='viridis', edgecolor='none')
ax.set_title('Surface')


# In[21]:


r = np.linspace(0, 6, 20)
theta = np.linspace(-0.9 * np.pi, 0.8 * np.pi, 40)
r, theta = np.meshgrid(r, theta)

X = r * np.sin(theta)
Y = r * np.cos(theta)
Z = f(X, Y)

ax = plt.axes(projection='3d')
ax.plot_surface(X, Y, Z, rstride=1, cstride=1,
               cmap='viridis', edgecolor='none');

# This creates a partial grid
# The surface3D plot is used to visualize


# In[25]:


##### Surface Triangulations
# triangulation is an alternative to the evenly sampled grids
# we can use the random draws instead of the polar or Cartesian grids


# In[26]:


theta = 2 * np.pi * np.random.random(1000)
r = 6 * np.random.random(1000)
x = np.ravel(r * np.sin(theta))
y = np.ravel(r * np.cos(theta))
z = f(x, y)


# In[27]:


# now we can create the scatter plots
ax = plt.axes(projection='3d')
ax.scatter(x, y, z, c=z, cmap='viridis', linewidth=0.5);


# In[28]:


# now we can triangulate the surface of the plot
ax = plt.axes(projection='3d')
ax.plot_trisurf(x, y, z,
               cmap='viridis', edgecolor='none');


# In[29]:


### visualizing a mobius trip
theta = np.linspace(0, 2 * np.pi, 30)
w = np.linspace(-0.25, 0.25, 8)
w, theta = np.meshgrid(w, theta)
## this is a 2D strip
### we need 2 intrinsic dimensions( we call them theta)
### Theta; ranges from 0 to 2pi, and w ranges from -1 to 1 across the width of the strip


# In[ ]:




