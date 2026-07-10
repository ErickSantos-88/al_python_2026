# Inicialização das variáveis
soma = 0
quantidade = 0
maior = None

print("Digite os números inteiros positivos (ou um número negativo para parar):")

while True:
    numero = int(input("Digite um número: "))
    
    # Condição de parada: se o número for negativo
    if numero < 0:
        break
        
    # Processamento dos números positivos
    soma += numero
    quantidade += 1
    
    # Verifica se é o maior número digitado até agora
    if maior is None or numero > maior:
        maior = numero

# Exibição dos resultados (apenas se pelo menos um número positivo foi digitado)
print("\n--- Resultados ---")
if quantidade > 0:
    media = soma / quantidade
    print(f"a) A soma de todos os números positivos: {soma}")
    print(f"b) A média aritmética: {media:.2f}")
    print(f"c) O maior número positivo: {maior}")
else:
    print("Nenhum número positivo foi informado.")
