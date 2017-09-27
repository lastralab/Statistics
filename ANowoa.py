# -*- coding: utf-8 -*-
#!/usr/bin/python
# Author: Niam Moltta
# UY - 2017
# License: MIT
# One way or another...
# One and Two ways ANOVA conducting with Python

import pandas as pd
import plotly.plotly as plt
import plotly.graph_objs as grow 
import plotly.figure_factory as FF
import re
import numpy as np
import statsmodels
from scipy import stats

print ' '
print ' '
print '               Welcome to ANowoa.py'
print '               -- by Niam Moltta --'
print '                     ~~/\//V\ '
print ' '
print ' '
print ' '

print "Application: Analysis of Variance (ANOVA).\n\nINSTRUCTIONS:\n\n- Make sure that the .csv file is in the same folder of this script.\n- To start, enter the name of the file without 'quotes' and ending with .csv\n  Example: scores.csv\n- Enter 'ya' to select number of ways again.\n- Enter 'ya' to quit.\n- Select file, select columns to analyze by group.\n- Returns Analysis of Variance between two or more group means.\n- Returns Degrees of Freedom, Sum of Squares, Mean Square.\n- Returns F-value and p-value.\n- Returns Eta squared and Omega squared for effect size.\n"

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

    ways = raw_input('Enter number of ways to conduct the ANOVA 1/2: ')
    print ' '
    hm = str(ways)

    if (hm == '') | (hm == '0'):
        break
    
    elif hm == 'ya':
        break

    elif hm == '1':
                
        print 'Columns in', re.findall('(.+?).csv', filecsv), 'are:\n'
        print columns
        print ' '
            
        hand1 = raw_input('Enter first column header: ')
        print ' '         
        if (hand1 == 'ya') | (hand1 == ''):
            print ' '
            continue
        handg = raw_input('Enter "by group" column header: ')

        print ' '    
            
        column1 = str(hand1)
        column2 = str(handg)
            
        # ONE WAY ANOVA:
        
        print ' '
        grps = pd.unique(data[column2].values)
        d_data = {grp:data[column1][data[column2] == grp] for grp in grps}
        print ' '
        k = len(pd.unique(data[column2]))
        N = len(data.values)
        n = data.groupby(data[column2]).size()

        print 'Number of conditions:'
        print 'k =', k
        print ' '
        print 'Conditions times participants:'
        print 'N =', N
        print ' '
        print 'Participants in each condition:'
        print 'n =', n
        
        DFbetween = k - 1
        DFwithin = N - k
        DFtotal = N - 1
        print ' '
        print 'Degrees of freedom:'
        print 'DFbetween =', DFbetween
        print 'DFwithin =', DFwithin
        print 'DFtotal =', DFtotal
        print ' '
        SSbetween = (sum(data.groupby(data[column2]).sum()[column1]**2)/n)-(data[column1].sum()**2)/N
        print 'Sum of Squares:'
        print 'SSbetween =', SSbetween
        print ' '
        Y2 = sum([value**2 for value in data[column1].values])
        SSwithin = Y2 - sum(data.groupby(data[column2]).sum()[column1]**2)/n
        SStotal = Y2 - (data[column1].sum()**2)/N
        print 'SSwithin =', SSwithin
        print ' '
        print 'SStotal =', SStotal
        print ' '
        MSbetween = SSbetween/DFbetween
        MSwithin = SSwithin/DFwithin
        print 'Mean Square:'
        print 'MSbetween =', MSbetween
        print ' '
        print 'MSwithin =', MSwithin
        print ' '
        F = MSbetween / MSwithin
        p = stats.f.sf(F, DFbetween, DFwithin)
        print 'F =', F
        print ' '
        print 'p =', p
        print ' '
        effsize = SSbetween/SStotal  # eta-squared
        print 'Effect size:'
        print ' '
        print 'eta-squared =', effsize
        print ' '
        om_sqrd = ((SSbetween-(DFbetween*MSwithin))/(SStotal+MSwithin))
        print 'Omega squared =', om_sqrd
        print ' '
        
        #
        
        print ' '

    elif hm == '2':

        print 'Columns in', re.findall('(.+?).csv', filecsv), 'are:\n'
        print columns
        print ' '
                
        hand1 = raw_input('Enter first column header: ')
        print ' '  
                
        if (hand1 == 'ya'):
            print ' '
            continue
        elif hand1 == '':
            break
                
        hand2 = raw_input('Enter second column header: ')
        print ' '

        hand3 = raw_input('Enter third column header: ')
        print ' '
                
        column1 = str(hand1)
        column2 = str(hand2)
        column3 = str(hand3)

        # TWO WAYS ANOVA:

        print ' '
        print 'Currently working on it'
        print ' '
        exit()
       
print ' '
print 'Hasta la vista, human.'
print ' '
exit()
