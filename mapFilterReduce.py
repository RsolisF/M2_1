from functools import reduce
lista=[1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]


listaDoble = map(lambda x: x*2, lista)
listaPares = filter(lambda x: x%2==0, lista)
listaSumatodo= reduce(lambda x, y: x+y, range(101))

print('{}\n{}\n{}\n'.format(list(listaDoble), list(listaPares), listaSumatodo))


sumaPares = reduce(lambda x, y: x+y, filter(lambda x: x%2==0,range(101)))#prueba para usar dos lambda en una misma función reduce y filter
