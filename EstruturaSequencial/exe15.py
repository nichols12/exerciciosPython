"""Faça um Programa que pergunte quanto você ganha por hora e o número de horas
trabalhadas no mês. Calcule e mostre o total do seu salário no referido mês,
sabendo-se que são descontados 11% para o Imposto de Renda, 8% para o INSS e 5%
para o sindicato, faça um programa que nos dê:
salário bruto.
quanto pagou ao INSS.
quanto pagou ao sindicato.
o salário líquido.
calcule os descontos e o salário líquido, conforme a tabela abaixo:"""
hours = int(input("numero de horas trabalhadas"))
pricePerHour = float(input("valor por hora trabalhada").replace(',','.'))
total = pricePerHour * hours
IR = total * 0.11
INSS = total * 0.08
sindicato = total * 0.05
print('+ salário bruto : ',total)
print('- IR : R$',IR)
print('- INSS : R$',INSS)
print('- Sindicato : R$',sindicato)
print('+ salário Liquido : ',total - IR - INSS - sindicato)
