import numpy as np
import math

n = 10
#-------
a = 1
b = 2
h = (b-a)/n

print("Passo: {}".format(h))
print("--------------- \n")

def func(x):
    fx = (2*x)+(1/x)
    return fx
	
xi = a
f_xi = func(xi)
ci = 1
res = ci*f_xi
total = 0

for i in range(0, n+1):
	if(n == i or i == 0):
		ci = 1
	else:
		ci = 2
	f_xi = func(xi)
	res = ci*f_xi
	xi = xi + h
	
	total += res
	print("[{}] - xi = {} | f_xi = {} | ci = {} | ci*f_xi = {}".format(i, xi-h, f_xi, ci, ci*f_xi))
	
print("---------------------\n")
print("Resposta | Th({}) {} * {} = {}".format(h, h/2, total, h/2*total ))