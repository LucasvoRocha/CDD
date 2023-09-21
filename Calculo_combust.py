litros_vendidos = float(input("Quantos litros?: "))
tipo_combusti = input("Qual o tipo do combustivel?: ")

etanol = 4.90
gasolina = 5.90

calculo_etanol = etanol * litros_vendidos
calculo_gasolina = gasolina * litros_vendidos

if tipo_combusti == "G" or tipo_combusti == "g":
    print(calculo_gasolina)

elif tipo_combusti == "E" or tipo_combusti == "e":
    print(f"{calculo_etanol}")
else:
    print("Invalido")
