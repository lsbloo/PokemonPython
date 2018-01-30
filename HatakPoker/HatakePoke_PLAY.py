"""
Modulo Main do jogo
"""
#AQUI ESTARA TODAS IMPORTACOES E PRE-REQUISITOS PARA O JOGO RODAR
#Usarei o modulo sys para , importar os diretorios e arquivos necessarios
#acredito que terei que usar classes , para meus programas
#mas estao em FUNCAO, por enquanto [e[e[e[e[
import time
import sys
sys.path.append("HatakPoker")
print("----------------------------------")
print("BEM VINDO AO HATAKPOKE")
print("----------------------------------")
print("+----\\-----------\\\------+")
time.sleep(1)
print("Bem vindo, novo Jogador porfavor digite seu nome")
#PROBLEMAAAAAAA PARA REINICIAR O JOGO.!
from Player import *
from poke_inimigos import *
from Luta import *
print()
from BOSS import *
from MEGAS import *
from Shinys_Player import *

def Boss_jogo():
    global chart
    global player_vida
    global vida_mega_charizard,atk_mega_charizard_cd1,atk_mega_charizard_cd2,atk_mega_charizard_cd3
    global vida_mega_blastoise,atk_mega_blastoise_cd1,atk_mega_blastoise_cd2,atk_mega_blastoise_cd3
    global vida_mega_venusaur,atk_mega_venusaur_cd1,atk_mega_venusaur_cd2,atk_mega_venusaur_cd3
    global last
    last=False
    boss = True
    if player_inimigo <=0:
        print("Voce Podera matar os boss !!!!!!!!!".upper())
        again = input("Digite [S-sim/N-nao] para Continuar: ")
        if again == "S" or again == "sim":
            print("Proxima Rodada!!")
            #PRECISO COLOCAR AGORA O COMBATE ENTRE OS POKERS DO PLAYER E OS BOSS!
            if chart == 1:
                print("Charmander, Voce tem a chance de Mega Evoluir..!!")
                print("Mega Charizard!!!")
                print()
            if chart == 2:
                print("Squirtle, Voce tem a chance de  Mega Evoluir..!!")
                print("Mega Blastoise!!!")
            if chart == 3:
                print("Bulbarsaur,Voce tem a chance de Mega Evoluir..!!")
                print("Mega Venusaur!!!") 
            while boss == True:
                if chart == 1: #MEGA CHARIZARD
                    print("Digite (1)-para usar ember,(2)-para usar flametower,(3)-para usar fireblast")
                    res = int(input("(1),(2),(3): "))
                    if res == 1:
                        print("MEGA CHARIZARD , USE EMBER!!!")
                        #Combate!
                        #A IMPPLEMENTACAO DOS BOSS ESTAO FUNCIONANDO PERFEITAMENTE, AGORA FALTA AJEITAR TODOS OS COMBATES ENTRE ELES
                        #OS MEGAS POKERS TBM ESTAO SENDO FORMADOS APOS ISTO FALTA BALANCEAR O COMBATE
                        # E COLOCAR POTIONS PARA OS MEGAS ..
                        # ENTRE OUTRAS COISAS...
                        mew.life -= atk_mega_charizard_cd1
                        print("Mewtwo,Recebe Dano , Life Atual:",mew.life)
                        if mew.life <= 0:
                            print("Mewtwo,Morreu!")
                            print()
                            print()
                            print()
                            print("THIS DEAD IS BENNING OF THE END!")
                            print()
                            print()
                            print()
                            last = True
                            break
                        

                        print()
                        print("Mewtwo,Contra-Ataca!")
                        vida_mega_charizard -= mew.atkcd
                        print("MEGA CHARIZARD , SOFRE DANO!!..Life atual..!",vida_mega_charizard)
                        if vida_mega_charizard <=0:
                            print("MEGA CHARIZARD MORREU!!")
                            print("Voce esta Vulneravel aos ataques do Mewtwo!!")
                            player_vida -= mew.atkcd
                            print("OHH NAAAAO")
                            print("Voce foi atacado sua vida é de:",player_vida)
                            if player_vida <=0:
                                print("END OF GAME")
                                print()
                                print("Voce perdeu!!")
                                break
                                
                        
                    elif res == 2:
                        print("MEGA CHARIZARD , USE FLAMETOWER!!!")
                        mew.life -= atk_mega_charizard_cd2
                        print("Mewtwo,Recebe Dano , Life Atual:",mew.life)
                        if mew.life <= 0:
                            print("Mewtwo,Morreu!")
                            print()
                            print()
                            print()
                            print("THIS DEAD IS BENNING OF THE END!")
                            print()
                            print()
                            print()
                            last = True
                            
                            
                            break

                        print()
                        print("Mewtwo,Contra-Ataca!")
                        vida_mega_charizard -= mew.atkcd
                        print("MEGA CHARIZARD , SOFRE DANO!!..Life atual..!",vida_mega_charizard)
                        if vida_mega_charizard <=0:
                            print("MEGA CHARIZARD MORREU!!")
                            print("Voce esta Vulneravel aos ataques do Mewtwo!!")
                            player_vida -= mew.atkcd
                            print("OHH NAAAAO")
                            print("Voce foi atacado sua vida é de:",player_vida)
                            if player_vida <=0:
                                print("END OF GAME")
                                print()
                                print("Voce perdeu!!")
                                break


                    elif res == 3:
                        print("MEGA CHARIZARD , USE FIREBLAST!!!")
                        mew.life -= atk_mega_charizard_cd3
                        print("Mewtwo,Recebe Dano , Life Atual:",mew.life)
                        if mew.life <= 0:
                            print("Mewtwo,Morreu!")
                            print()
                            print()
                            print()
                            print("THIS DEAD IS BENNING OF THE END!")
                            print()
                            print()
                            print()
                            last = True
                            
                            break

                        print()
                        print("Mewtwo,Contra-Ataca!")
                        vida_mega_charizard -= mew.atkcd
                        print("MEGA CHARIZARD , SOFRE DANO!!..Life atual..!",vida_mega_charizard)
                        if vida_mega_charizard <=0:
                            print("MEGA CHARIZARD MORREU!!")
                            print("Voce esta Vulneravel aos ataques do Mewtwo!!")
                            player_vida -= mew.atkcd
                            print("OHH NAAAAO")
                            print("Voce foi atacado sua vida é de:",player_vida)
                            if player_vida <=0:
                                print("END OF GAME")
                                print()
                                print("Voce perdeu!!")
                                break
                        

               
                if chart == 2: #MEGA BLASTOISE
                    print("Digite (1)-para usar Bubles,(2)-para usar Warteball,(3)-para usar Blubleam")
                    res = int(input("(1),(2),(3): "))
                    if res == 1:
                        print("MEGA BLASTOISE , USE BUBBLES!!!")
                        mew.life -= atk_mega_blastoise_cd1
                        print("Mewtwo,Recebe Dano , Life Atual:",mew.life)
                        if mew.life <= 0:
                            print("Mewtwo,Morreu!")
                            print()
                            print()
                            print()
                            print("THIS DEAD IS BENNING OF THE END!")
                            print()
                            print()
                            print()
                            last = True
                           
                            
                            break

                        print()
                        print("Mewtwo,Contra-Ataca!")
                        vida_mega_blastoise -= mew.atkcd
                        print("MEGA BLASTOISE , SOFRE DANO!!..Life atual..!",vida_mega_blastoise)
                        if vida_mega_blastoise <=0:
                            print("MEGA BLASTOISE MORREU!!")
                            print("Voce esta Vulneravel aos ataques do Mewtwo!!")
                            player_vida -= mew.atkcd
                            print("OHH NAAAAO")
                            print("Voce foi atacado sua vida é de:",player_vida)
                            if player_vida <=0:
                                print("END OF GAME")
                                print()
                                print("Voce perdeu!!")
                                break
                            
                    elif res == 2:
                        print("MEGA BLASTOISE , USE WATERBALL !!!")
                        mew.life -= atk_mega_blastoise_cd2
                        print("Mewtwo,Recebe Dano , Life Atual:",mew.life)
                        if mew.life <= 0:
                            print("Mewtwo,Morreu!")
                            print()
                            print()
                            print()
                            print("THIS DEAD IS BENNING OF THE END!")
                            print()
                            print()
                            print()
                            last = True
                            
                            break

                        print()
                        print("Mewtwo,Contra-Ataca!")
                        vida_mega_blastoise -= mew.atkcd
                        print("MEGA BLASTOISE , SOFRE DANO!!..Life atual..!",vida_mega_blastoise)
                        if vida_mega_blastoise <=0:
                            print("MEGA BLASTOISE MORREU!!")
                            print("Voce esta Vulneravel aos ataques do Mewtwo!!")
                            player_vida -= mew.atkcd
                            print("OHH NAAAAO")
                            print("Voce foi atacado sua vida é de:",player_vida)
                            if player_vida <=0:
                                print("END OF GAME")
                                print()
                                print("Voce perdeu!!")
                                break
                            
                    elif res == 3:
                        print("MEGA BLASTOISE , USE BUBBLEAM !!!")
                        mew.life -= atk_mega_blastoise_cd3
                        print("Mewtwo,Recebe Dano , Life Atual:",mew.life)
                        if mew.life <= 0:
                            print("Mewtwo,Morreu!")
                            print()
                            print()
                            print()
                            print("THIS DEAD IS BENNING OF THE END!")
                            print()
                            print()
                            print()
                            last = True
                            
                            break

                        print()
                        print("Mewtwo,Contra-Ataca!")
                        vida_mega_blastoise -= mew.atkcd
                        print("MEGA BLASTOISE , SOFRE DANO!!..Life atual..!",vida_mega_blastoise)
                        if vida_mega_blastoise <=0:
                            print("MEGA BLASTOISE MORREU!!")
                            print("Voce esta Vulneravel aos ataques do Mewtwo!!")
                            player_vida -= mew.atkcd
                            print("OHH NAAAAO")
                            print("Voce foi atacado sua vida é de:",player_vida)
                            if player_vida <=0:
                                print("END OF GAME")
                                print()
                                print("Voce perdeu!!")
                                break
                        



                if chart == 3:
                    #
                    print("Digite (1)-para usar WineVip,(2)-para usar Razor Leaf,(3)-para usar Leaf Store")
                    res = int(input("(1),(2),(3): "))
                    if res == 1:
                        print("MEGA VENUSAUR , USE WINEVIP!!!")
                        mew.life -= atk_mega_venusaur_cd1
                        print("Mewtwo,Recebe Dano , Life Atual:",mew.life)
                        if mew.life <= 0:
                            print("Mewtwo,Morreu!")
                            print()
                            print()
                            print()
                            print("THIS DEAD IS BENNING OF THE END!")
                            print()
                            print()
                            print()
                            last = True
                            
                            break

                        print()
                        print("Mewtwo,Contra-Ataca!")
                        vida_mega_venusaur -= mew.atkcd
                        print("MEGA VENUSAUR , SOFRE DANO!!..Life atual..!",vida_mega_venusaur)
                        if vida_mega_venusaur <=0:
                            print("MEGA VENUSAUR MORREU!!")
                            print("Voce esta Vulneravel aos ataques do Mewtwo!!")
                            player_vida -= mew.atkcd
                            print("OHH NAAAAO")
                            print("Voce foi atacado sua vida é de:",player_vida)
                            if player_vida <=0:
                                print("END OF GAME")
                                print()
                                print("Voce perdeu!!")
                                break
                    elif res == 2:
                        print("MEGA VENUSAUR , USE RAZOR LEAF!!!")
                        mew.life -= atk_mega_venusaur_cd2
                        print("Mewtwo,Recebe Dano , Life Atual:",mew.life)
                        if mew.life <= 0:
                            print("Mewtwo,Morreu!")
                            print()
                            print()
                            print()
                            print("THIS DEAD IS BENNING OF THE END!")
                            print()
                            print()
                            print()
                            last = True
                            
                            break

                        print()
                        print("Mewtwo,Contra-Ataca!")
                        vida_mega_venusaur -= mew.atkcd
                        print("MEGA VENUSAUR , SOFRE DANO!!..Life atual..!",vida_mega_venusaur)
                        if vida_mega_venusaur <=0:
                            print("MEGA VENUSAUR MORREU!!")
                            print("Voce esta Vulneravel aos ataques do Mewtwo!!")
                            player_vida -= mew.atkcd
                            print("OHH NAAAAO")
                            print("Voce foi atacado sua vida é de:",player_vida)
                            if player_vida <=0:
                                print("END OF GAME")
                                print()
                                print("Voce perdeu!!")
                                break
                    elif res == 3:
                        print("MEGA VENUSAUR , USE LEAF STORE!!!")
                        mew.life -= atk_mega_venusaur_cd3
                        print("Mewtwo,Recebe Dano , Life Atual:",mew.life)
                        if mew.life <= 0:
                            print("Mewtwo,Morreu!")
                            print()
                            print()
                            print()
                            print("THIS DEAD IS BENNING OF THE END!")
                            print()
                            print()
                            print()
                            last = True
                            
                            break

                        print()
                        print("Mewtwo,Contra-Ataca!")
                        vida_mega_venusaur -= mew.atkcd
                        print("MEGA VENUSAUR , SOFRE DANO!!..Life atual..!",vida_mega_venusaur)
                        if vida_mega_venusaur <=0:
                            print("MEGA VENUSAUR MORREU!!")
                            print("Voce esta Vulneravel aos ataques do Mewtwo!!")
                            player_vida -= mew.atkcd
                            print("OHH NAAAAO")
                            print("Voce foi atacado sua vida é de:",player_vida)
                            if player_vida <=0:
                                print("END OF GAME")
                                print()
                                print("Voce perdeu!!")
                                break
                        
                    
                        
        else:
            print("Fim De Jogo!!")


def main():
    Boss_jogo()


main()



    


