# -*- coding: utf-8 -*-
#!/usr/bin/python
# Author: Niam Moltta
# UY - 2017
# License: MIT
# One way or another...
# One and Two ways ANOVA conducting with Python
#%matplotlib inline

import warnings
warnings.filterwarnings('ignore')
import pandas as pd
import matplotlib
pd.set_option("display.width", 100)
import matplotlib.pylab as plt
import re
from statsmodels.compat import urlopen
import numpy as np
np.set_printoptions(precision=5, suppress=True)
import seaborn
from statsmodels.formula.api import ols
from statsmodels.graphics.api import interaction_plot, abline_plot
import statsmodels.api as sm
import statsmodels.formula.api as smf
from statsmodels.stats.anova import anova_lm
from scipy import stats
import matplotlib.cm as cm
#from __future__ import print_function
warnings.filterwarnings('ignore')

print (' ')
print (' ')
print ('               Welcome to ANowoa.py')
print ('               -- by Niam Moltta --')
print ('                     ~~/\//V\ ')
print (' ')
print (' ')
print (' ')

print ("Application: Analysis of Variance (ANOVA).\n\nINSTRUCTIONS:\n\n- Make sure that the .csv file is in the same folder of this script.\n- To start, enter the name of the file without 'quotes' and ending with .csv\n  Example: scores.csv\n- Enter 'ya' to select number of ways again.\n- Enter 'ya' to quit.\n- Select file, select columns to analyze by group.\n- Returns Analysis of Variance between two or more group means.\n- Returns Degrees of Freedom, Sum of Squares, Mean Square.\n- Returns F-value and p-value.\n- Returns Eta squared and Omega squared for effect size.\n- Returns scatter graph of selected variables.\n")

fhand = raw_input('Enter .csv file name: ')

filecsv = str(fhand)

if filecsv == (''):
    print(' ')
    print ('Ciao, human!')
    print(' ')
    exit()
'''    
elif re.findall('^http.*$', filecsv):
    
    try:

        url = urlopen(filecsv)
        dataframe = pd.read_table(url)
        last = re.findall('^http.*/([a-z].+[a-z])$', filecsv)
        dataframe.to_csv(str(last))

    # possible conflict: S(proa) X(socio) E(educa) M(sexo)       
    except:
'''        
data = pd.read_csv(filecsv)

print (' ')

frame = pd.DataFrame(data)

coolist = frame.columns
columns = np.asarray(coolist)

while True:

    ways = raw_input('Enter number of ways to conduct the ANOVA 1/2: ')
    print (' ')
    hm = str(ways)

    if (hm == '') | (hm == '0'):
        break
    
    elif hm == ('ya'):
        break

    elif hm == ('1'):
                
        print ('Columns in', re.findall('(.+?).csv', filecsv), 'are:\n')
        print (columns)
        print (' ')
            
        hand1 = raw_input('Enter first column header: ')
        print (' ')        
        if (hand1 == 'ya') | (hand1 == ''):
            print (' ')
            continue
        handg = raw_input('Enter "by group" column header: ')

        print (' ')   
            
        column1 = str(hand1)
        column2 = str(handg)
            
        # ONE WAY ANOVA:
        
        print (' ')
        grps = pd.unique(data[column2].values)
        d_data = {grp:data[column1][data[column2] == grp] for grp in grps}
        k = len(pd.unique(data[column2]))
        N = len(data.values)
        n = data.groupby(data[column2]).size()

        print ('Number of conditions:')
        print ('k =', k)
        print (' ')
        print ('Conditions times participants:')
        print ('N =', N)
        print (' ')
        print ('Participants in each condition:')
        print ('n =', n)
        
        DFbetween = k - 1
        DFwithin = N - k
        DFtotal = N - 1
        print (' ')
        print ('Degrees of freedom:')
        print ('DFbetween =', DFbetween)
        print ('DFwithin =', DFwithin)
        print ('DFtotal =', DFtotal)
        print (' ')
        SSbetween = (sum(data.groupby(data[column2]).sum()[column1]**2)/n)-(data[column1].sum()**2)/N
        print ('Sum of Squares:')
        print ('SSbetween =', SSbetween)
        print (' ')
        Y2 = sum([value**2 for value in data[column1].values])
        SSwithin = Y2 - sum(data.groupby(data[column2]).sum()[column1]**2)/n
        SStotal = Y2 - (data[column1].sum()**2)/N
        print ('SSwithin =', SSwithin)
        print (' ')
        print ('SStotal =', SStotal)
        print (' ')
        MSbetween = SSbetween/DFbetween
        MSwithin = SSwithin/DFwithin
        print ('Mean Square:')
        print ('MSbetween =', MSbetween)
        print (' ')
        print ('MSwithin =', MSwithin)
        print (' ')
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
        print 'Drawing scatter plot...'
        print ' '
        arr = np.asarray(sorted(data[column1]))
        arrG = np.asarray(sorted(data[column2]))
        name = str(column1)+' / '+str(column2)
        warnings.filterwarnings('ignore')
        fig1 = plt.scatter(arr, arrG, label=name)
        plt.title(name)
        plt.ylim((min(arrG)-1, max(arrG)+1))
        plt.xlabel(column1)
        plt.ylabel(column2)
        plt.show(fig1)

    elif hm == '2': 

        print 'Columns in', re.findall('(.+?).csv', filecsv), 'are:\n'
        print columns
        print ' '
        
        #hand0 = raw_input('Enter "by group" column header: ')
        #print ' '
        hand1 = raw_input('Enter "by group" column header: ')
        print ' '
        
        if hand1 == 'ya':
            print ' '
            continue
        elif hand1 == '':
            break
                
        hand2 = raw_input('Enter variable "X" column header: ')
        print ' '

        hand3 = raw_input('Enter variable "Y" column header: ')
        print ' '

        #M = str(hand0)
        E = str(hand1)
        X = str(hand2)
        S = str(hand3)

        # TWO WAYS:

        print ' '

        name1 = min(data[E])
        name2 = max(data[E])
        res = name2 - name1
        N = int(name2)

        groups = data.groupby(data[E])#, data[M]])

        colors = ['blue', 'red', 'yellow', 'green', 'purple', 'brown', 'orange', 'silver','magenta','cyan','black','white']

        fig, ax = plt.subplots()

        s = [300*2**n for n in range(len(groups))]

        for key, group in groups:
            group.plot(ax=ax, kind='scatter', x=X, y=S, label=key, color=colors[key-1], alpha=0.25, s=s)

        nomen = 'variable "'+str(E)+'" is represented by colors'

        nomenclature = nomen

        plt.title(nomenclature)
        plt.xlabel(X);
        plt.ylabel(S);
        plt.show()

        ''' working on this...
        print ' '
        XoY = stats.ttest_ind(data[column3], data[column4])
        print 'T test for X and Y ready (ind)'
        XyY = stats.ttest_rel(data[column3], data[column4])
        print 'T test for X and Y ready (rel)'
        xyy = stats.ttest_1samp(data[column3], data[column4])
        print 'T test for X and Y ready (1samp)'

        strings = "'"+str(column3)+' ~ '+str(column2)+' + '+str(column4)+"'"
       
        formula = str(strings)
        print 'Formula ready'
        print formula
        model = smf.ols(formula, data=data).fit()
        print 'model ready'
        print model.summary()
        
        aov_table = anova_lm(model, typ=2)
        eta_squared(aov_table)
        omega_squared(aov_table)
        
        print aov_table
        '''
        print ' '

            
print ' '
print 'Hasta la vista, human.'
print ' '
exit()
