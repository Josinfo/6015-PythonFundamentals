#!/usr/bin/python

# Criando minha classe de alunos
class alunos:

    # Criando minha lista de estados
    lstestados = ['SP','RJ','BA','CE','AM','DF']

    # Inicializando minhas variáveis
    nome = None
    idade = 0
    curso = None
    cidade = None
    estado = None
    notas = []
    media = 0

    # Cadastrar média
    def cadastrar_media(self):
        for i in self.notas:
            self.media += i
        self.media /= 5

    # Cadastrar notas
    def cadastrar_nota(self,notas):
        if len(self.notas) <= 5:
            self.notas.append(notas)

    # Cadastrar estado
    def cadastrar_estado(self,estado):
        for i in self.lstestados:
            if estado == i:
                self.estado = estado
                break
        else:
            print("Falha ao cadastrar estado")

    # Cadastrar idade
    def cadastrar_idade(self,idade):
        if idade > 0 and idade <= 200:
            self.idade = idade

    # Verificar se aluno está aprovado
    def isAprovado(self):
        if self.media >= 7:
            return True
        else:
            return False

estudante = alunos()
estudante.nome = input("Informe o nome do aluno: ")
estudante.cadastrar_idade(int(input("Informe a idade do aluno: ")))
estudante.curso = input("Informe o curso do estudante: ")
estudante.cidade = input("Informe a cidade do estudante: ")
estudante.cadastrar_estado(input("Informe o estado - SIGLA: "))
for i in range(5):
    estudante.cadastrar_nota(int(input("Informe a {0}º nota do estudante: ".format(i+1))))

estudante.cadastrar_media()

print("Nome do estudante: ",estudante.nome)
print("Idade: ",estudante.idade)
print("Curso: ",estudante.curso)
print("Cidade: ",estudante.cidade)
print("Estado: ",estudante.estado)
print("Média: ",estudante.media)
if estudante.isAprovado():
    print("Status: APROVADO")
else:
    print("Status: REPROVADO")
