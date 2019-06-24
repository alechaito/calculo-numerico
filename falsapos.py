#Author Leonardo Lisboa
import math
print("Metodo da Posicao Falsa")
print("###############################")
def funcao(x):
    fx = x**3-9*x+3
    return fx
print("Qual o intervalo [a,b] da raiz e a precisao e?")
a =float(input("Entre com a: "))
b =float(input("Entre com b: "))
e =float(input("Entre com e: "))
i = 0

k=(math.log10(b-a)-math.log10(e)/math.log10(2))
k=math.ceil(k)
print("Numero estimado de iteracoes: ",k)
print("###############################")


while True:
    i+=1
    fxa=funcao(a)
    fxb=funcao(b)
    x=(a*fxb-b*fxa)/(fxb-fxa)
    fx=funcao(x)
    #########################
    print("[%d] Fxa:%.3f | Fxb:%.3f | Xns:%.3f | Tolerancia Alcancada:%.3f | Ideal:%.3f"% (i, fxa, fxb, x, fx, e))
    #################
    if abs(fxa) < e:
        x=a
        break
    elif abs(fxb) < e:
        x=b
        break
    elif abs(fx) < e:
        break
    elif fxa*fx<0:
        b=x
    elif fxa*fx >0:
        a=x
    elif b-a<e:
        x=(b+a)/2
print("Raiz =",x)
print("Iteracoes = ",i)