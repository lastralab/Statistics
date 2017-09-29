# -*- coding: utf-8 -*-
#!/usr/bin/python
import pandas as pd

# Las series son matrices de una sola dimension similares a los vectores, pero con su propio indice.
# Creando una Serie

serie = pd.Series([2, 4, -8, 3])

print 'matriz de una sola dimension: serie:', serie

# podemos ver tantos los índices como los valores de las Series.
print 'serie.values:', serie.values
print 'serie.index:', serie.index

# Creando Series con nuestros propios índices.
serie2 = pd.Series([2, 4, -8, 3], index=['d', 'b', 'a', 'c'])
print 'serie con nuestros propios indices:'
print serie2

# Accediendo a los datos a través de los índices
print 'a: ', serie2['a']
print 'b,c,d: '
print serie2[['b', 'c', 'd']]
print '[serie2 > 0] #(backwards):'
print serie2[serie2 > 0]

