#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Oct 26 13:37:16 2020

@author: abdelgawad
"""

import numpy 
import matplotlib.pyplot as plt
#import timeit

#set the plot properties 
plt.rcParams['font.family'] = 'serif'
plt.rcParams['font.size'] = 16

# set the simulation parameters
nx =  81   # number of spatial grid points 
L = 2.0     # lenght of spatial 1D domain
dx = L/(nx-1)  # spatial grid size
nt = 25   # number of time steps 
#dt = .025   # time step size
#tf = 0.5    # final time (optional if we want to calc our sol. up to a certain time)
#dt = tf/(nt-1)  # time-step size as function of total time and the number of time steps     

#constants 
c = 1   # convection speed
sigma = 0.5 #CFL constant
dt = sigma * dx / c  # time step size calculated based on CFL constraint to assure the stability of the solution


# define the grid point coordinates
x = numpy.linspace(0,L,nx)

# Initialize data structure 
u0= numpy.ones(nx)      # gives all nx elemants in u a value of 1 as initial value 
#u0 = numpy.zeros(nx)    # will give all nx elements in u a value of zero

# Initial Conditions u = 2.0 where 0.5 <= x <= 1.0.
#u0[int(0.5/dx):int(1/dx+1)]=2 
mask = numpy.where(numpy.logical_and(x >= 0.5, x <= 1.0))
u0[mask] = 2.0
print(u0)


# Initialize the solution array
u = u0.copy()

# Boundary conditions 

u[0]=u[nx-1]=1 



#plot initial conditions
#plt.plot(x,u0)


# numerical scheme FD in time BD in space Euler`s method

# for n in range (0,nt):
#     un=u.copy()    
#     for i in range (1,nx):
#         u[i]= un[i]-c*(dt/dx)*(un[i]-un[i-1])
# plt.plot(x,u)
#print(u)


# numerical scheme Euler`s method with array slicing
for n in range (1,nt):
    u[1:]=u[1:]-c*(dt/dx)*(u[1:]-u[:-1])
    # u[0]=u[nx-1]=1 
#plt.plot(x,u)
    
#Plotting
plt.figure(figsize=(4.0,4.0))
plt.xlabel('X')
plt.ylabel('u')
plt.grid()
plt.plot(x, u0, label='initial', color = 'C0', linestyle = '--', linewidth = 2)
plt.plot(x, u, label='nt={}'.format(nt), color = 'C1', linestyle = '-', linewidth = 2)
plt.legend()
plt.xlim(0.0,L)
plt.ylim(0.0,2.5)