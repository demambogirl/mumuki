peliculas = [
    {"titulo": "Five Nights at Freddy's", "visualizaciones": 400, "duración": "2 horas", "género": "terror"},
    {"titulo": "Zootopia", "visualizaciones": 154, "duración": "1 hora 45 minutos", "género": "animación"},
    {"titulo": "El Planeta del Tesoro", "visualizaciones": 210, "duración": "1 hora 35 minutos", "género": "animación"},
    {"titulo": "Magbeth", "visualizaciones": 100, "duración": "2 horas", "género": "literario"},
    {"titulo": "Paranorman", "visualizaciones": 315, "duración": "2 horas", "género": "stop motion" },
    {"titulo": "El Viaje de Chihiro", "visualizaciones": 540, "duración": "1 hora 30 minutos", "género": "anime"},
    {"titulo": "Rango", "visualizaciones": 220, "duración": "2 horas", "género": "animación"},
    {"titulo": "El Increíble Castillo Vagabundo", "visualizaciones": 430, "duración": "2 horas 45 minutos", "género": "anime"},
    {"titulo": "Titanic", "visualizaciones": 600, "duración": "3 horas 45 minutos", "género": "romance, documental"},
    {"titulo": "Coraline", "visualizaciones": 300, "duración": "2 horas", "género": "stop motion"}
]


def mostrar_mas_vistos():
    mas_visto = peliculas[0]["visualizaciones"]
    for pelicula in peliculas:
        if pelicula["visualizaciones"] > mas_visto["visualizaciones"]:
            mas_visto = pelicula
    print(f'la película más vista es: {mas_visto["titulo"]} con {mas_visto["visualizaciones"]} vistas')