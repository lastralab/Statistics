# -*- coding: utf-8 -*-
#!/usr/bin/python
# Author: Niam Moltta
# UY - 2017
# License: MIT
# One way or another...
# One and Two ways ANOVA conducting with Python
# %matplotlib inline

import warnings
warnings.filterwarnings('ignore')
import pandas as pd
import matplotlib.axes
pd.set_option("display.width", 100)
import matplotlib.pylab as plt
import matplotlib
import re
from statsmodels.compat import urlopen
import numpy as np
np.set_printoptions(precision=5, suppress=True)
import seaborn
from statsmodels.formula.api import ols
from statsmodels.graphics.api import interaction_plot, abline_plot
import statsmodels.api as sm
import statsmodels.formula.api as smf
from statsmodels.stats.anova import anova_lm as lm
from scipy import stats
import matplotlib.cm as cm
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
        
        hand0 = raw_input('Enter "by Group A" column header: ')

        print ' '

        if hand0 == 'ya':

            print ' '

            continue

        elif hand0 == '':

            break

        hand1 = raw_input('Enter "by Group B", or hit Return to continue: ')

        if hand1 == '':
                
            print ' '
        
            hand2 = raw_input('Enter independent variable "X" column header: ')  
            print ' '
            
            hand3 = raw_input('Enter dependent variable "Y" column header: ')
            print ' '
            
            #M = str(hand1)
            
            E = str(hand0)
            X = str(hand2)
            S = str(hand3)
            
            # TWO WAY ANOVA:
                
            print ' '
            
            print 'Drawing preview of data...'
            
            groups = data.groupby(data[E])
            
            colors = ['blue', 'red', 'yellow', 'green', 'purple', 'brown', 'orange', 'silver','magenta','cyan','black','white']
            
            
            if len(groups) == 2:

                X = data[X]
                Y = data[S]
                
                s = 100
                
                plt.figure(figsize=(8,6))

                groups = data.groupby(data[E])
                
                for key, group in groups:
                    interaction_plot(X, group, np.log(Y+1), colors=['r','b'], markers=['D','^'], ms=10, ax=plt.gca())
                
                    plt.show() #?
                
            else:

                fig, ax = plt.subplots(figsize=(8,6))
                
                s = 100
                
                for key, group in groups:
                
                    group.plot(ax=ax, kind='scatter', x=X, y=S, label=key, color=colors[key-1], alpha=0.3, s=s)
                    
                    nomen = 'variable "'+str(E)+'" is represented by colors'
                    nomenclature = nomen
            
                    plt.title(nomenclature)       
                    plt.xlabel(X);
                    plt.ylabel(S);
                    plt.show()
            
            print ' '
            print '--------------------------------'
            XoY = stats.ttest_ind(data[X], data[S])
            
            print 'T test for X and Y (ind):\n'
            print 't-statistic=', XoY[0], '\n\np-value=', XoY[1]
            print ' '
            print '--------------------------------'
            XyY = stats.ttest_rel(data[X], data[S])
            
            print 'T test for X and Y (rel):\n'
            print 't-statistic=', XyY[0], '\n\np-value=', XyY[1]
            print ' '
            print '--------------------------------'
            xyy = stats.ttest_1samp(data[X], data[S])
            
            print 'T test for X and Y (1samp)\nReady as "xyy"'
            print ' '
            print '--------------------------------'
            
            Y = data[S]
            Group = data[E]
            X = data[X]

            # f-test
            
            formula = 'np.log(Y+1) ~ C(Group) * C(X)'
            
            print 'Formula ready:', formula
            
            print ' '
            
            model = ols(formula, data=data).fit()
            
            print 'MODEL SUMMARY:'
            print ' '
            
            print model.summary()
            print ' '
            
            #aov_table = lm(model, typ=2) # ERROR Singular matrix
            
            #print 'ANALYSIS OF VARIANCE (ANOVA) TABLE:'
            #print ' '
            #print aov_table
            print ' '

            print '    Drawing INTERACTION PLOT...'
            print ' '

            
            sumofsq = ols('np.log(Y+1) ~ C(Group, Sum) * C(X, Sum)', data=data).fit()

            print ' '
            print ' Sum of Squares'
            print lm(sumofsq)
            print ' '
            print ' Type 2'
            print lm(sumofsq, typ=2)
            print ' '
            print ' Type 3'
            print lm(sumofsq, typ=3)
            
            print ' '

            # 3 ways visualization:
            
        else:
            
            print ' '
            
            hand2 = raw_input('Enter independent variable "X" column header: ')  
            print ' '
        
            hand3 = raw_input('Enter dependent variable "Y" column header: ')

            print ' '
                
            M = str(hand1) 
            E = str(hand0) 
            X = str(hand2)
            S = str(hand3)
                
                # THREE WAY ANOVA:
                
            print ' '
                
            print 'Drawing preview of data...'

            print ' '

            print 'Calculating ANOVA...'
            
            groups = data.groupby([str(E), str(M)])
            
            colors = ['blue', 'red', 'yellow', 'green', 'purple', 'brown', 'orange', 'silver','magenta','cyan','black','white']
            
            symbols = ['o','d','^', 'h', 's', 'p', 's', 'v', '>','x','D','8','+']
            
            fig, ax = plt.subplots(figsize=(8,6))
            
            if len(groups) < 5:
                
                s = 10**2
                
            else:
                
                s = 81
            
            print ' '

            for values, group in groups:
                i, j = values
                group.plot(ax=ax, kind='scatter', x=X, y=S, label=values, color=colors[i-1], alpha=0.3, s=s, marker=symbols[j-1], edgecolors='black')           
                
            nomen = 'variable "'+str(E)+'" is represented by colors\nvariable "'+str(M)+'" is represented by figures'
            nomenclature = nomen
            
            plt.title(nomenclature)       
            plt.xlabel(X);
            plt.ylabel(S);
            plt.show()
            
            print ' '
            print '--------------------------------'
            XoY = stats.ttest_ind(data[X], data[S])
            
            print 'T test for X and Y (ind):\n'
            print 't-statistic=', XoY[0], '\n\np-value=', XoY[1]
            print ' '
            print '--------------------------------'
            XyY = stats.ttest_rel(data[X], data[S])
            
            print 'T test for X and Y (rel):\n'
            print 't-statistic=', XyY[0], '\n\np-value=', XyY[1]
            print ' '
            print '--------------------------------'
            xyy = stats.ttest_1samp(data[X], data[S])
            
            print 'T test for X and Y (1samp)\nReady as "xyy"'
            print ' '
            print '--------------------------------'
        
            GroupA = data[E] 
            Y = data[S]
            GroupB = data[M] 
            X = data[X]
            
            formula = 'Y ~ C(X) + C(GroupA) * C(GroupB)'
            
            print 'Formula ready:', formula
            
            print ' '
            
            model = ols(formula, data=data).fit()
            
            print 'MODEL SUMMARY:'
            print ' '
            
            print model.summary()
            print ' '
            
            aov_table = lm(model, typ=2)
            
            print 'ANALYSIS OF VARIANCE (ANOVA) TABLE:'
            print ' '
            print aov_table
            
            print ' '
            
            
print ' '

print 'Hasta la vista, human.'

print ' '

exit()
