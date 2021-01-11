class Perro():
    def __init__(self, name, raza, edad, peso):#función constructora, nos permite crear instancias
        self.name=name
        self.raza=raza
        self.edad=edad
        self.peso=peso
    def ladra(self):
        if self.peso >8:
            print('GUAU GUAU!!')
        else:
            print('guau, guau')
    def __str__(self):
        return "Hola, soy el perro {}, y soy un {}".format(self.name, self.raza)
    
#objeto herencia
class PerroGuia(Perro):
    def __init__(self, name, raza, edad, peso, amo):
        Perro.__init__(self, name, raza, edad, peso)
        self.amo=amo
        self.__trabajando=False
    def trabajo(self):
        print('Ayudo a {} a cruzar la calle'.format(self.amo))
    def ladra(self):
        if self.__trabajando==True:
            print('shh, estoy trabajando, no puedo ladrar ahora')
        else:
            Perro.ladra(self)
            
    def trabaja(self, valor=False):
        if valor==False:
            print('No estoy trabajando')
        else:
            self.__trabajando=True
            print('Ya estoy trabajando')
    def descansa(self):
        self.__trabajando=False
        print('Vale, dejo de trabajar')
        
cocke=PerroGuia('cocke', 'shibaInu', 5, 12, 'Gustavo')


'''Donde pone 'self' es donde payhton meterá el nombre de la instancia que nosotros asignemos
a la clase/objeto'''

