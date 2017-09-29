# -*- coding: utf-8 -*-
#!/usr/bin/python
# Author: Niam Moltta
# UY - 2017
# MIT License
# Measures of Central Tendency with Python

import math
import numpy as np
import pandas as pd
from scipy import stats
from scipy.stats import norm
import scipy.stats as st
import matplotlib.pyplot as plt
import re
import seaborn
import scipy.stats

print(' ')
print(' ')
print('                Welcome to MoCT.py')
print('                --by Niam Moltta--')
print ('                    ~~/\//V\ ')
print(' ')
print(' ')
print("Application: MEASURES OF CENTRAL TENDENCY.\n\nINSTRUCTIONS:\n\n- Make sure that the .csv file is in the same folder of this script.\n- To start, enter the name of the file without 'quotes' and ending with .csv\n  Example: scores.csv\n- Enter 'ya' to analyze more columns or quit.\n- Returns measures of central tendency:\n  N, mean, standard deviation, variance, standard error, etc...\n- Returns Normal Distribution graph.\n- Select sample, select point estimate for sampling distribution.\n- Returns z-score and p-value from z-table.\n- Returns Sampling Distribution graph.\n- Returns One tailed T-test: default alpha = 0.05\n- Returns acceptance/rejection of the null hypothesis.\n")

fhand = raw_input('Enter file name: ')

filecsv = str(fhand)

if filecsv == '':
    print(' ')
    print ('Ciao, human!')
    print(' ')
    exit()
    
data = pd.read_csv(filecsv)

print ' '

frame = pd.DataFrame(data)

coolist = frame.columns
columns = np.asarray(coolist)

