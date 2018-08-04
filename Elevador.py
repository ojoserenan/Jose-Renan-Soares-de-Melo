numero_pessoa = 0
peso = 0
new_peso = -1
while (new_peso != 0 and numero_pessoa <7 and peso <=560 ):
  numero_pessoa +=1
  new_peso = int(input('novo peso:'))
  peso = peso + new_peso
if peso > 500:
  peso = peso - new_peso
  numero_pessoa -=1
print("peso total:",peso)
print("numero de pessoas:",numero_pessoa)
