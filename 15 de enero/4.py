#- .Algoritmo para verificar si un número es primo
#    - Inicio
#    - Decirle al usuario que digite el número
#    - Leer número
#    - Si el número es menor a 1 finaliza el programa y se muestra “El número no es primo”
#    - Si el número es igual a 2 mostrar “El número es primo”
#    - Crear un bucle
#    - Dentro del bucle crear una variable “i” = 2 la cual añadirá +1 cada que se complete el bucle hasta llegar a “número” -1
#    - Dividir el número por “i” y si en algún momento llega a dar residuo 0 el programa finaliza mostrando “El número no es primo”
#    - Sino continuar con el bucle hasta acabarse
#    - Al finalizar el bucle mostrar “El número ingresado es primo”
#    - Fin

def es_primo(número):
    if número < 1:
        print("El número no es primo")
        return
    elif número == 2:
        print("El número ingresado es primo")
        return
    else:
        for i in range(2, número):
            if número % i == 0:
                print("El número no es primo")
                return
        print("El número ingresado es primo")

número_ingresado = int(input("Ingrese un número: "))

es_primo(número_ingresado)