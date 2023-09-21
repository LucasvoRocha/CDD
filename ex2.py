#numb = int(input("Digite um número: "))
#
# for x in range (1, numb + 1):
#     for y in range (1 , x + 1):
#             print(y, end = " ")
#     print( )

#---------------------------------------------

numb = int(input("Digite um número: "))

if numb > 0:
    for i in range(1, numb + 1):
        print(" " * (numb - i) + (str(i) + " ") * i)