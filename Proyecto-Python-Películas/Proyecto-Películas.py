peliculas = [
    {"titulo": "Five Nights at Freddy's", "visualizaciones": 400, "duración": "2 horas", "genero": "terror"},
    {"titulo": "Zootopia", "visualizaciones": 154, "duración": "1 hora 45 minutos", "genero": "animación"},
    {"titulo": "El Planeta del Tesoro", "visualizaciones": 210, "duración": "1 hora 35 minutos", "genero": "animación"},
    {"titulo": "Magbeth", "visualizaciones": 100, "duración": "2 horas", "genero": "literario"},
    {"titulo": "Paranorman", "visualizaciones": 315, "duración": "2 horas", "genero": "stop motion" },
    {"titulo": "El Viaje de Chihiro", "visualizaciones": 540, "duración": "1 hora 30 minutos", "genero": "anime"},
    {"titulo": "Rango", "visualizaciones": 220, "duración": "2 horas", "genero": "animación"},
    {"titulo": "El Increíble Castillo Vagabundo", "visualizaciones": 430, "duración": "2 horas 45 minutos", "genero": "anime"},
    {"titulo": "Titanic", "visualizaciones": 600, "duración": "3 horas 45 minutos", "genero": "romance, documental"},
    {"titulo": "Coraline", "visualizaciones": 300, "duración": "2 horas", "genero": "stop motion"}
]

def mostras_peliculas():
    titulos = [pelicula["titulo"] for pelicula in peliculas]
    print("Listado de películas")
    for titulo in titulos:
        print(titulo)

def mostrar_mas_vistos():
    mas_visto = peliculas[0]
    for pelicula in peliculas:
        if pelicula["visualizaciones"] > mas_visto["visualizaciones"]:
            mas_visto = pelicula
    print(f'la película más vista es: {mas_visto["titulo"]} con {mas_visto["visualizaciones"]} vistas')
    
def agregar_a_lista():
    titulo = input("Nombre de la película: ")
    genero = input("Género de la película ")
    pelicula = {
        "titulo": titulo,
        "genero": genero,
        "visualizaciones": 0
    }
    peliculas.append(pelicula)
    print(f"{titulo} se ha agregado a la lista")

def aumentar_visualizaciones(titulo):
    for pelicula in peliculas:
        if pelicula["titulo"] == titulo:
            pelicula["visualizaciones"] += 1
            print(f'{pelicula["titulo"]} ahora tiene {pelicula["visualizaciones"]} vistas')
            return
print(f'No se ha encontrado la pelicula {"titulo"}') 

def filtrar_generos(genero, peliculas):
    peliculas_por_genero = [pelicula["titulo"] for pelicula in peliculas if pelicula["genero"] == genero]
    print(f"Películas por género {genero}:")
    for titulo in peliculas_por_genero:
        print(titulo)

def menu():
    while True:
        print("\nOpciones:")
        print("1. Mostrar películas")
        print("2. Mostrar más visto")
        print("3. Agregar a Lista")
        print("4. Aumentar Vistas")
        print("5. Filtrar Géneros")
        print("6. Salir")
        opcion = int(input("Ingresa una opción: "))

        if opcion == 1:
            mostras_peliculas()
        elif opcion == 2:
            mostrar_mas_vistos()
        elif opcion == 3:
            agregar_a_lista()
        elif opcion == 4:
            titulo = input("Ingrese titulo: ")
            aumentar_visualizaciones(titulo)
        elif opcion == 5:
            genero = input("Ingrese un género: ")
            filtrar_generos(genero, peliculas)
        elif opcion == 6:
            print("Adios!")
            break

menu()
