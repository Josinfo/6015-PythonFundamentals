#!/usr/bin/python

# Crie uma string com um trecho de texto

frase = "Isso irritou profundamente muitas pessoas e, no geral, foi encarado como uma péssima idéia."

# Inclua a frase "No início, o universo foi criado." no começo da string;

concatenar = "No início, o universo foi criado."
resultado = "%s %s"% (frase, concatena)
print(resultado)

# Divida a frase em uma lista, sendo tudo dividido pelo símbolo de ",";
dividir = resultado.split(',')
print(dividir)

# Armazene cada conteúdo de sua lista numa variável diferente;
var1,var2,var3,var4 = dividir
print(var1)
print(var2)
print(var3)
print(var4)

# Remova a letra "n" de todo o texto;
print(c.lower().replace('n','_'))

# Coloque o texto inteiro em caixa alta e depois em caixa baixa;
print(c.upper())
print(c.lower())

# Deixe somente "uma péssima idéia".
print(var4[19:])
