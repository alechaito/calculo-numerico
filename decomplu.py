import numpy as np


A = np.matrix([
	[1, 2, -1],
	[2, 3, -2],
	[1, -2, 1]
])

B = [2, 3, 0]

def fatoraLU(A):  
    U = np.copy(A)  
    n = np.shape(U)[0]  
    L = np.eye(n)  
    for j in np.arange(n-1):  
        for i in np.arange(j+1,n):  
            L[i,j] = U[i,j]/U[j,j]  
            for k in np.arange(j+1,n):  
                U[i,k] = U[i,k] - L[i,j]*U[j,k]  
            U[i,j] = 0  
    return L, U

L, U = fatoraLU(A)

Y = np.linalg.solve(L, B)
X = np.linalg.solve(U, Y)

print("Vetor Y transposto")
print(Y)
print("------------------")
print("Vetor X transposto")
print(X)