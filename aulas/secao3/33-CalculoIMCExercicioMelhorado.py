nome = input("Qual o seu nome? ")
idade = int(input("Qual a sua idade? "))
peso = float(input("Qual o seu peso? "))
altura = float(input("Qual a sua altura? "))
imc = peso / altura ** 2

print(f"{nome} tem {idade} anos, pesa {peso}kg, mede {altura}m e seu IMC e de {imc:.2f}")
