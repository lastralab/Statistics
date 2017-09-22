# -*- coding: utf-8 -*-
#!/usr/bin/python
# Author: Niam Moltta
# UY - 2017
# MIT License
# Two tailed T-test for differences of Means

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
import matplotlib.pyplot as mlab

print ' '
print ' '
print '     *----------------------------*'
print '     |                            |'
print '     |  Welcome to DepT-test.py   |'
print '     |    --by Niam Moltta--      |'
print '     |                            |'
print '     *----------------------------*'
print ' '
print ' '
print 'INSTRUCTIONS:\n\nYou must run this program in the same folder of your data.'

print ' '

fh = raw_input('Enter .csv file name: ')
fhand = str(fh) 

if (fh == 'ya') | (fh == ''):
    print ' '
    print 'Hasta la vista, baby'
    print ' '
    exit()

data = pd.read_csv(fhand, header=0)
frame = pd.DataFrame(data)

colist = frame.columns
columns = np.asarray(colist)

while True:

    print ' '
    print 'Variables in file:\n'
    print columns
   
    print ' '
    print '--------------------------------------------------------'
    hand = raw_input('Enter first column header: ')
    if (hand == 'ya') | (hand == ''):
        print ' '
        print 'Ciao ciao, bambino!'
        print ' '
        exit()
    hand2 = raw_input('Enter second column header: ')
    print '--------------------------------------------------------'
    print ' '
    
    column1 = str(hand)
    column2 = str(hand2)
    
    frame['Difference'] = data[column1] - data[column2]
    Difs = frame['Difference'].values
    SumDifs = sum(Difs)
    nDifs = len(Difs)
    AvDifs = float(SumDifs)/float(nDifs)
    Avrg = float(AvDifs)
    print 'Mean of differences =', Avrg
    StdDevDifs = (Difs-Avrg)**2
    print ' '
    Var = sum(StdDevDifs)/(nDifs-1)
    StdDev = math.sqrt(Var)
    print 'Standard Deviation for the differences =', StdDev
    print ' '
    tstat = Avrg/(StdDev/math.sqrt(nDifs))
    print 't-statistic =', tstat
    print ' '
    print '--------------------------------------------------------'
    fh = raw_input('Enter alpha: ')
    print '--------------------------------------------------------'
    alpha = float(fh)
    def t(alpha, gl):
        return scipy.stats.t.ppf(1-(alpha/2), gl) # alpha/2 because two tailed
    gl = nDifs-1
    tvalue = (t(alpha,gl))
    print ' '
    t = 1
    if tstat < 0:
        t = t*(-1)
    else:
        t = t*(1)
    print 't-value =', tvalue*t
    pvalue = stats.t.sf(np.abs(tstat), nDifs-1)*2
    print ' '
    print 'p-value =', pvalue
    print ' '
    cohen = Avrg / StdDev
    print "Cohen's d =", cohen
    print ' '
    rootn = math.sqrt(nDifs)
    c = StdDev / rootn
    CIa = Avrg - (tvalue*c)
    CIb = Avrg + (tvalue*c)
    print 'Confidence Interval = (',CIa,',',CIb,')'
    print ' '
    if (tstat > CIa) | (tstat < CIb):
        print 'Ho = Reject'
    elif (tstat < CIa) | (tstat > CIb):
        print 'Ho = Fail to reject'

    print ' '
    
    while True:

        print 'KEYWORDS:\n\nEnter "plot" to see the columns behavior.\nEnter "graph" to see the Differences of Means distribution.\nEnter "next" to analyze another two columns in the same file.\nEnter "ya" to quit the program.\n\n'
        user = raw_input('Enter keyword: ')
        hands = str(user)
        print ' '
        if hands == 'graph':
            Array = sorted(Difs)
            pdf2 = stats.norm.pdf(Array, 0, tvalue)
            altn = int(nDifs)
            legen = ("n = "+str(altn))
            fig2 = plt.plot(Array, pdf2, label=legen)
            plt.title("Differences of Means distribution")
            plt.xlabel("Values")
            altm = str(Avrg)
            legenda = ("Mean =\n "+altm)
            V1 = 0 - tvalue
            V2 = 0 + tvalue
            plt.axvline(x= 0, color='r', linestyle='dashed', label=legenda)
            plt.axvline(x= V1, color ='g', linestyle='dashed', label=V1)
            plt.axvline(x= V2, color = 'g', linestyle='dashed', label=V2)
            score = ("t =\n"+str(tstat))
            plt.axvline(x=tstat, color = 'purple', label=score)
            print ' '
            print ('To continue, you must save the figure and close it, or just close it. You can also zoom in it or move the graph to see it better, use the buttons.\n')
            plt.legend()
            plt.show(fig2)
            print ' '
            continue

        elif hands == 'plot':
            Array = sorted(Difs)
            x = np.cumsum(data[column1])
            y = np.cumsum(data[column2])
            z = np.cumsum(Array)
            plt.plot(x, 'b', label=column1)
            plt.plot(y, 'g', label=column2)
            plt.plot(z, 'r', label="Differences")
            plt.title("Column behavior")
            plt.xlabel("Values") 
            plt.ylabel("Frequency")
            print ('To continue, you must save the figure and close it, or just close it. You can also zoom in it or move the graph to see it better, use the buttons.\n')
            plt.legend()
            plt.show()
            print ' '
            continue
            
        elif hands == 'next':
            break
        elif (hands == 'ya') | (hands == ''):
            print 'Hasta la vista, baby.'
            exit()

print' '
print 'Hasta la vista, baby.'
print' '
