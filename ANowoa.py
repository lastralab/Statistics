# -*- coding: utf-8 -*-
#!/usr/bin/python
# Author: Niam Moltta
# UY - 2017
# License: MIT
# One way or another...
# One and Two ways ANOVA conducting with Python

import pandas as pd
from pandas.tools import plotting
import matplotlib.pyplot as plt
import plotly.graph_objs as grow 
import plotly.figure_factory as FF
import re
import numpy as np
import seaborn
import statsmodels.formula.api as ols
from statsmodels.stats.anova import anova_lm
from statsmodels.graphics.factorplots import interaction_plot
from scipy import stats
import warnings


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
        
        #hand0 = raw_input('Enter the ID column name: ')
        
        hand1 = raw_input('Enter "by group" data: ')
        print ' '
        
        if hand1 == 'ya':
            print ' '
            continue
        elif hand1 == '':
            break
                
        hand2 = raw_input('Enter X data: ')
        print ' '

        hand3 = raw_input('Enter Y data: ')
        print ' '

        #column1 = str(hand0)
        column2 = str(hand1)
        column3 = str(hand2)
        column4 = str(hand3)

        # TWO WAYS:

        print 'Drawing preview of data'
        
        plotting.scatter_matrix(data[[column2, column3, column4]])
        plt.show()
        print '1'
        stats.ttest_ind(data[column3], data[column4])
        print '2'
        stats.ttest_rel(data[column3], data[column4])
        print '3'
        stats.ttest_1samp(data[column3], data[column4])
        print '4'
        plt.show()
        
        '''
        WORKING ON IT:
        figs = interaction_plot(data.dose, data.supp, data.len,
             colors=['red','blue'], markers=['D','^'], ms=10)

        N = len(data.len)
        df_a = len(data.supp.unique()) - 1
        df_b = len(data.dose.unique()) - 1
        df_axb = df_a*df_b 
        df_w = N - (len(data.supp.unique())*len(data.dose.unique()))

        grand_mean = data['len'].mean()

        #datas = [[column2, column3, column4]]

        formula = 'len ~ C(supp) + C(dose) + C(supp):C(dose)'
        model = ols(formula, datas).fit()
        aov_table = anova_lm(model, typ=2)
        eta_squared(aov_table)
        omega_squared(aov_table)
        
        print aov_table
        
        #sub = data[[column1, column2, column3, column4]]
        #sub_data = sub.copy()
        
        # data must be standardized
        #warnings.filterwarnings('ignore') 
        #seaborn.pairplot(sub_data);
        #plt.show()
        '''
        print ' '

            
print ' '
print 'Hasta la vista, human.'
print ' '
exit()
