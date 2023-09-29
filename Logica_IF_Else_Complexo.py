n1 = float(input("Insira a primeira nota: "))
n2 = float(input("Insira a segunda nota: "))
n3 = float(input("Insira a terceira nota: "))

media = (n1 + n2 + n3) / 3

if n1 <= 10 and n2 <= 10 and n3 <= 10 and n1 >=0 and n2 >=0 and n3 >=0:
    if media < 7:
        if media < 4:
         print(f"Você foi reprovado com a média: {media:.2f}")
        else:
          print("Recuperação fiot")
    else:
        print(f"Aprovado: {media:.2f}")
else:
    print("Valor inválido")
