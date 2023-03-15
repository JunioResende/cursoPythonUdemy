nome = "Junio"
altura = 1.88
peso = 130
imc = peso / altura ** 2

# Para exibir um texto formatado basta usar a flag f "f-strings"
# Nesse metodo usa-se as variaveis entre chaves{}
print(f"{nome} tem{altura: .2f}, pesa{peso} e seu IMC e de {imc: .2f}")
# Para formatar as casas decimais usamos ."quantidade de casas desejadas"f, no exemplo usamos duas casas entao .2f
