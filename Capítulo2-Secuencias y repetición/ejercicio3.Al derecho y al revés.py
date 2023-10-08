"hola mundo"[:4] # los primeros 4 caracteres, como ya conocemos
"hola" 
"hola mundo"[:-1] # todos los caracteres salvo el último
"hola mund" 
"hola mundo"[-5:] # los último 5 caracteres
"mundo"
"hola mundo"[0] # primer carácter, como ya conocemos
"h" 
"hola mundo"[-1] # último carácter
"o"                 
"hola mundo"[-2] # anteúltimo carácter
"d"

def sin_extremos(lista):
    return lista [1:-1]
  
def extremos(lista):
    return [lista[0], lista[-1]]