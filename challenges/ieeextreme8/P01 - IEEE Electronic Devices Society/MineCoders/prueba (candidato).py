# -*- coding: utf-8 -*-

first_line = raw_input().split()

N = int(first_line[0]) #Longitud secuencia

M = int(first_line[1]) #Longitud subsecuencia

K = int(first_line[2])


n_str = raw_input().split() #secuencia
n=[]

for s in n_str: 
    n.append(int(s))

menor = 2147483647 #mayor numero posible

n_prima=n[:] #una copia del vector para ir rotando el vector
n_sub=[] #el vector de subsecuencias
for i in range(N):
    n_sub=n_prima[0:M] #Coge la primera subsecuencia
    n_sub=sorted(n_sub)#ordenado de menor a mayor
#    print n_sub[K-1]
    if int(n_sub[K-1]) <= menor:
        menor = int(n_sub[K-1])
    #Ahora roto el vector
    n_prima.append(n_prima[0]) #Se añade el ultimo numero al final
    n_prima=n_prima[1:len(n)+1] #Se coge desde la posicion 1 hasta el final +1, para que asi este rotado
    
print menor
    
