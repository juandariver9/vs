#- Algoritmo para calcular el promedio de una lista de números
#    - Inicio
#    - Crear una lista de números
#    - Sumar todos los números de la lista y guardar el resultado en una variable llamada "total"
#    - Dividir "total" entre la cantidad de números en la lista y guardar el resultado en una variable llamada "promedio"
#    - Mostrar "promedio" como el promedio de la lista de números
#    - Fin

def calcular_promedio(lista):
    total = sum(lista)
    promedio = total / len(lista)
    return promedio

numeros = [2, 4, 6, 8, 10]
promedio = calcular_promedio(numeros)
print("El promedio de la lista es:", promedio)