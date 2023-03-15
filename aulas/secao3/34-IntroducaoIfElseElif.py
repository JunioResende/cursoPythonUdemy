# if / elif / else
# se / se nao se / se nao

entrada = input("Voce vai entrar ou sair do sistema? ")

if entrada == "entrar":  # Verifica se uma condicao e valida(verdadeira)
    print("Voce entrou no sistema!")  # Se for verdade ira executar esse trecho
elif entrada == "sair":  # Verifica se a outra condicao e valida
    print("Voce saiu do sistema!")  # Se for verdade ira executar esse trecho
else:
    # Se nenhuma condicao for valida executara esse trecho
    print("Voce nao digitou se quer entrar ou sair do sistema!")
