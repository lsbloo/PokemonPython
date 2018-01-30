"""
Luta
"""

from Player import *
from poke_inimigos import *
#Neste modulo estara contida as funcoes da luta entre o player e o inimigo
#
cash = 100
jogando = True
print()
print("Voce deseja atacar?")
res = int(input("Digite (1)= Atk: "))
if res == 1:
    if chart == 1:
        print("Charmander Possue 3 ataques...")
        print("Ember,flametower e fireblast...")
    if chart == 2:
        print("Squirtle Possue 3 ataques...")
        print("Bubles,Warteball e Blubleam!!")
        print()
    if chart == 3:
        print("Bulbasaur Possue 3 ataques...")
        print("WineVip,Razor Leaf e Leaf Store!!")
        print()
    #if chart == 4:
        #print("Gloom Possue 3 ataques...")
        #print("Poison Job,Acid e Poison Gás!!")
        #print()
    #if chart == 5:
        #print("Golbat Possue 3 ataques...")
        #print("Bite,Wirldtril e Wing Attack!!")
        #print()
    #if chart == 6:
        #print("Graveler Possue 3 ataques...")
        #print("Rock Trown,Rock Slide e EarthPower!!")
        #print()
elif res != 1:
    jogando = False
    print("Fim de JOGO!")
    print("End Of Game!")
    if chart1 == 1:
        print("Geodude Possue 3 ataques...")
        print("Rock Smash,RockSlide e EarthPower...")
        print()
    if chart1 == 2:
        print("Shiny Horsea Possue 3 ataques...")
        print("Bubbles,Warteball e HydroPump...")
        print()
    if chart1 == 3:
        print("Golden Possue 3 ataques...")
        print("Aquatail,Bubbleam e Horn Attack...")
        print()
    if chart1 == 4:
        print("Vulpix Possue 3 ataques...")
        print("Ember,Flametower e Fireblast...")
        print()
    if chart1 == 5:
        print("Oddish Possue 3 ataques...")
        print("Acid,Absorb e Poison Gás...")
        print()
    if chart1 == 6:
        print("Shiny Tentacool Possue 3 ataques...")
        print("Warteball,Aquatail e HydroPump...")
        print()
