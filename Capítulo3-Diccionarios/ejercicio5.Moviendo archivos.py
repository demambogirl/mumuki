def mover_archivo(archivo, nueva_ruta):
    # Verificar si el diccionario contiene la clave "ruta"
    if "ruta" in archivo:
        # Normalizar ambas rutas para evitar discrepancias
        ruta_actual = archivo["ruta"]
        
        
        archivo["ruta"] = nueva_ruta  