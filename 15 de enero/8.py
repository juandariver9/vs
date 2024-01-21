#- 8.Algoritmo para generar la serie de Fibonacci
#    - Inicio
#    - Decirle al usuario que digite la longitud de la serie de Fibonacci
#    - Leer Longitud
#    - Crear una lista para almacenar la serie con los dos primeros elementos (0 y 1)
#    - Crear un bucle para generar la serie hasta alcanzar la longitud deseada
#        - Calcular el siguiente término sumando los dos últimos términos en la lista
#        - Agregar el nuevo término a la lista
#    - Mostrar la serie de Fibonacci
#    - FIn

Longitud = int(input("Digite la longitud de la serie de Fibonacci: "))

serie_fibonacci = [0, 1]

for i in range(2, Longitud):
      siguiente_termino = serie_fibonacci[-1] + serie_fibonacci[-2]
      serie_fibonacci.append(siguiente_termino)

print(serie_fibonacci)