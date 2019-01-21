"""Faça um Programa que pergunte quanto você ganha por hora e o número de horas trabalhadas no mês. Calcule e mostre o total do seu salário no referido mês."""
price = float(input("qual o valor por horas trabalhadas").replace(',','.'))
hoursWorked = int(input("horas trabalhadas no mês"))

print("este mês você deve receber", (hoursWorked * price))
