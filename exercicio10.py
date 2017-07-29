#!/usr/bin/python

# Criar três variáveis chamadas OLD, NEW e MAX, cujo conteúdo é 0
OLD,NEW,MAX = 0,0,0

# Iniciar o loop do tipo while
while MAX <= 100:

    # Solicite para o usuário um número de 1 a 10 e armazene dentro de NEW
    while NEW < 1 or NEW > 10:
        NEW = int(input("Informe um valor entre 1 a 10: ") or '5') 

    # Confira se o valor informado pelo usuário é igual a OLD
    if NEW == OLD:

        # Se for igual imprima na tela a mensagem "São iguais"
        print("São iguais!")

        # Some os dois valores com o resultado de MAX
        MAX = (OLD + NEW) + MAX

        # Confira se o valor de MAX é igual a 100
        if MAX == 100:
            print("Valor máximo atingido")

        # Confira se o valor de MAX é maior que 100
        elif MAX > 100:
            print("Ultrapassado o limite. Encerrando o programa")
    
    # Verificar se NEW é maior que OLD
    elif NEW > OLD:

        # Imprima a mensagem "NEW maior que OLD"
        print("NEW maior que OLD")
        
        # Some os dois valores e subtraia do resultado de MAX
        MAX = (NEW + OLD) - MAX

        # Jogue o valor de NEW dentro da variável OLD
        OLD = NEW

    # Verificar se NEW é igual a 7
    elif NEW == 7:
        
        # Imprima a mensagem "NEW e OLD são diferentes, porém NEW é igual a 7"
        print("NEW e OLD são diferentes, porém NEW é igual a 7")

        # Subtraia NEW pelo OLD e substitua o MAX completamente por esse novo resultado
        MAX = NEW - OLD

    print("Valor de MAX: ",MAX)
    NEW = 0
