#- Algoritmo para calcular el factorial de un número
#    - Inicio
#    - Decirle al usuario que digite el número número factorial
#    - Leer número
#    - Crear un bucle
#    - Dentro del bucle, crear una variable llamada “factorial” = 1 La cual se le sumara 1 hasta llegar a el número+1
#    - Multiplicar la variable “factorial” * “número” y guardar el resultado
#    - Repetir hasta que finalice el bucle
#    - Mostrar resultado
#    - Fin

numero = int(input("Digite un número: "))

factorial = 1

for i in range(1, numero + 1):
    factorial *= i

print("El factorial de", numero, "es", factorial)