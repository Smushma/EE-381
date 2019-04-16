# -*- coding: utf-8 -*-
"""
Created on Thu Feb 28 14:28:31 2019

@author: Kommand
"""
import numpy as np
import matplotlib
import matplotlib.pyplot as plt

#Simulation
def bernoulliTrials(n, N, c, p):
    X = np.zeros((N,1))
   
    for experiment in range(0, N):
        count = 0
        die1 = np.random.choice(c, n, p)
        die2 = np.random.choice(c, n, p)
        die3 = np.random.choice(c, n, p)
        for i in range(0, n):
            if die1[i] == 1 and die2[i] == 2 and die3[i] == 3:
                count += 1
        X[experiment] = count
    
    # Plotting
    b=range(0, 20)
    sb=np.size(b)
    h1, bin_edges=np.histogram(X, bins=b)
    b1=bin_edges[0:sb-1]
    plt.close('all')
    prob=h1/N
    plt.stem(b1,prob)
    # Graph labels
    plt.title('Bernoulli Trials: PMF - Experimental Results')
    plt.xlabel('Number of successes in n = 1000 trials')
    plt.ylabel('Probability')
    plt.xticks(b1)
    plt.show()


import numpy as np
from scipy.stats import binom
import matplotlib.pyplot as plt 

#Actual formula - Binomial Formula  
def binomial(n, pArr):
    p = pArr[0] * pArr[1] * pArr[2]
    k = np.arange(0,20)
    y = binom.pmf(k, n, p) #Binomial formula
    
    #Graphing
    plt.stem(k, y)
    plt.title('Bernoulli Trials: PMF – Binomial Formula')
    plt.xlabel('Number of successes')
    plt.ylabel('Probability')
    plt.xticks(np.arange(min(k),max(k)+1, 1.0)) #Fix x-axis scale
    plt.show()

import numpy as np
import scipy.stats as ss
import matplotlib.pyplot as plt 

#Approximation to Binomial - Poisson Formula
def poisson(n, p): 
    lambd = n * p[0] * p[1] * p[2] #Lambda
    x = np.arange(0,20)
    y = ss.poisson.pmf(x, lambd) #Poisson formula
    
    #Graphing
    plt.stem(x, y)
    plt.title('Bernoulli Trials: PMF – Poisson Approximation')
    plt.xlabel('Number of Successes')
    plt.ylabel('Probability')
    plt.xticks(np.arange(min(x),max(x)+1, 1.0)) #Fix x-axis scale
    plt.show()
    
if __name__ == '__main__':
    #The probability vector for the multi-sided dice is:  p=[0.2,  0.1,  0.15, 0.3, 0.2, 0.05]
    n = 1000 #Num of times to roll 3 dice
    N = 10000 #Num of experiments
    c = [1, 2, 3, 4, 5, 6]
    p = [0.2, 0.1, 0.15, 0.3, 0.2, 0.05]
    
    bernoulliTrials(n, N, c, p)
    binomial(n, p)
    poisson(n, p)
    