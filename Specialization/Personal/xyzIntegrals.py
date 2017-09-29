# we use the tplquad command to integrate f(x,y,z)=ysin(x)+zcos(x)
# over the region

# 0<=x<=π
# 0<=y<=1
# −1<=z<=1

from scipy.integrate import tplquad
import numpy as np

def integrand(z, y, x):
    return y * np.sin(x) + z * np.cos(x)

ans, err = tplquad(integrand,
                   0, np.pi,  # x limits
                   lambda x: 0,
                   lambda x: 1, # y limits
                   lambda x,y: -1,
                   lambda x,y: 1) # z limits

print ans
