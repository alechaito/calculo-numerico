#Author Leonardo Lisboa
import math
print("Metodo de Newton")
print("###############################")
print("Qual a aproximacao inicial X0 e a precisao e?")

x0 = float(input("Entre com x0:"))
e = float(input("Entre com e:"))
i=0
cd=8 #numero de casa decimais para arredondamento de Wx

def funcao(x):
    fx = (2*x)-math.sin(x)-4
    return fx

def funcao_d1(x):
    fx = 2-math.cos(x)
    return fx

def funcao_d2(x):
    fx = math.sin(x)
    return fx

def Wx(x): # Funcao de interacao
    ## X[i+1] = X[i]-f[x(i)]/f[x(i)]
    Wx = x - (funcao(x)/funcao_d1(x))
    print("[X_i:%d] Fx: %.5f | F'X: %.5f"% (x, funcao(x), funcao_d1(x)))
    return Wx

#Fazendo as iteracoes
while True:
    i+=1
    x = Wx(x0)
    print("[%d] x_i: %.5f | x_i+1: %.5f | erro: %.3f | tolerancia:%.3f "% (i, x0, x, abs(x-x0), e))
    if abs(x-x0)<e:
        break
    else:
        x0 = x

print("Raiz = ",x)
print("Iteracoes = ",i)