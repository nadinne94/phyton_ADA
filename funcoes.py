# FUNÇÕES

# Função inicial

"""
def saudacao():
    print('Seja bem-vinda')

saudacao()
saudacao()
"""
# Função com  1 parâmetro

"""
nome = input('Digite seu nome: ')

def saudacao(nome):
    print('Seja bem-vinda,', nome)

saudacao(nome) """

# Função com  2 parâmetro

"""
nome = input('Digite seu nome: ')
curso = input('Digite o curso: ')

def saudacao(nome, curso):
    print('Seja bem-vinda,', nome)
    print('Aproveite o curso de', curso)

saudacao(nome, curso) """

# Função com  parâmetro por default

""" nome = input('Digite seu nome: ')

def saudacao(nome, curso='Python'):
    print(f'Seja bem-vinda, {nome}!')
    print(f'Aproveite o curso de {curso}!')

saudacao(nome, 'C++') """

# Função com retorno

""" def soma(num1, num2):
     return num1 + num2

resultado = soma(5,4)

print(resultado) """

def operacao(num1, num2, operacao='+'):
    if operacao == '+':
        return num1 + num2
    elif operacao == '-':
        return num1 - num2

resultado = operacao(4,5)

print(resultado)

resultado = operacao(9, 30, '-')

print(resultado)