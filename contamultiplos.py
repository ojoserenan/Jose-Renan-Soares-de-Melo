n1 = int(input("Digite um numero:"))
n2 = int(input("Digite um numero:"))
n = 50
count = 0
while n > 0:
  if n % n1 == 0 and n % n2 == 0:
    count +=1
  n -=1
print(count)
