"""
Pokemons Inimigos;
"""
#Neste modulo ficará os pokemons inimigos
#com seus respectivos lifes e atks
"""
Pokemons Inimigos serão:
1- Geodude 1600HP, cd1 == Rock Smash == 400 atk cd2 == Rock Slide == 600 atk cd3== EarthPower== 900
2- Shiny Horsea 1200HP, cd1 == Bubles == 400 atk cd2 == Warteball == 600 atk cd3== HydroPump== 1000
3- Golden 900HP, cd1 == Aquatail == 400 atk cd2 == Bubbleam == 600 atk cd3== Horn Attack== 700
4- Vulpix 1000HP , cd1 == ember == 400 atk cd2 == flametower== 600 atk cd3==fireblast == 800
5- Oddish  700HP, cd1 == Acid == 300 atk cd2 == Absorb == 500 atk cd3==Poison gás == 600
6- Shiny tentacool 1000HP , cd1 == Warteball == 400 atk cd2 == Aquatail== 500 atk cd3==HydroPump == 1000
"""
import random
import time
#

def main():
    player_inimigo()
    Pokemons_inimigo()
    geodude()
    shinyhorsea()
    golden()
    vulpix()
    oddish()
    shinytentacool()


def player_inimigo():
    global player_inimigo
    chart1 = 0
    print("Olá eu sou seu rival , Scottie..!")
    time.sleep(1)
    print("Estou aqui para te derrotar!!")
    #preciso criar um vetor para armezar o inimigo aleatorio
    #preciso chamar esse inimigo para essa funcao
    player_inimigo = 1000
    return player_inimigo
    

def Pokemons_inimigo():
    global chart1
    global poke
    poke = []
    poke_inimigo = random.randint(1,6)
    poke.append(poke_inimigo)
    #print(poke)
def geodude():
    global chart1
    global vida_geodude
    global atk_geodude_cd1
    global atk_geodude_cd2
    #Geodude
    if poke[0] == 1:
        print("O inimigo Escolhe Geodude!!!")
        chart1 = 1
        vida_geodude = 1600
        atk_geodude_cd1 = random.randint(380,400)
        atk_geodude_cd2 = random.randint(580,600)
        atk_geodude_cd3 = random.randint(880,900)
        return chart1,vida_geodude,atk_geodude_cd1,atk_geodude_cd2
    
def shinyhorsea():
    global chart1
    global vida_shiny_horsea
    global atk_horsea_cd1
    global atk_horsea_cd2
    
    #Shiny Horsea
    if poke[0] == 2:
        print("O inimigo Escolhe Shiny Horsea!!")
        chart1 = 2
        vida_shiny_horsea = 1200
        atk_horsea_cd1 = random.randint(380,400)
        atk_horsea_cd2 = random.randint(580,600)
        atk_horsea_cd3 = random.randint(990,1000)
        return chart1,vida_shiny_horsea,atk_horsea_cd1,atk_horsea_cd2

def golden():
    global chart1
    global vida_golden
    global atk_golden_cd1
    global atk_golden_cd2
    #Golden
    if poke[0] == 3:
        print("O inimigo Escolhe Golden!!")
        chart1 = 3
        vida_golden = 900
        atk_golden_cd1 = random.randint(380,400)
        atk_golden_cd2 = random.randint(580,600)
        atk_golden_cd3 = random.randint(680,700)
        return chart1,vida_golden,atk_golden_cd1,atk_golden_cd2

def vulpix():
    global chart1
    global vida_vulpix
    global atk_vulpix_cd1
    global atk_vulpix_cd2
    #Vulpix
    if poke[0] == 4:
        print("O inimigo Escolhe Vulpix!!")
        chart1 = 4
        vida_vulpix = 1000
        atk_vulpix_cd1 = random.randint(380,400)
        atk_vulpix_cd2 = random.randint(580,600)
        atk_vulpix_cd3 = random.randint(780,800)
        return chart1,vida_vulpix,atk_vulpix_cd1,atk_vulpix_cd2 

def oddish():
    global chart1
    global vida_oddish
    global atk_oddish_cd1
    global atk_oddish_cd2
    #Oddish
    if poke[0] == 5:
        print("O inimigo escolhe Oddish!!")
        chart1 = 5
        vida_oddish = 700
        atk_oddish_cd1 = random.randint(280,300)
        atk_oddish_cd2 = random.randint(480,500)
        atk_oddish_cd3 = random.randint(580,600)
        return chart1,vida_oddish,atk_oddish_cd1,atk_oddish_cd2

def shinytentacool():
    global chart1
    global vida_shiny_tentacool
    global atk_tentacool_cd1
    global atk_tentacool_cd2
    #Shiny Tentacool
    if poke[0] == 6:
        print("O inimigo escolhe Shiny Tentacol!!")
        chart1 = 6
        vida_shiny_tentacool = 1000
        atk_tentacool_cd1 = random.randint(380,400)
        atk_tentacool_cd2 = random.randint(480,500)
        atk_tentacool_cd3 = random.randint(980,1000)
        return chart1,vida_shiny_tentacool,atk_tentacool_cd1,atk_tentacool_cd2
    




main()
    

