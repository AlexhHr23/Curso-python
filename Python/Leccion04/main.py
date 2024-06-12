# Diccionario (key, value)

diccionario = {
    'IDE': 'Integrated Developmente Enviroment',
    'OPP': 'Object Oriented Programación',
    'DBMS': 'Database management System'
}

# Largo
print(len(diccionario))
# Accdender a un elemeto(key)
print(diccionario['OPP'])
# Otra forma de recuperar un elemento
print(diccionario.get('OPP'))

#Modificar elementos
diccionario['IDE'] = 'integrated deveploment enviroment'
print(diccionario)

#Recorrer los elementos
for termino, valor in diccionario.items():
    print(termino, valor)

for termino in diccionario.keys():
    print(termino)
for termino in diccionario.values():
    print(termino)

# comprobar existencia de alguno elemento
print('IDE' in diccionario)

# Agregar elemento
diccionario['FG'] = 'Foreng Key'
print(diccionario)

# Remover elemento
diccionario.pop('FG')
print(diccionario)

#Limpiar el diccionario
print(diccionario)

#Eliminar el diccionario
del diccionario
print(diccionario)