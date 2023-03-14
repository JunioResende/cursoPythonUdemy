print("Argumentos")
print("argumento1", "argumento2", 3)  # Os argumentos sao separados por virgula
print("========================================================")
print("Nova Linha Printada")
print(1)  # Ira printar uma nova linha na tela. O python interpreta os codigos da esquerda para a direita de cima para baixo
print("========================================================")
print("Separadores")
# Por padrao o python separa os argumentos printados em tela com um espaco. Podemos usar outros separadores com o argumento sep="seuSeparadorAqui(-,_,-> etc...)"
# Usamos o separador "-" para separar os argumentos. O retorno printado dessa funcao sera 1-2-3
print(1, 2, 3, sep="-")
print("========================================================")
# Para quebra de linha podemos usar \n que e um caracter que o sistema nao enxerga
print("Quebra de linha")
print("Junio", "Resende", sep="\n", end="\n############# <=============")
#################