#!/usr/bin/python

# Função de soma de valores
def soma(n1,n2):
    return n1 + n2 

# Função de subtração de valores
def subtracao(n1,n2):
    return n1 - n2

# Função de multiplicação de valores
def multiplica(n1,n2):
    return n1 * n2

# Função de divisão de valores
def divisao(n1,n2):
    return n1 / n2

# Dicionário de funções
dicionario = {"1":soma,
              "2":subtracao,
              "3":multiplica,
              "4":divisao}

# Informe os valores para a calculadora
n1 = int(input("Informe o primeiro valor: "))
n2 = int(input("Informe o segundo valor: "))

# Exiba um menu de opção e obrigue o usuário a selecionar uma das opções
print("1 - Soma")
print("2 - Subtração")
print("3 - Multiplicação")
print("4 - Divisão")
opt = input("Informe a operação: ")

# Chame a função através do dicionário e execute ela. O resultado deverá ser somado com a mensagem abaixo
print("Resultado da operação é: " + str(dicionario[opt](n1,n2)))
