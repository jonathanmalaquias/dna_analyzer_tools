#!/usr/bin/env python
# coding: utf-8

# In[ ]:


####### usei o Counter da biblioteca para contar as bases A,T,C,G
from collections import Counter

####### Variáveis Globais, poderia ter otmizado de outras formas mas ainda estou aprendendo
Eseguencia = False 
dna_limpo = " "
continuar_programa = True


####### Menu principal dessa simulação contem nova seguencia, transcrição DNA -> RNAm e Sair
def inicio():
    global continuar_programa
    if Eseguencia == False :
        print("Ainda não foi informada uma seguencia de DNA")
        entradaDNA()
    else :
        print("#####################  Oque deseja fazer ?  ###################################")
        print("1 Nova seguência de DNA")
        print("2 Transcrição")
        print("3 Sair")
        seleção = input("digite uma opção")
        if seleção == "1" :
            entradaDNA()
        elif seleção == "2" :
            transcrição()
        elif seleção == "3" :
            print("Fim do progrma, Obrigado por usar :)")
            return "parar"
        else :
            print("Comando não indentificado")

######## Pede uma seguencia de DNA, só lê as bases A,T,C,G, logo em seguida conta quantas tem de cada uma usei dois globais :P ,             
def entradaDNA():
    global Eseguencia
    global dna_limpo
    seguencia = input("digite a seguência de DNA").upper()
    dna_limpo = "".join([c for c in seguencia if c in "ATCG"])
    print(f"seguencia: {seguencia}")
    contagem = Counter(dna_limpo)
    resultado = list(contagem.items())
    if contagem["A"] != contagem["T"] or contagem["C"] != contagem["G"] :
        print(f"Erro: A quantidade de A :{contagem["A"]} e T : {contagem["T"]} ou C : {contagem["C"]} e G : {contagem["G"]} não bate!")
        return
    print(resultado)
    Eseguencia = True

######## Transcrição, diz que o RNA é igual ao DNA LIMPO porem com o T "replaced" por U

def transcrição():
    rna = dna_limpo.replace("T", "U")
    print(f"Fita de RNAm: {rna}")

######### while para criar o loop e não consumir tanta memória com recursividade

while continuar_programa == True:
    comando = inicio()
    if comando == "parar":
        break

