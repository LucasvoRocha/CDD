numb_negative = 0
numb_positivo = 0
soma_negative = 0
soma_positiva = 0

for x in range(10):
    numero = float(input(f"Digite o {x + 1}º número: "))

    if numero < 0:
        numb_negative += 1
        soma_negative += numero

        soma_positiva2 = 10 - numb_negative

print(f"Você digitou {numb_negative} números negativos\n e a soma dos negativos é"
      f" {soma_negative}"f"\n e a quantidade de numeros positivos é {soma_positiva2}.")

#------------------------------------------------------------------------------------------------------


"""numb_negative = 0

for x in range(10):
    numero = float(input(f"Digite o {x + 1}º número: "))

    if numero < 0:
        numb_negative += 1

print(f"Você digitou {numb_negative} números negativos.")"""