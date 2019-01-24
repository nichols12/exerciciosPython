"""
Faça um Programa que peça 2 números inteiros e um número real. Calcule e mostre:
    o produto do dobro do primeiro com metade do segundo .
    a soma do triplo do primeiro com o terceiro.
    o terceiro elevado ao cubo.
"""

numA = int(input("insira o primeiro número inteiro"))
numB = int(input("insira o segundo número inteiro"))
numC = float(input("insira um número real"))
print("o produto do dobro do primeiro com metade do segundo .", (numA * 2) * (numB / 2))
print("a soma do triplo do primeiro com o terceiro.", (numB * 3 ) + numC)
print("o terceiro elevado ao cubo.", numC**3)
