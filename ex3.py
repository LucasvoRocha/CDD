# resp = "s"
# while resp == "s":
#      idade = int(input("Digite sua idade: "))
#      result = 2023 - idade
#      if idade >= 18:
#          print("Dimaior")
#      else:
#          print("Dimenor")
#      resp = input("Deseja continuar S/N? ")
#======================================================

resp = "s"
while resp == "s":
    mes = int(input("Digite o mes: "))
    idade = int(input("Digite a idade: "))
    ano_atual = 2023
    ano_calcu = ano_atual - idade

    if mes > 12 or mes < 1:
        print("Mês de nascimento inválido.")
    else:
        if mes == 12:
            print(f"Voce nasceu em, {ano_calcu}")
        else:
            print(f"Voce nasceu em, {ano_calcu}" )
        resp = input("deseja continuar S/N?").lower()