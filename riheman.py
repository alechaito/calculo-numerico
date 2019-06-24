import numpy as np

f = lambda x: x/(1+x**2)  
 
A = 0  
B = 1 
n = 10  
h = (B-A)/n 
print("h:{}".format(h))
print("----------------- \n")
x = np.linspace(A, B, n+1)  
 
s_esq = 0  
s_dir = 0  
s_med = 0  
 
print("Soma de Riemman de {} a {} com {} intervalos:\n".format(A, B, n))  

r_fxi = []
a = 0
b = 0.1
xi = a+b/2
f_xi = f(xi)
vec_fxi = []
#print("i:0| a:{}| b:{}| xi:{}| fxi:{}|".format(a, b, xi, f_xi))

for i in range(n):
	xi = (a+b)/2
	f_xi = f(xi)
	vec_fxi.append(f_xi)
	print("i:{}| a:{}| b:{}| xi:{}| fxi:{}|".format(i+1, a, b, xi, f_xi))
	a = b
	b += 0.1
	
print("----------------- \n")
print("Total fxi:{}".format(sum(vec_fxi)))
print("----------------- \n")
print("R(h):{}".format(h*sum(vec_fxi)))
#print(r_fxi)