#!/usr/bin/python

# Inicialização das variáveis
lista = []
dicionario = {}
number, real, string = None, None, None

# Salve uma mensagem de texto dentro de uma variável chamada "string"
string = input("Digite um texto qualquer: ")
print(string,type(string),sep=":")

# Salve um valor numérico dentro de uma variável chamada "number"
number = int(input("Digite um número inteiro qualquer: "))
print(number,type(number),sep=":")

# Salve um valor flutuante dentro de uma variável chamada "real"
real = float(input("Digite um número float qualquer: "))
print(real,type(real),sep=":")

# Salve um dicionário contendo nome de usuário - String - e senha - int -
dicionario['usuario'] = input("Digite o seu login: ")
dicionario['senha'] = int(input("Digite sua senha numérica: "))

print(dicionario,type(dicionario),sep=":")
print(dicionario.get('usuario'),type(dicionario['usuario']),sep=":")
print(dicionario.get('senha'),type(dicionario['senha']),sep=":")

# Salve uma lista contendo 3 números
lista.append(int(input("Informe o primeiro número: ")))
lista.append(int(input("Informe o segundo número: ")))
lista.append(int(input("Informe o terceiro número: ")))

print(lista,type(lista),sep=":")
print(lista[0],type(lista[0]),sep=":")
print(lista[1],type(lista[1]),sep=":")
print(lista[2],type(lista[2]),sep=":")
