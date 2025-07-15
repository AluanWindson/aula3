#Indice de massa corporea
#IMC = peso / altura ** 2
#IMC = peso / (altura * altura)

nome = "Lucas"
peso= 70.02
altura = 1.82

#Processamento

imc = peso / altura ** 2
print(nome,"Tem",altura,"de altura","pesa", peso,"seu imc é =",imc)

#F-Strings

print(f"{nome} tem {altura} de altura, pesa {peso} e seu imc é = {imc:.2f}")