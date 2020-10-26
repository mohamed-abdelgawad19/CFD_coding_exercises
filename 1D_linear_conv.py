#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Oct 26 13:37:16 2020

@author: abdelgawad
"""

import numpy 
import matplotlib.pyplot as pl
import timeit

# set the simulation parameters
# nt = 51
nx = 21
nt = 25    #nt is the number of timesteps we want to calculate
dt = .025  #dt is the amount of time each timestep covers (delta t)
tf = 0.5
xf = 2.0
# dt = tf/(nt-1)
dx = xf/(nx-1)

# Initialize data structure 
u = numpy.ones(nx)
x = numpy.linspace(0,xf,nx)

# Boundary conditions 
u[0]=u[nx-1]=1

# Initial Conditions
u[int(0.5/dx):int(1/dx+1)]=2

#plot initial conditions
pl.plot(x,u)

# nummerical scheme FD in time BD in space 

for n in range (0,nt):
    un=u.copy()    
    for i in range (1,nx):
        u[i]= un[i]-1*(dt/dx)*(un[i]-un[i-1])
    pl.plot(x,u)
#print(u)