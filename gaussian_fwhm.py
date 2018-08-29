# -*- coding: utf-8 -*-
"""
Created on Wed Aug 29 11:32:29 2018

@author: semyanov
"""

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

file_name = 'C:/Users/semyanov/Desktop/gaussian_fwhm.txt'

N=1000
x = np.linspace(-10, 10, N)

"""
reference: 
https://www.originlab.com/doc/Origin-Help/Gaussian-Function-FitFunc
Meanings: 
y0 = base
xc = center
A = area
w = FWHM
"""
def gaussian_fwhm(y0, xc, A, w, x):
    C=4*np.log(2)
    pi=np.pi
    y = y0 + (A*np.exp((-C*(x-xc)**2)/(w*w))/(w*np.sqrt(pi/C)))
    return y

y=gaussian_fwhm(0.0, 0, 1.0, 2.0, x)

plt.figure(1)
plt.plot(x[0:N-1], y[0:N-1], 'g-', linewidth= 1.0)
plt.show()

data = np.stack((x, y), axis=-1)
df = pd.DataFrame({'Column1':data[:,0],'Column2':data[:,1]})
df.to_csv(file_name, sep='\t')