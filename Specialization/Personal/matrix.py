# -*- coding: utf-8 -*-
import numpy as np

# creating a vector from a python list

vector = np.array([1, 2, 3, 4])

print 'vector: '
print vector

# creating a matrix

matrix = np.array([[ 1, 2],
                    [3, 4]])

print 'matrix: '
print matrix

# El tipo de objeto de tanto de los vectores como de las matrices
# es ndarray

type(vector), type(matrix)

#Los objetos ndarray de Numpy cuentan con las propiedades shape
#y size que nos muestran sus dimensiones.

print 'vector shape:', vector.shape, 'vector size:', vector.size

print 'matrix shape:', matrix.shape, 'matrix size:', matrix.size

#ARANGE
#La funcion arange nos facilita la creación de matrices
x = np.arange(1, 11, 2) # argumentos: start, stop, step (ejemplo:
# inicia en el 1, termina en el 10, avanza de 2 en 2).

print 'arange:'
print x

#linspace
#linspace nos devuelve un vector con la cantidad de muestras
#que le ingresemos y separados uniformamente entre sí.

y = np.linspace(1, 25, 25)  # argumentos: start, stop, samples

print 'linspace:'
print y

#mgrid
#Con mgrid podemos crear arrays multimensionales.

x, y = np.mgrid[0:5, 0:5] 

print 'mgrid:'
print 'x = 0:5'
print x
print 'y = 0:5'
print y

#zeros y ones
#Estas funciones nos permiten crear matrices de ceros o de unos.

zeros = np.zeros((3,3))

print 'zeros:'
print zeros

ones = np.ones((3,3))

print 'ones:'
print ones

#random.randn
#Esta funcion nos permite generar una matriz con una distribución
#estándar de números.

r = np.random.randn(5,5)

print 'random (5,5):'
print r

#diag
#Nos permite crear una matriz con la diagonal de números
#que le ingresemos.

diag = np.diag([1,1,1])

print 'diagonal:'
print diag


