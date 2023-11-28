# DICIONÁRIOS

# criando dicionários

dicionario = {}
dicionario = dict()

dicionario = { 'nome': 'Nadinne', 'idade':29, 'altura':1.67 }

print(dicionario)
print(dicionario['idade'])

# Adicionando elementos em um dicionário

dicionario['programador'] = True

print(dicionario)

dicionario['altura'] = 2

print(dicionario)

# Pecorre os elementos dos dicionários

for i in dicionario:
    print(i, dicionario[i])

# Testando a existência de uma chave

print('peso' in dicionario)
print('altura' in dicionario)
