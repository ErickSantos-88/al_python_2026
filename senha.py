# Inicializa a variável com um valor vazio para entrar no loop
senha = ""

# Enquanto a senha digitada não for a correta, o loop continua
while senha != "12345":
    senha = input("Digite a senha: ")
    
    if senha != "12345":
        print("Tente novamente")

# Quando sai do loop, significa que a senha está correta
print("Acesso liberado")
