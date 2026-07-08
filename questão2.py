# Inicializa a variável que vai guardar a soma
somatorio = 0

print("Digite 10 números inteiros:")

# O laço vai repetir 10 vezes (de 0 a 9)
for i in range(10):
    numero = int(input(f"Digite o {i+1}º número: "))
    somatorio += numero  # Soma o número digitado ao total acumulado

# Imprime o resultado final
print(f"\nO resultado do somatório de todos eles é: {somatorio}")
