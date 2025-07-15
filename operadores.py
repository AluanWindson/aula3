exponenciacao = 2**10
print("Exponenciação =>", exponenciacao)

modulo = 55 % 2  #Resto da divisão
print("modulo =>", modulo)


concatenacao= "Senac" + "Curso python"

cinco_vezes_a = 5 *"a"
print(cinco_vezes_a)

#Precedência


#180 + 20 / 2 = > 190 - Priorização da divisão

#(180 + 20)/2 => 100 - Priorização do que está sendo executado em parênteses

#2 + 50 * 3 - Priorização da potência

# A adição( + ) e a subtração( - ) serão sempre as ultimas coisas a serem resolvidas

"""
1. (x + y / z ** 3) - Resolveria primeiro a potência

2. **(Potência)

3. /(divisão comum) ou // (divisão inteira) + %

Lembrar de sempre fazer a divisão comum primeiro, com a atenção de que os
parênteses devem ser resolvidos primeiro.


"""