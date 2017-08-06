"""
Created on Sun Jul 23 23:08:19 2017
@author: Dee
"""

#import pandas as pd
import numpy as np
#import math as math
#import matplotlib as mpl
import matplotlib.pyplot as plt

# 1 D Kinematics Solver Equation to solve for distance knowing time, accel, initial vel.

print('This is a one dimensional kinematics solver.')
print('This assumes we know acceleration, initial velocity, and' )
print('      the distance or time.')
known = input('What is known, distance (d) or time (t)? ')
known = str(known)
if known == 't':
    t = float(input('What is the time (seconds)? ')) 
    a = str(input('Is this freefall problem? yes or no: ' ))
    if a == 'yes':
         print('This is a freefall problem. Acceleration = 9.8 m/s^2')
         accel = 9.8  #m/s^2
    if a == 'no':
         accel = float(input ('What is the acceleration? '))
    v0 = float(input('What is the objects initial velocity (m/s)? '))

    d = round(v0* t + 0.5 * accel* t**2, 2)
    print ('Distance traveled is:', d, ' m')
    vf = (v0**2 + (2.0 * accel*d))**0.5
    vfround = round(vf,2)
    print ('Final velocity = ', vfround, 'm/s')


if known =='d':
    d = float(input('What is the distance? '))
    a = str(input('Is this freefall problem? yes or no: ' ))
    if a == 'yes':
         print('This is a freefall problem. Acceleration = 9.8 m/s^2')
         accel = 9.8  #m/s^2
    if a == 'no':
         accel = float(input ('What is the acceleration? '))
    v0 = float(input('What is the objects initial velocity (m/s)? '))
    polya = accel/2   
    polyb = v0
    polyc = -d 
    p = [polya, polyb, polyc]
    #print (np.roots(p))
    array = np.roots(p)
    if array[1] <0:
        ans = round(array[0], 2)
    if array[0] <0:
        ans = round(array[1], 2)
    print('time = ', ans, ' sec')
    vf = round((v0**2 + (2.0 * accel*d))**0.5, 2)
    print ('Final velocity = ', vf, 'm/s', fontsize=20)

if known =='d':
    t = ans

print('Do you want a graph of distance and velocity vs time? ')
graph = input('Type yes or no: ')
graph = str(graph)

#graph = str(input('Would you like to graph this motion vs time? y or n: '))
# graph results as a function of time:    
if graph == 'yes':
    distdata = True
    n = 0
    distg = []
    velg = []
    timeg = []
    while distdata == True:
        t1 = float(n/2)
        velg.append(v0 + accel*t1)
        distg.append ((v0*t1+(accel/2)*t1**2))
        timeg.append (t1)
        n = n+1
        if n >= (2*t+1):
            distdata = False

    maxd = round((distg[(n-1)])+4.999, -1)  # roundUP to nearest 10
    maxv = round((velg[(n-1)])+4.999, -1)
    print (timeg)
    print (velg)
  # graph distance vs time  
    plt.figure(figsize = (15,10))
    plt.title('Distance vs Time', fontsize=30)
    plt.tick_params(labelsize=20)
    plt.axes().get_xaxis().set_visible(True)
    plt.axes().get_yaxis().set_visible(True)
    plt.axis([0,(n/2),0,maxd])
    plt.grid()
    plt.ylabel('Distance, m', fontsize = 20)
    plt.xlabel(' Time, sec ', fontsize = 20)
    #plt.scatter(t, somedata, edgecolor='green', s=70)

    plt.plot(timeg, distg)
    plt.show()
 # graph velocity vs time   
    plt.figure(figsize = (15,10))
    plt.title('Velocity vs Time', fontsize=30)
    plt.tick_params(labelsize=20)
    plt.axes().get_xaxis().set_visible(True)
    plt.axes().get_yaxis().set_visible(True)
    plt.axis([0,(n/2),0,maxv])
    plt.grid()
    plt.ylabel('Velocity, m/s', fontsize = 20)
    plt.xlabel(' Time, sec ', fontsize = 20)
    
    plt.plot(timeg, velg)
    plt.show()