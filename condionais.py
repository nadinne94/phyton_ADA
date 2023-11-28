# Estrutaras de Condicionais
"""
idade = 15

if idade >= 18:
    print("Maior de idade ")
else: 
    print("Menor de idade ")
"""

"""
media = float(input("Digite a média? "))

if media >= 7:
    print("Aprovado")
else:
    print("Reprovado")

"""

"""
media = float(input("Digite a média? "))

if media >= 7:
    print("Aprovado")
elif 5 <= media < 7:
    print("Recuperação")
else:
    print("Reprovado")

"""

media = float(input("Digite a média? "))

frequencia = float(input("Digite a frequência: "))

if media >= 7 and frequencia >= 70:
    print("Aprovado")
elif 5 <= media < 7:
    print("Recuperação")
else:
    print("Reprovado")