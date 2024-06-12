print("Proporciona los siguientes datos del libro")
nombre_libro = input("Proporciona el nombre: ")
id = int(input("Proporciona el ID: "))
precio = float(input("Proporciona el precio: "))
envio = input("Endica si el envio es gratuito(Si/No): ")

if envio == 'Si':
    envio = True
elif envio == 'No':
    envio = False
else:
    envio= 'Valor incorrecto, debe escribir Si/No'

##Datos del libro
print(f'''
    Nombre: {nombre_libro}
    Id: {id}
    precio: {precio}
    envio: {envio}
''')