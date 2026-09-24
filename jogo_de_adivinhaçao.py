("Samuel e Erick Santos")

import random

def jogar():
    while True:
        print("\n=== JOGO DA ADIVINHAÇÃO ===")
        print("Escolha o nível de dificuldade:")
        print("1 - Fácil (1 a 10)")
        print("2 - Médio (1 a 20)")
        print("3 - Difícil (1 a 30)")
        
        opcao = input("Digite a opção desejada (1, 2 ou 3): ")
        
        if opcao == '1':
            limite_maximo = 10
        elif opcao == '2':
            limite_maximo = 20
        elif opcao == '3':
            limite_maximo = 30
        else:
            print("Opção inválida! O nível Fácil (1 a 10) será selecionado por padrão.")
            limite_maximo = 10

        numero_sorteado = random.randint(1, limite_maximo)
        chances = 3
        acertou = False

        print(f"\nTente adivinhar o número entre 1 e {limite_maximo}. Você tem 3 tentativas!\n")

        for tentativa in range(1, chances + 1):
            try:
                chute = int(input(f"Tentativa {tentativa} de {chances}. Digite seu palpite: "))
            except ValueError:
                print("Por favor, digite apenas números inteiros válidos.")
                continue

            if chute == numero_sorteado:
                print("Parabéns, você acertou!")
                acertou = True
                break
            else:
                print("Você errou!")
                if chute > numero_sorteado:
                    print("Tente um número menor")
                else:
                    print("Tente um número maior")
                print("-" * 20)

        if not acertou:
            print(f"Você perdeu! Fim de jogo. O número sorteado era {numero_sorteado}.")

        jogar_novamente = input("\nDeseja jogar novamente? (s/n): ").strip().lower()
        if jogar_novamente != 's':
            print("Obrigado por jogar! Até a próxima.")
            break

if __name__ == "__main__":
    jogar()
