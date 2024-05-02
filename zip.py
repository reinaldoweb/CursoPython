lista1 = [1,2,3,4,5]
lista2 = ["abacate", "abacaxi", "Uva", "mamão", "LARANJA"]
lista3 = ["R$5,00","R$7,00", "R$9,00","R$5,00", "R$8,00"]

for numero, nome, valor in zip(lista1, lista2, lista3):
	print(numero, nome, valor)