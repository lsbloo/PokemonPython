"""

"""

#MEGAS POKEMONS

############################# MEGAS POKEMONS ##############################
import time
import random
#
#

def mega_charizard():
    #Mega Charizard
    global vida_mega_charizard
    global atk_mega_charizard_cd1,atk_mega_charizard_cd2,atk_mega_charizard_cd3
    vida_mega_charizard = 4000
    atk_mega_charizard_cd1 = random.randint(550,600)
    atk_mega_charizard_cd2 = random.randint(800,850)
    atk_mega_charizard_cd3 = random.randint(900,970)

def mega_blastoise():
    #Mega Blastoise
    global vida_mega_blastoise
    global atk_mega_blastoise_cd1,atk_mega_blastoise_cd2,atk_mega_blastoise_cd3
    vida_mega_blastoise = 4000
    atk_mega_blastoise_cd1 = random.randint(600,650)
    atk_mega_blastoise_cd2 = random.randint(800,880)
    atk_mega_blastoise_cd3 = random.randint(900,980)

def mega_venusaur():
    #Mega Venusaur
    global vida_mega_venusaur
    global atk_mega_venusaur_cd1,atk_mega_venusaur_cd2,atk_mega_venusaur_cd3
    vida_mega_venusaur = 4000
    atk_mega_venusaur_cd1 = random.randint(600,680)
    atk_mega_venusaur_cd2 = random.randint(800,880)
    atk_mega_venusaur_cd3 = random.randint(900,980)
    
###############################################################################


def main():
    mega_charizard()
    mega_blastoise()
    mega_venusaur()


main()
