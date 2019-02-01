"""Não finalizado"""


"""Faça um Programa para uma loja de tintas. O programa deverá pedir o tamanho
em metros quadrados da área a ser pintada. Considere que a cobertura da tinta é
de 1 litro para cada 6 metros quadrados e que a tinta é vendida em latas de 18
litros, que custam R$ 80,00 ou em galões de 3,6 litros, que custam R$ 25,00.
Informe ao usuário as quantidades de tinta a serem compradas e os respectivos
preços em 3 situações:
comprar apenas latas de 18 litros;
comprar apenas galões de 3,6 litros;
misturar latas e galões, de forma que o preço seja o menor. Acrescente 10% de
folga e sempre arredonde os valores para cima, isto é, considere latas cheias."""


metros = float(input("numero de metros quadrados a ser pintado").replace(",","."))
litrosPorMetro = metros // 3 + metros % 3
latas = litrosPorMetro // 18
galao = litrosPorMetro // 3.6
if litrosPorMetro % 18 >= 1:
    latas = latas + 1
if litrosPorMetro % 3.6 >= 1:
    galao = galao + 1
precoTotalLatas = latas * 80
precoTotalGalao = galao * 25
print("a quantidade de litros necessários : ", litrosPorMetro)
print("a quantidade de latas : ", latas)
print("a quantidade de galões : ", galao)
print("a quantidade de preço total latas: ", precoTotalLatas)
print("a quantidade de preço total galões: ", precoTotalGalao)
