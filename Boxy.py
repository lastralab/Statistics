# -*- coding: utf-8 -*-
#!/usr/bin/python
# Author: Niam Moltta
# UY - 2017
# License : MIT
# Fixig skewness with Box Cox

import pandas as pd
import matplotlib.pylab as plt
from sklearn import preprocessing
import re
import seaborn
import numpy as np
from scipy.stats import boxcox
from scipy.stats import skew

print ' '
print ' '
print '                Welcome to Boxy.py'
print '               -- by Niam Moltta --'
print '                     ~~/\//V\ '
print ' '
print ' '
print 'Application: SKEWNESS REDUCTION WITH BOXCOX.\n\nINSTRUCTIONS:\n\n- You need to run this program in the same folder that contains your data.\n * Data must NOT contain negative values.\n- Select file, select column.\n- Returns original skewed data histogram. \n- Returns un-skewed data using sqrt histogram.\n- Returns un-skewed data using BoxCox histogram.\n- Select the un-skewed data that you prefer to print in a new file.\n- Create file with new data.\n\nWhen prompted:\n\n- Enter "Y" to create a .txt file with the BoxCox fixed data.\n- Enter "Ybut" to create a .txt file with the sqrt transformed data.\n- Enter "n" to work with another variable, or:\n- Enter "ya" to finish the program.\n\n * Sometimes using "sqrt" (square root) is enough to reduce skewness.\n'

fhand = raw_input('Enter file name: ')

filecsv = str(fhand)

if filecsv == '':
    print ' '
    print 'Arrivederci!'
    print ' '
    exit()
    
data = pd.read_csv(filecsv)

print ' '

frame = pd.DataFrame(data)

coolist = frame.columns
columns = np.asarray(coolist)

while True:

    print ' '
    print 'Columns in', re.findall('(.+?).csv', filecsv), 'are:\n'
    print columns
    print ' '
    
    hand = raw_input('Enter column header:\n\n')

    column = str(hand)

    if (column == 'ya') | (column == ''):
        break
    
    else:
    
        # Replace missing values with zeros in the selected [column]
        
        data[column].fillna(0,inplace=True)

        print ' '
        print 'Missing values were replaced with zeros'
        print ' '
        
        # Scale method from scikit-learn to transform the distribution 
        
        Col = preprocessing.scale(np.sqrt(data[column]))

        # Get rid of zeros:

        Boxy = preprocessing.scale(boxcox(data[column]+1)[0])
        

        PreBox = preprocessing.scale(data[column])

        # Calculate skewness again:

        skness = skew(Col)
        sknessBoxy = skew(Boxy)
        sknessPreBox = skew(PreBox)
        print ' '
        print 'Original Skewness =',sknessPreBox,'\nSqrt Skewness =', skness,'\nBoxCox Skewness =', sknessBoxy,'\n'
        print ' '

        #Draw histograms:
        
        figure = plt.figure() 
        figure.add_subplot(131) 
        plt.hist(Col,facecolor='red',alpha=0.75)
        label1 = str('Skewness = ') + str(round(skness, 4))
        lab = str(label1)
        plt.xlabel(lab) 
        plt.title("Transformed using 'sqrt'") 
        plt.text(2,100000,"Skewness: {0:.2f}".format(skness)) 
        
        figure.add_subplot(132) 
        plt.hist(Boxy,facecolor='lightblue',alpha=0.75)
        label2 = str('Skewness = ') + str(round(sknessBoxy, 4))
        labe = str(label2)
        plt.xlabel(labe)  
        plt.title("Transformed using 'BoxCox'") 
        plt.text(2,100000,"Skewness: {0:.2f}".format(sknessBoxy))

        figure.add_subplot(133)
        plt.hist(PreBox,facecolor='green',alpha=0.75) 
        label3 = str('Skewness = ') + str(round(sknessPreBox, 4))
        label = str(label3)
        plt.xlabel(label) 
        plt.title("Original Histogram") 
        plt.text(2,100000,"Skewness: {0:.2f}".format(sknessPreBox)) 
        plt.show()
    
        print ' '
        print ' --  Save the figure, or close it to continue  -- '
        print ' '
        
        user = raw_input('Enter Y/n to create file: ')
        answer = str(user)
        
        if answer == 'Y':
            
            Boxy = preprocessing.scale(boxcox(data[column]+1)[0])
            
            namef = raw_input('Enter the file name and make sure you add ".txt"\n\n')
            name = str(namef)

            # Create file with standarized data:

            nfile = open(name, 'w')

            # Fill it with data:

            for value in Boxy:
                val = str(value)
                nfile.write(val)
                nfile.write('\n')

            nfile.close()
            print ' '
            print 'File created as', name
            print ' '
            
        elif answer == 'Ybut':
            print ' '
            print "You'll get the sqrt transformed data instead of the BoxCox"
            print ' '
            Col = preprocessing.scale(np.sqrt(data[column]))
            
            namef = raw_input('Enter the file name and make sure you add ".txt"\n\n')
            name = str(namef)

            # Create file with standarized data:

            nfile = open(name, 'w')

            # Fill it with data:

            for value in Col:
                val = str(value)
                nfile.write(val)
                nfile.write('\n')

            nfile.close()
            print ' '
            print 'File created as', name
            print ' '
            
        elif (answer == 'n')|(answer == ''):
            print ' '
            print 'Not a single f***ile was created.'
            print ' '
        
        else:
            break
        
print ' '
print 'Hasta la vista, human.'
print ' '
exit()
