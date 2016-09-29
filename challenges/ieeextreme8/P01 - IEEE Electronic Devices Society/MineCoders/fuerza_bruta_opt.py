# -*- coding: utf-8 -*-
import random

#first_line = raw_input().split()
#N = int(first_line[0]) # Longitud secuencia
#M = int(first_line[1]) # Longitud subsecuencia
#K = int(first_line[2])
N = 100000
M = 2
K = 2
n = []
for i in range(N):
    n.append(random.randint(0, 2147483647))

# Lee la secuencia
#n = [ int(e) for e in raw_input().split() ]


menor = 2147483647 # Mayor número posible

for i in range(N):
    start = i
    end   = i + M        
    conjunto = n[start:end]
    if end > N:
        conjunto = conjunto + n[0 : end - N]  
    
    menor_local = sorted(conjunto)[K - 1]
    if menor_local < menor:
        menor = menor_local
    
print menor