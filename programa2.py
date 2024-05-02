nota1 = int(input("Digite a primeira nota: "))  # Convertendo a entrada para inteiro
nota2 = int(input("Digite a segunda nota: "))  # Convertendo a entrada para inteiro

nota = nota1+nota2
notafinal = nota / 2
print(notafinal)
if notafinal >= 6:
 	print("Aprovado")
else:
	print("Reprovado")

