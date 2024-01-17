import numpy as np
from numpy import random
from scipy import constants
from scipy.optimize import root
from math import sin
from math import cos

array1 = np.array([1, 2, 3, 4, 5])
array2 = array1.copy()
array2[0] = 0

print(array1)
print(array2)

x = random.randint(100)

print(x)

array=random.randint(100, size=(5))

print(array)

print(dir(constants))

inputecuatie = int(input())

def ecuatiesin(x):
  return x + sin(x)

def ecuatiecos(x):
  return x + cos(x)

myroot = root(ecuatiecos, inputecuatie)

print(myroot.x)