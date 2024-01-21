#- Algoritmo para convertir grados Celsius a Fahrenheit
#    - Inicio
#    - Decirle al usuario que digite la temperatura en grados Celsius
#    - Leer Temperatura
#    - Convertir Temperatura a Fahrenheit con la formula (Temperatura * 9/5) + 32
#    - Mostrar temperatura en Fahrenheit
#    - Fin

temperaturaCelsius = float(input("Ingrese la temperatura en grados Celsius: "))

temperaturaFahrenheit = (temperaturaCelsius * 9/5) + 32

print(f"La temperatura en grados Fahrenheit es: {temperaturaFahrenheit}")