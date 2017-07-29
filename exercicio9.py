#!/usr/bin/python

# Solicite os números a ser calculados
n1 = int(input("Informe um valor: "))
n2 = int(input("Informe outro valor: "))

# Solicite a operação
op = input("Informe a operação a ser executada[+,-,*,/]: ")

# Condição caso seja soma
if op == "+":
    print(n1 + n2)

# Condição caso seja subtração
elif op == "-":
    print(n1 - n2)

# Condição caso seja multiplicação
elif op == "*":
    print(n1 * n2)

# Condição caso seja divisão
elif op == "/":
    print(n1 / n2)

# Caso não seja nenhuma opção válida
else:
    print("Opção inválida")
