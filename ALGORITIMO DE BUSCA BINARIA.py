#ALGORITMO DE BUSCA BINARIA:
lista=[int(x) for x in input().split()]
numero=int(input())
esquerda=0
direita= len(lista)-1
print(direita)
while esquerda <= direita:
  meio=(esquerda+direita)//2
  if lista[meio] == numero:
     print("numero encontrado")
     break
  elif numero < lista[meio]:
    direita = meio - 1
  else:
    esquerda= meio + 1
print(meio)
  
if lista[meio] == numero:
  print("meio")
else:
  print("-1")