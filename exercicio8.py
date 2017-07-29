#!/usr/bin/python

# Carregar lista de produtos
with open('lista.txt','r') as fp:
    lista = fp.readlines()

# Exibir menu de opções
print("1) Incluir novos produtos")
print("2) Excluir produtos")
opt = input("Escolha uma das opções[1]: ") or "1"

# Se for opção 1, cadastre um novo produto
if opt == "1":
    lista.append(input("Digite um novo produto: ") + "\n")

# Se for opção 2, remova um produto da lista
elif opt == "1" or opt == "2":
    lista.remove(input("Digite o produto a ser removido: ") + "\n")

# Salve o resultado da lista dentro de um arquivo
with open('lista.txt','w') as fp:
    fp.writelines(lista)
