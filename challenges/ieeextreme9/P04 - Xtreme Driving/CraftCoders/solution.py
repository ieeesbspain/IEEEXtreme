#!/bin/python
# -*- coding: utf-8 -*-

import itertools

aux = ["_"]*5
carretera = []

def pintarMatriz(carretera):
    for x in carretera:
        for y in x:
            print("_"+y+"_|",end="")
        print()



def main():


    for x in range(0,4):
        carretera.append(aux[:])


    carretera[0][0]="X"
    carretera[0][4]="X"

    carretera[0][3]="V"
    carretera[1][3]="V"
    carretera[1][2]="V"
    carretera[0][3]="V"


    pos = {"x":0, "y":0}


    for y in range(0,len(carretera[0])-1):
        print(str(pos["x"])+" , "+str(pos["y"]))
        if carretera[pos["x"]][pos["y"]]=="X" and pos["y"]!=0 and pos["x"]!=0:
            print("OOOOOOOOOOOOOOOOOOK")
            return
        elif pos["x"]>0 and carretera[pos["x"]-1][pos["y"]+1]!="V": #Izquierda
            pos["x"]-=1
        elif carretera[pos["x"]][pos["y"]+1]!="V": #Adelante
            pass
        elif pos["x"]<3 and carretera[pos["x"]+1][pos["y"]+1]!="V": #Derecha
            pos["x"]+=1
        pos["y"]+=1
        carretera[pos["x"]][pos["y"]]="H"



    pintarMatriz(carretera)

    ''''
    aux = [" "]*5
    carretera = []

    for x in range(4):
        carretera.append(aux)


    pos = {}
    pos["x"] = 0
    pos["y"] = 0

    posiciones = []
    posiciones.append(pos)


    for x in range(len(carretera)-1):
        for y in range(len(carretera[0])-1):
            if carretera[pos["x"]][pos["y"]]=="X" and pos["y"]!=0:
                print("Encontrado")
                return
            elif pos["x"]>0 and carretera[pos["x"]-1][pos["y"]+1]!="V":
                pos["x"]-=1
            elif carretera[pos["x"]][pos["y"]+1]!="V":
                pass
            else:
                pos["x"]+=1
            pos["y"]+=1
            print(pos)
            posiciones.append(pos)
        print(posiciones)
'''

if __name__ == '__main__':
    main()
