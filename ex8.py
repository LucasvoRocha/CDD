soma = 0
quant = int(input("Quantos numero sao?: "))
for x in range (quant):
    numb = float(input("Digite um numero: "))
    soma = soma + numb
media = soma/quant
print(soma)
print(media)