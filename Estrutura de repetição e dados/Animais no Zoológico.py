lista = []
lista2 = []
lista3 = []
media = 0
count2 = 0
count3 = 0
animal = input('animal')
peso = float(input('peso'))
pais = input('pais')
lista.append(animal)
lista2.append(peso)
lista3.append(pais)
if pais  == 'Venezuela' and animal == 'cobra':
  count3 += 1
if animal == 'tigre':
  media = peso
  count2 += 1
saida = input('continuar ?')
while True:
  if saida == 'parrar' or saida == 'PARRAR':
    break
  else:
    animal = input('animal')
    peso = float(input('peso'))
    pais = input('pais')
    lista.append(animal)
    lista2.append(peso)
    lista3.append(pais)
    if pais  == 'Venezuela' and animal == 'cobra':
      count3 += 1
    if animal == 'tigre':
      media = media + peso
      count2 += 1
    saida = input('continuar ?')
if media != 0:
  media = (media/count2)
count = 0
i = 0
for i in range (0, len(lista)):
  if lista[i] == 'macaco':
    count += 1
  i += 1
print(count)
print('{:.2f}'.format(media))
print(count3)
