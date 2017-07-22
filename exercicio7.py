#!/usr/bin/python

# Abra o arquivo e converta ele em uma lista
with open("zen.txt",'r') as fp:
    lista = fp.readlines()

# Remova a 5º linha do arquivo
lista.pop(4)

# Coloquen a 6º linha em caixa alta
lista[5] = lista[5].upper()

# Altere a 10º linha para caixa baixa
lista[9] = lista[9].lower()

# Remova a palavra implementation da penultima linha
lista[16] = lista[16].replace('implementation','')

# Salvar o resultado do arquivo
with open("novo_zen.txt",'w') as fp:
    fp.writelines(lista)
