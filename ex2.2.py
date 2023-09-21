numb = int(input("Digite um numero: "))

if numb <= 0:
     print (" ")
else:
     contador = 1
     while contador <= numb:
         repeticoes = contador
         while repeticoes > 0:
             print(contador, end=" ")
             repeticoes -= 1
         print()
         contador += 1

#-----------------------------------------------

#numb = int(input("Digite um numero: "))
#x = 1

#while x <= numb:
#    print(x * str (x), end = " ")
#    x += 1
