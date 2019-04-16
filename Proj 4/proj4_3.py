# -*- coding: utf-8 -*-
"""
Created on Thu Mar 21 14:17:33 2019

PROBLEM 3. The parameter value is: beta =40 days

@author: Kommand
"""
import numpy as np
import matplotlib.pyplot as plt

def exponentialRV(beta):
    a = 300 
    b = 2000
    N = 10000
    numBatteries = 24
    
    carton = np.zeros((N,1))
    for i in range(0, N):
        t = np.random.exponential(beta, numBatteries)
        carton[i] = np.sum(t)
    
    mu_t = beta
    mu_c = numBatteries * beta
    sig_t = beta
    sig_c = beta * np.sqrt(numBatteries)
    rho_t = beta
    
    nbins=40; # Number of bins
    edgecolor='w'; # Color separating bars in the bargraph
    
    bins=[float(x) for x in np.linspace(a, b, nbins+1)]
    h1, bin_edges = np.histogram(carton,bins,density=True)
    # Define points on the horizontal axis
    be1=bin_edges[0:np.size(bin_edges)-1]
    be2=bin_edges[1:np.size(bin_edges)]
    b1=(be1+be2)/2
    barwidth=b1[1] -b1[0] # Width of bars in the bargraph
    plt.close('all')
    
    # PLOT THE BAR GRAPH
    fig1=plt.figure(1)
    plt.bar(b1,h1, width=barwidth, edgecolor=edgecolor)
    
    plt.title('PDF of lifetime of a 24 batteries carton')
    plt.xlabel('Lifetime of a 24 batteries carton')
    plt.ylabel('PDF')
    
    def gaussian(mu_x,sig_x,z):
        f = np.exp(-(z-mu_x)**2/(2 * sig_x**2))/(sig_x * np.sqrt(2*np.pi))
        return f
    f=gaussian(mu_c,sig_c,b1)
    plt.plot(b1,f,'r')

    fig2 = plt.figure(2)
    h2 = np.cumsum(h1)*barwidth
    plt.bar(b1,h2, width=barwidth, edgecolor = edgecolor)
    plt.title('CDF of lifetime of a 24 batteries carton')
    plt.xlabel('Lifetime of a 24 batteries carton')
    plt.ylabel('CDF')

if __name__ == '__main__':
    beta = 40
    exponentialRV(beta)