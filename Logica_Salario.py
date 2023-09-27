nome = input("Seu nome: ")
salario = float(input("Salario: "))
aumento = float(input("Aumento: "))
idade = input("Idade: ")
qf = int(input("Quandos filhos?: "))
soma = (salario + salario * aumento /100)
vabono = 150 * qf
apabono = vabono
soma_qf = vabono * qf + soma
ferias = salario /3 + salario
fe2 = salario /3
sabru = (vabono + soma + qf + ferias)
print(f"\n Abono:  {vabono}\n Ferias:  {fe2}\n Salario total: {sabru} ")
