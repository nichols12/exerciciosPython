"""João Papo-de-Pescador, homem de bem, comprou um microcomputador para controlar
 o rendimento diário de seu trabalho. Toda vez que ele traz um peso de peixes
 maior que o estabelecido pelo regulamento de pesca do estado de São Paulo
 (50 quilos) deve pagar uma multa de R$ 4,00 por quilo excedente. João precisa
  que você faça um programa que leia a variável peso (peso de peixes) e calcule
  o excesso. Gravar na variável excesso a quantidade de quilos além do limite e
   na variável multa o valor da multa que João deverá pagar. Imprima os dados do
    programa com as mensagens adequadas."""

peso = float(input("insira o peso do peixe em kg.").replace(',','.'))
multa = 0.00
pesoExcedente = 0.00
if peso > 50:
    pesoExcedente = peso - 50
    multa = (pesoExcedente // 4) * 4
print("o peso do peixe é ", peso)
print("a multa a ser paga é de ", multa)
print("o peso excedente é ", pesoExcedente)
