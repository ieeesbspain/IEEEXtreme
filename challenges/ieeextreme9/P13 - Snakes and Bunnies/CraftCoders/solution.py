#!/bin/python
# -*- coding: utf-8 -*-


def main():
    filas = int(input())

    tablero = []
    i = 0

    serpientes = {}
    conejos = {}

    while i<filas:
        if i%2==1:
            tablero.append(reversed(input()))
        else:
            tablero.append(input())
        i+=1
    tablero = reversed(tablero)
    i = 0

    for f in tablero:
        for c in f:
            if c.isalpha():
                if not c in serpientes.keys():
                    ser = {"cola": i}
                    serpientes[c]=ser
                else:
                    serpientes[c]["cabeza"]=i
            elif c.isdigit():
                if not c in conejos.keys():
                    con = {"cola": i}
                    conejos[c] = con
                else:
                    conejos[c]["cabeza"]=i
            i+=1


    n_jugadores = int(input())

    i=0

    jugadores = [0]*n_jugadores

    celdas = (filas)**2

    print("SERPIENTES===============")
    print(serpientes)
    print("CONEJOS!")
    print(conejos)

    while True:
        print("ITERACION     ================== "+str(i))
        print(jugadores)
        if jugadores[i]>=celdas:
            print(jugadores)
            return

        #primer dado
        dado = int(input())
        jugadores[i]+=dado

        if jugadores[i]>=celdas:
            print(jugadores)
            return

        dado2 = int(input())
        jugadores[i]+=dado2

        if jugadores[i]>=celdas:
            print(jugadores)
            return

        if dado==dado2:
            dadoN = int(input())
            print(str(jugadores[i])+" i "+str(i))
            jugadores[i]+=dadoN
            print("========================")
            print(dadoN)
            print(jugadores[i])
            print("========================")

            if jugadores[i]>=celdas:
                print(jugadores)
                return


        while jugadores.count(jugadores[i])>1:
            jugadores[i]+=1


        for s in serpientes:
            if serpientes[s]["cabeza"]==jugadores[i]:
                jugadores[i]=serpientes[s]["cola"]

        for c in conejos:
            if conejos[c]["cola"]==jugadores[i]:
                jugadores[i]=conejos[c]["cabeza"]


        i+=1
        i%=n_jugadores

'''
        #recojo dados
        dado1 = input()
        dado2 = input()

        if not dado1.isdigit():
            print(jugadores.sort())
            return
        elif not dado2.isdigit():
            jugadores[i] += int(dado1)
            print(jugadores.sort())
            return
        else:
            jugadores[i] += int(dado1)+int(dado2)

        #si dados dobles
        if dado1==dado2:
            dado1 = int(input())
            jugadores[i] += dado1

        #si se pusa con otro jugador
        while jugadores.count(jugadores[i])>1:
            jugadores[i]+=1


        for s in serpientes:
            if serpientes[s]["cabeza"]==jugadores[i]:
                jugadores[i]=serpientes[s]["cola"]


        for c in conejos:
            if conejos[c]["cola"]==jugadores[i]:
                jugadores[i]=conejos[c]["cabeza"]


        #si se pusa con otro jugador
        while jugadores.count(jugadores[i])>1:
            jugadores[i]+=1

        #siguiente jugador
        i+=1
        i%=n_jugadores

        if jugadores[i]==celdas:
            print(jugadores.sort())
            return
'''

if __name__ == '__main__':
    main()
