soma = 0
for x in range(10):
    numero = int(input(f"Digite o {x + 1}º número: "))
    soma += numero
    result = soma /10
print(f"A media é: {result}")