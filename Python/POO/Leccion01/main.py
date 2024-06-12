class Persona:
    #Metodo dunder init
    def __init__(self, nombre, apellido, edad):
        self.nombre = nombre
        self.apellido = apellido
        self.edad = edad

    def mostrar_detalle(self):
        print(f'Persona: {self.nombre} {self.apellido} {self.edad}')



persona1 = Persona('Alex', 'Hernandez', 28)
persona1.mostrar_detalle()
persona1.telefono = '2222222222'
#Persona.mostrar_detalle(persona1)
print(persona1.telefono)

persona2 = Persona('Karla', 'Gomez', 22)
persona2.mostrar_detalle()