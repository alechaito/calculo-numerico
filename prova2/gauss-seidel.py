import numpy as np
#from scipy.linalg import solve

TOL = 0.02
A = np.array([
	[10.0, 1.0, 1.0], 
	[2.0, 8.0, -4.0], 
	[1.0, 5.0, 9.0]
])
b = [12.0, 6.0, 15.0]

x = [0, 0.750, 1.250]

n = 9

erros = []

def gauss(A, b, x, n):
	L = np.tril(A)
	U = A - L
	old_x = x
	for i in range(n):
		if(len(old_x) > 0 ):
			er1 = abs(old_x[0] - x[0])
			er2 = abs(old_x[1] - x[1])
			er3 = abs(old_x[2] - x[2])
			erros.append([er1, er2, er3])
			if( er1 < TOL and er2 < TOL and er3 < TOL and er1 !=0):
				break
			#print("er1={}, er2={}, er3={}".format(er1, er2, er3))
		else:
			er1 = x[0]
			er2 = x[1]
			er3 = x[2]
		old_x = x
		x = np.dot(np.linalg.inv(L), b - np.dot(U, x))
		#print(str(i).zfill(3))
		if(i == 0):
			print("N={} | x1=0 | x2=0 | x3=0 | er1= X | er2= X | er3= X \n".format(i))
		else:
			print("N={} | x1={} | x2={} | x3={} | er1={} | er2={} | er3={} \n".format(i, x[0], x[1], x[2], er1, er2, er3))
	return x

'''___MAIN___'''

sol = gauss(A, b, x, n)
print("------------------\n")
print("FIM -> x1={} | x2={} | x3={} | er1={} | er2={} | er3={} \n".format(sol[0], sol[1], sol[2], erros[-1][0], erros[-1][1], erros[-1][2]))
