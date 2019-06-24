import numpy as np
#rom matplotlib.pyplot import *

#x1 = np.array([-3, -1.7, -0.5, 1.0, 2.3, 3.1, 5.1])  
#yi = np.array([-35, -20.5, -5.7, 7.6, 16.8, 21.4, 27.4])

#x2 = np.array([-3**2, -1.7**2, -0.5**2, 1.0**2, 2.3**2, 3.1**2, 5.1**2])  
#x3 = np.array([-3**3, -1.7**3, -0.5**3, 1.0**3, 2.3**3, 3.1**3, 5.1**3])  
#x4 = np.array([-3**4, -1.7**4, -0.5**4, 1.0**4, 2.3**4, 3.1**4, 5.1**4]) 

x1 = np.array([-3, -1.7, -0.5, 1.0, 2.3, 3.1, 5.1])  
yi = np.array([-35, -20.2 , -5.7, 7.6, 16.8, 21.4, 27.4])

x2 = np.array([abs(-3**2), abs(-1.7**2), abs(-0.5**2), 1.0**2, 2.3**2, 3.1**2, 5.1**2])  
x3 = np.array([-3**3, -1.7**3, -0.5**3, 1.0**3, 2.3**3, 3.1**3, 5.1**3])  
x4 = np.array([abs(-3**4), abs(-1.7**4), abs(-0.5**4), 1.0**4, 2.3**4, 3.1**4, 5.1**4])  


print(x1)
print(x2)
print(x3)
print(x4)
print("------------------")
## SOMATORIOS
sum_x1 = np.sum(x1)
sum_x2 = np.sum(x2)
sum_x3 = np.sum(x3)
sum_x4 = np.sum(x4)
sum_yi = np.sum(yi)

sum_yi_x1 = 0
for i in range(len(x1)):
	#Sum f(x)*x
	sum_yi_x1 += (yi[i]*x1[i])
	
sum_yi_x2 = 0
for i in range(len(x2)):
	#Sum f(x)*x
	sum_yi_x2 += (yi[i]*x2[i])
	
print("sum_x1:{}, sum_x2:{}, um_x3:{}, sum_x4:{}, sum_yi:{}, sum_y_x1:{}, sum_y_x2:{}".format(sum_x1, sum_x2, sum_x3, sum_x4, sum_yi, sum_yi_x1, sum_yi_x2))
A = np.matrix([[len(x1), sum_x1, sum_x2], [sum_x1, sum_x2, sum_x3], [sum_x2, sum_x3, sum_x4] ])
Y = np.matrix([[sum_yi], [sum_yi_x1], [sum_yi_x2] ])
print(A)
print("------------------")
print(Y)
# a1 + a2 * x
FI = np.linalg.solve(A, Y)
print("------------------")
print("A melhor reta que passa pelos pontos tem o seguinte coeficientes:{}+{}*x+{}*x**2".format(FI[0], FI[1], FI[2]))
print("------------------")
print("------------------")
print("Valor de FI no ponto 4:{}".format(FI[0]+FI[1]*4+FI[2]*16))
print("------------------")
#exit()
print("FI ate x iteracoes \n")

a_0 = 	float(FI[0])
a_1 =  	float(FI[1])
a_2 =  	float(FI[2])

fi_xi = []

for x in x1:
	#print("fi_xi({}) = {} ".format(x, FI[0] + FI[1]*x ))
	dob = abs(x**2)
	val = a_0 + (a_1*x) + (a_2*dob)

	fi_xi.append(float(val))

print(fi_xi)
#exit()

print("------------------")

print("Residuo ate x iteracoes \n")
r_xi = []
for i in range(0, 7):
	val = yi[i] - fi_xi[i]
	r_xi.append(val)
	
print(r_xi)
print("------------------")
print("Residuo ao quadrado ate x iteracoes \n")
r_xii = []
for i in range(0, 7):
	val = r_xi[i]**2
	r_xii.append(val)
	
print(r_xii)

print("------------------")
print("Soma dos quadrados dos residuos:{}".format(sum(r_xii)))

#V = np.array([np.sin(np.pi*xi),np.cos(np.pi*xi)]).transpose()  
#a = ((np.linalg.inv((V.transpose()).dot(V))).dot(V.transpose())).dot(yi)