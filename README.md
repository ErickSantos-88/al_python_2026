 
# Solicita os dados ao usuário
cargo = input("Digite o cargo do funcionário: ").strip()
salario = float(input("Digite o salário atual do funcionário: "))

# Inicializa a variável para o percentual de aumento
aumento = 0.0
cargo_valido = True

# Verifica o cargo e define o percentual de aumento correspondente
# Usamos .lower() para evitar problemas com letras maiúsculas/minúsculas
if cargo.lower() == "programador de sistemas":
    aumento = 0.30  # 30%
elif cargo.lower() == "analista de sistemas":
    aumento = 0.20  # 20%
elif cargo.lower() == "analista de banco de dados":
    aumento = 0.15  # 15%
else:
    cargo_valido = False

# Calcula e exibe o resultado
if cargo_valido:
    novo_salario = salario * (1 + aumento)
    print(f"Novo salário: R$ {novo_salario:.2f}")
else:
    print("Cargo inválido")
