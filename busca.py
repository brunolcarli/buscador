#coding=utf8

#Programa facilitador para busca no arquivo morto, retorna o código e o nome do aluno 
#Programa aberto para modificações posteriores

#Versão 1.0.0 por Bruno L. Carli / brunolcarli@gmail.com

loop = True

print "#############################"
print "# Programa que busca o nome #"
print "# do aluno no arquivo morto #"
print "#                           #"
print "#   Insira o nome do aluno  #"
print "#        entre 'aspas'      #"
print "#                           #"
print "#############################"

# loop principal
while loop == True:
    try:
        # pede o nome, guarda na variavel como string e converte para caixa alta
        nome = str(input("Insira o nome do Aluno: "))
        nome = nome.upper()
        # para cada linha no documento irá buscar o nome inserido
        for linha in open("arquivo_database.csv"): # <---- inserir aqui seu arquivo database para busca, entre aspas
            if nome in linha:
                print(linha)
                #se encontrar encerra o loop principal
                loop = False
        if nome not in open('arquivo_database.csv'): # <---- inserir aqui seu arquivo database para busca, entre aspas
            print "#############################"
            print "#      Busca Encerrada!     #"
            print "#     Não foi encontrado    #"
            print "#      mais nenhum nome     #"
            print "#        relacionado        #"
            print "#############################"
            break
    # caso o usuario nao coloque o nome entre aspas
    except:
        print"#############################"
        print"#     Por Favor Insira o    #"
        print"#     nome entre 'aspas'    #"
        print"#############################"
