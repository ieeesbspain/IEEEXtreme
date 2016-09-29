# -*- coding: utf-8 -*-

first_line = raw_input().split()

N = int(first_line[0]) #Longitud secuencia
M = int(first_line[1]) #Longitud subsecuencia
K = int(first_line[2])


n_str = raw_input().split() #secuencia

n=[]

for s in n_str: 
    n.append(int(s))

s = sorted(n)
e_anterior = -1
idx = 0
for e in s:
    if e_anterior != e:
        idx+=1
    e_anterior = e
    
    if idx == K:
        print e
        break