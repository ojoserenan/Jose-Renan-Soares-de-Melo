num = int(input("Digite a entrada:"))
i = 1
j = 1
k = 1
triangulo = 0
while triangulo < num:
  triangulo = i*(j+1)*(k+2)
  i = i+1
  j = j+1
  k = k+1
if triangulo == num:
  print(i-1,j,k+1)
  print("triangular")
else:
  print ("não é triangular")
