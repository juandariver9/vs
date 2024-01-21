#- Algoritmo para calcular el área de un triangulo
#    - Inicio
#    - Decirle al usuario que digite la altura del triangulo
#    - Leer Altura
#    - Decirle al usuario que digite la base del triangulo
#    - Leer Base
#    - Multiplicar Base * Altura y dividir el resultado entre dos
#    - Mostrar el resultado al usuario
#    - Fin

Altura = float(input("Digite la altura del triangulo: "))
Base = float(input("Digite la base del triangulo: "))

Area = ( Base * Altura ) / 2

print(Area)