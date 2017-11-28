#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Mar 30 09:37:04 2017

@author: zacharynussbaum
This program takes in an exit velocity and launch angle. The program then 
uses these parameters to calculate an estimated trajectory of a batted 
baseball using Runga Kutta methods to solve the differential equations. 
This program prints and plots the trajectory in meters. 
(1 m is approx 3.28084ft)
"""
from math import pi, cos, sin, exp, sqrt
from numpy import array 
from pylab import plot, show, ylim, axis
from module import drag

theta = float(input("input a launch angle : " ))*(pi/180) #initial conditions
vinitial = float(input("input an exit velocity in mph : " ))*0.44704


m = .145 #constants of baseball and conditions
g = 9.81
circumference = .23 
area = (circumference**2)/(4*pi)
rho = 1.225 
constant = .5*area*rho/m
h = .0001
w = (1424*2*(pi/60))
B = 4.1e-4

vhorizontal = vinitial*cos(theta) #Vx component
vvertical = vinitial*sin(theta) #Vy component
def diff(x): #setting up the differential equations 
    x = r[0]
    y = r[1]
    vx = r[2]
    vy = r[3]
    phi = r[4]
    fphi = w
    fx = vx
    fy = vy 
    v = sqrt(fx**2+fy**2)
    fvx = -1*(drag(v)*fx*v) + B*w*fy*sin(phi)
    fvy = -g - (drag(v)*fy*v) - (B*w*(fy)*sin(phi))
    return array([fx,fy,fvx,fvy, fphi],float)
phi= 90*(pi/180)    
r = array([0.0,1.0,vhorizontal,vvertical, phi])

xpoints = []
ypoints = [] 

while r[1]>= 0.0: #Runga Kutta to solve for the trajectory 
    k1 = h*diff(r)
    k2 = h*diff(r+.5*k1)
    k3 = h*diff(r+0.5*k2)
    k4 = h*diff(r+k3)
    r += (k1+2*k2+2*k3+k4)/6
    xpoints.append(r[0])
    ypoints.append(r[1])
    
print("the ball traveled" ,xpoints[-1] * 3.28084, "ft" ) #printing the final x position aka trajectory
plot(xpoints,ypoints) #plotting the x and y points 
ylim(0.0)
show()


