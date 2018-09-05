n1 = 0
tam = 0
loop = int(input("quantos numeros:"))
while loop > 0:
  n = float(input("digite quais:"))
  if n > 0 and n % 2 == 0: 
    n1 = n1 + n
    tam +=1
  loop -=1
print(n1/tam)
