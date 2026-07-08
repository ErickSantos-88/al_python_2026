# Define as credenciais corretas
usuario_correto = "aluno"
senha_correta = "12345"

# Inicializa o contador de tentativas
tentativas = 0
limite_tentativas = 3

while tentativas < limite_tentativas:
    # Recebe os dados do usuário
    usuario = input("Digite o usuário: ")
    senha = input("Digite a senha: ")
    
    # Soma 1 ao número de tentativas feitas
    tentativas += 1
    
    # Verifica se o usuário e senha estão corretos
    if usuario == usuario_correto and senha == senha_correta:
        print("Acesso liberado")
        break  # Encerra o programa se estiver correto
        
    else:
        # Se errou, mas ainda não atingiu o limite de 3 tentativas
        if tentativas < limite_tentativas:
            print("Tente novamente\n")
        else:
            # Se errou e atingiu a 3ª tentativa
            print("Você tentou 3 vezes")
