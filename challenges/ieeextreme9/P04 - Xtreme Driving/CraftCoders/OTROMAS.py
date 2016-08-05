#!/bin/python
# -*- coding: utf-8 -*-


def main():
    carretera = []
    cadena = input().split(" ")
    largo = int(cadena[0])
    vacas = int(cadena[1])
    i =0
    var_x = []
    var_y = []

    if not 2<= largo:
        print(0)
        return

    if not largo<=1e18:
        print(0)
        return

    if not 0<=vacas:
        print(0)
        return

    if not vacas<=100:
        print(0)
        return

    if not vacas<=4*(largo-2):
        print(0)
        return

    i = 0



    pos = []
    while(i<vacas):
        cadena = input().split(" ")
        var_x.append(int(cadena[0]))
        var_y.append(int(cadena[1]))
        i+=1
        pos.append(int(cadena[1]))


    for posiciones in pos:
        if pos.count(posiciones)==4:
            print(0)
            return

    while i<4:
        carretera.append([0]*largo)
        i+=1


    i=0
    for a,b in zip(var_x,var_y):
        i+=1
        carretera[a-1][b-1]=99

    carretera[0][0]=1

    i = 0
    k = 0

    while i<largo-1:
        if carretera[0][i+1]==99:
            carretera[0][i+1]=0
        else:
            carretera[0][i+1]=carretera[0][i]+carretera[1][i]

        if carretera[1][i+1]==99:
            carretera[1][i+1]=0
        else:
            carretera[1][i+1]=carretera[0][i]+carretera[1][i]+carretera[2][i]

        if carretera[2][i+1]==99:
            carretera[2][i+1]=0
        else:
            carretera[2][i+1]=carretera[1][i]+carretera[2][i]+carretera[3][i]

        if carretera[3][i+1]==99:
            carretera[3][i+1]=0
        else:
            carretera[3][i+1]=carretera[3][i]+carretera[2][i]
        i+=1

    print(int(carretera[0][largo-1]%(1e9+7)))


if __name__ == '__main__':
    main()