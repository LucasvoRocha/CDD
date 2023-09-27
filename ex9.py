n1 = float(input("Digite o primeiro numero: "))
n2 = float(input("Digite o segundo numero: "))

if n1 > n2:
    sub = n2 - n1
elif n2 == n1:
    sub = "numeros iguais"
else:
    sub = n2 > n1
print(sub)