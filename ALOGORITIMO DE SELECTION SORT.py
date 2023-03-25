#ALGORITIMO SELECTION SORT
def orden_add(lista):
  for i in range(0,len(lista)):
    inicio=i
    
    for j in range(i+1,len(lista)):
      if lista[j] < lista[i]:
        inicio=j
        lista[inicio], lista[i] = lista[i], lista[inicio]
lista=[int(x) for x in input().split()]
orden_add(lista)
print(lista)


