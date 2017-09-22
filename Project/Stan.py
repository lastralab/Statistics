# -*- coding: utf-8 -*-
#!/usr/bin/python
# Author: Niam Moltta
# UY - 2017
# License : MIT
# Centering & Scaling Data

import pandas as pd
import matplotlib.pylab as plt
from sklearn import preprocessing
import re
import numpy as np

print ' '
print ' '
print '            Welcome to Standardization.py'
print '                -- by Niam Moltta --'
print ' '
print ' '
print 'INSTRUCTIONS:\n\nYou need to run this program in the same folder that your data file is.\n\nWhen asked:\nEnter "Y" to create a .txt file with the standardized data.\nEnter "n" to analyze another column, or:\nEnter "ya" to finish the program.\n\n'

fhand = raw_input('Enter file name: ')

filecsv = str(fhand)

if filecsv == '':
    exit()
    
data = pd.read_csv(filecsv)

print ' '

frame = pd.DataFrame(data)

coolist = frame.columns
columns = np.asarray(coolist)

while True:

    print ' '
    print 'Your variables are:\n'
    print columns
    print ' '

    hand = raw_input('Enter column header:\n\n')

    column = str(hand)

    if (column == 'ya') | (column == ''):
        break
    
    else:
        print ' '
        print 'Searching...\n'
        print ' '
        print column,'identified.'
    
        # Replace missing values with zeros in the selected [column]
        data[column].fillna(0,inplace=True)

        print ' '
        print 'Missing values were replaced with zeros'
        print ' '
        
        # Scale method from scikit-learn to transform the distribution 
        
        Col = preprocessing.scale(data[column]) 

        print 'Data succesfully transformed\n\nDrawing histograms...'

        # Draw histograms:
    
        figure = plt.figure() 
        ax1 = figure.add_subplot(121) 
        plt.hist(data[column],facecolor='red',alpha=0.75) 
        plt.xlabel(column) 
        plt.ylabel("Frequency") 
        plt.title("Original Histogram") 
        ax1.text(300,100000,"Mean: {0:.2f} \n Std: {1:.2f}".format(data[column].mean(),data[column].std())) 
        
        ax2 = figure.add_subplot(122) 
        plt.hist(Col,facecolor='lightblue',alpha=0.75) 
        plt.xlabel("Data - Transformed") 
        plt.title("Standardized Histogram") 
        ax2.text(2,100000,"Mean: {0:.2f} \n Std: {1:.2f}".format(Col.mean(),Col.std())) 
        plt.show()
    
        print ' '
        print ' --  Save the figure, or close it to continue  -- '
        print ' '
        
        user = raw_input('Enter Y/n to create file: ')
        answer = str(user)
        
        if answer == 'Y':
            
            Col = preprocessing.scale(data[column]) 

            # Create file with standarized data:

            nfile = open('Standardized.txt', 'w')

            # Fill it with data:

            for value in Col:
                val = str(value)
                nfile.write(val)
                nfile.write('\n')

            nfile.close()
            print ' '
            print 'File created as "Standardized.txt"\n\nIf you want to transform another column, you need to change this file name in your folder in order to create a new one.'
            print ' '
            
        elif answer == '':
            break
        
        elif answer == 'n':
            print ' '
            print 'Not a single file was created.'
            print ' '
            continue
        else:
            break
        
print ' '
print 'Hasta la vista, human.'
print ' '
exit()
