palavra_secreta = "python"
letras_descobertas = ["_" for _ in palavra_secreta]
erros = 0
limite_erros = 6
letras_tentadas = []

print("=== JOGO DA FORCA ===")

while erros < limite_erros and "_" in letras_descobertas:
    print("\nPalavra:", " ".join(letras_descobertas))
    print(f"Erros: {erros}/{limite_erros}")
    
    chute = input("Digite uma letra: ").lower()
    
    if chute in letras_tentadas:
        print("Você já tentou essa letra, mano. Tenta outra.")
        continue
        
    letras_tentadas.append(chute)
    
    if chute in palavra_secreta:
        print("Boa! Acertou uma letra.")
        for i in range(len(palavra_secreta)):
            if palavra_secreta[i] == chute:
                letras_descobertas[i] = chute
    else:
        print("Errou! Essa letra não tem na palavra.")
        erros += 1

if "_" not in letras_descobertas:
    print("\nParabéns! Você venceu, a palavra era:", palavra_secreta)
else:
    print("\nGame Over! Você estourou o limite de erros. A palavra era:", palavra_secreta)
