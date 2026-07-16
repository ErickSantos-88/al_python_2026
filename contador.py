# Inicializa o contador de números pares
pares = 0

# Loop para ler exatamente 10 números
for i in range(10):
    numero = int(input(f"Digite o {i+1}º número inteiro positivo: "))
    
    # Verifica se o número é par (resto da divisão por 2 é igual a 0)
    if numero % 2 == 0:
        pares += 1

# Exibe o resultado final
print(f"Quantidade de números pares informados: {pares}")
