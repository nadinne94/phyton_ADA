# > MÉTODOS DE LISTAS

lista = [1, 3, 12, 8, 2]

print('Lista original: ', lista)

# append

lista.append(4) #adiciona elemento no final da lista

print('Lista append: ', lista)

# insert

lista.insert(2, 10) #adiciona elemento na posição indicada

print('Lista insert: ', lista)

# extend

lista_2 = [1, 2, 3]

print('Lista 2: ', lista_2)

lista.extend(lista_2) # concatenação de listas

print('Lista extend: ', lista)

# pop

lista.pop() # elimina o elemento da última posição da lista

print('Lista pop(0): ', lista)

lista.pop(3) # elimina o elemento da 3ª posição da lista

print('Lista pop(3): ', lista)

# remove 

lista.remove(4) # procura o elemento que deve ser removido

print('Lista remove(4)', lista)

lista.remove(2)

print('Lista remove(2): ', lista) #removeu apenas o 1ª elemento '2'

# count - conta a quantidade de vez  que o número aparece na lista

print('Conte 2 ', lista.count(2))

print('Conte 1 ', lista.count(1))

# index - retorna a posição do elemento

print('Posição do elemento: ', lista.index(8))

# sort - ordena de forma crescente

lista.sort()

print('Lista ordenada crescente: ', lista)

lista.sort(reverse=True)

print('Lista ordenada decrescente: ', lista)

# > FUNÇÕES PARA LISTAS

# len
print('Comprimento da lista', len(lista)) # tamanho da lista

# sum
print('Soma da lista', sum(lista)) # soma de todos os números da lista

# Máx
print('Maior nº da lista', max(lista)) # tamanho da lista

# Min
print('Menor nº da lista', min(lista)) # tamanho da lista

