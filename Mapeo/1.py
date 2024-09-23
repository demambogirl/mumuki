# Mapeo map()

# map(funcion, iterable)

# convertir Celsius a Fahrenheit

def celsius_a_Fahrenheit(temp_c):
    return(temp_c * 9/5) + 32

temperaturas_c = [0, 25, 30, 100, 47]

temperaturas_f = map(celsius_a_Fahrenheit, temperaturas_c)

print(temperaturas_c)

print(list(temperaturas_f))



palabras = ["python", "mapeo", "lista", "comprension"]

palabras_mayuscula = map(str.upper, palabras)

print(type(palabras[0]))
print(palabras[0].upper())

print(list(palabras_mayuscula))



# Lista por comprension

cuadrados = [x**2 for x in range(1, 11)]

print(list(range(1, 11)))
cuadrados = [x**2 for x in range(1, 21)]
print(cuadrados)

palabras_2 = ["yo", "me", "divierto", "mucho", "escuchando", "música"]
largas = [palabra for palabra in palabras_2 if len(palabra) > 3]
print(largas)


# lambda

suma = lambda x, y: x + y
resultado = suma(5, 3)
print(f"suma lambda: {resultado}")


# filtrar numeros pares de una lista usando filter() y lambda

numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9]
pares = filter(lambda num: num % 2 == 0, numeros)
print(f"Numeros pares: {list(pares)}")