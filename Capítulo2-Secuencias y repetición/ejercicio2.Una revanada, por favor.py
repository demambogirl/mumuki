primera_estrofa = ['Aquí me pongo a cantar\t\t\nal compás de la vigüela,\t\t\nque el hombre que lo desvela\t\t\nuna pena estraordinaria,\t\t\ncomo la ave solitaria\t\ncon el cantar se consuela']
(primera_estrofa[0:22])
'Aquí me pongo a cantar'
(primera_estrofa[(len(primera_estrofa)-25):len(primera_estrofa)])
'con el cantar se consuela'

numeros = [10, 20, 30, 40, 50]
numeros[0:2]
[10, 20]         # es la lista conformada por el 1er y 2do elemento;
                 # ⚠️ recordemos que los índices en Python cuentan desde 0
numeros[2:4]
[30, 40]         # es la lista conformada por el 3er y 4to elemento
numeros[0:4]
[10, 20, 30, 40] # es la lista conformada 
                 # por los elementos 1 al 4
numeros[:4]
[10, 20, 30, 40] # equivalente al ejemplo anterior; 
                 # si no ponemos el límite inferior, 
                 # trae todos los elementos desde el principio
numeros[3:]
[40, 50]         # es la lista conformada 
                 # por todos los elementos partir del 4to  
                 # si no ponemos el límite superior, 
                 # trae todos los elementos hasta el final      