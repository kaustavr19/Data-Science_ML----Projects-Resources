# -*- coding: utf-8 -*-
"""NumPy Practical.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1hbr44Efedv5B7eyvmZ2KHEpbDUcyW6J_
"""

import numpy as np

array_1d = np.array([1,2,3,4])
print(array_1d)

type(array_1d)

array_1d.ndim

arr_2d = np.array([[1,2,3,4],[5,6,7,8]])
print(arr_2d)

arr_2d.ndim

array_1d.size

arr_2d.size

array_1d.shape

arr_2d.shape

array_1d.dtype

arr_2d.dtype

"""# Practical Part - 2"""

mx_1s = np.array([[1,1,1],[1,1,1],[1,1,1]])
print(mx_1s)

mx_1s = np.ones(5)
print(mx_1s)

mx_1s.dtype

mx_1s = np.ones((3,4))
print(mx_1s)

mx_1s = np.ones((3,4),dtype=int)
print(mx_1s)

mx_0s = np.zeros((3,4))
print(mx_0s)

mx_0s = np.zeros((3,4), dtype=bool)
print(mx_0s)

mx_1s = np.ones((3,4),dtype=bool)
print(mx_1s)

mx_0s = np.zeros((3,4), dtype=str)
print(mx_0s)

mx_1s = np.ones((3,4),dtype=str)
print(mx_1s)

em_str = ''
print(bool(em_str))

em_mx = np.empty((3,3))
print(em_mx)

"""# Practical part-3

## NumPy Functions:
"""

#arange functions(for range)
#np.arange(start, end, steps)
arr_1d = np.arange(1,13)
print(arr_1d)

even_arr1d = np.arange(0,13,2)
print(even_arr1d)

#linespace
print(np.linspace(1,5,4))

#reshape (for converting dimension of array)
arr_2d = arr_1d.reshape(2,6)
print(arr_2d)

arr_3d = arr_1d.reshape(2,2,3)
print(arr_3d)

arr_3d = arr_1d.reshape(4,3)
print(arr_3d)

ar_2d = np.arange(1,13).reshape(2,6)
print(ar_2d)

ar_2d.ravel()

ar_2d.flatten()

arr_3d.transpose()

arr_3d.T

"""# Practical Part-4

## Mathematical Operations
"""

arr1 = np.arange(1,10).reshape(3,3)
arr2 = np.arange(1,10).reshape(3,3)
print(arr1)
print(arr2)

arr1 + arr2

np.add(arr1,arr2)

arr1 - arr2

np.subtract(arr1, arr2)

arr1 / arr2

np.divide(arr1, arr2)

#normal element wise multiplication
arr1 * arr2

np.multiply(arr1, arr2)

#matrix multiplication
arr1 @ arr2

arr1.dot(arr2)

arr1.max()

arr1.argmax()

arr1.max(axis = 0)

arr1.max(axis = 1)

arr1.min()

arr1.argmin()

arr1.min(axis = 0)

arr1.min(axis = 1)

np.sum(arr1)

np.sum(arr1, axis = 0)

np.sum(arr1, axis = 1)

np.mean(arr1)

np.sqrt(arr1)

np.std(arr1)

np.exp(arr1)

np.log(arr1)

np.log10(arr1)

"""# Practical part - 5

## NumPy Array slicing(:)
"""

mx = np.arange(1,101).reshape(10,10)
print(mx)

mx[0,0]

mx[0,0].ndim

mx[0]

mx[:, 0]

mx[:,0:1]

mx[:,0:1].ndim

mx[1:4,1:4]

mx[:,1:3]

mx[:]

mx[::]

mx[:,:]

mx.itemsize

mx.dtype

"""# Practical part - 6"""

arr1 = np.arange(1,17).reshape(4,4)
print(arr1)

arr2 = np.arange(17,33).reshape(4,4)
print(arr2)

np.concatenate((arr1,arr2))

np.concatenate((arr1,arr2), axis = 1)

np.vstack((arr1,arr2))

np.hstack((arr1,arr2))

np.hstack((arr1,arr2,arr1))

list1 = np.split(arr1,2)
print(list1)

type(list1)

list1[0]

type(list1[0])

np.split(arr1, 2, axis=1)

d1 = np.array([4,7,1,3,9])
np.split(d1,[1,3])

"""# Practical part - 7

## Trigonometric Functions
"""

import matplotlib.pyplot as plt

np.sin(180)

np.sin(90)

np.cos(180)

np.tan(180)

x_sin = np.arange(0, 3*np.pi, 0.1)
print(x_sin)

y_sin = np.sin(x_sin)
print(y_sin)

plt.plot(x_sin, y_sin)
plt.show()

y_cos = np.cos(x_sin)
plt.plot(x_sin, y_cos)
plt.show()

y_tan = np.tan(x_sin)
plt.plot(x_sin, y_tan)
plt.show()

np.sin(180 * np.pi/180) #to take angle in radian

"""# Practical part - 8

## Random Sampling with NumPy
"""

import random

np.random.random(1)

np.random.random((3,3))

np.random.randint(1,4)

np.random.randint(1,50,(4,4))

np.random.randint(1,50,(2,4,4))

np.random.seed(10)
np.random.randint(1,50,(2,4,4))

np.random.seed(10)
np.random.randint(1,50,(2,4,4))

np.random.rand(3)

np.random.rand(3,3)

np.random.randn(3,3)

x = [1,2,3,4]
np.random.choice(x) #gives random single item from a given sequence

np.random.choice(x)

np.random.choice(x)

for i in range(20):
    print(np.random.choice(x))

np.random.permutation(x)

np.random.permutation(x)

"""# Practical part - 9

## String Operations, Comparison and Information
"""

ch_name = "Println "
str1 = "Ruko Zara, Code Karo"

np.char.add(ch_name,str1)

np.char.lower(ch_name)

np.char.upper(str1)

np.char.center(str1, 60, fillchar="*")

np.char.split(str1)

np.char.splitlines("Hello\n Println")

str4 = "dmy"
str5 = "dmy"

np.char.join([":","/"],[str4,str5])

np.char.replace(str1,"Code", "CODING")

np.char.equal(str4,str5)

np.char.count(str1, "a")

np.char.find(str1, "r")
