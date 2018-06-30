monetario = float(input("Digite um valor de saque:"))
total = monetario
ced100 = 0
ced50 = 0
ced20 = 0
ced10 = 0
ced5 = 0
ced2 = 0
moe1 = 0
moe050 = 0
moe025 = 0
moe010 = 0
moe005 = 0
moe001 = 0
while total > 100:
  total = total - 100
  ced100 = ced100 + 1
while total > 50:
  total = total - 50
  ced50 = ced50 + 1
while total > 20:
  total = total - 20
  ced20 = ced20 + 1
while total > 10:
  total = total - 10
  ced10 = ced10 + 1
while total > 5:
  total = total - 5
  ced5 = ced5 + 1
while total > 2:
  total = total - 2
  ced2 = ced2 + 1
while total > 1:
  total = total - 1
  moe1 = moe1 + 1
while total > 0.50:
  total = total - 0.50
  moe050 = moe050 + 1
while total > 0.25:
  total = total - 0.25
  moe025 = moe025 + 1
while total > 0.10:
  total = total - 0.10
  moe010 = moe010 + 1
while total > 0.05:
  total = total - 0.05
  moe005 = moe005 + 1
while total > 0.01:
  total = total - 0.01
  moe001 = moe001 + 1
print ("NOTAS:")
print (ced100,"Nota(s) de R$ 100.00")
print (ced50,"Nota(s) de R$ 50.00")
print (ced20,"Nota(s) de R$ 20.00")
print (ced10,"Nota(s) de R$ 10.00")
print (ced5,"Nota(s) de R$ 5.00")
print (ced2,"Nota(s) de R$ 2.00")
print ("MOEDAS:")
print (moe1,"Moeda(s) de R$ 1.00")
print (moe050,"Moeda(s) de R$ 0.50")
print (moe025,"Moeda(s) de R$ 0.25")
print (moe010,"Moeda(s) de R$ 0.10")
print (moe005,"Moeda(s) de R$ 0.05")
print (moe001,"Moeda(s) de R$ 0.01")
