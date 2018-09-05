lista = []
lista2 = []
lista3 = []
i = 0
j = 0
for i in range(1,5):
  i = int(input(""))
  lista.append(i)
for j in range(1,3):
  j = int(input(""))
  lista2.append(j)
for i in lista :
  if i in lista2:
    lista3.append(i)
print(lista3)
