def calculadora():
    while True:
        # 1. Imprime o menu de opções
        print("\n--- MENU DA CALCULADORA ---")
        print("1 - Somar")
        print("2 - Subtrair")
        print("3 - Multiplicar")
        print("4 - Dividir")
        print("0 - Sair")
        
        # Recebe a opção do usuário
        opcao = input("Escolha uma opção: ")
        
        # 2. Verifica se o usuário quer sair do programa
        if opcao == "0":
            print("Encerrando o programa. Até mais!")
            break  # Interrompe o laço while, parando o programa
            
        # 3. Verifica se a opção digitada é válida
        elif opcao in ["1", "2", "3", "4"]:
            # Recebe os dois números apenas se a opção for válida
            num1 = float(input("Digite o primeiro número: "))
            num2 = float(input("Digite o segundo número: "))
            
            # Executa a operação correspondente
            if opcao == "1":
                resultado = num1 + num2
                print(f"Resultado da Soma: {resultado}")
            elif opcao ==
