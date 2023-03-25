
#ALGORITIMO DE BUSCA SENQUENCIAL
lista=[int(x) for x in input().split()]
numero=int(input())
for y in range(len(lista)):
  if lista[y] == numero:
    print("numero encontrado")
    break
  elif y == len(lista)-1:
    print("numero não encontrado")