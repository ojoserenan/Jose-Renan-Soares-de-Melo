listaano = []
listavelo = []
continuar = input("Deseja adicionar algum veiculo s ou n ?")
if continuar == "n" or continuar == "N":
	print("Nenhum dado coletado")
while continuar == "s" or continuar == "S":
	ano = int(input("Digite o ano do carro:"))
	velocidade = float(input("Digite a velocidade do carro:"))
	listaano.append (ano)
	listavelo.append (velocidade)
	continuar = input("Deseja adicionar mais algum s ou n ?")
	if continuar == "n" or continuar == "N":
		maiorvel = max(listavelo)
		maiorano = max(listaano)
		mediavel = (sum(listavelo))/(len(listavelo))
if len(listaano)!=0:
  print ("A maior velocidade encontrada foi de {:.2f}km/h o carro mais novo é de {} e a media de velocidade é {:.2f} km/h".format (maiorvel,maiorano,mediavel)) km/h".format (maiorvel,maiorano,mediavel))

