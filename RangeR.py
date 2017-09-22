# -*- coding: utf-8 -*-
#!/usr/bin/python
# Author: Niam Moltta
# UY - 2017
# MIT License
import math
import re
import numpy as np
import pandas as pd


print ' '
print ' '
print '                Welcome to RangeR.py'
print '                -- by Niam Moltta --'
print ' '
print ' '

fhand = raw_input('Enter file name: ')

if fhand == '':
    exit()

filecsv = str(fhand)
    
data = pd.read_csv(filecsv)

print ' '

frame = pd.DataFrame(data)

colist = frame.columns
columns = np.asarray(colist)

print columns
print ' '
hand = raw_input('Enter column header to apply ranges: ')
print ' '
puntajede = data[hand]

puntajes = np.asarray(puntajede)

scoresD = list()
scores = list()

total = 0 # control

range1 = 0
range2 = 0
range3 = 0
range4 = 0
range5 = 0
range55 = 0
range6 = 0
range7 = 0
range8 = 0
range9 = 0
range10 = 0

newScore = list() #ranged values

for line in puntajes:
    punts = float(line)
    scoresD.append(punts)

for value in scoresD : 
    scores.append(float(value))

print ' '
print 'Values to assign:', len(scores)
print ' '

while True:

    for score in scores:
        value = float(score)
        if 14.041 < value <= 45.6542:
            val = 1
            newScore.append(val)
            range1 = range1 + 1
            total = total +1

        elif 45.6542 < value <= 49.935018:
            val = 2
            newScore.append(val)
            range2 = range2 + 1
            total = total +1

        elif 49.935018 < value <= 50.099664:
            val = 3
            newScore.append(val)
            range3 = range3 + 1
            total = total +1
            
        elif 50.099664 < value <= 50.264311: # negatives range reference
            val = 4
            newScore.append(val)
            range4 = range4 + 1
            total = total +1

        elif 50.264311 < value <= 66.729:
            val = 5
            newScore.append(val)
            range5 = range5 + 1
            total = total + 1
            
        else:
            print 'value could not be assigned:', value
            continue
    break

print ' '
print 'Ranges succesfully applied, total reduced to', total, 'values.'
print ' '
print 'Number of scores in range 1 =', range1
print 'Number of scores in range 2 =', range2
print 'Number of scores in range 3 =', range3
print 'Number of scores in range 4 =', range4
print 'Number of scores in range 5 =', range5
'''print 'Number of scores in range 5.5', range55
print 'Number of scores in range 6 =', range6
print 'Number of scores in range 7 =', range7
print 'Number of scores in range 8 =', range8
print 'Number of scores in range 9 =', range9
print 'Number of scores in range 10 =', range10'''

print ' '
print 'Number of values assigned to newScore list =', len(newScore)
print ' '

nfile = open('Ranges.txt', 'w')

for value in newScore:
    valor = str(value)
    nfile.write(valor)
    nfile.write('\n')

nfile.close()

print 'File created as "Ranges.txt"'
print ' '
