# FUNÇÕES

def saudacao(n, i):
    print(f'Olá {n}, sua idade é {i}')



def soma(t):
    print(f'A soma dos numeros fornecidos dá: {t}.')



def soma(n1, n2):
    total = n1 + n2
    print(f'O total é: {total}')



def maior_numero(a, b):
    if a > b:
        print(f'O numero maior é {a}')
    elif a < b:
        print(f'O numero maior é {b}')
    else:
        print('Os numeros são iguais')



def somar_numeros(x, y):
    total = x + y
    print(f'O total é {total}')



#---------------------------------- programa principal


# nome = input('Informe seu nome: ')
# idade = int(input('Informe sua idade: '))
# saudacao(nome, idade)


#---------------------------------- soma


# num1 = int(input('Informe o 1o numero: '))
# num2 = int(input('Informe o 2o numero: '))
# total = num1 + num2
# soma(total)


#---------------------------------- soma


# num1 = int(input('Informe o 1o numero: '))
# num2 = int(input('Informe o 2o numero: '))
# soma(num1, num2)


#---------------------------------- descobre o maior


# numero1 = float(input('Informe o primeiro numero: '))
# numero2 = float(input('Informe o segundo numero: '))
# maior_numero(numero1, numero2)


#---------------------------------- somar 3 pares de numeros


# for n in range(3):
#     n1 = float(input('Digite o primeiro numero: '))
#     n2 = float(input('Digite o segundo numero: '))
#     somar_numeros(n1, n2)