#!/usr/bin/python

# Inicializando variaveis
op1,op2 = None,None

# Função de validação de usuário
def funcusuario(usuario):
    global op1
    op1 = ('batatinha' == usuario)

# Função de validação de senha
def funcsenha(senha):
    global op2
    op2 = ('123456' == senha)

# Solicite ao usuário o login e senha e compare dentro das respectivas funções
funcusuario(input("Informe o login do usuário: "))
funcsenha(input("Informe a senha do usuário: "))

# Se op1 e op2 forem True, o usuário estará autenticado. Se não, acesso negado!
if op1 and op2:
    print("Usuário autenticado!")
else:
    print("Acesso negado!")
