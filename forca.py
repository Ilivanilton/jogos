def jogar():
    print("*********************************")
    print("***Bem vindo ao jogo da Forca!***")
    print("*********************************")

    palavra_secreta = "banana"
    letras_acertadas = ["_","_","_","_","_","_"]

    enforcou = False
    acertou = False

    while not acertou and not enforcou:
        chute = input("Qual letra?").lower().strip()

        idx = 0
        for letra in palavra_secreta:
            if letra == chute:
                print("Acertou a letra {} na posição {}".format(chute, idx))
                letras_acertadas[idx] = chute
            idx = idx + 1
        print("====================")
        print(letras_acertadas)
        print("====================")
        print("Jogando...")

    print("Fim do jogo")


if(__name__ == "__main__"):
    jogar()
