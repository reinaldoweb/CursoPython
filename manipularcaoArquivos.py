arquivo = open("meuArquivo.txt")

texto = arquivo.read()

print(texto)

w = open("meuArquivo2.txt", "w")
w.write("Esse é meu novo arquivo")

w.close()