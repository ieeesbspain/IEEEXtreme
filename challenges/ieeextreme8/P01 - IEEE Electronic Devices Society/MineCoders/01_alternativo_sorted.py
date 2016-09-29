# -*- coding: utf-8 -*-

import random

first_line = raw_input().split()

N = int(first_line[0]) #Longitud secuencia
N = 10000
M = int(first_line[1]) #Longitud subsecuencia
M = 1241
K = int(first_line[2])
K = 121

n_str = raw_input().split() #secuencia
n_str = []

for i in range(N):
    n_str.append(str(random.randint(1,10)))
    
#print n_str

#print "generado"

#menor = 2147483647 #mayor numero posible

n=[]

for s in n_str: 
    n.append(int(s))

s = sorted(n)[K-1]
print s


#e_anterior = -1
#idx = 0
#print s
#for e in s:
#    if e_anterior != e:
#        #print idx
#        idx+=1
#    e_anterior = e
#    
#    if idx == K:
#        print e
#        break
#    
menor = 2147483647 #mayor numero posible

n_prima=n[:] #una copia del vector para ir rotando el vector
n_sub=[] #el vector de subsecuencias
for i in range(N):
    n_sub=n_prima[0:M] #Coge la primera subsecuencia
    n_sub=sorted(n_sub)#ordenado de menor a mayor
    if int(n_sub[K-1]) <= menor:
        menor = int(n_sub[K-1])
        
    #Ahora roto el vector
    n_prima.append(n_prima[0]) #Se añade el ultimo numero al final
    n_prima=n_prima[1:len(n)+1] #Se coge desde la posicion 1 hasta el final +1, para que asi este rotado

print menor