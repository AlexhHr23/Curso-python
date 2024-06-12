print("Etapas de la edad según tu edad: ")

edad = int(input("Proporciona tu edad: "))
mensaje = None

if 0 <= edad < 10:
    mensaje = 'La infancia es increible...'
elif 10 <= edad < 20:
    mensaje = 'Muchos cambios, mucho estudio...'
elif 20 <= edad < 30:
    mensaje = 'Amor y comienza el trabajo...'
else:
    "Etapa  de vida no reconocida"

print(f"Tu edad  es: {edad}, {mensaje}")