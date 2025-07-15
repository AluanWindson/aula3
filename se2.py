entrada = input('Você quer [entrar ou sair]? ')
entrada = entrada.lower()
print(entrada)
"""
=Atribuição
número = 10

= Comparação
10 == 10

"""
if entrada == "entrar":
    print("Seja bem vindo! Login efetuado com sucesso.")

elif entrada == "sair":
    print('Você saiu do sistema..')

else:
    print("Você não digitou nem entrar e nem sair....")