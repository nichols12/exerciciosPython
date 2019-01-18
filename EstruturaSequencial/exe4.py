""" Faça um Programa que peça as 4 notas bimestrais e mostre a média."""
notas = 0
for i in range(0,4):
    notas = notas + int(input("digite a nota " + str(i + 1) + ": "))
print("a média das notas é: " + str( notas/4 ))
