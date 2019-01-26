"""
Tendo como dado de entrada a altura (h) de uma pessoa, construa um algoritmo que calcule seu peso ideal, utilizando as seguintes fórmulas:
Para homens: (72.7*h) - 58
Para mulheres: (62.1*h) - 44.7
"""
altura = float(input("insira a altura").replace(",","."))
print("o peso ideal para homem será", (72.8 * altura) - 58)
print("o peso ideal para homem será", (62.1 * altura) - 44.7)
