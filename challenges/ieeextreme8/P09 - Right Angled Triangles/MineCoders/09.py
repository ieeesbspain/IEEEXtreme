# -*- coding: utf-8 -*-

def is_integer_triangle(legs):
    
    def isqrt(n):
        '''newton's method'''
        x = n
        y = (x + 1) // 2
        while y < x:
            x = y
            y = (x + n // x) // 2
        return x
    
    a0s = range(1, legs[0]-1)
    p0s = []
    for a in a0s:
        b_candidato = isqrt(legs[0]**2-a**2)
        
        if b_candidato**2 == legs[0]**2-a**2: #cuadrado perfecto
            p0s.append((a,b_candidato))
    
    
    a1s = range(1, legs[1]-1)

    p1s = []
    for a in a1s:
        b_candidato = isqrt(legs[1]**2-a**2)
        
        if b_candidato**2 == legs[1]**2-a**2: #cuadrado perfecto
            p1s.append((-a,b_candidato)) #cambiar signo para el prod. escalar 
    
    #De todas las parejas (a,b), solo aquellas cuyo producto escalar es 0 son coordenadas válidas
    
    for p0 in p0s:
        for p1 in p1s:
            if p0[0]*p1[0]*p0[1]*p1[1] == 0:
                #Si alguna coordenada es 0, el triangulo esta vertical y no vale
                return "FALSE"
            if p0[0]*p1[0] + p0[1]*p1[1] == 0 or p0[1]*p1[0] + p0[0]*p1[1] == 0:
                return "TRUE"
    
    return "FALSE"


n_casos = int(raw_input())
entradas = []
for i in range(n_casos):
    entradas.append(tuple(raw_input().split()))

for i in range(len(entradas)):
    print is_integer_triangle((int(entradas[i][0]), int(entradas[i][1])))

#print is_integer_triangle((1, 1))
