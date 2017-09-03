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
import scipy.stats

print(' ')
print(' Welcome to MoCTpy! ')
print(' --by Tania Mol-- ')
print(' ')
print("INSTRUCTIONS:\n \n- Make sure that the .txt file is in the same folder of this script, otherwise it won't be found.\n- To start, enter the name of the file without 'quotes' and ending with .txt (example: scores.txt).\n- The name of the file will be the legend on the first plot, I recommend you to choose the name wisely.\n- Later, when you are done selecting values for sample distribution, type 'ya', hit Return and the program will finish nicely.\n")
fhand = raw_input('Enter file name: ')

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
print ('Standard Deviation ='), StdDev
# print ('Standard Error ='), StdE # optional
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
print ('To continue, you must save the figure and close it. You can also zoom in it or move the graph to see it better, use the buttons.\n')
plt.show(fig)

while True:
    fh = raw_input('Enter n value for sample distribution: ')
    if fh[0] == '#':
        continue
    if fh == 'ya':
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
    if anyvalue == 'ya':
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
    # Some notes for T-test:
    # Ho = (null hypothesis):
    #       Mean = Intervention Mean:
    #       - The sample mean falls somewhere out the critical region.
    # Ha = (alternative hypothesis):
    #       Mean != Intervention Mean (two-tailed),
    #       Mean < Intervention Mean (one-tailed - right side),
    #       Mean > Intervention Mean (one-tailed - left side):
    #       - The sample mean falls somewhere in the critical region.
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
    plt.title("Sampling distribution\nalpha = 0.05") # or 98% if you uncomment some lines below
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
    # Uncomment next two lines for 98% confidence interval
    #plt.axvline(x= Dev3, color = 'orange', linestyle='dashed', label=Dev3)
    #plt.axvline(x= Dev4, color = 'orange', linestyle='dashed', label=Dev4)
    print ('To continue, you must save the figure and close it, or just close it. You can also zoom in it or move the graph to see it better, use the buttons.\n')
    plt.legend()
    plt.show(fig2)
    print ' '
    continue
print(' ')
print 'It was a pleasure to make your life easier.\nHasta la vista, baby.'
print(' ')
