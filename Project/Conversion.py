# -*- coding: utf-8 -*-
#!/usr/bin/python
# Author: Niam Moltta
# UY - 2017
# MIT License
import math
import re
import numpy as np

fhand = raw_input('Enter file name: ')

numbers = open(fhand)
keeps = 0
replaces = 0
total = 0
numeros = list() # converted list

for line in numbers:
    if len(line) <= 3: # values of -1 and 1 are considered
        valor = int(line)
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

nfile = open('newlist.txt', 'w')
array = list()

for numero in numeros:
    value = str(numero)
    nfile.write(value)
    nfile.write('\n')

nfile.close()

print 'File created as "newlist.txt"'
print ' '
