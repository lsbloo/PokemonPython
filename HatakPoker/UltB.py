#Ultima fase para zerar o game!

##############
import random
import time
import sys
#############
ultimaB = True
loop_gaming = True
from HatakePoke_PLAY import *



def quizz_x():
    global win
    global pergunta1,pergunta2,pergunta3,pergunta4,pergunta5,pergunta6,pergunta7,pergunta8,pergunta9,pergunta10
    global resposta1,resposta2,resposta3,resposta4,resposta5,resposta6,resposta7,resposta8,resposta9,resposta10
    win = 5
    pergunta1 = "Quantos Pokemons existem na Pokédex?"
    pergunta2 = "Qual Pokémon Lendário podemos obter na caverna de Sootopolis?"
    pergunta3 = "Quais são os três pokémons iniciais que podemos escolher na liga Ruby?"
    pergunta4 = "Quem é o líder do ginásio de Sootopolis?"
    pergunta5= "Quem é o campeão da Liga dos 4?"
    pergunta6= "Qual o ginásio que tem como lideres duas irmãs gêmeas?"
    pergunta7 = "Em que cidade se localiza a loja de bicicletas do Rydel?"
    pergunta8 = "Qual o total de insígnias presente no jogo Pokémon Ruby?"
    pergunta9 = "O ginásio do Norman se localiza em Petalburg. verdadeiro ou falso?"
    pergunta10 = "Qual TM é necessário para criarmos uma base secreta?"
    resposta1 = '386'
    resposta2 = 'groundon'
    resposta3 = 'treecko'
    resposta4='wallace'
    resposta5='steven'
    resposta6='mossdeep'
    resposta7='mauville'
    resposta8='8'
    resposta9="verdadeiro"
    resposta10="secret power"

def ultimaB_game():
    res=''
    cont = 0

    
    print()
    print(pergunta1)
    res = input("Your Aswner: ")
    if res == resposta1:
        cont = cont +1
    else:
        print("Error!")

    print()
    print(pergunta2)
    res = input("Your Aswner: ")
    if res == resposta2:
        cont = cont +1
    else:
        print("Error!")

    print()
    print(pergunta3)
    res = input("Your Aswner: ")
    if res == resposta3:
        cont = cont +1
    else:
        print("Error!")

    print()
    print(pergunta4)
    res = input("Your Aswner: ")
    if res == resposta4:
        cont = cont +1
    else:
        print("Error!")


    print()
    print(pergunta5)
    res = input("Your Aswner: ")
    if res == resposta5:
        cont = cont +1
    else:
        print("Error!")

    print()
    print(pergunta6)
    res = input("Your Aswner: ")
    if res == resposta6:
        cont = cont +1
    else:
        print("Error!")

    print()
    print(pergunta7)
    res = input("Your Aswner: ")
    if res == resposta7:
        cont = cont +1
    else:
        print("Error!")

    print()
    print(pergunta8)
    res = input("Your Aswner: ")
    if res == resposta8:
        cont = cont +1
    else:
        print("Error!")

    print()
    print(pergunta9)
    res = input("Your Aswner: ")
    if res == resposta9:
        cont = cont +1
    else:
        print("Error!")

    print()
    print(pergunta10)
    res = input("Your Aswner: ")
    if res == resposta10:
        cont = cont +1
    else:
        print("Error!")

    if cont >= 6:
        print()
        print("You Win Concragulations!")
        print()
        print("Very good, you are indeed a good pokemon trainer!")
    else:
        
        print("You Lose , Sorry!")
        print("accumulate points: ",cont)
    
if ultimaB == True and last == True:
    print()
    print()
    GHP = """
    
    *¦¦¦¦¦¦+ ¦¦¦¦¦¦¦¦+     ¦¦¦¦¦¦+¦¦¦¦¦¦+  ¦¦¦¦¦+ ¦¦¦¦¦¦¦+¦¦+  ¦¦+
     ¦¦+--¦¦++--¦¦+--+    ¦¦+----+¦¦+--¦¦+¦¦+--¦¦+¦¦+----+¦¦¦  ¦¦¦
     ¦¦¦¦¦¦++   ¦¦¦       ¦¦¦     ¦¦¦¦¦¦++¦¦¦¦¦¦¦¦¦¦¦¦¦¦¦+¦¦¦¦¦¦¦¦
     ¦¦+--¦¦+   ¦¦¦       ¦¦¦     ¦¦+--¦¦+¦¦+--¦¦¦+----¦¦¦¦¦+--¦¦¦
     ¦¦¦  ¦¦¦   ¦¦¦       +¦¦¦¦¦¦+¦¦¦  ¦¦¦¦¦¦  ¦¦¦¦¦¦¦¦¦¦¦¦¦¦  ¦¦¦
     +-+  +-+   +-+        +-----++-+  +-++-+  +-++------++-+  +-+
    * 

    """
    print(GHP)
    print()
    print()
    print("Welcome to the last Fight of game.. you dont have more chances of win!")
    print()
    print("You need to answer a series of questions and accumulate 6 points.")
    print()
    print("Lets go!!!")

def main():
    quizz_x()
    ultimaB_game()

main()

