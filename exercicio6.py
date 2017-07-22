#!/usr/bin/python

# Abrir arquivo de texto para adição
with open("compra.txt","a") as b:
    valor = input("Digite um produto para a lista: ")
    b.write(valor + "\n")

# Abrir o arquivo de texto para leitura
with open("compra.txt","r") as i:
    print(i.read())
