# -*- coding: utf-8 -*-
"""
Created on Thu Mar 14 13:53:51 2019

PROBLEM 1. The parameter values are    (P1a).   a=1.0 ;  b=4.0  ; (P1b).   beta =40 ;   (P1c).   mu=2.5  ;  sigma= 0.75

@author: Kommand
"""
import numpy as np
import matplotlib.pyplot as plt
#1.1
def uniRV(a, b, n):
    X = np.random.uniform(a, b, n)
    
    # Create bins and histogram
    nbins = 30; # Number of bins
    edgecolor = 'w'; # Color separating bars in the bargraph
    bins = [float(X) for X in np.linspace(a, b, nbins+1)]
    h1, bin_edges = np.histogram(X, bins, density=True)
    
    # Define points on the horizontal axis
    be1 = bin_edges[0:np.size(bin_edges)-1]
    be2 = bin_edges[1:np.size(bin_edges)]
    b1 = (be1+be2)/2
    barwidth = b1[1]-b1[0] # Width of bars in the bargraph
    plt.close('all')
    
    # PLOT THE BAR GRAPH
    fig1 = plt.figure(1)
    plt.bar(b1, h1, width=barwidth, edgecolor=edgecolor)
    plt.title('Experimental Values of Uniform R.V. "X"') #PROPER LABELS
    plt.xlabel('X')
    plt.ylabel('PDF') 
    
    #PLOT THE UNIFORM PDF
    def unifPDF(a, b, X):
        f = (1/abs(b-a))*np.ones(np.size(X))
        return f
    
    f = unifPDF(a, b, b1)
    plt.plot(b1, f, 'r')
    
    #CALCULATE THE MEAN AND STANDARD DEVIATION
    mu_x = np.mean(X)
    sig_x = np.std(X)
    
    print('Mean:', mu_x)
    print('Standard deviation:', sig_x)

import numpy as np
import matplotlib.pyplot as plt
#1.2
def expRV(beta, n):
    T = np.random.exponential(beta, n)
    
    # Create bins and histogram
    nbins = 30; # Number of bins
    edgecolor = 'w'; # Color separating bars in the bargraph
    bins = [float(T) for T in np.linspace(0, 220, nbins+1)]
    h1, bin_edges = np.histogram(T, bins, density=True)
    
    # Define points on the horizontal axis
    be1 = bin_edges[0:np.size(bin_edges)-1]
    be2 = bin_edges[1:np.size(bin_edges)]
    b1 = (be1+be2)/2
    barwidth = b1[1]-b1[0] # Width of bars in the bargraph
    plt.close('all')
    
    # PLOT THE BAR GRAPH
    fig1 = plt.figure(1)
    plt.bar(b1, h1, width=barwidth, edgecolor=edgecolor)
    plt.title('Experimental Values of Exponential R.V. "T"') #PROPER LABELS
    plt.xlabel('T')
    plt.ylabel('PDF') 
    
    #PLOT THE UNIFORM PDF
    def expPDF(beta, T):
        f = ((1/beta)*np.exp(-(1/beta)*T))*np.ones(np.size(T))
        return f
    
    f = expPDF(beta, b1)
    plt.plot(b1, f, 'r')
    
    #CALCULATE THE MEAN AND STANDARD DEVIATION
    mu_t = np.mean(T)
    sig_t = np.std(T)
    
    print('Mean:', mu_t)
    print('Standard deviation:', sig_t)

import numpy as np
import matplotlib.pyplot as plt
import math
#1.3
def normRV(mu, sigma, n):
    X = np.random.normal(mu, sigma, n)
    
    # Create bins and histogram
    nbins = 50; # Number of bins
    edgecolor = 'w'; # Color separating bars in the bargraph
    bins = [float(X) for X in np.linspace(0, 5, nbins+1)]
    h1, bin_edges = np.histogram(X, bins, density=True)
    
    # Define points on the horizontal axis
    be1 = bin_edges[0:np.size(bin_edges)-1]
    be2 = bin_edges[1:np.size(bin_edges)]
    b1 = (be1+be2)/2
    barwidth = b1[1]-b1[0] # Width of bars in the bargraph
    plt.close('all')
    
    # PLOT THE BAR GRAPH
    fig1 = plt.figure(1)
    plt.bar(b1, h1, width=barwidth, edgecolor=edgecolor)
    plt.title('Experimental Values of Normal R.V. "X"') #PROPER LABELS
    plt.xlabel('X')
    plt.ylabel('PDF') 
    
    #PLOT THE UNIFORM PDF
    def unifPDF(mu, sigma, X):
        f = ( 1/(sigma*math.sqrt(2*math.pi) ) )*np.exp( -( (X-mu)**2)/(2*(sigma)**2) )*np.ones(np.size(X) )
        return f
    
    f = unifPDF(mu, sigma, b1)
    plt.plot(b1, f, 'r')
    
    #CALCULATE THE MEAN AND STANDARD DEVIATION
    mu_x = np.mean(X)
    sig_x = np.std(X)
    
    print('Mean:', mu_x)
    print('Standard deviation:', sig_x)
    
if __name__ == '__main__':
    a = 1.0
    b = 4.0
    n = 10000
    beta = 40
    mu = 2.5
    sigma = 0.75
    
    #uniRV(a, b, n)
    #expRV(beta, n)
    normRV(mu, sigma, n)