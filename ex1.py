n1 = float(input("Nota 1: "))
resp = "s"
while resp in "sS":
    while n1 < 0 or n1 > 10:
        n1 = float(input("Digite novamente: "))

    n2 = float(input("Nota 2: "))
    while n2 < 0 or n2 > 10:
            n2 = float(input("Digite novamente: "))

    media = (n1 + n2)/2
    print(media)
    resp = input("Deseja fzr outro calculo n/s?: ")