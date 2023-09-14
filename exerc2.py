hora1 = int(input("hora 1: "))
minuto1 = int(input("minuto 1: "))
hora2 = int(input("hora 2: "))
minuto2 = int(input("minuto 2: "))
minuto_temp = 0
minutos = minuto1 + minuto2
if minutos >= 60:
    htemp = 1
    minutos = minutos - 60

if hora1 > 12:
    hora1 = hora1 - 12

if hora2 > 12:
    hora2 = hora2 - 12

horas_total = hora1 + hora2 + htemp
minutos_total = minutos
print(htemp, ":", minutos)