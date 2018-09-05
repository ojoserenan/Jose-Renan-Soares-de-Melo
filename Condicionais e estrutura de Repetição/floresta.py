n = int(input(""))
count = 0
possivel = 5
arvore = 3
i = 0
while (i*i <= n/2):
  if ((n - possivel)% arvore == 0):
    count +=1
  possivel +=3
  arvore += 2
  i +=1
print(count)
