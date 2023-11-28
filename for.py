#LAÇOS DE REPETIÇÃO

"""
for i in range(10):
    print(i)

"""

""" for i in range(1,10):#inclui o '1' e vai até o '9'
    print(i) """

""" for i in range(0,12,2):#inclui o '1' e vai até o '11' e pula de 2 e 2
    print(i)  """

""" for i in range(1,4):
    nota = float(input(f'Informe sua nota {i}: ')) """

soma = 0

for i in range(1,4):
    nota = float(input(f'Informe sua nota {i}: '))

    soma = soma + nota

print('Soma ', soma)
print('Média ', soma/3)