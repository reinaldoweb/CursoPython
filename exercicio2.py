nome = input("Digite o nome do arquivo que deseja abrir: ")

meu_arquivo = open(nome)

linhas = meu_arquivo.readlines()

for linha in linhas:
 print(linha.strip())