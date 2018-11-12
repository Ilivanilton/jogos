def jogar():
    print("*********************************")
    print("***Bem vindo ao jogo da Forca!***")
    print("*********************************")

    palavra_secreta = "banana".upper()
    letras_acertadas = ["_" for letra in palavra_secreta]

    #for letra in palavra_secreta:
     #   letras_acertadas.append("_")

    enforcou = False
    acertou = False
    erros = 0

    while not acertou and not enforcou:

        chute = input("Qual letra?").upper().strip()

        if(chute in palavra_secreta):
            idx = 0
            for letra in palavra_secreta:
                if letra == chute:
                    print("Acertou a letra {} na posição {}".format(chute, idx))
                    letras_acertadas[idx] = chute
                idx += 1
            print("====================")
            print(letras_acertadas)
            print("====================")
            print("Jogando...")
        else:
            erros += 1
        enforcou = erros == 6
        acertou = "_" not in letras_acertadas
    print("Fim do jogo")


if(__name__ == "__main__"):
    jogar()
