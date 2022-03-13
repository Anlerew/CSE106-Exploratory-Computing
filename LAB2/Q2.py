import numpy as np
from numpy import linalg

A = np.array([[1,2,3],[4,5,6],[7,8,9]])
B = np.array([[3,1,4],[2,6,1],[2,9,7]])

print("(A)\n")
C = A + B
print(C)
print("\n")

print("(B)\n")
D = A @ B
print(D)
print("\n")

print("(C)\n")
determinate = linalg.det(A) 
print(determinate)
print("\n")

print("(D)\n")
inverse = linalg.inv(B)
print(inverse)
print("\n")

print("(E)\n")
eigenvalue = linalg.eig(A)
print(eigenvalue)
print("\n")