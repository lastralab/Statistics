# -*- coding: utf-8 -*-
import pandas as pd

#Dataframe
# El DataFrame es una estructura de datos tabular similar a las hojas de cálculo de Excel.
# Posee tanto indices de columnas como de filas.

# Creando un DataFrame.
data = {'state': ['Ohio', 'Ohio', 'Ohio', 'Nevada', 'Nevada'],
        'year' : [2000, 2001, 2002, 2001, 2002],
        'pop'  : [1.5, 1.7, 3.6, 2.4, 2.9]}
frame = pd.DataFrame(data) # Creando un DataFrame desde un diccionario
print 'frame 5 rows x 3 columns:'
print frame

# Creando un DataFrame desde un archivo. uncomment next lines:
#!cat 'dataset.csv' # ejemplo archivo csv.

# Leyendo el archivo dataset.csv para crear el DataFrame
#frame2 = pd.read_csv('dataset.csv', header=0) 
#print 'frame2:'
#print frame2

# Seleccionando una columna como una Serie
print 'state column:'
print frame['state']

# Seleccionando una línea como una Serie.
print 'frame.ix[1]:'
print frame.ix[1]

# Verificando las columnas
print 'verificando columnas:'
print frame.columns

# Verificando los índices.
print 'verificando indices:'
print frame.index


