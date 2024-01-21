#- Algoritmo para determinar si un número es par o impar
#    - Inicio
#    - Decirle al usuario que digite el primer número
#    - Leer número
#    - Dividir el número entre dos, si la división da residuo de 0 es Par
#    - Si el residuo da 1 es impar
#    - Mostrar al usuario
#    - Fin

Número = float(input("Digite un número: "))

Residuo = Número // 2

if Residuo == 1:
		print("El número es impar")
else:
		print("El número es par")
		 