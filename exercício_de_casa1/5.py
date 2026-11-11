import random

[span_1](start_span)[span_1](end_span)
rifas = []

print("Digite os nomes (ou 'sair' para terminar):")
while True:
  nome = input("Nome: ")
  if nome.lower() == "sair":
    break
  if nome.strip():
    rifas.append(nome)

[span_2](start_span)[span_2](end_span)
if rifas:
  ganhador = random.choice(rifas)
  print(f"\nO ganhador da rifa é: {ganhador}")
else:
  print("\nNenhum participante cadastrado.")
