# -*- coding: utf-8 -*-
#!/usr/bin/python
# Author: Niam Moltta
# UY - 2017
# Spearman Correlation Coefficient

import numpy as np
from scipy.stats import spearmanr
import matplotlib.pylab as plt
import re
from sklearn import preprocessing
import pandas as pd

print ' '
print ' '
print '                Welcome to SpeaR.py'
print '                - by Niam Moltta -'
print ' '
print ' '

fhand = raw_input('Enter file name: ')
print ' '

if fhand == '':
    exit()
    
filecsv = str(fhand)
    
data = pd.read_csv(filecsv)

print ' '

frame = pd.DataFrame(data)

colist = frame.columns
columns = np.asarray(colist)

while True:

    print ' '
    print 'Variables in file:\n'
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
            
            # Calculate the Spearman coefficient and the p-value for testing non-correlation
            
            Spear = spearmanr(x, y)
            
            if (Spear[0] == 1)|(Spear[0] == -1):
                print "Spearman's Correlation =", Spear[0]
                print ' '
            else:
                print "Spearman's Correlation =", Spear[0]
                print ' '
                print 'p-value =', Spear[1]
                print ' '
                
                Coef = Spear[0]
                pval = Spear[1]
                
                r2 = str(Coef)
                p = str(pval)
                pvalue = 'p-value = '+ p
                R2 = "Spearman's = "+ r2
                
                xcums = np.cumsum(x)
                ycums = np.cumsum(y)
                
                yc = sorted(ycums, reverse=True)
                
                if Coef < 0 :
                    
                    plt.plot(xcums, 'g', label=column1)
                    plt.plot(yc, 'b', label=column2)
                    plt.title(R2)
                    plt.xlabel(pvalue)
                    plt.ylabel("Correlation")
                    print ('To continue, you must save the figure and close it, or just close it. You can also zoom in it or move the graph to see it better, use the buttons.\n')
                    plt.legend()
                    plt.show()
                    print ' '
                else:
                    plt.plot(xcums, 'g', label=column1)
                    plt.plot(ycums, 'b', label=column2)
                    plt.title(R2)
                    plt.xlabel(pvalue)
                    plt.ylabel("Correlation")
                    print ('To continue, you must save the figure and close it, or just close it. You can also zoom in it or move the graph to see it better, use the buttons.\n')
                    plt.legend()
                    plt.show()
                    print ' '
                    
'''The Spearman correlation is a nonparametric measure of the monotonicity of the relationship between two datasets. Unlike the Pearson correlation, the Spearman correlation does not assume that both datasets are normally distributed. Like other correlation coefficients, this one varies between -1 and +1 with 0 implying no correlation. Correlations of -1 or +1 imply an exact monotonic relationship. Positive correlations imply that as x increases, so does y. Negative correlations imply that as x increases, y decreases.

The p-value roughly indicates the probability of an uncorrelated system producing datasets that have a Spearman correlation at least as extreme as the one computed from these datasets. The p-values are not entirely reliable but are probably reasonable for datasets larger than 500 or so.'''
        
print ' '
print 'Hasta la vista, human.'
print ' '
exit()
