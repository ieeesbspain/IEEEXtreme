#!/bin/python
# -*- coding: utf-8 -*-


def extraerPatron(cadena):
    n = 1
    i = 0
    encontrado = False
    while not encontrado:
        division =[cadena[i:i+n] for i in range(0, len(cadena), n)]
        patron = division[0]

        encontrado = True
        for elemento in division:
            if patron!=elemento and len(elemento)==len(patron):
                encontrado = False
                n+=1
                break
            elif len(elemento)<len(patron):
                for e,p in zip(elemento, patron):
                    if e!=p:
                        encontrado = False
                        n+=1
                        break

    return patron


def main():
    test = int(input())
    i = 0
    while i<test:
        i+=1
        cadena = input()
        print(len(extraerPatron(cadena)))



if __name__ == '__main__':
    main()
