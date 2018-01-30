


#  Shiny Lucario,Shiny Magmar,Shiny Mr.Mime
# Modulo para pokemons Shinys..

"""
Modulo para pokemons shinys, somente o player podera usar.
"""
import random
import time


def Magmar():
    # SHINY MAgmar
    global vida_magmar
    global atk1_magmar , atk2_magmar

    vida_magmar = 4000
    atk1_magmar = random.randint(800,100)
    atk2_magmar = random.randint(1200,1400)

def Lucario():
    # SHINY LUcario
    global vida_lucario
    global atk1_lucario,atk2_lucario

    vida_lucario = 4500
    atk1_lucario = random.randint(1000,1300)
    atk2_lucario = random.randint(1300,1500)

def MrMime():
    # SHINY MR.MIME
    global vida_mime
    global atk1_mime,atk2_mime

    vida_mime =  3500
    atk1_mime = random.randint(1100,1350)
    atk2_mime = random.randint(1400,1600)
    


def main():
    #
    #
    Magmar()
    Lucario()
    MrMime()
