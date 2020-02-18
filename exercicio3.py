import random
qt=int(input("Insira quantos elementos você deseja na lista: "))
contador= 0
lista = []
while contador < qt:
    lista.append(random.randint(0,1000))
    contador=contador+1
print("Lista: ",lista)
print("O maior valor é: ",max(lista))
print("O menor valor é: ",min(lista))"""
