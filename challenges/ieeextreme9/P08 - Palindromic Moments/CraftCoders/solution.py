#!/bin/python
# -*- coding: utf-8 -*-


def calculo(cadena):
    if len(cadena)==int(cadena):
        print(int(cadena))
        return

    result = 0
    iter = 0

    while result != len(cadena):
        result = len(cadena)
        cadena = str(result)
        iter+=1
    iter+=1
    print(iter)



def main():
    cadena = input()

    while cadena != "END":
        calculo(cadena)
        cadena = input()



if __name__ == '__main__':
    main()
