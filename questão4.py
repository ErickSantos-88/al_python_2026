# Inicialização das variáveis
soma = 0
quantidade = 0
maior = None

print("Digite números inteiros positivos (ou um número negativo para parar):")

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

# Exibição dos resultados apenas se pelo menos um número positivo foi digitado
if quantidade > 0:
    media = soma / quantidade
    
    print("\n--- Resultados ---")
    print(f"a) Soma de todos os números positivos: {soma}")
    print(f"b) Média aritmética: {media:.2f}")
    print(f"c) Maior número informado: {maior}")
else:
    print("\nNenhum número positivo foi informado.")
