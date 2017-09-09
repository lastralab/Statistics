# -*- coding: utf-8 -*-
#!/usr/bin/python
# Author: Niam Moltta
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
import matplotlib.pyplot as mlab

print ' '
print '*----------------------------*'
print '|                            |'
print '|  Welcome to DepT-test.py   |'
print '|                            |'
print '*----------------------------*'
print ' '
print 'KEYWORDS: After you analyze the file, you can type other stuff instead of another file name, like:\n\n- "print", to see the Data Frame you just analyzed.\n- "graph", to see the dependent two tailed t-test.\n- "plot", to graph columns behavior, and finally:\n- "ya", to finish the program.\n'

while True:
    
    fhand = raw_input('Enter .csv file name or keyword: ')

    if fhand == 'ya':
        break
    if fhand == 'print':
        print frame
        continue
    if fhand == 'graph':
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
    if fhand == 'plot':
        df = pd.DataFrame(data, index=frame.index, columns=frame.columns)
        df = df.cumsum()
        fig = df.plot()
        plt.title("Column behavior")
        plt.xlabel("Values") 
        plt.ylabel("Frequency")
        plt.show(fig)
        print ' '
        continue
    data = pd.read_csv(fhand, header=0)
    frame = pd.DataFrame(data)

    print ' '
    print 'Index:'
    print frame.index
    print ' '
    print 'Columns:'
    print frame.columns[0]
    print frame.columns[1]
    print ' '
    
    ############################################################################

    coln1= str(frame.columns[0])
    coln2= str(frame.columns[1])
    col1 = frame[coln1].values
    col2 = frame[coln2].values
    frame['Difference'] = col1 - col2
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
        return scipy.stats.t.ppf(1-(alpha/2), gl)
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
    print ' '
# print frame                      # uncomment line to see it automatically.
print(' ')
print 'Hasta la vista, baby.'
print(' ')
