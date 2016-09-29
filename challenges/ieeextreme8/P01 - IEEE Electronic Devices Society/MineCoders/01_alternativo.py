# -*- coding: utf-8 -*-

first_line = raw_input().split()

N = int(first_line[0]) #Longitud secuencia
M = int(first_line[1]) #Longitud subsecuencia
K = int(first_line[2])

n = raw_input().split() #secuencia

menor = 2147483647 #mayor numero posible

for i in range(N):
    num = int(n[i])
    if num < menor:
        menor = num

print menor
