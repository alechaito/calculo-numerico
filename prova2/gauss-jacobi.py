from pprint import pprint
from numpy import array, zeros, diag, diagflat, dot

TOL = 0.02
erros = []
#-----------------
A = array([
	[10.0, -2.0, 1.0], # 10 > 3 elemento da diagonal deve ser maior que os outros 2 elementos em valor absoluto
	[1.0, 12.0, 5.0],   # 12 > 6
	[1.0, 5.0, -10.0] # 10 > 6
	#[10.0, 1.0, 1.0],
	#[2.0, 8.0, -4.0],
	#[1.0, 5.0, 9.0]
])
#-----------------
b = array(
	#[12.0, 6.0, 15.0]
	[5, 3.0, 10.0]
)
#-----------------

def jacobi(A, b):

	"""Solves the equation Ax=b via the Jacobi iterative method."""
	# Create an initial guess if needed                                                                                                                                                            
	init = None
	if init is None:
		x = zeros(len(A[0]))

	# Create a vector of the diagonal elements of A                                                                                                                                                
	# and subtract them from A                                                                                                                                                                     
	D = diag(A)
	R = A - diagflat(D)

	# Iterate for N times
	old_x = x
	for i in range(0, 20):
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
		x = (b - dot(R,x)) / D
		#print(x)
		if(i == 0):
			print("N={} | x1=0 | x2=0 | x3=0 | er1= X | er2= X | er3= X \n".format(i))
		else:
			print("N={} | x1={} | x2={} | x3={} | er1={} | er2={} | er3={} \n".format(i, x[0], x[1], x[2], er1, er2, er3))
	return x


sol = jacobi(A, b)
print("------------------\n")
print("FIM -> x1={} | x2={} | x3={} | er1={} | er2={} | er3={} \n".format(sol[0], sol[1], sol[2], erros[-1][0], erros[-1][1], erros[-1][2]))
print("solution: {}".format(sol))