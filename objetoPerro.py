class Perro():
    def __init__(self, raza, edad, peso):#función constructora, nos permite crear instancias
        self.raza=raza
        self.edad=edad
        self.peso=peso
    def ladra(self):
        if self.peso >8:
            print('GUAU GUAU!!')
        else:
            print('guau, guau')
        
'''Donde pone 'self' es donde payhton meterá el nombre de la instancia que nosotros asignemos
a la clase/objeto, en este caso será Titán'''

Titán = Perro('Labrador', 8, 40)
Pope = Perro('Yorkshire', 10, 2)