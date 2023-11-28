#LISTAS

notas = [7.9, 9.7, 8.2]

lista = []

lista_1 = list()

lista_2 = [26, 'Nadinne', False]

lista_de_listas = [10, [1, 2, 3]]

#Indexação e Slices (fatiamento)

""" lista = [10, 'nadinne', True]
print(lista)
print(lista[0])
print(lista[1])
print(lista[2])
print(lista[-1])
print(lista[-2])
print(lista[-3]) """

#Slices

lista = [10, 50, 30, 40, 25, 60, 5]
""" 
print(lista[0:3])
print(lista[3:6])
print(lista[2:])
print(lista[0:6:2]) """

""" for i in lista:
    print(i)

print('Comprimento da lista: ', len(lista)) """

""" for i in range(len(lista)):
    print(i) """

for i in range(len(lista)):
    print(lista[i], 'Posição: ', i)
