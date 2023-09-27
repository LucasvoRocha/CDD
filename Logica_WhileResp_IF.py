resp = "s"
while resp == "s":
    n1 = float(input("Nota 1: "))
    n2 = float(input("Nota 2: "))
    n3 = float(input("Nota 3: "))
    n4 = float(input("Nota 4: "))

    result = (n1 + n2 + n3 + n4) / 4
    if result < 7:
            print("Reprovado")
    if result >= 7:
            print("Apavorado")
    resp = input("Deseja continuar S/N? ")
else: print("Fim")
