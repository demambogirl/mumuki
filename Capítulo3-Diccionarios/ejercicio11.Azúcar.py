def endulzar_menu(menu):
    nuevo_ingrediente = "azúcar"
    
    # Acceder directamente a la clave "ingredientes" en el diccionario "postre"
    menu["postre"]["ingredientes"].append(nuevo_ingrediente)

menu_ejemplo = {
    "plato_principal": "pasta",
    "postre": {
        "nombre": "pastel",
        "ingredientes": ["harina", "huevos", "leche"]
    }
}
endulzar_menu(menu_ejemplo)

print(menu_ejemplo)