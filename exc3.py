numeros = []

for x in range(10):
    numero = float(input(f"Digite o {x + 1}º número entre 10 e 20: "))
    numeros.append(numero)

print("Números entre 10 e 20: ")
for numero in numeros:
    if 10 <= numero <= 20:
        print(numero)