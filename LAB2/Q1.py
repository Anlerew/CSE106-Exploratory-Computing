import numpy as np
print("(A)\n")
matrix= np.arange(2,10).reshape(4,2)
print(matrix)
print("\n")

print("(B)\n")
checker = np.zeros((8,8))
checker[::2, 1::2] = 1
checker[1::2, ::2]= 1
print(checker)
print("\n")

print("(C)\n")
list = [10, 20, 10, 30, 20, 40, 20, 20, 10, 30, 0, 50, 10]
get = np.unique(list)
print(get)
print("\n")

print("(D)\n")
list1 = [6, 75, 9, 82, 36, 42, 59, 3, 52, 1, 32, 68, 93, 4, 27, 85, 0, -3, 57]
arr = np.array(list1)
great = np.where(arr > 37)
print(arr[great])
print("\n")

print("(E)\n")
list2 =[0, 12, 45.21 ,34, 99.91]
arr1 = np.array(list2)
print((5*(arr1))/9 - (5*32)/9)