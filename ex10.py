while True:
    numb = int(input("Digite um numero: "))
    print("Digite 1 para mostrar o antecessor.")
    print("Digite 2 para mostrar o sucessor.")
    print("Digite 3 para encerrar o programa.")

    escolha = (input("Escolha uma opçao: "))

    if escolha == "1":
        antece = numb - 1
        print("O antecessor de", numb, "é:", antece)
    elif escolha == "2":
        numb = int(input("Digite um numero inteiro: "))
        sucessor = numb + 1
        print("O sucessor de", numb, "é:", sucessor)
        print("Digita um numero animal")
    elif escolha == "3":
        print("Programa encerrado.")
        break
    else:
        print("Opçao invalida. Escolha entre 1, 2, e 3.")
