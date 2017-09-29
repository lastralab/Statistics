# -*- coding: utf-8 -*-
#!/usr/bin/python
# Author: Niam Moltta
# UY - 2017
# Pearson's Correlation Coefficient

import numpy as np
from scipy.stats.stats import pearsonr
import matplotlib.pylab as plt
import re
from sklearn import preprocessing
import pandas as pd
import seaborn

print ' '
print ' '
print '                Welcome to PeaR.py'
print '                - by Niam Moltta -'
print '                    ~~/\//V\ '
print ' '
print ' '
print ' '
print "Application: PEARSON'S CORRELATION COEFFICIENT.\n\nINSTRUCTIONS:\n\n- Select file, select two numeric columns.\n- Returns Pearson's Coefficient and p-value.\n- Returns graph of correlation relationship.\n\n * Up to +-0.6 may indicate it is a considerable correlation for social sciences, \n   but not for data that you got from very sophisticated instruments.\n\n"

fhand = raw_input('Enter file name: ')
print ' '

if fhand == '':
    print ' '
    print "Avoid becoming a vanellus chilensis!"
    print ' '
    exit()
    
filecsv = str(fhand)
    
data = pd.read_csv(filecsv)

print ' '

frame = pd.DataFrame(data)

colist = frame.columns
columns = np.asarray(colist)

while True:

    print ' '
    print 'Columns in', re.findall('(.+?).csv', filecsv), 'are:\n'
    print columns
    print ' '
    hand = raw_input('Enter column header for variable x: ')
    column1 = str(hand)
    print ' '
    if (column1 == 'ya') | (column1 == ''):
        break
    else:

        hand2 = raw_input('Enter column header for variable y: ')
        column2 = str(hand2)
        print ' '
        if (column2 == 'ya') | (column2 == ''):
            break  
        else:
            print ' --------------------------------------------------------- '
            print "Calculating correlation for:\n", column1,"and", column2
            print ' --------------------------------------------------------- '
            
            C1 = data[column1]
            C2 = data[column2]
            
            x = np.asarray(C1)
            y = np.asarray(C2)
            # Calculate a Pearson correlation coefficient and the p-value for testing non-correlation
            
            Pear = pearsonr(x, y)
            
            if (Pear[0] == 1)|(Pear[0] == -1):
                print "Pearson's Coefficient =", Pear[0]
                print ' '
            else:
                print "Pearson's Coefficient =", Pear[0]
                print ' '
                print 'p-value =', Pear[1]
                print ' '
                
                Coef = Pear[0]
                pval = Pear[1]
                
                r2 = str(Coef)
                p = str(pval)
                pvalue = 'p-value = '+ p
                R2 = "Pearson's = "+ r2
                
                xcums = np.cumsum(x)
                ycums = np.cumsum(y)
                
                yc = sorted(ycums, reverse=True)
                
                if Coef < 0 :
                    
                    plt.plot(xcums, 'b', label=column1)
                    plt.plot(yc, 'r', label=column2)
                    plt.title(R2)
                    plt.xlabel(pvalue)
                    plt.ylabel("Correlation")
                    print ('To continue, you must save the figure and close it, or just close it. You can also zoom in it or move the graph to see it better, use the buttons.\n')
                    plt.legend()
                    plt.show()
                    print ' '
                else:
                    plt.plot(xcums, 'b', label=column1)
                    plt.plot(ycums, 'r', label=column2)
                    plt.title(R2)
                    plt.xlabel(pvalue)
                    plt.ylabel("Correlation")
                    print ('To continue, you must save the figure and close it, or just close it. You can also zoom in it or move the graph to see it better, use the buttons.\n')
                    plt.legend()
                    plt.show()
                    print ' '
                    
'''The Pearson correlation coefficient measures the linear relationship
 between two datasets. Strictly speaking, Pearson's correlation requires
 that each dataset be normally distributed. Like other correlation
 coefficients, this one varies between -1 and +1 with 0 implying no
 correlation. Correlations of -1 or +1 imply an exact linear
 relationship. Positive correlations imply that as x increases, so does
 y. Negative correlations imply that as x increases, y decreases.

 The p-value roughly indicates the probability of an uncorrelated system
 producing datasets that have a Pearson correlation at least as extreme
 as the one computed from these datasets. The p-values are not entirely
 reliable but are probably reasonable for datasets larger than 500 or so.'''
        
print ' '
print 'Hasta la vista, human.'
print ' '
exit()
