# -*- coding: utf-8 -*-
#!/usr/bin/python
# Author: Niam Moltta
# UY - 2017
# MIT License
# Creating intervals and assigning them values to create a new list

import math
import re
import numpy as np
import pandas as pd

print ' '
print ' '
print '                Welcome to RangeR.py'
print '                -- by Niam Moltta --'
print '                      ~~/\//V\ '
print ' '
print ' '
print ' '
print 'Application: ASSIGNING DATA TO INTERVALS.\n\nINSTRUCTIONS:\n\n- Select file, select column.\n- Returns minimum and maximum.\n- Returns factors for that range.\n- Select number of intervals.\n- Create file with data split by intervals.\n\n'

fhand = raw_input('Enter file name: ')

if fhand == '':
    print '\nSee you next time...\n\n'
    exit()

filecsv = str(fhand)
    
data = pd.read_csv(filecsv)

print ' '

frame = pd.DataFrame(data)

colist = frame.columns
columns = np.asarray(colist)

while True:

    print 'Columns in', re.findall('(.+?).csv', filecsv), 'are:\n'
    print ' '
    print columns
    print ' '
    column = raw_input('Enter column header: ')
    print ' '
    if column == '':
        break
    hand = str(column)
    puntos = data[hand]
    
    puntajes = np.asarray(puntos)
    largo = len(puntajes)
    
    minimo = min(puntos)
    maximo = max(puntos)
    space = maximo - minimo
    print 'Total cases =', largo
    print 'Min =', minimo
    print 'Max =', maximo
    print 'Length =', space
    print ' '
    
    def factors(x):
       facts = list()

       print "The factors of",x,"are:"
       for i in range(1, x + 1):
           if x % i == 0:
               facts.append(i)
       print facts
               
    num = int(space)
    factors(num)
    print ' '
    handy = raw_input('Enter number of intervals: ')
    if handy == '':
        break
    numero = str(handy)
    divisor = int(numero)

    start = minimo
    stop = maximo + 1
    step = space / divisor

    Ranges = np.arange(start, stop, step, dtype=float)

    print ' '
    print 'Intervals =', Ranges
    print ' '
    spacer = Ranges[1] - Ranges[0]
    print 'Range =', spacer
    print '------------------------------------'
    print ' '
    
    scoresD = list()
    scores = list()

    total = 0 # control

    newValues = list() # ranged values

    for line in puntajes:
        punts = float(line)
        scoresD.append(punts)

    for value in scoresD : 
        scores.append(float(value))

    while True:
        
        for score in scores:
            
            value = float(score)
  
            try:
                if Ranges[0] <= value <= Ranges[1]:
                    val = 1
                    newValues.append(val)
                    
                    total = total +1

                elif Ranges[1]< value <= Ranges[2]:
                    val = 2
                    newValues.append(val)
        
                    total = total +1

                elif Ranges[2]< value <= Ranges[3]:
                    val = 3
                    newValues.append(val)
                    
                    total = total +1
                    
                elif Ranges[3] < value <= Ranges[4]: 
                    val = 4
                    newValues.append(val)
          
                    total = total +1

                elif Ranges[4] < value <= Ranges[5]: # Up to 5 intervals
                    val = 5
                    newValues.append(val)
            
                    total = total + 1
                    
                elif Ranges[5] < value <= Ranges[6]:
                    val = 6
                    newValues.append(val)
            
                    total = total + 1
                    
                elif Ranges[6] < value <= Ranges[7]: 
                    val = 7
                    newValues.append(val)
            
                    total = total + 1
                
                    
                elif Ranges[7] < value <= Ranges[8]:
                    val = 8
                    newValues.append(val)
            
                    total = total + 1
                
                    
                elif Ranges[8] < value <= Ranges[9]:
                    val = 9
                    newValues.append(val)
            
                    total = total + 1
                
                    
                elif Ranges[9] < value <= Ranges[10]: # Up to 10 intervals
                    val = 10
                    newValues.append(val)
                    
                    total = total + 1
                
                    
                elif Ranges[10] < value <= Ranges[11]:
                    val = 11
                    newValues.append(val)

                    total = total + 1
                
                    
                elif Ranges[11] < value <= Ranges[12]:
                    val = 12
                    newValues.append(val)
            
                    total = total + 1
                
                    
                elif Ranges[12] < value <= Ranges[13]:
                    val = 13
                    newValues.append(val)
            
                    total = total + 1
                
                    
                elif Ranges[13] < value <= Ranges[14]:
                    val = 14
                    newValues.append(val)
            
                    total = total + 1
                
                    
                elif Ranges[14] < value <= Ranges[15]: # Up to 15 intervals
                    val = 15
                    newValues.append(val)
            
                    total = total + 1
                
                    
                elif Ranges[15] < value <= Ranges[16]:
                    val = 16
                    newValues.append(val)
            
                    total = total + 1
                
                    
                elif Ranges[16] < value <= Ranges[17]:
                    val = 17
                    newValues.append(val)
            
                    total = total + 1
                
                    
                elif Ranges[17] < value <= Ranges[18]:
                    val = 18
                    newValues.append(val)
            
                    total = total + 1
                
                    
                elif Ranges[18] < value <= Ranges[19]:
                    val = 19
                    newValues.append(val)
            
                    total = total + 1
                
                    
                elif Ranges[19] < value <= Ranges[20]: # Up to 20 intervals you greedy
                    val = 20
                    newValues.append(val)
            
                    total = total + 1

                else:
                    print 'Value not assigned:', value
                    continue
                
            except IndexError:
                pass
        break

    print ' '
    print 'RangeR succesfully implemented!'
    print "Number of values that weren't assigned =", len(scores) - total
    print ' '   

    nfile = open('Ranged.csv', 'w')

    for value in newValues:
        valor = str(value)
        nfile.write(valor)
        nfile.write(',\n')

    nfile.close()

    print 'File created as "Ranged.csv"'
    print ' '
    
print ' '
print "Baur baur"
print ' '
