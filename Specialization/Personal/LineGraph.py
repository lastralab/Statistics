# -*- coding: utf-8 -*-
#!/usr/bin/python
import re
import matplotlib
import matplotlib.pyplot as plt
import numpy as np

#graficar: f(x)=e(exp=-x(squared))

#definir funcion

def f(x):
    return np.exp(-x ** 2)

#creamos vector con los puntos que le pasaremos a la funcion
#previamente creada:

x = np.linspace(-1, 5, num=30)

#representamos la funcion con plt de matplotlib:

plt.xlabel("Eje $x$")
plt.ylabel("$f(x)$")
plt.legend()
plt.title("Function $f(x)$")
plt.grid(True)

fig = plt.plot(x, f(x), label="Function f(x)")

plt.show(fig)
