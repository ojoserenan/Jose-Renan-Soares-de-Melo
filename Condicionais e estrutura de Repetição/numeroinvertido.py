n = int(input("Digite uma entrada:"))
tam = len(str(n))
count = 0
invert = 0
while (tam>=1):
  tam = tam - 1
  poten = 10**tam
  v = int(n/poten)
  invert = invert + v*(10**count)
  n = n%poten
  count = count + 1
print(invert)