def jogo():
    global jogando,vida_geodude,atk_charmander_cd1,atk_charmander_cd2,vida_shiny_horsea,vida_golden,vida_vulpix,vida_geodude,player_vida
    global player_inimigo
    global vida_charmander
    global vida_oddish
    global vida_shiny_tentacool
    global vida_squirte
    global vida_bulbarsaur
    global cash, Porcao
    #uma porcao cura 3000 de Life...
    Porcao = 3000
    buy = not False
    while jogando == True:
        
        #CHARMANDER
        if chart == 1 and chart1 == 1: #CHAMANDER X GEODUDE
            print("-------------------")
            print("Charmander!,Eu escolho você")
            #Erro nessa funcao!
            #ja consertei as funcoes do player
            #Falta consertar as funcoes do Inimigo
            #Para colocar aq
            
            print("Digite (1)-para usar ember,(2)-para usar flametower,(3)-para usar fireblast")
            res = int(input("(1),(2),(3): "))
            if res == 1:
                print("Charmander Use Ember!!")
                vida_geodude -= atk_charmander_cd1
                print("Vida do Geodude",vida_geodude)
                if vida_geodude <= 0:
                    print("Geodude,Morreu")
                    try:
                        print("Voce tem a chance de matar seu inimigo!!")
                        print("Antes que ele coloque outro poke!")
                        print()
                        print("Charmander use Ember!!")
                        player_inimigo -= atk_charmander_cd1
                        print("Vida do Seu inimigo",player_inimigo)
                        if player_inimigo <= 0:
                            print("Voce o Derrotou")
                            print("Vida do Inimigo",player_inimigo)
                            break
                    except:
                        print("Deseja matar outro inimigo?")
    
                print()
                print("Geodude,Contra-Ataca")
                vida_charmander -= atk_geodude_cd2
                print("Vida do seu charmander",vida_charmander)
                #POtions MArket
                if vida_charmander <=0:
                    print()
                    print("Seu Charmander Morreu")
                    fly = input("Deseja comprar Potions: [S-sim/N-nao]: ")
                    if fly == "S" or fly == "sim":
                        from NPCS import NPC
                        vida_charmander += Porcao
                        print("Seu charmander Foi curado ,Life Atual",vida_charmander)
                       
                        
                        
                    else:
                        print("Voce esta Vulneravel aos ataques!!")
                        player_vida -= atk_geodude_cd2
                        print("OHH NAOOO!!")
                        print("Voce foi atacado sua é vida é de:",player_vida)
                        if player_vida <=0:
                            print("END OF GAME")
                            print()
                            print("VOCE PERDEU!!")
                            break
            elif res == 2:
                print("Charmander use Flametower!!")
                vida_geodude -= atk_charmander_cd2
                print("Vida do Geodude",vida_geodude)
                if vida_geodude <= 0:
                    print("Geodude,Morreu")
                    try:
                        print("Voce tem a chance de matar seu inimigo!!")
                        print("Antes que ele coloque outro poke!")
                        print()
                        print("Charmander use Ember!!")
                        player_inimigo -= atk_charmander_cd1
                        print("Vida do Seu inimigo",player_inimigo)
                        if player_inimigo <= 0:
                            print("Voce o Derrotou")
                            print("Vida do Inimigo",player_inimigo)
                            break
                            
                    except:
                        print("Deseja matar outro inimigo?")

                print()
                print("Geodude,Contra-Ataca")
                vida_charmander -= atk_geodude_cd2
                print("Vida do seu charmander",vida_charmander)
                #POtions MArket
                if vida_charmander <=0:
                    print()
                    print("Seu Charmander Morreu")
                    fly = input("Deseja comprar Potions: [S-sim/N-nao]: ")
                    if fly == "S" or fly == "sim":
                        from NPCS import NPC
                        vida_charmander += Porcao
                        print("Seu charmander Foi curado ,Life Atual",vida_charmander)
                       
                        
                        
                    else:
                        print("Voce esta Vulneravel aos ataques!!")
                        player_vida -= atk_geodude_cd2
                        print("OHH NAOOO!!")
                        print("Voce foi atacado sua é vida é de:",player_vida)
                        if player_vida <=0:
                            print("END OF GAME")
                            print()
                            print("VOCE PERDEU!!")
                            break
                    
            elif res == 3:
                print("Charmander use FireBlast!!")
                vida_geodude -= atk_charmander_cd3
                print("Vida do Geodude",vida_geodude)
                if vida_geodude <=0:
                    print("Geodude,Morreu")
                    try:
                        print("Voce tem a chance de matar seu inimigo!!")
                        print("Antes que ele coloque outro poke!")
                        print()
                        print("Charmander use Ember!!")
                        player_inimigo -= atk_charmander_cd1
                        print("Vida do Seu inimigo",player_inimigo)
                        if player_inimigo <= 0:
                            print("Voce o Derrotou")
                            print("Vida do Inimigo",player_inimigo)
                            break
                            
                    except:
                        print("Deseja matar outro inimigo?")

                print()
                print("Geodude,Contra-Ataca")
                vida_charmander -= atk_geodude_cd2
                print("Vida do seu charmander",vida_charmander)
                #POtions MArket
                
                if vida_charmander <=0:
                    print()
                    print("Seu Charmander Morreu")
                    fly = input("Deseja comprar Potions: [S-sim/N-nao]: ")
                    if fly == "S" or fly == "sim":
                        from NPCS import NPC
                        vida_charmander += Porcao
                        print("Seu charmander Foi curado ,Life Atual",vida_charmander)
                       
                        
                        
                    else:
                        print("Voce esta Vulneravel aos ataques!!")
                        player_vida -= atk_geodude_cd2
                        print("OHH NAOOO!!")
                        print("Voce foi atacado sua é vida é de:",player_vida)
                        if player_vida <=0:
                            print("END OF GAME")
                            print()
                            print("VOCE PERDEU!!")
                            break
                 
       
        elif chart == 1 and chart1 == 2: # CHARMANDER X SHINY HORSEA
            print("-------------------")
            print("Charmander!,Eu escolho você")
            print("Digite (1)-para usar ember,(2)-para usar flametower,(3)-para usar fireblast")
            res = int(input("(1),(2),(3): "))
            if res == 1:
                print("Charmander Use Ember!!")
                vida_shiny_horsea -= atk_charmander_cd1
                print("Vida do Shiny Horsea",vida_shiny_horsea)
                if vida_shiny_horsea <= 0:
                    print("Shiny Horsea,Morreu")

                #
                try:
                    print("Você tem a chance de matar seu inimigo")
                    print("Antes que ele coloque outro pokemon:")
                    print()
                    print("Charmander use Ember")
                    player_inimigo -= atk_charmander_cd1
                    if player_inimigo <= 0:
                        print("Voce o Derrotou")
                        print("Vida do Inimigo",player_inimigo)
                        break
                       
                except:
                    print("Deseja matar outro inimigo:")
                print()
                print("Shiny Horsea,Contra-Ataca")
                vida_charmander -= atk_horsea_cd2
                print("Vida do seu charmander",vida_charmander)
                print("Vida do seu charmander",vida_charmander)
                if vida_charmander <=0:
                    print()
                    print("Seu Charmander Morreu")
                    fly = input("Deseja comprar Potions: [S-sim/N-nao]: ")
                    if fly == "S" or fly == "sim":
                        from NPCS import NPC
                        #CONSEGUIR COLOCAR A CURA DOS POKEMON IMPORTANDO A FUNCAO NPC DO MODULO.
                        #MAS ELA MEIO QUE FICOU FICTICIA.. MAS COLOQUEI UMA CURA MAIOR PARA O POKEMON...
                        #AINDA EM TESTES...
                        vida_charmander += Porcao
                        print("Seu charmander Foi curado ,Life Atual",vida_charmander)
                        
                    else:
                        print("Voce esta Vulneravel aos ataques!!")
                        player_vida -= atk_horsea_cd2
                        print("OHH NAOOO!!")
                        print("Voce foi atacado sua é vida é de:",player_vida)
                        if player_vida <=0:
                            print("END OF GAME")
                            print()
                            print("VOCE PERDEU!!")
                            break
                
            elif res == 2:
                print("Charmander Use Flametower!!")
                vida_shiny_horsea -= atk_horsea_cd2
                print("Vida do Shiny Horsea",vida_shiny_horsea)
                if vida_shiny_horsea <=0:
                    print("Shiny Horsea,Morreu")
                    try:
                        print("Voce tem a chance de matar seu inimigo!!")
                        print("Antes que ele coloque outro poke!")
                        print()
                        print("Charmander use Ember!!")
                        player_inimigo -= atk_charmander_cd1
                        print("Vida do Seu inimigo",player_inimigo)
                        if player_inimigo <= 0:
                            print("Voce o Derrotou")
                            print("Vida do Inimigo",player_inimigo)
                            break
                            
                    except:
                        print("Deseja matar outro inimigo?")

                
                print()
                print("Shiny Horsea,Contra-Ataca")
                vida_charmander -= atk_horsea_cd2
                print("Vida do seu charmander",vida_charmander)
                #POTIONS MAKET
                if vida_charmander <=0:
                    print()
                    print("Seu Charmander Morreu")
                    fly = input("Deseja comprar Potions: [S-sim/N-nao]: ")
                    if fly == "S" or fly == "sim":
                        from NPCS import NPC
                        vida_charmander += Porcao
                        print("Seu charmander Foi curado ,Life Atual",vida_charmander)
                       
                        
                        
                    else:
                        print("Voce esta Vulneravel aos ataques!!")
                        player_vida -= atk_horsea_cd2
                        print("OHH NAOOO!!")
                        print("Voce foi atacado sua é vida é de:",player_vida)
                        if player_vida <=0:
                            print("END OF GAME")
                            print()
                            print("VOCE PERDEU!!")
                            break
                
            elif res == 3:
                print("Charmander use FireBlast!!")
                vida_shiny_horsea -= atk_charmander_cd3
                print("Vida do Geodude",vida_shiny_horsea)
                if vida_shiny_horsea <= 0:
                    print("Shiny Horsea,Morreu")
                    try:
                        print("Voce tem a chance de matar seu inimigo!!")
                        print("Antes que ele coloque outro poke!")
                        print()
                        print("Charmander use Ember!!")
                        player_inimigo -= atk_charmander_cd1
                        print("Vida do Seu inimigo",player_inimigo)
                        if player_inimigo <= 0:
                            print("Voce o Derrotou")
                            print("Vida do Inimigo",player_inimigo)
                            break
                           
                    except:
                        print("Deseja matar outro inimigo?")

                
                print()
                print("Shiny Horsea,Contra-Ataca")
                vida_charmander -= atk_horsea_cd2
                print("Vida do seu charmander",vida_charmander)
                
                #POTIONS MAKET
                if vida_charmander <=0:
                    print()
                    print("Seu Charmander Morreu")
                    fly = input("Deseja comprar Potions: [S-sim/N-nao]: ")
                    if fly == "S" or fly == "sim":
                        from NPCS import NPC
                        vida_charmander += Porcao
                        print("Seu charmander Foi curado ,Life Atual",vida_charmander)
                       
                        
                        
                    else:
                        print("Voce esta Vulneravel aos ataques!!")
                        player_vida -= atk_horsea_cd2
                        print("OHH NAOOO!!")
                        print("Voce foi atacado sua é vida é de:",player_vida)
                        if player_vida <=0:
                            print("END OF GAME")
                            print()
                            print("VOCE PERDEU!!")
                            break
                
                
        elif chart == 1 and chart1 == 3: #CHAMANDER X GOLDEN
            print("-------------------")
            print("Charmander!,Eu escolho você")
            
            print("Digite (1)-para usar ember,(2)-para usar flametower,(3)-para usar fireblast")
            res = int(input("(1),(2),(3): "))
            if res == 1:
                print("Charmander Use Ember!!")
                vida_golden -= atk_charmander_cd1
                print("Vida do Golden",vida_golden)
                if vida_golden <= 0:
                    print("Golden,Morreu")
                    try:
                        print("Você tem a chance de matar seu inimigo")
                        print("Antes que ele coloque outro pokemon:")
                        print()
                        print("Charmander use Ember")
                        player_inimigo -= atk_charmander_cd1
                        if player_inimigo <= 0:
                            print("Vida do Inimigo",player_inimigo)
                            print("Voce o Derrotou")
                            break
                           
                    except:
                        print("Deseja matar outro inimigo:")
                        

                print()
                print("Golden,Contra-Ataca")
                vida_charmander -= atk_golden_cd2
                print("Vida do seu charmander",vida_charmander)
                if vida_charmander <=0:
                    print()
                    print("Seu Charmander Morreu")
                    fly = input("Deseja comprar Potions: [S-sim/N-nao]: ")
                    if fly == "S" or fly == "sim":
                        from NPCS import NPC
                        vida_charmander += Porcao
                        print("Seu charmander Foi curado ,Life Atual",vida_charmander)
                        
                        
                    else:
                        print("Voce esta Vulneravel aos ataques!!")
                        player_vida -= atk_golden_cd2
                        print("OHH NAOOO!!")
                        print("Voce foi atacado sua é vida é de:",player_vida)
                        if player_vida <=0:
                            print("END OF GAME")
                            print()
                            print("VOCE PERDEU!!")
                            break
                
            elif res == 2:
                print("Charmander use Flametower!!")
                vida_golden -= atk_charmander_cd2
                print("Vida do Golden",vida_golden)
                if vida_golden <= 0:
                    print("Golden,Morreu")
                    try:
                        print("Voce tem a chance de matar seu inimigo!!")
                        print("Antes que ele coloque outro poke!")
                        print()
                        print("Charmander use Ember!!")
                        player_inimigo -= atk_charmander_cd1
                        print("Vida do Seu inimigo",player_inimigo)
                        if player_inimigo <= 0:
                            print("Voce o Derrotou")
                            print("Vida do Inimigo",player_inimigo)
                            break
                            
                    except:
                        print("Deseja matar outro inimigo?")

                print()
                print("Golden,Contra-Ataca")
                vida_charmander -= atk_golden_cd2
                print("Vida do seu charmander",vida_golden)
                #POTIONS MARKET
                if vida_charmander <=0:
                    print()
                    print("Seu Charmander Morreu")
                    fly = input("Deseja comprar Potions: [S-sim/N-nao]: ")
                    if fly == "S" or fly == "sim":
                        from NPCS import NPC
                        vida_charmander += Porcao
                        print("Seu charmander Foi curado ,Life Atual",vida_charmander)
                        
                        
                    else:
                        print("Voce esta Vulneravel aos ataques!!")
                        player_vida -= atk_golden_cd2
                        print("OHH NAOOO!!")
                        print("Voce foi atacado sua é vida é de:",player_vida)
                        if player_vida <=0:
                            print("END OF GAME")
                            print()
                            print("VOCE PERDEU!!")
                            break
                        
            elif res == 3:
                print("Charmander use FireBlast!!")
                vida_golden -= atk_charmander_cd3
                print("Vida do Geodude",vida_golden)
                if vida_golden <= 0:
                    print("Golden,Morreu")
                    try:
                        print("Voce tem a chance de matar seu inimigo!!")
                        print("Antes que ele coloque outro poke!")
                        print()
                        print("Charmander use Ember!!")
                        player_inimigo -= atk_charmander_cd1
                        print("Vida do Seu inimigo",player_inimigo)
                        if player_inimigo <= 0:
                            print("Voce o Derrotou")
                            print("Vida do Inimigo",player_inimigo)
                            break
                            
                    except:
                        print("Deseja matar outro inimigo?")

                print()
                print("Golden,Contra-Ataca")
                vida_charmander -= atk_golden_cd2
                print("Vida do seu charmander",vida_charmander)

                #POTIONS MARKET
                if vida_charmander <=0:
                    print()
                    print("Seu Charmander Morreu")
                    fly = input("Deseja comprar Potions: [S-sim/N-nao]: ")
                    if fly == "S" or fly == "sim":
                        from NPCS import NPC
                        vida_charmander += Porcao
                        print("Seu charmander Foi curado ,Life Atual",vida_charmander)
                        
                        
                    else:
                        print("Voce esta Vulneravel aos ataques!!")
                        player_vida -= atk_golden_cd2
                        print("OHH NAOOO!!")
                        print("Voce foi atacado sua é vida é de:",player_vida)
                        if player_vida <=0:
                            print("END OF GAME")
                            print()
                            print("VOCE PERDEU!!")
                            break
                
                
        elif chart == 1 and chart1 == 4: #CHAMANDER X VULPIX
            print("-------------------")
            print("Charmander!,Eu escolho você")
            charmander()
            print("Digite (1)-para usar ember,(2)-para usar flametower,(3)-para usar fireblast")
            res = int(input("(1),(2),(3): "))
            if res == 1:
                print("Charmander Use Ember!!")
                vida_vulpix -= atk_charmander_cd1
                print("Vida do Vulpix",vida_vulpix)
                if vida_vulpix <= 0:
                    print("Vulpix ,Morreu")
                    try:
                        print("Voce tem a chance de matar seu inimigo!!")
                        print("Antes que ele coloque outro poke!")
                        print()
                        print("Charmander use Ember!!")
                        player_inimigo -= atk_charmander_cd1
                        print("Vida do Seu inimigo",player_inimigo)
                        if player_inimigo <= 0:
                            print("Voce o Derrotou")
                            print("Vida do Inimigo",player_inimigo)
                            break
                           
                    except:
                        print("Deseja matar outro inimigo?")

                print()
                print("Vulpix,Contra-Ataca")
                vida_charmander -= atk_vulpix_cd2
                print("Vida do seu charmander",vida_charmander)

                #POTIONS MARKET
                        
                if vida_charmander <=0:
                    print()
                    print("Seu Charmander Morreu")
                    fly = input("Deseja comprar Potions: [S-sim/N-nao]: ")
                    if fly == "S" or fly == "sim":
                        from NPCS import NPC
                        vida_charmander += Porcao
                        print("Seu charmander Foi curado ,Life Atual",vida_charmander)
                        
                    else:
                        print("Voce esta Vulneravel aos ataques!!")
                        player_vida -= atk_vulpix_cd2
                        print("OHH NAOOO!!")
                        print("Voce foi atacado sua é vida é de:",player_vida)
                        if player_vida <=0:
                            print("END OF GAME")
                            print()
                            print("VOCE PERDEU!!")
                            break
                
            elif res ==2:
                print("Charmander Use Flametower!!")
                vida_vulpix -= atk_charmander_cd2
                print("Vida do Vulpix",vida_vulpix)
                if vida_vulpix <= 0:
                    print("Vulpix,Morreu")
                    try:
                        print("Voce tem a chance de matar seu inimigo!!")
                        print("Antes que ele coloque outro poke!")
                        print()
                        print("Charmander use Ember!!")
                        player_inimigo -= atk_charmander_cd1
                        print("Vida do Seu inimigo",player_inimigo)
                        if player_inimigo <= 0:
                            print("Voce o Derrotou")
                            print("Vida do Inimigo",player_inimigo)
                            break
                            
                    except:
                        print("Deseja matar outro inimigo?")
                print()
                print("Vulpix,Contra-Ataca")
                vida_charmander -= atk_vulpix_cd2
                print("Vida do seu charmander",vida_charmander)

                #POTIONS MARKET

                if vida_charmander <=0:
                    print()
                    print("Seu Charmander Morreu")
                    fly = input("Deseja comprar Potions: [S-sim/N-nao]: ")
                    if fly == "S" or fly == "sim":
                        from NPCS import NPC
                        vida_charmander += Porcao
                        print("Seu charmander Foi curado ,Life Atual",vida_charmander)
                        
                        
                    else:
                        print("Voce esta Vulneravel aos ataques!!")
                        player_vida -= atk_vulpix_cd2
                        print("OHH NAOOO!!")
                        print("Voce foi atacado sua é vida é de:",player_vida)
                        if player_vida <=0:
                            print("END OF GAME")
                            print()
                            print("VOCE PERDEU!!")
                            break
                
            elif res == 3:
                print("Charmander use FireBlast!!")
                vida_vulpix -= atk_charmander_cd3
                print("Vida do Geodude",vida_vulpix)
                if vida_vulpix <= 0:
                    print("Vulpix,Morreu")
                    try:
                        print("Voce tem a chance de matar seu inimigo!!")
                        print("Antes que ele coloque outro poke!")
                        print()
                        print("Charmander use Ember!!")
                        player_inimigo -= atk_charmander_cd1
                        print("Vida do Seu inimigo",player_inimigo)
                        if player_inimigo <= 0:
                            print("Voce o Derrotou")
                            print("Vida do Inimigo",player_inimigo)
                            break
                            
                    except:
                        print("Deseja matar outro inimigo?")

                print()
                print("Vulpix,Contra-Ataca")
                vida_charmander -= atk_vulpix_cd2
                print("Vida do seu charmander",vida_charmander)

                 #POTIONS MARKET

                if vida_charmander <=0:
                    print()
                    print("Seu Charmander Morreu")
                    fly = input("Deseja comprar Potions: [S-sim/N-nao]: ")
                    if fly == "S" or fly == "sim":
                        from NPCS import NPC
                        vida_charmander += Porcao
                        print("Seu charmander Foi curado ,Life Atual",vida_charmander)
                        
                        
                    else:
                        print("Voce esta Vulneravel aos ataques!!")
                        player_vida -= atk_vulpix_cd2
                        print("OHH NAOOO!!")
                        print("Voce foi atacado sua é vida é de:",player_vida)
                        if player_vida <=0:
                            print("END OF GAME")
                            print()
                            print("VOCE PERDEU!!")
                            break
                
                

        elif chart == 1 and chart1 == 5: #CHAMANDER X ODDISH
            print("-------------------")
            print("Charmander!,Eu escolho você")
            print("Digite (1)-para usar ember,(2)-para usar flametower,(3)-para usar fireblast")
            res = int(input("(1),(2),(3): "))
            if res == 1:
                print("Charmander Use Ember!!")
                vida_oddish -= atk_charmander_cd1
                print("Vida do Oddish",vida_oddish)
                if vida_oddish <= 0:
                    print("Oddish,Morreu")
                    try:
                        print("Voce tem a chance de matar seu inimigo!!")
                        print("Antes que ele coloque outro poke!")
                        print()
                        print("Charmander use Ember!!")
                        player_inimigo -= atk_charmander_cd1
                        print("Vida do Seu inimigo",player_inimigo)
                        if player_inimigo <= 0:
                            print("Voce o Derrotou")
                            print("Vida do Inimigo",player_inimigo)
                            break
                            
                    except:
                        print("Deseja matar outro inimigo?")

                print()
                print("Oddish,Contra-Ataca")
                vida_charmander -= atk_oddish_cd2
                print("Vida do charmander",vida_charmander)

                 #POTIONS MARKET

                if vida_charmander <=0:
                    print()
                    print("Seu Charmander Morreu")
                    fly = input("Deseja comprar Potions: [S-sim/N-nao]: ")
                    if fly == "S" or fly == "sim":
                        from NPCS import NPC
                        vida_charmander += Porcao
                        print("Seu charmander Foi curado ,Life Atual",vida_charmander)
                        
                        
                    else:
                        print("Voce esta Vulneravel aos ataques!!")
                        player_vida -= atk_oddish_cd2
                        print("OHH NAOOO!!")
                        print("Voce foi atacado sua é vida é de:",player_vida)
                        if player_vida <=0:
                            print("END OF GAME")
                            print()
                            print("VOCE PERDEU!!")
                            break
                
            elif res == 2:
                print("Charmander use Flametower!!")
                vida_oddish -= atk_charmander_cd2
                print("Vida do Oddish",vida_oddish)
                if vida_oddish <= 0:
                    print("Oddish,Morreu")
                    try:
                        print("Voce tem a chance de matar seu inimigo!!")
                        print("Antes que ele coloque outro poke!")
                        print()
                        print("Charmander use Ember!!")
                        player_inimigo -= atk_charmander_cd1
                        print("Vida do Seu inimigo",player_inimigo)
                        if player_inimigo <= 0:
                            print("Voce o Derrotou")
                            print("Vida do Inimigo",player_inimigo)
                            break
                            
                    except:
                        print("Deseja matar outro inimigo?")

                print()
                print("Oddish,Contra-Ataca")
                vida_charmander -= atk_oddish_cd2
                print("Vida do charmander",vida_charmander)

                 #POTIONS MARKET

                if vida_charmander <=0:
                    print()
                    print("Seu Charmander Morreu")
                    fly = input("Deseja comprar Potions: [S-sim/N-nao]: ")
                    if fly == "S" or fly == "sim":
                        from NPCS import NPC
                        vida_charmander += Porcao
                        print("Seu charmander Foi curado ,Life Atual",vida_charmander)
                        
                        
                    else:
                        print("Voce esta Vulneravel aos ataques!!")
                        player_vida -= atk_oddish_cd2
                        print("OHH NAOOO!!")
                        print("Voce foi atacado sua é vida é de:",player_vida)
                        if player_vida <=0:
                            print("END OF GAME")
                            print()
                            print("VOCE PERDEU!!")
                            break
                
            elif res == 3:
                print("Charmander use FireBlast!!")
                vida_oddish -= atk_charmander_cd3
                print("Vida do Oddish",vida_oddish)
                if vida_oddish <= 0:
                    print("Oddish,Morreu")
                    try:
                        print("Voce tem a chance de matar seu inimigo!!")
                        print("Antes que ele coloque outro poke!")
                        print()
                        print("Charmander use Ember!!")
                        player_inimigo -= atk_charmander_cd1
                        print("Vida do Seu inimigo",player_inimigo)
                        if player_inimigo <= 0:
                            print("Voce o Derrotou")
                            print("Vida do Inimigo",player_inimigo)
                            break
                            
                    except:
                        print("Deseja matar outro inimigo?")
                
                print()
                print("Oddish,Contra-Ataca")
                vida_charmander -= atk_oddish_cd2
                print("Vida do charmander",vida_charmander)

                 #POTIONS MARKET

                if vida_charmander <=0:
                    print()
                    print("Seu Charmander Morreu")
                    fly = input("Deseja comprar Potions: [S-sim/N-nao]: ")
                    if fly == "S" or fly == "sim":
                        from NPCS import NPC
                        vida_charmander += Porcao
                        print("Seu charmander Foi curado ,Life Atual",vida_charmander)
                        
                        
                    else:
                        print("Voce esta Vulneravel aos ataques!!")
                        player_vida -= atk_oddish_cd2
                        print("OHH NAOOO!!")
                        print("Voce foi atacado sua é vida é de:",player_vida)
                        if player_vida <=0:
                            print("END OF GAME")
                            print()
                            print("VOCE PERDEU!!")
                            break
                
        elif chart == 1 and chart1 == 6: #CHARMANDER X SHINY TENTACOOL
            print("-------------------")
            print("Charmander!,Eu escolho você")
            print("Digite (1)-para usar ember,(2)-para usar flametower,(3)-para usar fireblast")
            res = int(input("(1),(2),(3): "))
            if res == 1:
                print("Charmander Use Ember!!")
                vida_shiny_tentacool -= atk_charmander_cd1
                print("Vida do Shiny Tentacool",vida_shiny_tentacool)
                if vida_shiny_tentacool <=0:
                    print("Shiny Tentacool,Morreu")
                    try:
                        print("Voce tem a chance de matar seu inimigo!!")
                        print("Antes que ele coloque outro poke!")
                        print()
                        print("Charmander use Ember!!")
                        player_inimigo -= atk_charmander_cd1
                        print("Vida do Seu inimigo",player_inimigo)
                        if player_inimigo <= 0:
                            print("Voce o Derrotou")
                            print("Vida do Inimigo",player_inimigo)
                            break
                            
                    except:
                        print("Deseja matar outro inimigo?")

                print()
                print("Shiny Tentacool,Contra-Ataca")
                vida_charmander -= atk_tentacool_cd2
                print("vida do charmander",vida_charmander)

                 #POTIONS MARKET

                if vida_charmander <=0:
                    print()
                    print("Seu Charmander Morreu")
                    fly = input("Deseja comprar Potions: [S-sim/N-nao]: ")
                    if fly == "S" or fly == "sim":
                        from NPCS import NPC
                        vida_charmander += Porcao
                        print("Seu charmander Foi curado ,Life Atual",vida_charmander)
                        
                        
                    else:
                        print("Voce esta Vulneravel aos ataques!!")
                        player_vida -= atk_tentacool_cd2
                        print("OHH NAOOO!!")
                        print("Voce foi atacado sua é vida é de:",player_vida)
                        if player_vida <=0:
                            print("END OF GAME")
                            print()
                            print("VOCE PERDEU!!")
                            break
            elif res == 2:
                print("Charmander use Flametower!!")
                vida_shiny_tentacool -= atk_charmander_cd2
                print("Vida do Shiny tentacool",vida_shiny_tentacool)
                if vida_shiny_tentacool <= 0:
                    print("Shiny Tentacool,Morreu")
                    try:
                        print("Voce tem a chance de matar seu inimigo!!")
                        print("Antes que ele coloque outro poke!")
                        print()
                        print("Charmander use Ember!!")
                        player_inimigo -= atk_charmander_cd1
                        print("Vida do Seu inimigo",player_inimigo)
                        if player_inimigo <= 0:
                            print("Voce o Derrotou")
                            print("Vida do Inimigo",player_inimigo)
                            break
                            
                    except:
                        print("Deseja matar outro inimigo?")

                print()
                print("Shiny Tentacool,Contra-Ataca")
                vida_charmander -= atk_tentacool_cd2
                print("vida do charmander",vida_charmander)

                 #POTIONS MARKET

                if vida_charmander <=0:
                    print()
                    print("Seu Charmander Morreu")
                    fly = input("Deseja comprar Potions: [S-sim/N-nao]: ")
                    if fly == "S" or fly == "sim":
                        from NPCS import NPC
                        vida_charmander += Porcao
                        print("Seu charmander Foi curado ,Life Atual",vida_charmander)
                        
                        
                    else:
                        print("Voce esta Vulneravel aos ataques!!")
                        player_vida -= atk_tentacool_cd2
                        print("OHH NAOOO!!")
                        print("Voce foi atacado sua é vida é de:",player_vida)
                        if player_vida <=0:
                            print("END OF GAME")
                            print()
                            print("VOCE PERDEU!!")
                            break
                
            elif res == 3:
                print("Charmander use FireBlast!!")
                vida_shiny_tentacool -= atk_charmander_cd3
                print("Vida do Shiny Tentacool",vida_shiny_tentacool)
                if vida_shiny_tentacool <=0:
                    print("Shiny Tentacool,Morreu")
                    try:
                        print("Voce tem a chance de matar seu inimigo!!")
                        print("Antes que ele coloque outro poke!")
                        print()
                        print("Charmander use Ember!!")
                        player_inimigo -= atk_charmander_cd1
                        print("Vida do Seu inimigo",player_inimigo)
                        if player_inimigo <= 0:
                            print("Voce o Derrotou")
                            print("Vida do Inimigo",player_inimigo)
                            print("----------------")
                            break
                            
                                
                    except:
                        print("Deseja matar outro inimigo?")

                print()
                print("Shiny Tentacool,Contra-Ataca")
                vida_charmander -= atk_tentacool_cd2
                print("vida do charmander",vida_charmander)

                 #POTIONS MARKET

                if vida_charmander <=0:
                    print()
                    print("Seu Charmander Morreu")
                    fly = input("Deseja comprar Potions: [S-sim/N-nao]: ")
                    if fly == "S" or fly == "sim":
                        from NPCS import NPC
                        vida_charmander += Porcao
                        print("Seu charmander Foi curado ,Life Atual",vida_charmander)
                        
                        
                    else:
                        print("Voce esta Vulneravel aos ataques!!")
                        player_vida -= atk_tentacool_cd2
                        print("OHH NAOOO!!")
                        print("Voce foi atacado sua é vida é de:",player_vida)
                        if player_vida <=0:
                            print("END OF GAME")
                            print()
                            print("VOCE PERDEU!!")
                            break
                

       #Squirtle
        if chart == 2 and chart1 == 1: #SQUIRTLE X GEODUDE
            print("---------------------")
            print("Squirtle,Eu escolho você")
            print()
            print("Digite (1)-para usar Bubles,(2)-para usar Warteball,(3)-para usar Blubleam")
            res = int(input("(1),(2),(3): "))
            if res == 1:
                print("Squirtle,use Bubles")
                vida_geodude -= atk_squirte_cd1
                print("Vida do Geodude",vida_geodude)
                if vida_geodude <= 0:
                    try:
                        print("Voce tem a chance de matar seu inimigo!!")
                        print("Antes que ele coloque outro poke!")
                        print()
                        print("Charmander use Ember!!")
                        player_inimigo -= atk_charmander_cd1
                        print("Vida do Seu inimigo",player_inimigo)
                        if player_inimigo <= 0:
                            print("Voce o Derrotou")
                            print("Vida do Inimigo",player_inimigo)
                            break
                    except:
                        print("Deseja matar outro inimigo?")

                print()
                print("Geodude,Contra-Ataca")
                vida_squirte -= atk_geodude_cd2
                print("Vida do seu Squirtle",vida_squirte)

                 #POTIONS MARKET

                if vida_squirte <=0:
                    print()
                    print("Seu Squirtle Morreu")
                    fly = input("Deseja comprar Potions: [S-sim/N-nao]: ")
                    if fly == "S" or fly == "sim":
                        from NPCS import NPC
                        vida_squirte += Porcao
                        print("Seu squirtle Foi curado ,Life Atual",vida_charmander)
                        
                        
                    else:
                        print("Voce esta Vulneravel aos ataques!!")
                        player_vida -= atk_geodude_cd2
                        print("OHH NAOOO!!")
                        print("Voce foi atacado sua é vida é de:",player_vida)
                        if player_vida <=0:
                            print("END OF GAME")
                            print()
                            print("VOCE PERDEU!!")
                            break
            
            elif res == 2:
                print("Squirtle,use Warteball")
                vida_geodude -= atk_squirte_cd2
                print("Vida do Geodude",vida_geodude)
                if vida_geodude <= 0:
                    try:
                        print("Voce tem a chance de matar seu inimigo!!")
                        print("Antes que ele coloque outro poke!")
                        print()
                        print("Charmander use Ember!!")
                        player_inimigo -= atk_charmander_cd1
                        print("Vida do Seu inimigo",player_inimigo)
                        if player_inimigo <= 0:
                            print("Voce o Derrotou")
                            print("Vida do Inimigo",player_inimigo)
                            break
                    except:
                        print("Deseja matar outro inimigo?")
                print()
                print("Geodude,Contra-Ataca")
                vida_squirte -= atk_geodude_cd2
                print("Vida do seu Squirtle",vida_squirte)

                 #POTIONS MARKET

                if vida_squirte <=0:
                    print()
                    print("Seu Squirtle Morreu")
                    fly = input("Deseja comprar Potions: [S-sim/N-nao]: ")
                    if fly == "S" or fly == "sim":
                        from NPCS import NPC
                        vida_squirte += Porcao
                        print("Seu squirtle Foi curado ,Life Atual",vida_charmander)
                        
                        
                    else:
                        print("Voce esta Vulneravel aos ataques!!")
                        player_vida -= atk_geodude_cd2
                        print("OHH NAOOO!!")
                        print("Voce foi atacado sua é vida é de:",player_vida)
                        if player_vida <=0:
                            print("END OF GAME")
                            print()
                            print("VOCE PERDEU!!")
                            break
                        
            elif res == 3:
                print("Squirtle,use Blubleam")
                vida_geodude -= atk_squirte_cd3
                print("Vida do Geodude",vida_geodude)
                if vida_geodude <= 0:
                    try:
                        print("Voce tem a chance de matar seu inimigo!!")
                        print("Antes que ele coloque outro poke!")
                        print()
                        print("Charmander use Ember!!")
                        player_inimigo -= atk_charmander_cd1
                        print("Vida do Seu inimigo",player_inimigo)
                        if player_inimigo <= 0:
                            print("Voce o Derrotou")
                            print("Vida do Inimigo",player_inimigo)
                            break
                    except:
                        print("Deseja matar outro inimigo?")
                print()
                print("Geodude,Contra-Ataca")
                vida_squirte -= atk_geodude_cd2
                print("Vida do seu Squirtle",vida_squirte)

                 #POTIONS MARKET

                if vida_squirte <=0:
                    print()
                    print("Seu Squirtle Morreu")
                    fly = input("Deseja comprar Potions: [S-sim/N-nao]: ")
                    if fly == "S" or fly == "sim":
                        from NPCS import NPC
                        vida_squirte += Porcao
                        print("Seu squirtle Foi curado ,Life Atual",vida_charmander)
                        
                        
                    else:
                        print("Voce esta Vulneravel aos ataques!!")
                        player_vida -= atk_geodude_cd2
                        print("OHH NAOOO!!")
                        print("Voce foi atacado sua é vida é de:",player_vida)
                        if player_vida <=0:
                            print("END OF GAME")
                            print()
                            print("VOCE PERDEU!!")
                            break

        if chart == 2 and chart1 == 2: #SQUIRTLE X SHINY HORSEA
            print("---------------------")
            print("Squirtle,Eu escolho você")
            print()
            print("Digite (1)-para usar Bubles,(2)-para usar Warteball,(3)-para usar Blubleam")
            res = int(input("(1),(2),(3): "))
            if res == 1:
                print("Squirtle,use Bubbles")
                vida_shiny_horsea -= atk_squirte_cd1
                print("Vida da Shiny Horsea",vida_shiny_horsea)
                
                if vida_shiny_horsea <=0:
                    try:
                        print("Voce tem a chance de matar seu inimigo!!")
                        print("Antes que ele coloque outro poke!")
                        print()
                        print("Squirtle  use Bubbles!!")
                        player_inimigo -= atk_squirte_cd1
                        print("Vida do Seu inimigo",player_inimigo)
                        if player_inimigo <= 0:
                            print("Voce o Derrotou")
                            print("Vida do Inimigo",player_inimigo)
                            break
                    except:
                        print("Deseja matar outro inimigo?")
                print()
                print("Shiny Horsea,Contra-Ataca")
                vida_squirte -= atk_horsea_cd2
                print("Vida do seu Squirtle",vida_squirte)

                 #POTIONS MARKET

                if vida_squirte <=0:
                    print()
                    print("Seu Squirtle Morreu")
                    fly = input("Deseja comprar Potions: [S-sim/N-nao]: ")
                    if fly == "S" or fly == "sim":
                        from NPCS import NPC
                        vida_squirte += Porcao
                        print("Seu squirtle Foi curado ,Life Atual",vida_charmander)
                        
                        
                    else:
                        print("Voce esta Vulneravel aos ataques!!")
                        player_vida -= atk_horsea_cd2
                        print("OHH NAOOO!!")
                        print("Voce foi atacado sua é vida é de:",player_vida)
                        if player_vida <=0:
                            print("END OF GAME")
                            print()
                            print("VOCE PERDEU!!")
                            break
            
            elif res == 2:
                print("Squirtle,use Warteball")
                vida_shiny_horsea -= atk_squirte_cd2
                print("Vida da Shiny Horsea",vida_shiny_horsea)
                if vida_shiny_horsea <=0:
                    try:
                        print("Voce tem a chance de matar seu inimigo!!")
                        print("Antes que ele coloque outro poke!")
                        print()
                        print("Squirtle  use Warteball !!")
                        player_inimigo -= atk_squirte_cd2
                        print("Vida do Seu inimigo",player_inimigo)
                        if player_inimigo <= 0:
                            print("Voce o Derrotou")
                            print("Vida do Inimigo",player_inimigo)
                            break
                    except:
                        print("Deseja matar outro inimigo?")

                print()
                print("Shiny Horsea,Contra-Ataca")
                vida_squirte -= atk_horsea_cd2
                print("Vida do seu Squirtle",vida_squirte)

                #POTIONS MARKET

                if vida_squirte <=0:
                    print()
                    print("Seu Squirtle Morreu")
                    fly = input("Deseja comprar Potions: [S-sim/N-nao]: ")
                    if fly == "S" or fly == "sim":
                        from NPCS import NPC
                        vida_squirte += Porcao
                        print("Seu squirtle Foi curado ,Life Atual",vida_charmander)
                        
                        
                    else:
                        print("Voce esta Vulneravel aos ataques!!")
                        player_vida -= atk_horsea_cd2
                        print("OHH NAOOO!!")
                        print("Voce foi atacado sua é vida é de:",player_vida)
                        if player_vida <=0:
                            print("END OF GAME")
                            print()
                            print("VOCE PERDEU!!")
                            break
                    
                
            elif res == 3:
                print("Squirtle,use Bubbleam")
                vida_shiny_horsea -= atk_squirte_cd3
                print("Vida da Shiny Horsea",vida_shiny_horsea)
                if vida_shiny_horsea <=0:
                    try:
                        print("Voce tem a chance de matar seu inimigo!!")
                        print("Antes que ele coloque outro poke!")
                        print()
                        print("Squirtle  use Bubbleam !!")
                        player_inimigo -= atk_squirte_cd3
                        print("Vida do Seu inimigo",player_inimigo)
                        if player_inimigo <= 0:
                            print("Voce o Derrotou")
                            print("Vida do Inimigo",player_inimigo)
                            break
                    except:
                        print("Deseja matar outro inimigo?")

                print()
                print("Shiny Horsea,Contra-Ataca")
                vida_squirte -= atk_horsea_cd2
                print("Vida do seu Squirtle",vida_squirte)

                #POTIONS MARKET

                if vida_squirte <=0:
                    print()
                    print("Seu Squirtle Morreu")
                    fly = input("Deseja comprar Potions: [S-sim/N-nao]: ")
                    if fly == "S" or fly == "sim":
                        from NPCS import NPC
                        vida_squirte += Porcao
                        print("Seu squirtle Foi curado ,Life Atual",vida_charmander)
                        
                        
                    else:
                        print("Voce esta Vulneravel aos ataques!!")
                        player_vida -= atk_horsea_cd2
                        print("OHH NAOOO!!")
                        print("Voce foi atacado sua é vida é de:",player_vida)
                        if player_vida <=0:
                            print("END OF GAME")
                            print()
                            print("VOCE PERDEU!!")
                            break
                    
                
                
        if chart == 2 and chart1 == 3: # SQUIRTLE X GOLDEN
            print("---------------------")
            print("Squirtle,Eu escolho você")
            print()
            print("Digite (1)-para usar Bubles,(2)-para usar Warteball,(3)-para usar Blubleam")
            res = int(input("(1),(2),(3): "))
            if res == 1:
                print("Squirtle,use Bubbles")
                vida_golden -= atk_squirte_cd1
                print("Vida do Golden",vida_golden)
                if vida_golden <=0:
                    try:
                        print("Voce tem a chance de matar seu inimigo!!")
                        print("Antes que ele coloque outro poke!")
                        print()
                        print("Squirtle  use Bubbles !!")
                        player_inimigo -= atk_squirte_cd1
                        print("Vida do Seu inimigo",player_inimigo)
                        if player_inimigo <= 0:
                            print("Voce o Derrotou")
                            print("Vida do Inimigo",player_inimigo)
                            break
                    except:
                        print("Deseja matar outro inimigo?")
                print()
                print()
                print("Golden,Contra-Ataca")
                vida_squirte -= atk_golden_cd2
                print("Vida do seu Squirtle",vida_squirte)

                #POTIONS MARKET

                if vida_squirte <=0:
                    print()
                    print("Seu Squirtle Morreu")
                    fly = input("Deseja comprar Potions: [S-sim/N-nao]: ")
                    if fly == "S" or fly == "sim":
                        from NPCS import NPC
                        vida_squirte += Porcao
                        print("Seu squirtle Foi curado ,Life Atual",vida_charmander)
                        
                        
                    else:
                        print("Voce esta Vulneravel aos ataques!!")
                        player_vida -= atk_golden_cd2
                        print("OHH NAOOO!!")
                        print("Voce foi atacado sua é vida é de:",player_vida)
                        if player_vida <=0:
                            print("END OF GAME")
                            print()
                            print("VOCE PERDEU!!")
                            break
            
            elif res == 2:
                print("Squirtle,use Warteball")
                vida_golden -= atk_squirte_cd2
                print("Vida do Golden",vida_golden)
                if vida_golden <=0:
                    try:
                        print("Voce tem a chance de matar seu inimigo!!")
                        print("Antes que ele coloque outro poke!")
                        print()
                        print("Squirtle use Warteball")
                        player_inimigo -= atk_squirte_cd2
                        print("Vida do seu Inimigo",player_inimigo)
                        if player_inimigo <=0:
                            print("Voce o derrotou")
                            print("Vida do Inimigo",player_inimigo)
                            break
                    except:
                        print("Deseja matar outro inimigo?")
                print()
                print()
                print("Golden,Contra-Ataca")
                vida_squirte -= atk_golden_cd2
                print("Vida do seu Squirtle",vida_squirte)

                #POTIONS MARKET

                if vida_squirte <=0:
                    print()
                    print("Seu Squirtle Morreu")
                    fly = input("Deseja comprar Potions: [S-sim/N-nao]: ")
                    if fly == "S" or fly == "sim":
                        from NPCS import NPC
                        vida_squirte += Porcao
                        print("Seu squirtle Foi curado ,Life Atual",vida_charmander)
                        
                        
                    else:
                        print("Voce esta Vulneravel aos ataques!!")
                        player_vida -= atk_golden_cd2
                        print("OHH NAOOO!!")
                        print("Voce foi atacado sua é vida é de:",player_vida)
                        if player_vida <=0:
                            print("END OF GAME")
                            print()
                            print("VOCE PERDEU!!")
                            break
            
            elif res == 3:
                print("Squirtle,use Bubbleam")
                vida_golden -= atk_squirte_cd3
                print("Vida do Golden",vida_golden)
                if vida_golden <=0:
                    try:
                        print("Voce tem a chance de matar seu inimigo!!")
                        print("Antes que ele coloque outro poke!")
                        print()
                        print("Squirtle use Warteball")
                        player_inimigo -= atk_squirte_cd2
                        print("Vida do seu Inimigo",player_inimigo)
                        if player_inimigo <=0:
                            print("Voce o derrotou")
                            print("Vida do Inimigo",player_inimigo)
                            break
                    except:
                        print("Deseja matar outro inimigo?")
                print()
                print()
                print("Golden,Contra-Ataca")
                vida_squirte -= atk_golden_cd2
                print("Vida do seu Squirtle",vida_squirte)

                #POTIONS MARKET

                if vida_squirte <=0:
                    print()
                    print("Seu Squirtle Morreu")
                    fly = input("Deseja comprar Potions: [S-sim/N-nao]: ")
                    if fly == "S" or fly == "sim":
                        from NPCS import NPC
                        vida_squirte += Porcao
                        print("Seu squirtle Foi curado ,Life Atual",vida_charmander)
                        
                        
                    else:
                        print("Voce esta Vulneravel aos ataques!!")
                        player_vida -= atk_golden_cd2
                        print("OHH NAOOO!!")
                        print("Voce foi atacado sua é vida é de:",player_vida)
                        if player_vida <=0:
                            print("END OF GAME")
                            print()
                            print("VOCE PERDEU!!")
                            break

                    
        if chart == 2 and chart1 == 4: # SQUIRTLE X VULPIX
            print("---------------------")
            print("Squirtle,Eu escolho você")
            print()
            print("Digite (1)-para usar Bubles,(2)-para usar Warteball,(3)-para usar Blubleam")
            res = int(input("(1),(2),(3): "))
            if res == 1:
                print("Squirtle use Bubbles")
                vida_vulpix -= atk_squirte_cd1
                print("Vida do Vulpix",vida_vulpix)
                if vida_vulpix <=0:
                    try:
                        print("Voce tem a chance de matar seu inimigo!!")
                        print("Antes que ele coloque outro poke!")
                        print()
                        print("Squirtle use Bubbles")
                        player_inimigo -= atk_squirte_cd1
                        print("Vida do seu Inimigo",player_inimigo)
                        if player_inimigo <=0:
                            print("Voce o derrotou")
                            print("Vida do Inimigo",player_inimigo)
                            break
                    except:
                        print("Deseja matar outro inimigo?")
                print()
                print()
                print("Golden,Contra-Ataca")
                vida_squirte -= atk_vulpix_cd2
                print("Vida do seu Squirtle",vida_squirte)

                #POTIONS MARKET

                if vida_squirte <=0:
                    print()
                    print("Seu Squirtle Morreu")
                    fly = input("Deseja comprar Potions: [S-sim/N-nao]: ")
                    if fly == "S" or fly == "sim":
                        from NPCS import NPC
                        vida_squirte += Porcao
                        print("Seu squirtle Foi curado ,Life Atual",vida_charmander)
                        
                        
                    else:
                        print("Voce esta Vulneravel aos ataques!!")
                        player_vida -= atk_vulpix_cd2
                        print("OHH NAOOO!!")
                        print("Voce foi atacado sua é vida é de:",player_vida)
                        if player_vida <=0:
                            print("END OF GAME")
                            print()
                            print("VOCE PERDEU!!")
                            break
            
            elif res == 2:
                print("Squirtle use Warteball")
                vida_vulpix -= atk_squirte_cd2
                print("Vida do Vulpix",vida_vulpix)
                if vida_vulpix <=0:
                    try:
                        print("Voce tem a chance de matar seu inimigo!!")
                        print("Antes que ele coloque outro poke!")
                        print()
                        print("Squirtle use Warteball")
                        player_inimigo -= atk_squirte_cd2
                        print("Vida do seu Inimigo",player_inimigo)
                        if player_inimigo <=0:
                            print("Voce o derrotou")
                            print("Vida do Inimigo",player_inimigo)
                            break
                    except:
                        print("Deseja matar outro inimigo?")
                print()
                print()
                print("Golden,Contra-Ataca")
                vida_squirte -= atk_vulpix_cd2
                print("Vida do seu Squirtle",vida_squirte)

                 #POTIONS MARKET

                if vida_squirte <=0:
                    print()
                    print("Seu Squirtle Morreu")
                    fly = input("Deseja comprar Potions: [S-sim/N-nao]: ")
                    if fly == "S" or fly == "sim":
                        from NPCS import NPC
                        vida_squirte += Porcao
                        print("Seu squirtle Foi curado ,Life Atual",vida_charmander)
                        
                        
                    else:
                        print("Voce esta Vulneravel aos ataques!!")
                        player_vida -= atk_vulpix_cd2
                        print("OHH NAOOO!!")
                        print("Voce foi atacado sua é vida é de:",player_vida)
                        if player_vida <=0:
                            print("END OF GAME")
                            print()
                            print("VOCE PERDEU!!")
                            break
                    

            elif res == 3:
                print("Squirtle use Bubbleam")
                vida_vulpix -= atk_squirte_cd3
                print("Vida do Vulpix",vida_vulpix)
                if vida_vulpix <=0:
                    try:
                        print("Voce tem a chance de matar seu inimigo!!")
                        print("Antes que ele coloque outro poke!")
                        print()
                        print("Squirtle use Bubbleam")
                        player_inimigo -= atk_squirte_cd3
                        print("Vida do seu Inimigo",player_inimigo)
                        if player_inimigo <=0:
                            print("Voce o derrotou")
                            print("Vida do Inimigo",player_inimigo)
                            break
                    except:
                        print("Deseja matar outro inimigo?")
                print()
                print()
                print("Golden,Contra-Ataca")
                vida_squirte -= atk_vulpix_cd2
                print("Vida do seu Squirtle",vida_squirte)

                 #POTIONS MARKET

                if vida_squirte <=0:
                    print()
                    print("Seu Squirtle Morreu")
                    fly = input("Deseja comprar Potions: [S-sim/N-nao]: ")
                    if fly == "S" or fly == "sim":
                        from NPCS import NPC
                        vida_squirte += Porcao
                        print("Seu squirtle Foi curado ,Life Atual",vida_charmander)
                        
                        
                    else:
                        print("Voce esta Vulneravel aos ataques!!")
                        player_vida -= atk_vulpix_cd2
                        print("OHH NAOOO!!")
                        print("Voce foi atacado sua é vida é de:",player_vida)
                        if player_vida <=0:
                            print("END OF GAME")
                            print()
                            print("VOCE PERDEU!!")
                            break

                
        if chart == 2 and chart1 == 5: #SQUIRTLE X ODDISH
            print("---------------------")
            print("Squirtle,Eu escolho você")
            print()
            print("Digite (1)-para usar Bubles,(2)-para usar Warteball,(3)-para usar Blubleam")
            res = int(input("(1),(2),(3): "))
            if res == 1:
                print("Squirtle , use Bubbles")
                vida_oddish -= atk_squirte_cd1
                print("Vida do Oddish",vida_oddish)
                if vida_oddish <=0:
                    try:
                        print("Voce tem a chance de matar seu inimigo!!")
                        print("Antes que ele coloque outro poke!")
                        print()
                        print("Squirtle use Bubbles")
                        player_inimigo -= atk_squirte_cd1
                        print("Vida do seu Inimigo",player_inimigo)
                        if player_inimigo <=0:
                            print("Voce o derrotou")
                            print("Vida do Inimigo",player_inimigo)
                            break
                    except:
                        print("Deseja matar outro inimigo?")

                print()
                print("Oddish,Contra-Ataca")
                vida_squirte -= atk_oddish_cd2
                print("Vida do Squirtle",vida_squirte)

                 #POTIONS MARKET

                if vida_squirte <=0:
                    print()
                    print("Seu Squirtle Morreu")
                    fly = input("Deseja comprar Potions: [S-sim/N-nao]: ")
                    if fly == "S" or fly == "sim":
                        from NPCS import NPC
                        vida_squirte += Porcao
                        print("Seu squirtle Foi curado ,Life Atual",vida_charmander)
                        
                        
                    else:
                        print("Voce esta Vulneravel aos ataques!!")
                        player_vida -= atk_oddish_cd2
                        print("OHH NAOOO!!")
                        print("Voce foi atacado sua é vida é de:",player_vida)
                        if player_vida <=0:
                            print("END OF GAME")
                            print()
                            print("VOCE PERDEU!!")
                            break
        
            elif res == 2:
                print("Squirtle , use Warteball")
                vida_oddish -= atk_squirte_cd2
                print("Vida do Oddish",vida_oddish)
                if vida_oddish <=0:
                    try:
                        print("Voce tem a chance de matar seu inimigo!!")
                        print("Antes que ele coloque outro poke!")
                        print()
                        print("Squirtle use Warteball")
                        player_inimigo -= atk_squirte_cd2
                        print("Vida do seu Inimigo",player_inimigo)
                        if player_inimigo <=0:
                            print("Voce o derrotou")
                            print("Vida do Inimigo",player_inimigo)
                            break
                    except:
                        print("Deseja matar outro inimigo?")

                print()
                print("Oddish,Contra-Ataca")
                vida_squirte -= atk_oddish_cd2
                print("Vida do Squirtle",vida_squirte)

                 #POTIONS MARKET

                if vida_squirte <=0:
                    print()
                    print("Seu Squirtle Morreu")
                    fly = input("Deseja comprar Potions: [S-sim/N-nao]: ")
                    if fly == "S" or fly == "sim":
                        from NPCS import NPC
                        vida_squirte += Porcao
                        print("Seu squirtle Foi curado ,Life Atual",vida_charmander)
                        
                        
                    else:
                        print("Voce esta Vulneravel aos ataques!!")
                        player_vida -= atk_oddish_cd2
                        print("OHH NAOOO!!")
                        print("Voce foi atacado sua é vida é de:",player_vida)
                        if player_vida <=0:
                            print("END OF GAME")
                            print()
                            print("VOCE PERDEU!!")
                            break
                        
            elif res ==3:
                print("Squirtle , use Bubbleam")
                vida_oddish -= atk_squirte_cd1
                print("Vida do Oddish",vida_oddish)
                if vida_oddish <=0:
                    try:
                        print("Voce tem a chance de matar seu inimigo!!")
                        print("Antes que ele coloque outro poke!")
                        print()
                        print("Squirtle use Bubbleam")
                        player_inimigo -= atk_squirte_cd3
                        print("Vida do seu Inimigo",player_inimigo)
                        if player_inimigo <=0:
                            print("Voce o derrotou")
                            print("Vida do Inimigo",player_inimigo)
                            break
                    except:
                        print("Deseja matar outro inimigo?")

                print()
                print("Oddish,Contra-Ataca")
                vida_squirte -= atk_oddish_cd2
                print("Vida do Squirtle",vida_squirte)

                 #POTIONS MARKET

                if vida_squirte <=0:
                    print()
                    print("Seu Squirtle Morreu")
                    fly = input("Deseja comprar Potions: [S-sim/N-nao]: ")
                    if fly == "S" or fly == "sim":
                        from NPCS import NPC
                        vida_squirte += Porcao
                        print("Seu squirtle Foi curado ,Life Atual",vida_charmander)
                        
                        
                    else:
                        print("Voce esta Vulneravel aos ataques!!")
                        player_vida -= atk_oddish_cd2
                        print("OHH NAOOO!!")
                        print("Voce foi atacado sua é vida é de:",player_vida)
                        if player_vida <=0:
                            print("END OF GAME")
                            print()
                            print("VOCE PERDEU!!")
                            break
                        
        if chart == 2 and chart1 == 6: #SQUIRTLE X SHINY TENTACOOL
            print("---------------------")
            print("Squirtle,Eu escolho você")
            print()
            print("Digite (1)-para usar Bubles,(2)-para usar Warteball,(3)-para usar Blubleam")
            res = int(input("(1),(2),(3): "))
            if res == 1:
                print("Squirtle,use Bubbles")
                vida_shiny_tentacool -= atk_squirte_cd1
                print("Vida do Shiny Tentacool",vida_shiny_tentacool)
                if vida_shiny_tentacool <=0:
                    try:
                        print("Voce tem a chance de matar seu inimigo!!")
                        print("Antes que ele coloque outro poke!")
                        print()
                        print("Squirtle use Bubbles")
                        player_inimigo -= atk_squirte_cd1
                        print("Vida do seu Inimigo",player_inimigo)
                        if player_inimigo <=0:
                            print("Voce o derrotou")
                            print("Vida do Inimigo",player_inimigo)
                            break
                    except:
                        print("Deseja matar outro inimigo?")

                print()
                print("Shiny Tentacool,Contra-Ataca")
                vida_squirte -= atk_tentacool_cd2
                print("Vida do seu Squirtle",vida_squirte)

                 #POTIONS MARKET

                if vida_squirte <=0:
                    print()
                    print("Seu Squirtle Morreu")
                    fly = input("Deseja comprar Potions: [S-sim/N-nao]: ")
                    if fly == "S" or fly == "sim":
                        from NPCS import NPC
                        vida_squirte += Porcao
                        print("Seu squirtle Foi curado ,Life Atual",vida_charmander)
                        
                        
                    else:
                        print("Voce esta Vulneravel aos ataques!!")
                        player_vida -= atk_tentacool_cd2
                        print("OHH NAOOO!!")
                        print("Voce foi atacado sua é vida é de:",player_vida)
                        if player_vida <=0:
                            print("END OF GAME")
                            print()
                            print("VOCE PERDEU!!")
                            break
        
            elif res == 2:
                print("Squirte, use Warteball")
                vida_shiny_tentacool -= atk_squirte_cd2
                print("Vida do Shiny Tentacool",vida_shiny_tentacool)
                if vida_shiny_tentacool <=0:
                    try:
                        print("Voce tem a chance de matar seu inimigo!!")
                        print("Antes que ele coloque outro poke!")
                        print()
                        print("Squirtle use Warteball")
                        player_inimigo -= atk_squirte_cd2
                        print("Vida do seu Inimigo",player_inimigo)
                        if player_inimigo <=0:
                            print("Voce o derrotou")
                            print("Vida do Inimigo",player_inimigo)
                            break
                    except:
                        print("Deseja matar outro inimigo?")

                print()
                print("Shiny Tentacool,Contra-Ataca")
                vida_squirte -= atk_tentacool_cd2
                print("Vida do seu Squirtle",vida_squirte)

                #POTIONS MARKET

                if vida_squirte <=0:
                    print()
                    print("Seu Squirtle Morreu")
                    fly = input("Deseja comprar Potions: [S-sim/N-nao]: ")
                    if fly == "S" or fly == "sim":
                        from NPCS import NPC
                        vida_squirte += Porcao
                        print("Seu squirtle Foi curado ,Life Atual",vida_charmander)
                        
                        
                    else:
                        print("Voce esta Vulneravel aos ataques!!")
                        player_vida -= atk_tentacool_cd2
                        print("OHH NAOOO!!")
                        print("Voce foi atacado sua é vida é de:",player_vida)
                        if player_vida <=0:
                            print("END OF GAME")
                            print()
                            print("VOCE PERDEU!!")
                            break
                        
            elif res == 3:
                print("Squirtle,use Bubbleam")
                vida_shiny_tentacool -= atk_squirte_cd3
                print("Vida do Shiny Tentacool",vida_shiny_tentacool)
                if vida_shiny_tentacool <=0:
                    try:
                        print("Voce tem a chance de matar seu inimigo!!")
                        print("Antes que ele coloque outro poke!")
                        print()
                        print("Squirtle use Bubbleam")
                        player_inimigo -= atk_squirte_cd3
                        print("Vida do seu Inimigo",player_inimigo)
                        if player_inimigo <=0:
                            print("Voce o derrotou")
                            print("Vida do Inimigo",player_inimigo)
                            break
                    except:
                        print("Deseja matar outro inimigo?")

                print()
                print("Shiny Tentacool,Contra-Ataca")
                vida_squirte -= atk_tentacool_cd2
                print("Vida do seu Squirtle",vida_squirte)

                #POTIONS MARKET

                if vida_squirte <=0:
                    print()
                    print("Seu Squirtle Morreu")
                    fly = input("Deseja comprar Potions: [S-sim/N-nao]: ")
                    if fly == "S" or fly == "sim":
                        from NPCS import NPC
                        vida_squirte += Porcao
                        print("Seu squirtle Foi curado ,Life Atual",vida_charmander)
                        
                        
                    else:
                        print("Voce esta Vulneravel aos ataques!!")
                        player_vida -= atk_tentacool_cd2
                        print("OHH NAOOO!!")
                        print("Voce foi atacado sua é vida é de:",player_vida)
                        if player_vida <=0:
                            print("END OF GAME")
                            print()
                            print("VOCE PERDEU!!")
                            break
                
                        
                
         #Bulbasaur   
        if chart == 3 and chart1 == 1: #BUBALSAUR X GEODUDE
            print("---------------------")
            print("Bulbasaur,Eu escolho você")
            print()
            print("Digite (1)-para usar WineVip,(2)-para usar Razor Leaf,(3)-para usar Leaf Store")
            res = int(input("(1),(2),(3): "))
            if res == 1:
                print("Bulbasaur, use WineVip")
                vida_geodude -= atk_bulbarsaur_cd1
                print("Vida do Geodude",vida_geodude)
                if vida_geodude <= 0:
                    try:
                        print("Voce tem a chance de matar seu inimigo!!")
                        print("Antes que ele coloque outro poke!")
                        print()
                        print("Bulbasaur use Wine Vip")
                        player_inimigo -= atk_bulbarsaur_cd1
                        print("Vida do seu Inimigo",player_inimigo)
                        if player_inimigo <=0:
                            print("Voce o Derrotou")
                            print("Vida do Inimigo",player_inimigo)
                            break
                    except:
                        print("Deseja matar outro inimigo?")
                print()
                print("Geodude ,Contra-Ataca")
                vida_bulbarsaur -= atk_geodude_cd2
                print("Vida do seu Bulbarsaur",vida_bulbarsaur)

                #POTIONS MARKET

                if vida_bulbarsaur <=0:
                    print()
                    print("Seu Bulbasaur Morreu")
                    fly = input("Deseja comprar Potions: [S-sim/N-nao]: ")
                    if fly == "S" or fly == "sim":
                        from NPCS import NPC
                        vida_bulbarsaur += Porcao
                        print("Seu Bulbasaur Foi curado ,Life Atual",vida_bulbarsaur)
                        
                        
                    else:
                        print("Voce esta Vulneravel aos ataques!!")
                        player_vida -= atk_geodude_cd2
                        print("OHH NAOOO!!")
                        print("Voce foi atacado sua é vida é de:",player_vida)
                        if player_vida <=0:
                            print("END OF GAME")
                            print()
                            print("VOCE PERDEU!!")
                            break
                            
            elif res == 2:
                print("Bulbarsaur , use Razor Leaf")
                vida_geodude -= atk_bulbarsaur_cd2
                print("Vida do Geodude",vida_geodude)
                if vida_geodude <=0:
                    try:
                        print("Voce tem a chance de matar seu inimigo!!")
                        print("Antes que ele coloque outro poke!")
                        print()
                        print("Bulbasaur use Razor Leaf")
                        player_inimigo -= atk_bulbarsaur_cd2
                        print("Vida do seu Inimigo",player_inimigo)
                        if player_inimigo <=0:
                            print("Voce o Derrotou")
                            print("Vida do Inimigo",player_inimigo)
                            break
                    except:
                        print("Deseja matar outro inimigo?")
                print()
                print("Geodude ,Contra-Ataca")
                vida_bulbarsaur -= atk_geodude_cd2
                print("Vida do seu Bulbarsaur",vida_bulbarsaur)

                #POTIONS MARKET

                if vida_bulbarsaur<=0:
                    print()
                    print("Seu Bulbasaur Morreu")
                    fly = input("Deseja comprar Potions: [S-sim/N-nao]: ")
                    if fly == "S" or fly == "sim":
                        from NPCS import NPC
                        vida_bulbarsaur += Porcao
                        print("Seu Bulbasaur Foi curado ,Life Atual",vida_bulbarsaur)
                        
                        
                    else:
                        print("Voce esta Vulneravel aos ataques!!")
                        player_vida -= atk_geodude_cd2
                        print("OHH NAOOO!!")
                        print("Voce foi atacado sua é vida é de:",player_vida)
                        if player_vida <=0:
                            print("END OF GAME")
                            print()
                            print("VOCE PERDEU!!")
                            break

            elif res ==3:
                print("Bulbarsaur, use Leaf Store")
                vida_geodude -= atk_bulbarsaur_cd3
                print("Vida do Geodude",vida_geodude)
                if vida_geodude <=0:
                    try:
                        print("Voce tem a chance de matar seu inimigo!!")
                        print("Antes que ele coloque outro poke!")
                        print()
                        print("Bulbasaur use Leaf Store")
                        player_inimigo -= atk_bulbarsaur_cd3
                        print("Vida do seu Inimigo",player_inimigo)
                        if player_inimigo <=0:
                            print("Voce o Derrotou")
                            print("Vida do Inimigo",player_inimigo)
                            break
                    except:
                        print("Deseja matar outro inimigo?")
                print()
                print("Geodude ,Contra-Ataca")
                vida_bulbarsaur -= atk_geodude_cd2
                print("Vida do seu Bulbarsaur",vida_bulbarsaur)

                #POTIONS MARKET

                if vida_bulbarsaur<=0:
                    print()
                    print("Seu Bulbasaur Morreu")
                    fly = input("Deseja comprar Potions: [S-sim/N-nao]: ")
                    if fly == "S" or fly == "sim":
                        from NPCS import NPC
                        vida_bulbarsaur += Porcao
                        print("Seu Bulbasaur Foi curado ,Life Atual",vida_bulbarsaur)
                        
                        
                    else:
                        print("Voce esta Vulneravel aos ataques!!")
                        player_vida -= atk_geodude_cd2
                        print("OHH NAOOO!!")
                        print("Voce foi atacado sua é vida é de:",player_vida)
                        if player_vida <=0:
                            print("END OF GAME")
                            print()
                            print("VOCE PERDEU!!")
                            break
                        
                
        #Bulbarsaur                
        if chart == 3 and chart1 == 2: #BULBASAUR X SHINY HORSEA
            print("---------------------")
            print("Bulbasaur,Eu escolho você")
            print()
            print("Digite (1)-para usar WineVip,(2)-para usar Razor Leaf,(3)-para usar Leaf Store")
            res = int(input("(1),(2),(3): "))
            if res == 1:
                print("Bulbarsaur use WineVip")
                vida_shiny_horsea -= atk_bulbarsaur_cd1
                print("Vida da Shiny Horsea",vida_shiny_horsea)
                if vida_shiny_horsea <=0:
                    try:
                        print("Voce tem a chance de matar seu inimigo!!")
                        print("Antes que ele coloque outro poke!")
                        print()
                        print("Bulbasaur use WineVip")
                        player_inimigo -= atk_bulbarsaur_cd1
                        print("Vida do seu Inimigo",player_inimigo)
                        if player_inimigo <=0:
                            print("Voce o Derrotou")
                            print("Vida do Inimigo",player_inimigo)
                            break
                    except:
                        print("Deseja matar outro inimigo?")
                print()
                print("Shiny Horsea ,Contra-Ataca")
                vida_bulbarsaur -= atk_horsea_cd2
                print("Vida do seu Bulbarsaur",vida_bulbarsaur)

                #POTIONS MARKET

                if vida_bulbarsaur <=0:
                    print()
                    print("Seu Bulbasaur Morreu")
                    fly = input("Deseja comprar Potions: [S-sim/N-nao]: ")
                    if fly == "S" or fly == "sim":
                        from NPCS import NPC
                        vida_bulbarsaur += Porcao
                        print("Seu Bulbasaur Foi curado ,Life Atual",vida_bulbarsaur)
                        
                        
                    else:
                        print("Voce esta Vulneravel aos ataques!!")
                        player_vida -= atk_horsea_cd2
                        print("OHH NAOOO!!")
                        print("Voce foi atacado sua é vida é de:",player_vida)
                        if player_vida <=0:
                            print("END OF GAME")
                            print()
                            print("VOCE PERDEU!!")
                            break
                        
            elif res == 2:
                print("Bulbarsaur use RazorLeaf")
                vida_shiny_horsea -= atk_bulbarsaur_cd2
                print("Vida da Shiny Horsea",vida_shiny_horsea)
                if vida_shiny_horsea <=0:
                    try:
                        print("Voce tem a chance de matar seu inimigo!!")
                        print("Antes que ele coloque outro poke!")
                        print()
                        print("Bulbasaur use Razor Leaf")
                        player_inimigo -= atk_bulbarsaur_cd2
                        print("Vida do seu Inimigo",player_inimigo)
                        if player_inimigo <=0:
                            print("Voce o Derrotou")
                            print("Vida do Inimigo",player_inimigo)
                            break
                    except:
                        print("Deseja matar outro inimigo?")
                print()
                print("Shiny Horsea ,Contra-Ataca")
                vida_bulbarsaur -= atk_horsea_cd2
                print("Vida do seu Bulbarsaur",vida_bulbarsaur)

                 #POTIONS MARKET

                if vida_bulbarsaur <=0:
                    print()
                    print("Seu Bulbasaur Morreu")
                    fly = input("Deseja comprar Potions: [S-sim/N-nao]: ")
                    if fly == "S" or fly == "sim":
                        from NPCS import NPC
                        vida_bulbarsaur += Porcao
                        print("Seu Bulbasaur Foi curado ,Life Atual",vida_bulbarsaur)
                        
                        
                    else:
                        print("Voce esta Vulneravel aos ataques!!")
                        player_vida -= atk_horsea_cd2
                        print("OHH NAOOO!!")
                        print("Voce foi atacado sua é vida é de:",player_vida)
                        if player_vida <=0:
                            print("END OF GAME")
                            print()
                            print("VOCE PERDEU!!")
                            break
                        
            elif res == 3:
                print("Bulbarsaur use Leaf Store")
                vida_shiny_horsea -= atk_bulbarsaur_cd3
                print("Vida da Shiny Horsea",vida_shiny_horsea)
                if vida_shiny_horsea <=0:
                    try:
                        print("Voce tem a chance de matar seu inimigo!!")
                        print("Antes que ele coloque outro poke!")
                        print()
                        print("Bulbasaur use Leaf Store")
                        player_inimigo -= atk_bulbarsaur_cd3
                        print("Vida do seu Inimigo",player_inimigo)
                        if player_inimigo <=0:
                            print("Voce o Derrotou")
                            print("Vida do Inimigo",player_inimigo)
                            break
                    except:
                        print("Deseja matar outro inimigo?")
                print()
                print("Shiny Horsea ,Contra-Ataca")
                vida_bulbarsaur -= atk_horsea_cd2
                print("Vida do seu Bulbarsaur",vida_bulbarsaur)

                 #POTIONS MARKET

                if vida_bulbarsaur <=0:
                    print()
                    print("Seu Bulbasaur Morreu")
                    fly = input("Deseja comprar Potions: [S-sim/N-nao]: ")
                    if fly == "S" or fly == "sim":
                        from NPCS import NPC
                        vida_bulbarsaur += Porcao
                        print("Seu Bulbasaur Foi curado ,Life Atual",vida_bulbarsaur)
                        
                        
                    else:
                        print("Voce esta Vulneravel aos ataques!!")
                        player_vida -= atk_horsea_cd2
                        print("OHH NAOOO!!")
                        print("Voce foi atacado sua é vida é de:",player_vida)
                        if player_vida <=0:
                            print("END OF GAME")
                            print()
                            print("VOCE PERDEU!!")
                            break
                        
        #BULBASAUR
        if chart == 3 and chart1 == 3: #BULBASAUR X GOLDEN
            print("---------------------")
            print("Bulbasaur,Eu escolho você")
            print()
            print("Digite (1)-para usar WineVip,(2)-para usar Razor Leaf,(3)-para usar Leaf Store")
            res = int(input("(1),(2),(3): "))
            if res == 1:
                print("Bulbarsaur,Use WineVip")
                vida_golden -= atk_bulbarsaur_cd1
                print("Vida do Golden",vida_golden)
                if vida_golden <=0:
                    try:
                        print("Voce tem a chance de matar seu inimigo!!")
                        print("Antes que ele coloque outro poke!")
                        print()
                        print("Bulbarsaur use WineVip")
                        player_inimigo -= atk_bulbarsaur_cd1
                        print("Vida do Seu Inimigo",player_inimigo)
                        if player_inimigo <=0:
                            print("Voce o Derrotou")
                            print("Vida do Inimigo",player_inimigo)
                            break
                    except:
                        print("Deseja matar outro inimigo?")
                print()
                print("Golden,Contra-Ataca")
                vida_bulbarsaur -= atk_golden_cd2
                print("Vida do seu Bulbarsaur",vida_bulbarsaur)

                 #POTIONS MARKET

                if vida_bulbarsaur <=0:
                    print()
                    print("Seu Bulbasaur Morreu")
                    fly = input("Deseja comprar Potions: [S-sim/N-nao]: ")
                    if fly == "S" or fly == "sim":
                        from NPCS import NPC
                        vida_bulbarsaur += Porcao
                        print("Seu Bulbasaur Foi curado ,Life Atual",vida_bulbarsaur)
                        
                        
                    else:
                        print("Voce esta Vulneravel aos ataques!!")
                        player_vida -= atk_golden_cd2
                        print("OHH NAOOO!!")
                        print("Voce foi atacado sua é vida é de:",player_vida)
                        if player_vida <=0:
                            print("END OF GAME")
                            print()
                            print("VOCE PERDEU!!")
                            break

            elif res == 2:
                print("Bulbarsaur,Use Razor Leaf")
                vida_golden -= atk_bulbarsaur_cd2
                print("Vida do Golden",vida_golden)
                if vida_golden <=0:
                    try:
                        print("Voce tem a chance de matar seu inimigo!!")
                        print("Antes que ele coloque outro poke!")
                        print()
                        print("Bulbarsaur use Razor Leaf")
                        player_inimigo -= atk_bulbarsaur_cd2
                        print("Vida do Seu Inimigo",player_inimigo)
                        if player_inimigo <=0:
                            print("Voce o Derrotou")
                            print("Vida do Inimigo",player_inimigo)
                            break
                    except:
                        print("Deseja matar outro inimigo?")
                print()
                print("Golden,Contra-Ataca")
                vida_bulbarsaur -= atk_golden_cd2
                print("Vida do seu Bulbarsaur",vida_bulbarsaur)

                #POTIONS MARKET

                if vida_bulbarsaur <=0:
                    print()
                    print("Seu Bulbasaur Morreu")
                    fly = input("Deseja comprar Potions: [S-sim/N-nao]: ")
                    if fly == "S" or fly == "sim":
                        from NPCS import NPC
                        vida_bulbarsaur += Porcao
                        print("Seu Bulbasaur Foi curado ,Life Atual",vida_bulbarsaur)
                        
                        
                    else:
                        print("Voce esta Vulneravel aos ataques!!")
                        player_vida -= atk_golden_cd2
                        print("OHH NAOOO!!")
                        print("Voce foi atacado sua é vida é de:",player_vida)
                        if player_vida <=0:
                            print("END OF GAME")
                            print()
                            print("VOCE PERDEU!!")
                            break
                        
                
            elif res == 3:
                print("Bulbarsaur,Use Leaf Store")
                vida_golden -= atk_bulbarsaur_cd3
                print("Vida do Golden",vida_golden)
                if vida_golden <=0:
                    try:
                        print("Voce tem a chance de matar seu inimigo!!")
                        print("Antes que ele coloque outro poke!")
                        print()
                        print("Bulbarsaur use Leaf Store")
                        player_inimigo -= atk_bulbarsaur_cd3
                        print("Vida do Seu Inimigo",player_inimigo)
                        if player_inimigo <=0:
                            print("Voce o Derrotou")
                            print("Vida do Inimigo",player_inimigo)
                            break
                    except:
                        print("Deseja matar outro inimigo?")
                print()
                print("Golden,Contra-Ataca")
                vida_bulbarsaur -= atk_golden_cd2
                print("Vida do seu Bulbarsaur",vida_bulbarsaur)
                
                 #POTIONS MARKET

                if vida_squirtle <=0:
                    print()
                    print("Seu Bulbasaur Morreu")
                    fly = input("Deseja comprar Potions: [S-sim/N-nao]: ")
                    if fly == "S" or fly == "sim":
                        from NPCS import NPC
                        vida_bulbarsaur += Porcao
                        print("Seu Bulbasaur Foi curado ,Life Atual",vida_bulbarsaur)
                        
                        
                    else:
                        print("Voce esta Vulneravel aos ataques!!")
                        player_vida -= atk_golden_cd2
                        print("OHH NAOOO!!")
                        print("Voce foi atacado sua é vida é de:",player_vida)
                        if player_vida <=0:
                            print("END OF GAME")
                            print()
                            print("VOCE PERDEU!!")
                            break    

    
        #Bulbasaur
        if chart == 3 and chart1 == 4: #BULBASAUR X VULPIX
            print("---------------------")
            print("Bulbasaur,Eu escolho você")
            print()
            print("Digite (1)-para usar WineVip,(2)-para usar Razor Leaf,(3)-para usar Leaf Store")
            res = int(input("(1),(2),(3): "))
            if res == 1:
                print("Bulbarsaur, use WineVip")
                vida_vulpix -= atk_bulbarsaur_cd1
                print("Vida do Vulpix",vida_vulpix)
                if vida_vulpix <=0:
                    try:
                        print("Voce tem a chance de matar seu inimigo!!")
                        print("Antes que ele coloque outro poke ")
                        print()
                        print("Bulbasaur use WineVip")
                        player_inimigo -= atk_bulbarsaur_cd1
                        print("Vida do seu Inimigo",player_inimigo)
                        if player_inimigo <=0:
                            print("Voce o Derrotou")
                            print("Vida do Inimigo",player_inimigo)
                            break
                    except:
                        print("Deseja matar outro inimigo?")
                print()
                print("Vulpix,Contra-Ataca")
                vida_bulbarsaur -= atk_vulpix_cd2
                print("Vida do seu Bulbarsaur",vida_bulbarsaur)

                #POTIONS MARKET

                if vida_bulbarsaur <=0:
                    print()
                    print("Seu Bulbasaur Morreu")
                    fly = input("Deseja comprar Potions: [S-sim/N-nao]: ")
                    if fly == "S" or fly == "sim":
                        from NPCS import NPC
                        vida_bulbarsaur += Porcao
                        print("Seu Bulbasaur Foi curado ,Life Atual",vida_bulbarsaur)
                        
                        
                    else:
                        print("Voce esta Vulneravel aos ataques!!")
                        player_vida -= atk_vulpix_cd2
                        print("OHH NAOOO!!")
                        print("Voce foi atacado sua é vida é de:",player_vida)
                        if player_vida <=0:
                            print("END OF GAME")
                            print()
                            print("VOCE PERDEU!!")
                            break
                
            elif res == 2:
                print("Bulbarsaur, use Razor Leaf")
                vida_vulpix -= atk_bulbarsaur_cd2
                print("Vida do Vulpix",vida_vulpix)
                if vida_vulpix <=0:
                    try:
                        print("Voce tem a chance de matar seu inimigo!!")
                        print("Antes que ele coloque outro poke ")
                        print()
                        print("Bulbasaur use Razor Leaf")
                        player_inimigo -= atk_bulbarsaur_cd2
                        print("Vida do seu Inimigo",player_inimigo)
                        if player_inimigo <=0:
                            print("Voce o Derrotou")
                            print("Vida do Inimigo",player_inimigo)
                            break
                    except:
                        print("Deseja matar outro inimigo?")
                print()
                print("Vulpix,Contra-Ataca")
                vida_bulbarsaur -= atk_vulpix_cd2
                print("Vida do seu Bulbarsaur",vida_bulbarsaur)

                #POTIONS MARKET

                if vida_squirtle <=0:
                    print()
                    print("Seu Bulbasaur Morreu")
                    fly = input("Deseja comprar Potions: [S-sim/N-nao]: ")
                    if fly == "S" or fly == "sim":
                        from NPCS import NPC
                        vida_bulbarsaur += Porcao
                        print("Seu Bulbasaur Foi curado ,Life Atual",vida_bulbarsaur)
                        
                        
                    else:
                        print("Voce esta Vulneravel aos ataques!!")
                        player_vida -= atk_vulpix_cd2
                        print("OHH NAOOO!!")
                        print("Voce foi atacado sua é vida é de:",player_vida)
                        if player_vida <=0:
                            print("END OF GAME")
                            print()
                            print("VOCE PERDEU!!")
                            break
                
            elif res == 3:
                print("Bulbarsaur, use Leaf Store")
                vida_vulpix -= atk_bulbarsaur_cd3
                print("Vida do Vulpix",vida_vulpix)
                if vida_vulpix <=0:
                    try:
                        print("Voce tem a chance de matar seu inimigo!!")
                        print("Antes que ele coloque outro poke ")
                        print()
                        print("Bulbasaur use Leaf Store")
                        player_inimigo -= atk_bulbarsaur_cd3
                        print("Vida do seu Inimigo",player_inimigo)
                        if player_inimigo <=0:
                            print("Voce o Derrotou")
                            print("Vida do Inimigo",player_inimigo)
                            break
                    except:
                        print("Deseja matar outro inimigo?")
                print()
                print("Vulpix,Contra-Ataca")
                vida_bulbarsaur -= atk_vulpix_cd2
                print("Vida do seu Bulbarsaur",vida_bulbarsaur)

                #POTIONS MARKET

                if vida_bulbarsaur <=0:
                    print()
                    print("Seu Bulbasaur Morreu")
                    fly = input("Deseja comprar Potions: [S-sim/N-nao]: ")
                    if fly == "S" or fly == "sim":
                        from NPCS import NPC
                        vida_bulbarsaur += Porcao
                        print("Seu Bulbasaur Foi curado ,Life Atual",vida_bulbarsaur)
                        
                        
                    else:
                        print("Voce esta Vulneravel aos ataques!!")
                        player_vida -= atk_vulpix_cd2
                        print("OHH NAOOO!!")
                        print("Voce foi atacado sua é vida é de:",player_vida)
                        if player_vida <=0:
                            print("END OF GAME")
                            print()
                            print("VOCE PERDEU!!")
                            break

        #bulbasaur
        if chart == 3 and chart1 == 5: #BULBASAUR X ODDISH
            print("---------------------")
            print("Bulbasaur,Eu escolho você")
            print()
            print("Digite (1)-para usar WineVip,(2)-para usar Razor Leaf,(3)-para usar Leaf Store")
            res = int(input("(1),(2),(3): "))
            if res == 1:
                print("Bulbarsaur,use WineVip")
                vida_oddish -= atk_bulbarsaur_cd1
                print("Vida do Oddish",vida_oddish)
                if vida_oddish <=0:
                    try:
                        print("Voce tem a chance de matar seu inimigo!!")
                        print("Antes que ele coloque outro poke")
                        print()
                        print("Bulbasaur, use WineVip")
                        player_inimigo -= atk_bulbarsaur_cd1
                        print("Vida do Seu Inimigo",player_inimgo)
                        if player_inimigo <=0:
                            print("Voce o Derrotou")
                            print("Vida do Seu Inimigo",player_inimigo)
                            break
                    except:
                        print("Deseja matar outro Inimigo?")
                print()
                print("Oddish,Contra-Ataca")
                vida_bulbarsaur -= atk_oddish_cd2
                print("Vida do seu Bulbarsaur",vida_bulbarsaur)

                #POTIONS MARKET

                if vida_bulbarsaur <=0:
                    print()
                    print("Seu Bulbasaur Morreu")
                    fly = input("Deseja comprar Potions: [S-sim/N-nao]: ")
                    if fly == "S" or fly == "sim":
                        from NPCS import NPC
                        vida_bulbarsaur += Porcao
                        print("Seu Bulbasaur Foi curado ,Life Atual",vida_bulbarsaur)
                        
                        
                    else:
                        print("Voce esta Vulneravel aos ataques!!")
                        player_vida -= atk_oddish_cd2
                        print("OHH NAOOO!!")
                        print("Voce foi atacado sua é vida é de:",player_vida)
                        if player_vida <=0:
                            print("END OF GAME")
                            print()
                            print("VOCE PERDEU!!")
                            break
                    
            elif res == 2:
                print("Bulbarsaur,use Razor Leaf")
                vida_oddish -= atk_bulbarsaur_cd2
                print("Vida do Oddish",vida_oddish)
                if vida_oddish <=0:
                    try:
                        print("Voce tem a chance de matar seu inimigo!!")
                        print("Antes que ele coloque outro poke")
                        print()
                        print("Bulbasaur, use Razor Leaf")
                        player_inimigo -= atk_bulbarsaur_cd2
                        print("Vida do Seu Inimigo",player_inimgo)
                        if player_inimigo <=0:
                            print("Voce o Derrotou")
                            print("Vida do Seu Inimigo",player_inimigo)
                            break
                    except:
                        print("Deseja matar outro Inimigo?")
                print()
                print("Oddish,Contra-Ataca")
                vida_bulbarsaur -= atk_oddish_cd2
                print("Vida do seu Bulbarsaur",vida_bulbarsaur)

                #POTIONS MARKET

                if vida_bulbarsaur <=0:
                    print()
                    print("Seu Bulbasaur Morreu")
                    fly = input("Deseja comprar Potions: [S-sim/N-nao]: ")
                    if fly == "S" or fly == "sim":
                        from NPCS import NPC
                        vida_bulbarsaur += Porcao
                        print("Seu Bulbasaur Foi curado ,Life Atual",vida_bulbarsaur)
                        
                        
                    else:
                        print("Voce esta Vulneravel aos ataques!!")
                        player_vida -= atk_oddish_cd2
                        print("OHH NAOOO!!")
                        print("Voce foi atacado sua é vida é de:",player_vida)
                        if player_vida <=0:
                            print("END OF GAME")
                            print()
                            print("VOCE PERDEU!!")
                            break

            elif res == 3:
                print("Bulbarsaur,use Leaf Store")
                vida_oddish -= atk_bulbarsaur_cd3
                print("Vida do Oddish",vida_oddish)
                if vida_oddish <=0:
                    try:
                        print("Voce tem a chance de matar seu inimigo!!")
                        print("Antes que ele coloque outro poke")
                        print()
                        print("Bulbasaur, use Leaf Store")
                        player_inimigo -= atk_bulbarsaur_cd3
                        print("Vida do Seu Inimigo",player_inimgo)
                        if player_inimigo <=0:
                            print("Voce o Derrotou")
                            print("Vida do Seu Inimigo",player_inimigo)
                            break
                    except:
                        print("Deseja matar outro Inimigo?")
                print()
                print("Oddish,Contra-Ataca")
                vida_bulbarsaur -= atk_oddish_cd2
                print("Vida do seu Bulbarsaur",vida_bulbarsaur)

                #POTIONS MARKET

                if vida_bulbarsaur <=0:
                    print()
                    print("Seu Bulbasaur Morreu")
                    fly = input("Deseja comprar Potions: [S-sim/N-nao]: ")
                    if fly == "S" or fly == "sim":
                        from NPCS import NPC
                        vida_bulbarsaur += Porcao
                        print("Seu Bulbasaur Foi curado ,Life Atual",vida_bulbarsaur)
                        
                        
                    else:
                        print("Voce esta Vulneravel aos ataques!!")
                        player_vida -= atk_oddish_cd2
                        print("OHH NAOOO!!")
                        print("Voce foi atacado sua é vida é de:",player_vida)
                        if player_vida <=0:
                            print("END OF GAME")
                            print()
                            print("VOCE PERDEU!!")
                            break



        if chart == 3 and chart1 == 6: #BULBASAUR X SHINY TENTACOOL
            print("---------------------")
            print("Bulbasaur,Eu escolho você")
            print()
            print("Digite (1)-para usar WineVip,(2)-para usar Razor Leaf,(3)-para usar Leaf Store")
            res = int(input("(1),(2),(3): "))
            if res == 1:
                print("Bulbarsaur,use WineVip")
                vida_shiny_tentacool -= atk_bulbarsaur_cd1
                print("Vida do Shiny Tentacool",vida_shiny_tentacool)
                if vida_shiny_tentacool <=0:
                    try:
                        print("Voce tem a chance de matar seu inimigo!!")
                        print("Antes que ele coloque outro poke")
                        print()
                        print("Bulbasaur, use WineVip")
                        player_inimigo -= atk_bulbarsaur_cd1
                        print("Vida do Seu Inimigo",player_inimgo)
                        if player_inimigo <=0:
                            print("Voce o Derrotou")
                            print("Vida do Seu Inimigo",player_inimigo)
                            break
                    except:
                        print("Deseja matar outro Inimigo?")
                print()
                print("Shiny tentacool,Contra-Ataca")
                vida_bulbarsaur -= atk_tentacool_cd2
                print("Vida do seu Bulbarsaur",vida_bulbarsaur)

                #POTIONS MARKET

                if vida_bulbarsaur <=0:
                    print()
                    print("Seu Bulbasaur Morreu")
                    fly = input("Deseja comprar Potions: [S-sim/N-nao]: ")
                    if fly == "S" or fly == "sim":
                        from NPCS import NPC
                        vida_bulbarsaur += Porcao
                        print("Seu Bulbasaur Foi curado ,Life Atual",vida_bulbarsaur)
                        
                        
                    else:
                        print("Voce esta Vulneravel aos ataques!!")
                        player_vida -= atk_tentacool_cd2
                        print("OHH NAOOO!!")
                        print("Voce foi atacado sua é vida é de:",player_vida)
                        if player_vida <=0:
                            print("END OF GAME")
                            print()
                            print("VOCE PERDEU!!")
                            break
                    
            elif res == 2:
                print("Bulbarsaur,use Razor Leaf")
                vida_shiny_tentacool -= atk_bulbarsaur_cd2
                print("Vida do Shiny tentacool",vida_shiny_tentacool)
                if vida_shiny_tentacool <=0:
                    try:
                        print("Voce tem a chance de matar seu inimigo!!")
                        print("Antes que ele coloque outro poke")
                        print()
                        print("Bulbasaur, use Razor Leaf")
                        player_inimigo -= atk_bulbarsaur_cd2
                        print("Vida do Seu Inimigo",player_inimgo)
                        if player_inimigo <=0:
                            print("Voce o Derrotou")
                            print("Vida do Seu Inimigo",player_inimigo)
                            break
                    except:
                        print("Deseja matar outro Inimigo?")
                print()
                print("Shiny tentacool,Contra-Ataca")
                vida_bulbarsaur -= atk_tentacool_cd2
                print("Vida do seu Bulbarsaur",vida_bulbarsaur)

                 #POTIONS MARKET

                if vida_bulbarsaure <=0:
                    print()
                    print("Seu Bulbasaur Morreu")
                    fly = input("Deseja comprar Potions: [S-sim/N-nao]: ")
                    if fly == "S" or fly == "sim":
                        from NPCS import NPC
                        vida_bulbarsaur += Porcao
                        print("Seu Bulbasaur Foi curado ,Life Atual",vida_bulbarsaur)
                        
                        
                    else:
                        print("Voce esta Vulneravel aos ataques!!")
                        player_vida -= atk_tentacool_cd2
                        print("OHH NAOOO!!")
                        print("Voce foi atacado sua é vida é de:",player_vida)
                        if player_vida <=0:
                            print("END OF GAME")
                            print()
                            print("VOCE PERDEU!!")
                            break

            elif res == 3:
                print("Bulbarsaur,use Leaf Store")
                vida_shiny_tentacool -= atk_bulbarsaur_cd3
                print("Vida do Shiny tentacool",vida_shiny_tentacool)
                if vida_oddish <=0:
                    try:
                        print("Voce tem a chance de matar seu inimigo!!")
                        print("Antes que ele coloque outro poke")
                        print()
                        print("Bulbasaur, use Leaf Store")
                        player_inimigo -= atk_bulbarsaur_cd3
                        print("Vida do Seu Inimigo",player_inimgo)
                        if player_inimigo <=0:
                            print("Voce o Derrotou")
                            print("Vida do Seu Inimigo",player_inimigo)
                            break
                    except:
                        print("Deseja matar outro Inimigo?")
                print()
                print("Shiny Tentacool,Contra-Ataca")
                vida_bulbarsaur -= atk_tentacool_cd2
                print("Vida do seu Bulbarsaur",vida_bulbarsaur)

                 #POTIONS MARKET

                if vida_bulbarsaur <=0:
                    print()
                    print("Seu Bulbasaur Morreu")
                    fly = input("Deseja comprar Potions: [S-sim/N-nao]: ")
                    if fly == "S" or fly == "sim":
                        from NPCS import NPC
                        vida_bulbarsaur += Porcao
                        print("Seu Bulbasaur Foi curado ,Life Atual",vida_bulbarsaur)
                        
                        
                    else:
                        print("Voce esta Vulneravel aos ataques!!")
                        player_vida -= atk_tentacool_cd2
                        print("OHH NAOOO!!")
                        print("Voce foi atacado sua é vida é de:",player_vida)
                        if player_vida <=0:
                            print("END OF GAME")
                            print()
                            print("VOCE PERDEU!!")
                            break
                
                
            
                
                
            
                            
                    

            
                
                    
                    
            
                
                    
                
            
            
                     
def main():
    jogo() 
    
    
            
      
 
            
        
main()

