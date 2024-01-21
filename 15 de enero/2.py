#- Algoritmo para encontrar el mayor de tres números
#    - Inicio
#    - Decirle al usuario que digite el primer número
#    - Leer el primer número
#    - Decirle al usuario que digite el segundo número
#    - Leer el segundo número
#    - Decirle al usuario que digite el tercer número
#    - Leer el tercer número
#    - Comparar el primer número con el segundo número y guardar el mayor en una variable llamada "mayor"
#    - Comparar "mayor" con el tercer número y guardar el mayor en "mayor"
#    - Mostrar "mayor" como el mayor de los tres números al usuario
#    - Fin

Número1 = int(input("Digite el primer número: "))
Número2 = int(input("Digite el segundo número: "))
Número3 = int(input("Digite el tercer número: "))

if Número1 > Número2 and Número1 > Número3:
    print("El mayor es:", Número1)

elif Número2 > Número1 and Número2 > Número3:
    print("El mayor es:", Número2)

else:
    print("El mayor es ", Número3)