num = int(input("Digite uma entrada:"))
i = 1
triangulo = 0
while triangulo < num:
  triangulo = i*(i+1)*(i+2)
  i = i+1
if triangulo == num:
  print (i,"*",i+1,"*",i+2,"=",num )
  print ("\n verdadeiro")
else:
  print ("falso")
