# -*- coding: utf-8 -*-
"""
@author Kevin Long
@version Spring 2019
"""
import numpy as np
import matplotlib
import matplotlib.pyplot as plt

def nSidedDie(p):
	"""
	1)
	Function that simulates a single roll of a n-sided die. 
	Inputs: The probabilities for each side, given as a vector p = [p_1,p_2,...p_n]
	Outputs:The number on the face of the die after a single roll, 
	i.e. one number from the set of integers {1,2,...n}
	Note: The sum of p must be equal to 1.0, otherwise the probability values
	are incorrect.
	"""
    n = len(p) #Number of elements in 'p'
    
    pSum = 0
    for k in range(n):
        pSum += p[k]
        
    if pSum > 1.0: #Checking for correct probability total
        print("Cumulative sum of p cannot be greater than 1.0")
    else:
        N = 10000 #Number of tests
        
        sampleSpace = np.zeros((N,1)) #Return a new array of given shape and type, filled with zeros.
        cs = np.cumsum(p) #Return the cumulative sum of the elements along a given axis.
        cp = np.append(0, cs) #Append values to the end of an array.
        
        for i in range(0, N): #For every iteration in N
            r = np.random.rand()
            for j in range(0, n): #count how frequent that number 'n' is rolled
                if r > cp[j] and r <= cp[j+1]:
                    d = j + 1
            sampleSpace[i] = d
        
        # Plotting
        b=range(1,n+2)
        sb=np.size(b)
        h1, bin_edges=np.histogram(sampleSpace, bins=b)
        b1=bin_edges[0:sb-1]
        plt.close('all')
        prob=h1/N
        plt.stem(b1,prob)
        # Graph labels
        plt.title('PMF for an unfair n-sided die')
        plt.xlabel('Number on the face of the die')
        plt.ylabel('Probability')
        plt.xticks(b1)
        plt.show()
        
        return d

def numDiceRollsNeeded():
	"""
	2)
	Number of rolls needed to get a "7" with two dice
	Input: None
	Output: None
	"""
    N = 100000 #Number of tests
    
    timesRolled = 0 
    timesGotSeven = 0
    timesGotArr = [None] * N
    
    for i in range(0, N): #For each experiment
        test = True 
        while test: #Conduct the test until a 7 is rolled
            timesRolled += 1
            d1 = np.random.randint(1,7) #Dice 1
            d2 = np.random.randint(1,7) #Dice 2
            dSum = d1 + d2
            if dSum == 7:
                timesGotSeven += 1
                timesGotArr[i] = timesRolled
                timesRolled = 0
                test = False #Exit test
    
    b=range(1,30) 
    sb=np.size(b)
    h1, bin_edges = np.histogram(timesGotArr,bins=b)
    b1=bin_edges[0: sb-1]
    plt.close('all')
    
    fig1=plt.figure(1)
    plt.stem(b1,h1)
    plt.title('Stem plot - Sum of two dice equal to 7')
    plt.xlabel('Number of Rolls Needed for 7')
    plt.ylabel('Number of occurrences')
     
    fig2=plt.figure(2)
    p1=h1/N
    plt.stem(b1,p1)
    plt.title('Stem plot - Sum of two dice equal to 7: Probability mass function')
    plt.xlabel('Number of Rolls Needed for 7')
    plt.ylabel('Probability')

def fiftyHeadsPercent():
	"""
	3)
	Calculates the probability of success of getting exactly 50 heads after
	tossing 100 coins 100,000 times.
	Input: None
	Output: The probability of success of getting exactly 50 heads
	"""
    heads = 0 #Counter for heads
    n = 100 #Number of coins
    N = 100000 #Number of tests
    
    numSuccessfulTests = 0
    for i in range(0, N):
        coin = np.random.randint(0,2,n) #Tossing 100 coins
        heads = sum(coin)
        if heads == 50:
            numSuccessfulTests += 1
    
    return numSuccessfulTests/N


import random
import string

def pwGen():
	"""
	Input: None
	Output: None 
	Function calculates the probability of guessing the correct password in a 
	randomly generated password list of 4 lowercase English characters.
	The print statements are for the probability of 'm' words, 'k*m' words, and
	number of words needed to achieve a p = 0.5 
	"""
    return ''.join(random.choice(string.ascii_lowercase) for x in range(4))

def passwordHacking(k, m):
	"""
	4)
	Input: k, m integers
	Output: probability of hacking password
	Function calculates the probability of guessing the correct password in a 
	randomly generated password list of 4 lowercase English characters.
	The print statements are for the probability of 'm' words, 'k*m' words.
	"""
    n = 26**4
    N = 1000
    
    #m or k*m
    count = 0
    pwList = list() #Generate a list to store passwords
    for i in range(0, k*m): #Fills list with 'k*m' 4char pw's with function pwGen()
        pwList.append(pwGen())
    for j in range(0, N): #Check the list to see if our guessed pw is in the list
        hackPw = pwGen()
        if hackPw in pwList:
            count += 1 #Increment if found
    result = count/N
    return result

def probPwHack():
	"""
	Input: None
	Output: None
	Prints out vital information about the probability of the password
	hacking experiment. Also prints out the words needed to achieve
	p = 0.5 in a list of 'm' passwords.
	"""
    k = 7
    m = 80000
    
    result1 = passwordHacking(1, m)
    print("Probability for m words:", result1)
    
    result2 =passwordHacking(k, m)
    print("Probability for k*m words:", result2)
    
    while not (result1 > 0.49 and result1 < 0.51):
        if result1 < 0.5:
            m += 10000
            result1 = passwordHacking(1, m)
        elif result1 > 0.5:
            m -= 10000
            result1 = passwordHacking(1, m)
    print("Words needed for p = 0.50:", m)   
    
if __name__ == "__main__":  
    #1
    #p = np.array([0.10, 0.15, 0.20, 0.05, 0.30, 0.10, 0.10])
    #print("You rolled: " + str(nSidedDie(p)))
    
    #p2 = np.array([0.10, 0.15, 0.20, 0.05, 0.30, 0.10, 0.20])
    #print("You rolled: " + str(nSidedDie(p2)))
    #print("-----")
    
    #2
    #numDiceRollsNeeded()
    
    #3
    #print("Probability of getting exactly 50 heads:", fiftyHeadsPercent())
    
    #4
    probPwHack()