ano1 = int(input('Digite ano antigo: '))
ano2 = int(input('Digite ano recente: '))
bisextos = []
if ano1 > ano2:
  i = ano1 - ano2
else:
  i = ano2 - ano1 
while i > 0:
  if ano1 % 4 == 0:
    bisextos.append(ano1)
  if ano1 < ano2:
    ano1 += 1
  else:
    ano1 -= 1  
  i -=1
if ano2 % 4 == 0:
  bisextos.append(ano2)
print (bisextos)
