def cuadrado(x):
    return x*x



def sumaTodos(limit, f):
    resultado=0
    for i in range (limit+1):
        resultado+= f(i)
    return resultado

print(sumaTodos(100, cuadrado))
