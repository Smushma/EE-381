# -*- coding: utf-8 -*-
"""
Created on Thu Feb 14 14:08:29 2019

@author: Kommand
"""
import numpy as np

p0, e0, e1 = 0.6, 0.05, 0.03

def nSidedDie(p):
    """
    1)
    """
    n = len(p) #Number of elements in 'p'
    
    pSum = 0
    for k in range(n):
        pSum += p[k]
        
    if pSum > 1.0: #Checking for correct probability total
        print("Cumulative sum of p cannot be greater than 1.0")
    else:
        N = 1 #Number of rolls
        
        sampleSpace = np.zeros((N,1)) #Return a new array of given shape and type, filled with zeros.
        cs = np.cumsum(p) #Return the cumulative sum of the elements along a given axis.
        cp = np.append(0, cs) #Append values to the end of an array.
        
        for i in range(0, N): #For every iteration in N
            r = np.random.rand()
            for j in range(0, n): #count how frequent that number 'n' is rolled
                if r > cp[j] and r <= cp[j+1]:
                    d = j + 1
            sampleSpace[i] = d
    return d

def problem1(p0, e0, e1):
    N = 100000 #Num of trials
    
    error = 0
    for i in range(0, N):
        S = nSidedDie([p0, 1 - p0]) #Message genration
        S -= 1

        if S == 1: #Transmitting message simulation
            R = nSidedDie([e1, 1 - e1])
            R -= 1

        elif S == 0:
            R = nSidedDie([1 - e0, e0])
            R -= 1
        
        if R != S: #Checking if bits are correct
            error += 1
        
    print("Probability of transmission error:", error / N)
    
problem1(p0, e0, e1)

def problem2(p0, e0, e1):
    """
    2)
    """
    N = 100000 #Num of trials
    
    sent = 0
    received = 0
    r = 0
    for i in range(0, N):
        s = nSidedDie([p0, 1 - p0])
        s -= 1
        
        if s == 1:
            sent += 1
            r = nSidedDie([e1, 1 - e1])
            r -= 1
            
            if r == 1:
                received += 1
        else:
            r = nSidedDie([1 - e0, e0])
            r -= 1
    
    print()    
    print("Focus on S=1, P(R=1|S=1):", received/sent)
    
problem2(p0, e0, e1)

def problem3(p0, e0, e1):
    """
    3)
    """
    N = 100000 #Num of trials
    
    sent = 0
    received = 0
    r = 0
    for i in range(0, N):
        s = nSidedDie([p0, 1 - p0])
        s -= 1
        
        if s == 1:
            r = nSidedDie([e1, 1 - e1])
            r -= 1
        else:
            r = nSidedDie([1 - e0, e0])
            r -= 1
        if r == 1:
            received += 1
            if s == 1:
                sent += 1
    print()
    print("Focus on R=1, P(S=1|R=1):", sent/received)
    
problem3(p0, e0, e1)

def problem4(p0, e0, e1):
    """
    4)
    """
    N = 100000 #Num of trials
    
    count = 0
    decode = -1
    rSum = 0
    sList = []
    rList = []
    for i in range(0, N):
        s = nSidedDie([p0, 1 - p0])
        s -= 1
       
        sList = [s, s, s]
        if 1 in sList:
            rList = [nSidedDie([e1, 1 - e1]) - 1, nSidedDie([e1, 1 - e1]) - 1, nSidedDie([e1, 1 - e1]) - 1]
        if 0 in sList:
            rList = [nSidedDie([1 - e0, e0]) - 1, nSidedDie([1 - e0, e0]) - 1, nSidedDie([1 - e0, e0]) - 1]
        rSum = np.sum(rList)
        if rSum >= 2:
            decode = 1
        else:
            decode = 0
        if decode != s:
            count+=1
                
    print()
    print("Probability of error with enhanced transmission: ", count/N)

problem4(p0, e0, e1)
