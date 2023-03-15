email_digitado = input("Digite seu email: ")
senha_digitada = input("Digite sua senha: ")
email_permitido = "junio@email.com"
senha_permitida = "123456"

if email_digitado == email_permitido and senha_digitada == senha_permitida:
    # Para Logar as duas condicoes precisam ser verdadeiras. email tem que ser junio@email.com e senha tem que ser 123456
    print("Login efetuado com sucesso!")
else:
    # Caso uma das condicoes nao sejam verdadeiras.
    print("Acesso negado! Verifique as credenciais.")
