from operator import truediv

import numpy as np
import pandas as pd
import numpy as nd

# mas1 = nd.array(range(10))
# print(mas1)
#
# A = nd.random.randint(10, size = (3,5))
# print('Matrica A')
# print(A)
#
# mat = np.array(range(1,50,4))
# print(mat)
#
# B = np.random.randint(-5,3, size = (3,5))
# print('Matrica B')
# print(B)

# A=np.array([[-12,15,7],[0,9,7]])
# print(A)

# A = np.array([[1, 2], [3, 4]])
# print(A)
# B = np.array([[5, 6], [7, 8]])
# print(B)
# print(A.dot(B))
#
# mas = np.eye(2,3)
# islyginti = mas.flatten()
# print(mas)
# print(islyginti)
#
# mat = np.random.randint(20,size=(8,9))
# print(mat)
# # ------------------------
# A=np.random.randint( low=0,high=1,size=5)
# print('Masyvas A:\n',A)
# print('Vieno elemento įterpimas iš galo:\n',np.append(A,7))
# B = [7, 14, 15, 16]
# print('Vieno elemento įterpimas iš galo:\n',np.append(A,B))

# ----------5--------------

# def get_matrix():
#     while True:
#         rows = int(input(f'Iveskite eiluciu skaiciu:'))
#         columns = int(input(f'Iveskite stulpeliu skaiciu:'))
#         if rows * columns >= 2:
#             return rows, columns
#         else:
#             print(f'Negalima suformuoti matricos is tiek elementu. Bandykite vesti is naujo didesnes reiksmes')
# rows, columns = get_matrix()
# matrix = np.random.randint(-10, 10, size=(rows,columns))
# print(matrix)

# ----------1--------------

# A = [3, 5, 8, 1, 5]
# B = [10, 23, 32, 17]
# print(A)
# print(B)
# C = np.delete(A, 2, axis=0)
# D = np.append(A,B)
# print(C)
# print(D)

# ----------2--------------

# A = [3, 5, 8, 1, 5, 4, 6, 1, 8, 9, 4, 2]
# A= np.array(A)
# B = np.delete(A, 2, axis=0)
# C = np.append(B,8)
# print(A)
# print(C)

# ----------3--------------
# A = [3, 5, 8, 1, 5, 4, 6, 1, 8, 9, 4, 2]
# A= np.array(A)
# min = A.min()
# max = A.max()
# A1 = A[(A !=min) & (A != max)]
# position = int(input(f"Nurodyti pozicija, kur iterpti 12345"))
# A2 = np.insert(A1, position, 12345)
# print("Pradinis:", A)
# print("Maziausia reiksme:", min)
# print("Didziausia reiksme:", max)
# print("Pasalintos min ir max:", A1)
# print("Iterpta reiksme:", A2)

# ----------5--------------
# A = np.random.randint(-10, 10, size=(5,4))
# print(A)
# while True:
#     position = int(input(f"Nurodyti kuri stulpeli istrinti"))
#     if 0 <= position < A.shape[1]:
#         break
#     else:
#         print("Ivesta neteisinga reiksme. Tiek stulpeliu matricoje nera.")
# B = np.delete(A, position, axis=1)
# print(B)

# ----------6--------------
# A = np.random.randint(1, 10, size=(2,10))
# print(A)
# while True:
#     row = int(input(f"Nurodyti kuria eilute susumuoti"))
#     if 0 <= row < A.shape[0]:
#         break
#     else:
#         print("Ivesta neteisinga reiksme. Tiek eiluciu matricoje nera.")
# sum= np.sum(A [row, :])
# print(A)
# print(row)
# print(sum)

# ----------8--------------
# matrica = np.random.randint(1, 101, size = (4,4))
# print("Pradine")
# print(matrica)
# matrica[:,[0,-1]] = matrica[:,[-1,0]]
# print("Pakeista")
# print(matrica)

# ----------9--------------
# matric = np.random.randint(1,101, size=(5,5))
# minimum = np.min(matric)
# values = np.sum(matric == minimum)
# print(matric)
# print(minimum)
# print(values)

# ----------10--------------
# matric = np.random.randint(1,101, size=(5,5))
# maximum = np.max(matric)
# values = np.sum(matric == maximum)
# print("Sugeneruota matrica", matric)
# print("Didziausia reiksme:", maximum)
# print("Kiek tokiu reiksmiu yra?:", values)

# ------------------------------------------------------------------
matrica = np.random.randint(1,10, size =(2,2,3,3))
print(matrica)


def make_nd_list(sizes, depth=0):
    if depth == len(sizes) - 1:
        return [7] * sizes[depth]

    result = []
    for _ in range(sizes[depth]):
        result.append(make_nd_list(sizes, depth + 1))

    return result

print(make_nd_list([2,3,2]))
# ----------------------------------------------------
