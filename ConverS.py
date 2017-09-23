# -*- coding: utf-8 -*-
#!/usr/bin/python
# Author: Niam Moltta
# UY - 2017
# MIT License
# Converting str('Clave') to int (value)

import math
import re
import numpy as np
import pandas as pd

print ' '
print ' '
print ' '
print '          Welcome to ConverS.py'
print '           --by Niam Moltta--'
print ' '
print ' '
print ' '

fhand = raw_input('Enter file name: ')

if fhand == '':
    exit()

data = pd.read_csv(fhand)

print ' '

frame = pd.DataFrame(data)

coolist = frame.columns
columns = np.asarray(coolist)

print ' '
print 'Your variables are:\n'
print columns
print ' '

hand = raw_input('Enter column header:\n\n')

column = str(hand)

if (column == 'ya') | (column == ''):
    exit()

# Replace missing values with zeros in the selected [column]
        
data[column].fillna(0,inplace=True)

numbers = data[column]

keeps = 0
replaces = 0
total = 0
numeros = list() # converted list

for line in numbers:
    line = str(line)
    if len(line) <= 3: # values of -1 and 1 are considered
        valor = str(line)
        numeros.append(valor)
        keeps = keeps + 1
        total = total + 1
        print 'Keeping value'
    else : # values of 4 characters, starting with letters that need to be converted to 0
        valor = int(0)
        numeros.append(valor)
        replaces = replaces + 1
        total = total + 1
        print 'Replacing value'

print ' '
print 'New list created'
print ' '
print 'Number of replaced values =', replaces
print 'Number of kept values =', keeps
print 'Total =', total
print ' '

nfile = open('ChangedValues.txt', 'w')
array = list()

for numero in numeros:
    value = str(numero)
    nfile.write(value)
    nfile.write('\n')

nfile.close()

print 'File created as "ChangedValues.txt"'
print ' '