while True:

    print ' '
    print 'Columns in', re.findall('(.+?).csv', filecsv), 'are:\n'
    print columns
    print ' '
    
    hand = raw_input('Enter column header:\n\n')

    column = str(hand)

    if (column == 'ya') | (column == ''):
        print ' '
        print 'Hasta la vista, human.'
        print ' '
        exit()
    
    else:
        
        numbers = data[column]

        data[column].fillna(0,inplace=True) # Missing values to zeros.
            
        A = list()
        
        for number in numbers :
            value = float(number)
            A.append(value)

        sigma = sum(A) #sumation
        n = len(A) #total of elements
        mean = sigma / n
        Dev = list()
        AbsDev = list()
        SqDev = list()
        
        for number in A :
            val = number - mean
            Dev.append(val) #Deviation from the mean
            
        for element in Dev :
            val = abs(element)
            AbsDev.append(val) # Absolute Deviation
            
        for element in AbsDev :
            val = (element**2)
            SqDev.append(val) #Square Deviations

        SS = sum(SqDev) #Sum of Squares
        Var = SS / n #Variance
        StdDev = math.sqrt(Var) #Standard Deviation
        StdE = StdDev / math.sqrt(n) #Standard Error

        print ('---------------------------------------------')
        print ('MEASURES OF CENTRAL TENDENCY for:'), column
        print (' ')
        print ('N ='), n
        print ('Mean ='), mean
        print ('Sum of Squares ='), SS
        print ('Variance ='), Var
        print ('Standard Deviation ='), StdDev
        print ('Standard Error ='), StdE 
        print ('---------------------------------------------')
        print(' ')
        
        Array = np.asarray(A)
        lista = Array.sort()
        legend = str(column) + ' distribution'

        Mean = np.mean(Array)
        Variance = np.var(Array)
        Sigma = np.sqrt(Variance)

        plt.figure(1)
        plt.hist(Array, bins=20, normed=True)
        plt.xlim((min(Array), max(Array)))

        x = np.linspace(min(Array), max(Array), n)
        fig = plt.plot(x, mlab.normpdf(x,Mean,Sigma))

        plt.title(legend)
        plt.xlabel("Value")
        plt.ylabel("Frequency")
        plt.show(fig)

        print ('To continue, you must save the figure and close it. \nYou can also zoom in it or move the graph to see it better, \nuse the buttons.\n')
        print ' '

    while True:
        
        sample = raw_input('Enter n value for sample distribution: ')
        fh = str(sample)
        
        if fh[0] == '#':
            continue
        
        if (fh == 'ya') | (fh == ''):
            print  ' '
            break
        
        newn = float(fh)
        standarderror = StdDev / math.sqrt(newn)
        
        print('----------------------------------------------------------------')
        print 'The Standard Error for', newn,'is: ', standarderror
        print('----------------------------------------------------------------')
        print ' '
        
        anyvalue = raw_input('Enter point estimate: ')
        
        if anyvalue[0] == '#':
            continue
        
        if anyvalue == '':
            print  ' '
            break
        
        newmean = float(anyvalue)
        rest = newmean - mean
        zscore = rest / standarderror
        
        print ' '
        print '| The z-score for', anyvalue, 'is:', zscore, '|'
        pvalue = st.norm.cdf(zscore)
        print('---------------------------------------------')
        print '| Z table value =', pvalue, '|'
        print('---------------------------------------------')
        prob = 1 - pvalue
        print 'The probability of getting at least', anyvalue,'is:'
        print ' '
        print 'p =', prob
        print ' '
        print '-------------------------------------------------------------'
        Devs = (1.96 * standarderror)
        print 'Approximately 95% of the sample means fall within', Devs, '\nof', mean, '(Population mean)'
        Dev1 = mean - Devs
        Dev2 = mean + Devs
        print ' '
        print 'The 95% confidence interval is:', Dev1,'<', newmean, '<', Dev2
        print ' '
        Devss = (2.33 * standarderror)
        
        ''' Some notes for T-test:
         Ho = (null hypothesis):
               Mean = Intervention Mean:
               - The sample mean falls somewhere out the critical region.
         Ha = (alternative hypothesis):
               Mean != Intervention Mean (two-tailed),
               Mean < Intervention Mean (one-tailed - right side),
               Mean > Intervention Mean (one-tailed - left side):
               - The sample mean falls somewhere in the critical region.'''

        Dev3 = mean - Devss
        Dev4 = mean + Devss
        
        print 'The 98% confidence interval is:', Dev3,'<', newmean, '<', Dev4
        print ' '
        print 'The margin of error is:', Devs, 'for 95% \nand:', Devss,'for 98%'
        print '--------------------------------------------------------------'
        print ' '
        
        if (zscore < 1.96)&(zscore > -1.96):
            print 'Alpha = 0.05\nHo = Accepted' # Alpha is 0.05 because is used more often
            print ' '
            print '--------------------------------------------------------------'

        else:
            print 'Alpha = 0.05\nHo = Rejected'
            print ' '
            print '--------------------------------------------------------------'

        pdf2 = stats.norm.pdf(Array, mean, standarderror)
        altn = int(newn)
        legen = ("n = "+str(altn))
        fig2 = plt.plot(Array, pdf2, label=legen)
        plt.title("Sampling distribution\nalpha = 0.05") 
        plt.xlabel("Value")
        plt.ylabel("Frequency")
        altm = str(mean)
        legenda = ("Mean =\n "+altm)
        plt.axvline(x= mean, color='r', linestyle='dashed', label=legenda)
        plt.axvline(x= Dev1, color ='g', linestyle='dashed', label=Dev1)
        plt.axvline(x= Dev2, color = 'g', linestyle='dashed', label=Dev2)
        zscorev = mean+(zscore*standarderror)
        zscor = ("z-score =\n"+str(zscore))
        plt.axvline(x= zscorev, color = 'purple', label=zscor)
        print ('To continue, you must save the figure and close it, or just close it. \nYou can also zoom in it or move the graph to see it better, \nuse the buttons.\n')
        plt.legend()
        plt.show(fig2)
        continue
    
print(' ')
print 'Ciao, human!'
print(' ')
