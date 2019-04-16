# -*- coding: utf-8 -*-
"""
Created on Wed Mar 20 17:52:57 2019

PROBLEM 2. The parameter values are:   a=1.0   cm;  b=4.0 cm

@author: Kommand
"""

import numpy as np
import matplotlib.pyplot as plt
import math as m

def centralLimit(a, b, n):
    X = [None] * 10000
    for i in range(0, 10000):
        w = np.random.uniform(a, b, n)
        X[i] = np.sum(w)
        
    #Calculations
    rho_w = m.sqrt(((b-a)**2) / 12)
    print("rho_w:", rho_w)
    
    rho_s = rho_w*m.sqrt(n)
    print("rho_s:", rho_s)
    
    mu_w = (a+b)/2
    print('mu_w:', mu_w)
    
    mu_s = n*mu_w
    print('mu_s:', mu_s)
    
    mu_x=np.mean(X)
    sig_x=np.std(X)
    
    print('mean:', mu_x)
    print('std:', sig_x)
    
    # Create bins and histogram
    nbins = 30  # Number of bins
    edgecolor = 'w' # Color separating bars in the bargraph
    bins = [float (x) for x in np.linspace(n*a,n*b,nbins+1)]
    h1, bin_edges = np.histogram(X,bins,density=True)
    
    be1 = bin_edges[0:np.size(bin_edges)-1]
    be2 = bin_edges[1:np.size(bin_edges)]
    b1 = (be1+be2)/2
    barwidth = b1[1]-b1[0] # Width of bars in the bargraph
    plt.close('all')
    
    # PLOT THE BAR GRAPH
    fig1 = plt.figure(1)
    plt.bar(b1,h1, width=barwidth, edgecolor = edgecolor)
    label = 'Book stack height for n = %d' % n
    plt.title('PDF of %d book stack height and comparison with Gaussian' % n)
    plt.xlabel(label)
    plt.ylabel('PDF')    
    
    def gaussian(mu,sig,z):
        f=np.exp(-(z-mu_x)**2/(2*sig_x**2))/(sig_x*np.sqrt(2*np.pi))
        return f
    f=gaussian(mu_x*n, sig_x*np.sqrt(n),b1)
    plt.plot(b1,f,'r')
    
if __name__ == '__main__':  
    a = 1
    b = 4
    #centralLimit(a, b, 1)
    #centralLimit(a, b, 2)
    #centralLimit(a, b, 5)
    #centralLimit(a, b, 10)
    centralLimit(a, b, 15)
