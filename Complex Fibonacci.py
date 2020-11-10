# -*- coding: utf-8 -*-
"""
Created on Fri Jul  3 15:26:53 2020

@author: thiag
"""

import cmath
import numpy as np
import matplotlib.pyplot as plt
from sympy import sieve

x = np.linspace(0,4,200)

# Use sieve.primerange() method  
prime_gen = sieve.primerange(1, 10000)  
prime_list = list(prime_gen)

#prime_list = [k*2 for k in range(0,7)]
x = []
leg = []
u = 0
for p in prime_list:
    for p1 in prime_list:
        x.append(complex(p,p1))
        leg.append("(" + str(p) + "," + str(p1) + ") at index: " + str(u))
        u = u+1
    
x = [complex(cmath.log(p),p) for p in prime_list]

#Lei de Bernaut
#O n-Ésimo termo de fibonnaci é definido como
def nTermFibonnaci(n):
   PHI = 1.61803398875
   return (cmath.exp(n*cmath.log(PHI)) - cmath.exp(n*cmath.log(-1/PHI)))/cmath.sqrt(5)

z = []
for pt in x:
    fpt = nTermFibonnaci(pt)
    z.append(fpt)
    r, phi = cmath.polar(fpt)

x_r = []
y_i = []
y_leg = []
for i in z:
    x_r.append(i.real)
    y_i.append(i.imag)
    y_leg.append(i.imag)
    
#%%

def plotScatterwithLabel(x,y,leg = [], title="Fib", xlabel = "Real", ylabel="Imz"):    
    fig, ax1 = plt.subplots(figsize=(14,6))
    plt.xticks(rotation=0)
    plt.title(title)
    color = 'tab:red'
    ax1.set_xlabel(xlabel)
    ax1.set_ylabel(ylabel, color=color)
    ax1.scatter(x, y, color='g')
    
    if(len(leg)>0):
        for l,k in enumerate(leg):
            ax1.text(x_r[l] - 0.15,y_leg[l] - 0.4,k)
    
    ax1.tick_params(axis='y', labelcolor=color)
    
    fig.tight_layout()  # otherwise the right y-label is slightly clipped
    plt.show()
    plt.close()
#%%
    plotScatterwithLabel(x_r,y_i)

#%%

dist = []
def distanceEuclidean(z1,z2):
    r1 = z1.real
    i1 = z1.imag
    r2 = z2.real
    i2 = z2.imag
    d = cmath.sqrt((r1-r2)**2+(i1-i2)**2)
    return d.real

#%%
    x_plot = [k.real for k in x]
    y_plot = [k.imag for k in x]
    plotScatterwithLabel(x_plot,y_plot)
    
#%%
dist = []
for elem in prime_list:
    index_list = []
    for index,el in enumerate(x):
        if (el.imag == elem):
            index_list.append(index)
            
    print('------ Imprimindo ----> {0}'.format(elem))
    print(index_list)
    for k,i in enumerate(index_list):
        if(k < len(index_list) - 1):
            print('Calculando a distancia entre {0} e {1}'.format(leg[index_list[k]],leg[index_list[k+1]]))
            print(distanceEuclidean(z[index_list[k]],z[index_list[k+1]]))
            dist.append(distanceEuclidean(z[index_list[k]],z[index_list[k+1]]))
    break
#%%
    
for k,d in enumerate(dist):
    if(k < len(dist) - 1):
        print(dist[k+1]/dist[k])

    
       
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    