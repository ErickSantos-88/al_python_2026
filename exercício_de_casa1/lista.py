produtos = []

while True:
    nome_produto = input("Digite o nome do produto eletrônico: ")
    produtos.append(nome_produto)
    
    continuar = input("Deseja adicionar outro? (s/n): ").lower()
    if continuar != 's':
        break

print("\n--- Lista de Produtos Eletrônicos Recebida ---")
for i, prod in enumerate(produtos):
    print(f"{i + 1}. {prod}")