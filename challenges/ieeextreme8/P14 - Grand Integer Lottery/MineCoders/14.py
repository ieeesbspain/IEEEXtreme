# -*- coding: utf-8 -*-

def generate_number(inner, size):
    holgura = size-len(str(inner))
    
    if holgura == 0:
        yield inner
    else:
        for i in range(holgura):
            for k in range(0,10**i):
                for l in range(0,10**(holgura-i)):
                    yield k + inner*10**(size-holgura) + l
    


first_line = raw_input().split()

S = int(first_line[0])
E = int(first_line[1])
P = int(first_line[2])
N = int(first_line[3])

nN_str = []

for n in range(N):
    nN_str.append(raw_input())

#Ahora toca comprobar si los nN están contenidos en los numeros del intervalo [S,E]

for n_str in nN_str:
    n_str
    
