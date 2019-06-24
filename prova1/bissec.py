import math
print("Metodo da Bissecao")
print("###############################")

def funcao(x):
    fx = x**3-10
    return fx

print("Qual o intervalo [a,b] da raiz e a precisao e?")
a=float(input("Entre com o inicio do intervalo: "))#inicio do intervalo
b=float(input("Entre com o fim do intervalo: "))#fim do intervalo
e=float(input("Entre com a precisao desejada: "))
i=0#contador
k=(math.log10(b-a)-math.log10(e)/math.log10(2))
k=math.ceil(k) 
print("Numero estimado de iteracoes: ",k)
if b-a<e:# se o intervalo a b for menor q a precio o programa acaba pegando o valor medio de a b
    x=(a+b)/2
    print("Raiz:", x)
else:
    while True:
        i+=1#incrementa o contador para medir o nmero de iteras
        x=(a+b)/2 #pega x como o ponto central do intervalo a b
        fxa=funcao(a)#calcula fx no ponto a
        fxb=funcao(b)#calcula fx no ponto b
        fx=funcao(x) #calcula fx no ponto x
        print("[%d] Fxa:%.3f | Fxb:%.3f | Xns:%.3f | Tolerancia Alcancada:%.3f | Ideal:%.3f"% (i, fxa, fxb, x, fx, e))
        if fx==0.0:#se fx de x for menor q a preci o programa acabar pegando x como resposta
            print("Raiz: ",x)
            break
        elif fxa*fx<0: #verifica se houve troca de sinal no valor de y a de a para x, se sim x e novo b
            b=x
        elif fxa*fx>0:#caso contrario x e o novo a
            a=x
        if b-a<e: # se o intervalo a b for menor q a precisao o programa acaba pegando o valor medio de a b
            x = (a + b) / 2
            print("Raiz:", x)
            print("Numero de iteracoes = ",i)
            break