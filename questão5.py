while True:
    print("\n" + '-' * 50)
    print("MENU BLACK FRIDAY")
    print("[1] A vista 15% de desconto")
    print("[2] Cartão de debito 10% de desconto")
    print("[3] Cartão de credito 5% de desconto")
    print("[0] Sair do programa")
    print('-' * 50)
    
    opcao = int(input("Selecione a opção desejada: "))
    
    # Condição de parada: se a opção for 0, o programa fecha
    if opcao == 0:
        print("Programa encerrado. Até logo!")
        break
        
    # Se a opção for válida (1, 2 ou 3), o programa pede o valor do produto
    if opcao in [1, 2, 3]:
        valor = float(input("Digite o valor do produto: R$ "))
        
        if opcao == 1:
            print(f"O valor do desconto é de R$ {valor * 0.15:.2f} e o valor final a ser pago é de R$ {valor * 0.85:.2f}")
        elif opcao == 2:
            print(f"O valor do desconto é de R$ {valor * 0.10:.2f} e o valor final a ser pago é de R$ {valor * 0.90:.2f}")
        elif opcao == 3:
            print(f"O valor do desconto é de R$ {valor * 0.05:.2f} e o valor final a ser pago é de R$ {valor * 0.95:.2f}")
            
    else:
        print("Opção inválida! Tente novamente.")
