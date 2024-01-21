#- .Algoritmo para generar una tabla de multiplicar
#    - Inicio
#    - Decirle al usuario que digite el número que quiere que se muestren sus multiplicaciones del 1 al 10
#    - Crear un bucle con una variable “i” en el cual se sumara +1 hasta llegar a 10
#    - Imprimir la multiplicación del ( número * i )cada vez que se haga el bucle
#    - Fin

Número = int(input("Digite el número y se le mostrara las multiplicaciones del 1 al 10: "))

for i in range (1, 11):
    Multiplicación = Número * i
    print(Número, "x", i ,"=", Multiplicación)