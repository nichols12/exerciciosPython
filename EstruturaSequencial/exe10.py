"""Faça um Programa que peça a temperatura em graus Celsius, transforme e mostre em graus Farenheit."""

temp = float(input("insira a temperatura em Celsius ").replace(',','.'))
print("temperatura em Farenheit", (temp * 9/5) + 32)
