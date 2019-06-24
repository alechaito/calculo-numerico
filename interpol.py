import numpy as np
#rom matplotlib.pyplot import *

xi = np.array([0, 1], dtype='double')  
yi = np.array([1.35, 2.94], dtype='double')  
A = np.array([xi**1, xi**0]).transpose() 
pt_1 = 0.73
pt_2 = 1.00

print("Matriz A")
print(A)
print("-----------------")
a = np.linalg.inv(A).dot(yi)
print("Coeficientes Ax do polinomio interpolador")
print(a)
print("-----------------")

#result = a[1]*(pto_x) + a[0]
# P(X) = a1*x + a0
result = a[0]*(pt_1) + a[1]
print(result)
print("-----------------")
result = a[0]*(pt_2) + a[1]
print(result)