usuarios = []

while True:
    print("\n--- MENU ---")
    print("1. Cadastrar usuário")
    print("2. Listar usuários")
    print("3. Buscar usuário")
    print("4. Remover usuário")
    print("5. Sair")
    
    opcao = input("Escolha uma opção: ")
    
    if opcao == "1":
        nome = input("Digite o nome do usuário: ")
        usuarios.append(nome)
        print(f"Usuário '{nome}' cadastrado com sucesso!")
        
    elif opcao == "2":
        if not usuarios:
            print("Nenhum usuário cadastrado ainda.")
        else:
            print("\nLista de usuários:")
            for i, u in enumerate(usuarios):
                print(f"{i + 1}. {u}")
                
    elif opcao == "3":
        busca = input("Digite o nome que quer buscar: ")
        if busca in usuarios:
            print(f"O usuário '{busca}' está cadastrado!")
        else:
            print("Usuário não encontrado.")
            
    elif opcao == "4":
        remover = input("Digite o nome do usuário que deseja remover: ")
        if remover in usuarios:
            usuarios.remove(remover)
            print(f"Usuário '{remover}' removido com sucesso!")
        else:
            print("Usuário não encontrado na lista.")
            
    elif opcao == "5":
        print("Saindo do sistema...")
        break
    else:
        print("Opção inválida, tenta de novo.")
