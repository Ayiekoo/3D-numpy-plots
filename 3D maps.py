#!/usr/bin/env python
# coding: utf-8

# In[1]:


### 3D plotting in Matplotlib
from mpl_toolkits import mplot3d


# In[3]:


## import the necessary packages
get_ipython().run_line_magic('matplotlib', 'inline')
import numpy as np
import matplotlib.pyplot as plt


# In[4]:


fig = plt.figure()
ax = plt.axes(projection='3d')

## passing the keyword projection='3d' gives a 3d axes


# In[11]:


ax = plt.axes(projection='3d') # pass the keyword for a 3d plot

## input the data for a 3d line
zline = np.linspace(0, 15, 1000)
xline = np.sin(zline)
yline = np.cos(zline)
ax.plot3D(xline, yline, zline, 'gray')

### input data for the 3D scattered points
zdata = 15 * np.random.random(100)
xdata = np.sin(zdata) + 0.1 * np.random.randn(100)
ydata = np.cos(zdata) + 0.1 * np.random.randn(100)
ax.scatter3D(xdata, ydata, zdata, c=zdata, cmap='Reds');


# In[12]:


ax = plt.axes(projection='3d') # pass the keyword for a 3d plot

## input the data for a 3d line
zline = np.linspace(0, 25, 1500)
xline = np.sin(zline)
yline = np.cos(zline)
ax.plot3D(xline, yline, zline, 'gray')

### input data for the 3D scattered points
zdata = 15 * np.random.random(100)
xdata = np.sin(zdata) + 0.1 * np.random.randn(100)
ydata = np.cos(zdata) + 0.1 * np.random.randn(100)
ax.scatter3D(xdata, ydata, zdata, c=zdata, cmap='Reds');


# In[13]:


ax = plt.axes(projection='3d') # pass the keyword for a 3d plot

## input the data for a 3d line
zline = np.linspace(0, 30, 2500)
xline = np.sin(zline)
yline = np.cos(zline)
ax.plot3D(xline, yline, zline, 'gray')

### input data for the 3D scattered points
zdata = 15 * np.random.random(100)
xdata = np.sin(zdata) + 0.1 * np.random.randn(100)
ydata = np.cos(zdata) + 0.1 * np.random.randn(100)
ax.scatter3D(xdata, ydata, zdata, c=zdata, cmap='Reds');


# In[14]:


### 3D contour plots
def f(x, y):
    return np.sin(np.sqrt(x ** 2 + y ** 2))

x = np.linspace(-6, 6, 30)
y = np.linspace(-6, 6, 30)

X, Y = np.meshgrid(x, y)
Z = f(X, Y)


# In[15]:


fig = plt.figure()
ax = plt.axes(projection='3d')
ax.contour3D(X, Y, Z, 50, cmap='binary')
ax.set_xlabel('x-axis')
ax.set_ylabel('y-axis')
ax.set_zlabel('z-axis')


# In[19]:


## we can pass the function "view_init" to set an elevated angle of view and azimuthan angles
ax.view_init(65, 35)
fig
## elevation angle of 65//// 60 degress above x-y plane
## azimuth angle of 35 degrees /// 35 degrees counter-clockwise about z-axis


# In[20]:


### wireframes and surface plots
fig = plt.figure()
ax = plt.axes(projection='3d')
ax.plot_wireframe(X, Y, Z, color='red')
ax.set_title('wireframe 3D plot')


# In[21]:


## we can fill each wireframe with a polygon
## we can add a color map to be filled with polygons to help perception of topology of surface being visualized
ax = plt.axes(projection='3d')
ax.plot_surface(X, Y, Z, rstride=1, cstride=1,
               cmap='viridis', edgecolor='none')
ax.set_title('Filled wireframe')


# In[22]:


## a partial polar grid
r = np.linspace(0, 6, 20)
theta = np.linspace(-0.9 * np.pi, 0.8 * np.pi, 40)
r, theta = np.meshgrid(r, theta)

X = r * np.sin(theta)
Y = r * np.cos(theta)
Z = f(X, Y)

ax = plt.axes(projection='3d')
ax.plot_surface(X, Y, Z, rstride=1, cstride=1,
               cmap='viridis', edgecolor='none')


# In[25]:


## triangulation of surfaces
theta = 2 * np.pi * np.random.random(1000)
r = 6 * np.random.random(1000)
x = np.ravel(r * np.sin(theta))
y = np.ravel(r * np.cos(theta))
z = f(x, y)


# In[26]:


## we can generate a scatter plot
ax = plt.axes(projection='3d')
ax.scatter(x, y, z, c=z, cmap='viridis', linewidth=0.5); 
## passing the code converts the polar grid to a scatter plot in the 3D plot


# In[27]:


ax= plt.axes(projection='3d')
ax.plot_trisurf(x, y, z,
               cmap='viridis', edgecolor='none')

### the function "ax.plot_trisurf" creates a surface of first finding set of a triangles between adjacent points


# In[28]:


### a mobius strip
theta = np.linspace(0, 2 * np.pi, 30)
w = np.linspace(-0.25, 0.25, 8)
w, theta = np.meshgrid(w, theta)


# In[29]:


phi = 0.5 * theta # determines the position of (x, y, z)


# In[30]:


# radius in x-y line
r = 1 + w * np.cos(phi)

x = np.ravel(r * np.cos(theta))
y = np.ravel(r * np.sin(theta))
z = np.ravel(w * np.sin(phi))

# we define the distance of r of each point from the center
# we find the embedded coordinates of the x, y, z


# In[32]:


## now we triangulate underlying parameteriazation
from matplotlib.tri import Triangulation


# In[33]:


tri = Triangulation(np.ravel(w), np.ravel(theta))

ax = plt.axes(projection='3d')
ax.plot_trisurf(x, y, z, triangles=tri.triangles,
               cmap='viridis', linewidths=0.2);

ax.set_xlim(-1, 1); ax.set_ylim(-1, 1); ax.set_zlim(-1, 1);


# In[ ]:




