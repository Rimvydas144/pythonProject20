from array import array
from xml.dom.minidom import Attr

import numpy as np
# --------- pvz --------------
# print(np.cbrt(64))
# print(np.linspace(1, 5, 3))
# pazymiai = [1, 2, 3, 4, 5]
# np_pazymiai = np.asarray(pazymiai)
# print(type(np_pazymiai))
# array = np.arange(0, 100, 13)*2
# print(array)
# vidurkis = np.min(pazymiai)
# print(vidurkis)

# reiksme = [1,2,3,4,5]
# svoriai = [0.1,0.2,0.3,0.2,0.2]
# vidurkis = np.average(reiksme,weights=svoriai)
# print(vidurkis)

# --------- 1 --------------

# masyvas = np.random.randint(1,50,10)
# maziausias = np.min(masyvas)
# didziausias = np.max(masyvas)
# print(masyvas)
# print(maziausias)
# print(didziausias)

# --------- 2 --------------

# A = int(input('Nurodykite maziausia masyvo reiksme'))
# B = int(input('Nurodykite didziausia masyvo reiksme'))
# C = int(input('Nurodykite elementu skaiciu masyve'))
# masyvas = np.random.randint(A, B, C)
# maziausias = np.min(masyvas)
# didziausias = np.max(masyvas)
# print(array)
# print(maziausias)
# print(didziausias)

# --------- 3 --------------

n = np.random.randint(1,11)
masyvas = np.random.randint(1,100,n)
print(masyvas)
print(n)

