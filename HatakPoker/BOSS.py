"""
BOSS'S
"""
#Modulo que vai conter os boss!
#Demorar para mexer aq
#ATE PQ EU NAO SEI PROGRAMACAO ORIENTADA OBJETO TOMA NO CU1 ?|
import random
import time

def modularizar_BOSS():
    #Funcao Responsavel pelas classes de Boss.
    #Inicia e reinicia as classes.
    """
    Sao chamados no modulo htk_play.
    com chart1 e 2
    """
    return 0
    
class Pokemon_Boss(object):
    def __init__(self):
        self.pokemon = 'BOSS'
        self.boss = True
class Mewtwo(Pokemon_Boss):
    def __init__(self):
        self.life = 3500
        self.atkcd = random.randint(700,900)
        self.atkcd2= random.randint(1000,1100)
        self.say = 'Eu Sou Mewtwo,Estou aqui para te derrotar.!'
    def show(self,mew):
        print(self.say)
class Rayquaza(Pokemon_Boss):
    def __init__(self):
        self.life = 3000
        self.atkcd = random.randint(600,700)
        self.atkcd2= random.randint(800,1000)
        self.say = 'Eu sou Rayquaza,Estou aqui para te derrotar.!'
    def show(self,rayquaza):
        print(self.say)


class Groudon(Pokemon_Boss):
    def __init__(self):
        self.life = 2700
        self.atkcd = random.randint(650,750)
        self.atkcd2= random.randint(800,950)
        self.say = 'Eu sou Groudon,Estou aqui para te derrotar.!'
    def show(self,groudon):
        print(self.say)




def main():
    modularizar_BOSS
mew = Mewtwo()
mew.show(mew)
#rayquaza = Rayquaza()
#rayquaza.show(rayquaza)
#groudon = Groudon()
#groudon.show(groudon)
