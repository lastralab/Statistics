# -*- coding: utf-8 -*-
#!/usr/bin/python
# Author: Niam Moltta
# UY - 2017
# MIT License
# Two tailed T-test for differences of Means

import math
import numpy as np
import pandas as pd
from scipy.stats import norm
import scipy.stats as st
import matplotlib.pyplot as plt
import re
import seaborn

print ' '
print ' '
print ' '
print '               Welcome to DepT-test.py'
print '                 --by Niam Moltta-- '
print '                      ~~/\//V\ '
print ' '
print ' '
print ' '
print "Application: DIFFERENCES OF MEANS (TWO TAILED T-TEST).\n\nINSTRUCTIONS:\n\n- You must run this program in the same folder that contains your data.\n- Select file, select two columns, select alpha.\n- Returns Mean and Standard Deviation for the differences.\n- Returns t-statistic.\n- Returns p-value and t-value from the t-table.\n- Returns Cohen's D.\n- Returns Confidence Interval.\n- Returns acceptance/rejection of the null hypothesis.\n- The columns you choose must have the same length and numeric values.\n- It will ask you a lot if you are using columns from different files.\nPlease, be patient and answer.\n- The answer is important so that you can get the correct results.\n"
print ' '

while True:
    
    fh = raw_input('Enter first .csv file name: ')
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
    print ' '
    print 'Columns in', re.findall('(.+?).csv', fhand), 'are:\n'
    print columns
   
    print ' '
    print '--------------------------------------------------------'
    hand = raw_input('Enter first column header: ')
    print ' '
    
    if (hand == 'ya') | (hand == ''):
        print ' '
        print 'Ciao, bambino!'
        print ' '
        exit()
        
    fha = raw_input('Enter second .csv file name or "s" to continue: ')  # in case column is in a different file
    fhan = str(fha)
    print ' '

    if (fhan == 'ya') | (fhan == ''):
        print ' '
        print 'Hasta la vista, baby'
        print ' '
        exit()
    elif fhan == 's':
        
        hand2 = raw_input('Enter second column header: ')
        print '--------------------------------------------------------'
        print ' '
        
        column1 = str(hand)
        column2 = str(hand2)
        
        frame['Difference'] = data[column1] - data[column2] #
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
            return st.t.ppf(1-(alpha/2), gl) # alpha/2 because two tailed
        gl = nDifs-1
        tvalue = (t(alpha,gl))
        print ' '
        t = 1
        if tstat < 0:
            t = t*(-1)
        else:
            t = t*(1)
        print 't-value =', tvalue*t
        pvalue = st.t.sf(np.abs(tstat), nDifs-1)*2
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
        
    else:

        data2 = pd.read_csv(fhan, header=0)
        frame2 = pd.DataFrame(data2)

        colist2 = frame2.columns
        columns2 = np.asarray(colist2)
        print ' '
        print 'Columns in', re.findall('(.+?).csv', fhan), 'are:\n'
        print columns2
        print ' '

        hand2 = raw_input('Enter second column header: ')
        print '--------------------------------------------------------'
        print ' '
        
        column1 = str(hand)
        column2 = str(hand2)
        
        frame['Difference'] = data[column1] - data2[column2] #
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
            return st.t.ppf(1-(alpha/2), gl) # alpha/2 because two tailed
        gl = nDifs-1
        tvalue = (t(alpha,gl))
        print ' '
        t = 1
        if tstat < 0:
            t = t*(-1)
        else:
            t = t*(1)
        print 't-value =', tvalue*t
        pvalue = st.t.sf(np.abs(tstat), nDifs-1)*2
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

        path = raw_input('Are you working on the same file? Enter "yes", or "no" to continue: ')

        answer = str(path)
        print ' '
        if (answer == 'yes') | (answer == ''):

            print 'KEYWORDS:\n\nEnter "plot" to see the columns behavior.\nEnter "graph" to see the Differences of Means distribution.\nEnter "next" to analyze another two columns in the same file.\nEnter "ya" to quit the program.\n\n'
            user = raw_input('Enter keyword: ')
            hands = str(user)
            print ' '
            if hands == 'graph':
                Array = sorted(Difs)
                Arr = np.asarray(Array)
                pdf2 = st.norm.pdf(Arr, Avrg, tvalue)
                altn = int(nDifs)
                legen = ("n = "+str(altn))
                fig2 = plt.plot(Arr, pdf2, label=legen)
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
                break
                
            elif (hands == 'ya') | (hands == ''):
                print ' '
                print 'Hasta la vista, baby.'
                print ' '
                exit()
                
        elif answer == 'no':
            
            print 'KEYWORDS:\n\nEnter "plot" to see the columns behavior.\nEnter "graph" to see the Differences of Means distribution.\nEnter "next" to analyze another two columns.\nEnter "ya" to quit the program.\n\n'
            user = raw_input('Enter keyword: ')
            hands = str(user)
            print ' '
            if hands == 'graph':
                Array = sorted(Difs)
                Arr = np.asarray(Array)
                pdf2 = st.norm.pdf(Arr, Avrg, tvalue)
                altn = int(nDifs)
                legen = ("n = "+str(altn))
                fig2 = plt.plot(Arr, pdf2, label=legen)
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
                y = np.cumsum(data2[column2])
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
                print ' '
                print 'Hasta la vista, baby.'
                print ' '
                exit()

print ' '
print 'Hasta la vista, baby.'
print ' '
