n1 = int(input("Digite um numero: "))  # Convertendo a entrada para inteiro
sinal = (input("Digite um sinal: "))
n2 = int(input("Digite outro numero "))  # Convertendo a entrada para inteiro


if sinal == "+":
	op = n1 + n2

elif sinal == "-":
	op = n1 - n2

elif sinal == "*":
	op == "*"
elif sinal == "/":
	op = n1 / n2
else:
	print("Sinal inválido")
print(op)

