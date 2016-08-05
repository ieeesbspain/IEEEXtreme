#!/bin/python
# -*- coding: utf-8 -*-



def main():
    entrada = input().split(" ")
    K = int(entrada[0])
    N = int(entrada[1])


    #Comprobaciones base
    if not 2<=K:
        print(0)
        return

    if not K<=1e18:
        print(0)
        return

    if not 0<=N:
        print(0)
        return

    if not N<=100:
        print(0)
        return

    if not N<=4*(K-2):
        print(0)
        return


    i = 0

    var_x = []
    var_y = []

    #Vamos a recoger a las vacas
    while(i<N):
        cadena = input().split(" ")
        var_x.append(int(cadena[0]))
        var_y.append(int(cadena[1]))
        i+=1

    #Busco que no se repita la posición de la Y 4 veces, que sería bloquear el paso
    for y in var_y:
        if var_y.count(y)==4:
            print(0)
            return



    #Creo la matriz que representa la carretera
    carretera = []

    i = 0
    aux = [0]*K
    while i<4:
        carretera.append(aux[:])
        i+=1

    #Rellenamos las vacas
    for a,b in zip(var_x,var_y):
        i+=1
        carretera[a-1][b-1]=99

    #Posición inicial
    carretera[0][0]=1

    i = 0
    #Vamos a calcular las posibilidades
    while i<(K-1) and K>1:
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


    print(int(carretera[0][K-1]%(1e9+7)))


if __name__ == '__main__':
    main()