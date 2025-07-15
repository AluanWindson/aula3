"""
4.	Faça um Programa que peça as 4 notas bimestrais e mostre a média.
"""

print('Bom dia!')

n0 = int(input('Qual foi a sua nota no 1º Bimestre? '))
n1 = int(input('Qual foi a sua nota no 2º Bimestre? '))
n2 = int(input('Qual foi a sua nota no 3º Bimestre? '))
n3 = int(input('Qual foi a sua nota no 4º Bimestre? '))

soma = n0 + n1 + n2 + n3

print(f"Sua média é de {soma/4}")