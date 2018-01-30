"""
Modulo do Player

"""
#Neste modulo estara contido as informacoes do player
#como vida , pokemons , nome , level , dinheiro
#a principio a conter o nome do player
#a sua vida inicial ,
# seu diinheiro inicial,
#level 5
#pokemons , padrao!
"""
Os pokers Iniciais , serao
Charmander,Squirtle,Bulbarsaur,Gloom,Golbat,Graveler
Charmander == 1000HP , cd1 == ember == 300 atk cd2 == flametower== 500 atk cd3==fireblast == 700
Squirtle == 900HP ,cd1 == bubbles == 300 atk cd2 == Waterball = 500 atk cd3 == Blubleam == 700 atk
Bulbasaur = 1200HP,cd1 == Wine Vip == 300 atk cd2 == Razor Leaf = 500 atk cd3 == Leaf Store == 700 atk
Gloom == 960 HP , cd1 == Poison Job == 350 atk cd2 == Acid = 500 atk cd3 == Poison GÁS == 700 atk
Golbat == 1000HP, cd1 == Bite == 350 atk cd2 == Wirldthril = 500 atk cd3 == Wing Attack == 700 atk
Graveler == 2000HP ,cd1 == Rock Trown == 350 atk cd2 == Rock Slide = 500 atk cd3 == EARTHPOWER == 700 atk
"""
import time
import random
level = 5
dinheiro = 0

def player():
    nome = input("Digite seu nome: ")
    global player_vida
    player_vida = 500
    print("Olá %s Bem vindo ao Pokemon!!"%nome)
    print("Nesse jogo voce terá seis pokemons iniciais", end = " ")
    print("Para upar voce , terá que matar os pokemons inimigos..")
    print("")
    print("Boa sorte!")
    time.sleep(2)
    print("Olá %s meu nome é Professor Oak e tenho alguns Pokemons para você.... !!!"%nome)
    time.sleep(1)
    print("Voce Recebeu...")
    print("Charmander,Squirtle,Bulbasaur..!!")
    time.sleep(1)
    print("Sua equipe de pokemons está formada")
    return player_vida


def charmander():
    global vida_charmander
    global atk_charmander_cd1,atk_charmander_cd2,atk_charmander_cd3
    
    #CHARMANDER
    vida_charmander = 1000
    atk_charmander_cd1 = random.randint(280,300)
    atk_charmander_cd2 = random.randint(480,500)
    atk_charmander_cd3 = random.randint(680,700)
    return vida_charmander,atk_charmander_cd1,atk_charmander_cd2,atk_charmander_cd3
    
        
def squirtle():
    #Squirte
    global vida_squirte
    global atk_squirte_cd1,atk_squirte_cd2,atk_squirte_cd3
    vida_squirte = 1700
    atk_squirte_cd1 = random.randint(280,300)
    atk_squirte_cd2 = random.randint(480,500)
    atk_squirte_cd3 = random.randint(680,700)
    return vida_squirte,atk_squirte_cd1,atk_squirte_cd2,atk_squirte_cd3
       
        
def bulbarsaur():
    #Bulbarsaur
    global vida_bulbarsaur
    global atk_bulbarsaur_cd1,atk_bulbarsaur_cd2,atk_bulbarsaur_cd3
    vida_bulbarsaur = 1200
    atk_bulbarsaur_cd1 = random.randint(280,300)
    atk_bulbarsaur_cd2 = random.randint(480,500)
    atk_bulbarsaur_cd3 = random.randint(680,700)
    return vida_bulbarsaur,atk_bulbarsaur_cd1,atk_bulbarsaur_cd2,atk_bulbarsaur_cd3
        
       
def gloom():
    #Gloom
    vida_gloom = 960
    atk_gloom_cd1 = random.randint(330,350)
    atk_gloom_cd2 = random.randint(480,500)
    atk_gloom_cd3 = random.randint(680,700)
        
       
def golbat():
    #Golbat
    vida_golbat = 1000
    atk_golbat_cd1 = random.randint(330,350)
    atk_golbat_cd2 = random.randint(480,500)
    atk_golbat_cd3 = random.randint(680,700)
        
        
def graveler():
    #Graveler
    vida_graveler = 2000
    atk_graveler_cd1 = random.randint(330,350)
    atk_graveler_cd2 = random.randint(480,500)
    atk_graveler_cd3 = random.randint(680,700)
        
        


def escolhe():
    global chart
    print("----------------------------------")
    print("Qual Pokemon Inicial voce deseja escolher: ")
    res = int(input("Digite os numeros (1)-Charmander,(2)-Squirte,(3)-Bulbasaur: "))
    if res == 1:
        chart = 1
        print("Voce escolheu, Charmander!!")
        #Informacoes sobre o pokemon
        time.sleep(1)
        print()
        print("O pokemon Charmander, é um pokemon do tipo Fogo , seu poder de atk é surpreendente!!")
        print()
        #charmander()
        return chart
    if res == 2:
        chart = 2
        print("Voce escolheu , Squirtle!!")
        #Informacoes sobre o pokemon
        time.sleep(1)
        print()
        print("O pokemon Squirtle , é um pokemon do tipo Água , seu poder de atk é surpreendente!!")
        print()
        #squirte()
        return chart
    if res == 3:
        chart = 3
        print("Voce escolheu , Bulbasaur!!")
        #Informacoes sobre o pokemon
        time.sleep(1)
        print()
        print("O Pokemon Bulbasaur, é um pokemon do tipo Planta , seu poder de atk é surpreendente!!")
        print()
        #bulbarsaur()
        return chart
    """
    if res == 4:
        chart =4
        print("Voce escolheu,Gloom!!")
        #Informacoes sobre o pokemon
        time.sleep(1)
        print()
        print("O pokemon Gloom, é um pokemon do Tipo Planta/Veneno, seu poder de atk é surpreendente!!")
        print()
        #()
        return chart
    if res == 5:
        chart = 5
        print("Voce escolheu,Golbat!!")
        #Informacoes sobre o pokemon
        time.sleep(1)
        print()
        print("O pokemon Golbat, é um pokemon do tipo Voador/Veneno, seu poder de atk é surpreendente!!")
        print()
        #golbat()
        return chart
    if res == 6:
        chart = 6
        print("Voce escolheu,Graveler!!")
        #Informacoes sobre o pokemon
        time.sleep(1)
        print()
        print("O pokemon Graveler, é um pokemon do tipo Pedra, seu poder de atk é surpreendente!!")
        print()
        #graveler()
        return chart
   """ 

def main():
    player()
    #Pokemons_Player()
    charmander()
    squirtle()
    bulbarsaur()
    gloom()
    golbat()
    graveler()
    escolhe()
    





    
    
main()
