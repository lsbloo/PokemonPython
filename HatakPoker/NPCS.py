"""
NPCS
"""
#Neste modulo estara os npcs com suas vendas
#De Potion e Revive
import time
import random

def NPC():
    #FUNCAO INACABADA FALTA TERMINAR:
    #PRECISO AJEITAR URGENTEMENTE ESSA FUNCAO
    #PRA PODER JOGAR ELA NO MODULO LUTA CORRETAMENTE/
    cont = 0
    cash = 1000
    print("Olá,eu sou o Mark....")
    time.sleep(1)
    print("Aqui voce encontrará revives,e potions..")
    time.sleep(1)
    num = int(input("Digite Quantas vezes voce deseja comprar: "))
    while cont < num:
        print("Voce deseja comprar Potions?")
        n1 = int(input("Digite (1) para comprar Potions ou (2) para pular: "))
        print("Voce deseja comprar Potions?")
        n2 = int(input("Digite (1) para comprar Revives ou (2) para pular: "))
        if n1 == 1:
            Potions = 100
            print("HMM")
            time.sleep(1)
            print("-------------------")
            print("1 Potion = 100 Reais")
            print("voce tem",cash,"Reais")
            #print("Voce so pode comprar 1 revive!")
            buy = input("Deseja comprar sim/nao: ")
            if buy == "sim":
                print("Voce comprou um POTION")
                cash -= Potions
                print("voce ficou com",cash,"Reais")
                
        if n2 == 1:
            potions = 100
            print("HMM")
            time.sleep(1)
            print("----------------------")
            print("Quantas Potions voce deseja:")
            print("-------------------------")
            print("1 Potion - 5 dl")
            #Falta terminar Pulei,.;;;
        cont += 1



NPC()
