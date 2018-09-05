crianca1 = 0
crianca2 = 0
remessa  = 0
continuar = 'sim'
count = 0
while True:
  if continuar == 'sim':
    idade = int(input('idade'))
    if idade <= 2:
      crianca1 = (crianca1 + 9*30)
    else:
      crianca2 = (crianca2 + 6*30)
    continuar = input('continuar? ')
  else:
    break
soma = crianca1 + crianca2
while remessa < soma:
  remessa += 100
  count += 1
print(count)
print(remessa - soma)
