"""Faça um programa para uma loja de tintas. O programa deverá pedir o tamanho
em metros quadrados da área a ser pintada. Considere que a cobertura da tinta é
de 1 litro para cada 3 metros quadrados e que a tinta é vendida em latas de 18
litros, que custam R$ 80,00. Informe ao usuário a quantidades de latas de tinta
a serem compradas e o preço total."""

metros = float(input("numero de metros quadrados a ser pintado").replace(",","."))
litrosPorMetro = metros // 3 + metros % 3
latas = litrosPorMetro // 18
if litrosPorMetro % 18 >= 1:
    latas = latas + 1
precoTotal = latas * 80
print("a quantidade de litros necessários : ", litrosPorMetro)
print("a quantidade de latas : ", latas)
print("a quantidade de preço total : ", precoTotal)
