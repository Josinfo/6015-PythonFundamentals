#!/usr/bin/python

# func1 deve construir uma lista de numeros de 1 a 100
def func1():
    print("Lista criada")
    return list(range(1,101))

# func2 deve imprimir os números pares de 1 a 100 recebidos pela func1
def func2():
    for i in func1():
        rst = i % 2
        if rst == 0:
            print(i)

# func3 deve somar a String "Número do Exercício" com o Inteiro "14"
def func3():
    print("Número do Exercício: " + str(14))

# func4 deve acessar a variável global opt e alterar para '5' e imprimir resultado
def func4():
    global opt
    opt = 5
    print(opt)

# Dicionário de funçoes
dicionario = {'1':func1,
              '2':func2,
              '3':func3,
              '4':func4}

# Imprimir as opções válidas, e solicitar o usuário para informar uma delas
print("1 - Lista ")
print("2 - Pares")
print("3 - Concatenação")
print("4 - Acesso Global")
opt = input("Informe uma opção: ")

# Informar a opção de acordo com a opção selecionada
dicionario[opt]()
