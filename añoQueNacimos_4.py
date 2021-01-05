diasMeses = (31, 28, 31, 30, 31, 30, 31, 31, 30, 31 ,30)

nombre =input('Cómo te llamas: ')
print('Hola, ',nombre)

edad=input('Cuantos años tienes?: ')
edad = int(edad)

annoActual=input('¿En qué año estamos?: ')
mesActual=input('¿En qué mes estamos?: ')
diaActual=input('¿Qué día del mes es?: ')
mesActual=int(mesActual)
diaActual=int(diaActual)
annoActual=int(annoActual)

transc=0
indice=0

while indice < mesActual-1:
    transc = transc + diasMeses[indice]
    indice = indice +1

transc = transc+diaActual 

prob= ((transc / 360) *100)       

annoNacimiento = annoActual - edad

        

print(nombre, 'Hay una probabilidad del ',round(prob),'% de haber nacido en el', annoNacimiento, 'y una probabilidad del ',100-round(prob), '% de haber nacido en ',annoNacimiento-1) 
    