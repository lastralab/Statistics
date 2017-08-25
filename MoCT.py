# -*- coding: utf-8 -*-
#!/usr/bin/python
# Author: Tania M. Molina
# UY - 2017
# MIT License
import math
import numpy as np
import pandas as pd
from scipy import stats
from scipy.stats import norm
import scipy.stats as stats
import scipy.stats as st
import matplotlib
import matplotlib.pyplot as plt
import re

print(' ')
print(' Welcome to MoCTpy! ')
print(' --by Tania Mol-- ')
print(' ')
print("INSTRUCTIONS:\n \n- Make sure that the .txt file is in the same folder of this script, otherwise it won't be found.\n- To start, enter the name of the file without 'quotes' and ending with .txt (example: scores.txt).\n- The name of the file will be the legend on the first plot, I recommend you to choose the name wisely.\n- Later, when you are done selecting values for sample distribution, type 'ya', hit Return and the program will finish nicely.\n")
fhand = raw_input('Now, enter the file name: ')

numbers = open(fhand)

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
print ('MEASURES OF CENTRAL TENDENCY for:'), fhand
print (' ')
print ('N ='), n
print ('Mean ='), mean
print ('Sum of Squares ='), SS
print ('Variance ='), Var
print ('Population Standard Deviation ='), StdDev
print ('Standard Error ='), StdE
print ('---------------------------------------------')
print(' ')
Array = np.asarray(A)
Array.sort()
#pdf = stats.norm.pdf(Array, mean, StdDev)
#fig = plt.plot(Array, pdf)
legend = re.findall('(.*).txt', fhand)
fig = plt.hist(Array, color='c', bins=20, histtype='stepfilled', label=legend) # to see the behavior better, set bins for resolution
plt.title("Population distribution")
plt.xlabel("Value")
plt.ylabel("Frequency")
plt.legend()
print ('To continue, you must save the figure and close it.\n')
plt.show(fig)

while True:
    fh = raw_input('Enter value for sample distribution: ')
    if fh[0] == '#':
        continue
    if fh == 'ya':
        break
    newn = float(fh)
    newdeviation = StdDev / math.sqrt(newn)
    print('----------------------------------------------------------------')
    print 'The Standard Error for', newn,'is: ', newdeviation
    print('----------------------------------------------------------------')
    print ' '
    anyvalue = raw_input('Enter point estimate: ')
    if anyvalue[0] == '#':
        continue
    if anyvalue == 'ya':
        break
    newmean = float(anyvalue)
    rest = newmean - mean
    zscore = rest / newdeviation
    print ' '
    print '| The z-score for', anyvalue, 'is:', zscore, '|'
    pvalue = st.norm.cdf(zscore)
    print('---------------------------------------------')
    print '| Z table value =', pvalue, '|'
    print('---------------------------------------------')
    greater = 1 - pvalue
    print 'The probability of getting at least', anyvalue,'is:'
    print 'p =', greater
    percent = greater * 100
    print 'p =', percent,'%'
    Devs = (1.96 * newdeviation)
    print '---------------------------------------------'
    print 'Approximately 95% of the sample means fall within', Devs, '\nof', mean, '(Population mean)'
    Dev1 = newmean - Devs
    Dev2 = newmean + Devs
    print ' '
    print 'The 95% confidence interval is:', Dev1,'<', newmean, '<', Dev2
    print ' '
    Devss = (2.33 * newdeviation)
    Dev3 = newmean - Devss
    Dev4 = newmean + Devss
    print 'The 98% confidence interval is:', Dev3,'<', newmean, '<', Dev4
    print '---------------------------------------------'
    pdf2 = stats.norm.pdf(Array, newmean, Devs)
    altn = int(newn)
    legen = ("n= "+str(altn))
    fig2 = plt.plot(Array, pdf2, label=legen)
    plt.title("Sampling distribution + Confidence intervals: 95%(green) 98%(orange)")
    plt.xlabel("Value")
    plt.ylabel("Frequency")
    altm = str(newmean)
    legenda = ("mean= "+altm)
    plt.axvline(x= newmean, color='r', linestyle='dashed', label=legenda)
    plt.axvline(x= Dev1, color ='g', linestyle='dashed', label=Dev1)
    plt.axvline(x= Dev2, color = 'g', linestyle='dashed', label=Dev2)
    plt.axvline(x= Dev3, color = 'orange', linestyle='dashed', label=Dev3)
    plt.axvline(x= Dev4, color = 'orange', linestyle='dashed', label=Dev4)
    print ('To continue, you must save the figure and close it, or just close it.\n')
    plt.legend()
    plt.show(fig2)
    continue
print(' ')
print 'It was a pleasure to make your life easier,\nHasta la vista, baby.'
print(' ')
