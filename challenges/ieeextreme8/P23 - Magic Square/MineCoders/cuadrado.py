# -*- coding: utf-8 -*-
"""
Created on Sat Oct 18 21:08:50 2014

@author: nitehack
"""
N=int(raw_input())
a=[]
for i in range(N):    
    datos=raw_input()
    cuadrado_linea=datos.split()
    a.append([ int(c) for c in cuadrado_linea])
    
tam_error=0
error=[]
 


#K es el valor que de la diagonal principal q se tiene que recibir
k=0

#Comprobacion
#Diagonal
for i in range(N):
    k=k+a[i][i]

#Filas

for i in range(N):    
    temp=sum(a[i])
    if temp!=k :
        error.append(i+1)

        
#Columnas

for j in range(N):
    temp2=0
    for i in range(N):
        temp2=a[i][j]+temp2
    if temp2!=k:
        error.append(-(j+1))
    
        

#diagonal inversa
temp3=0
for i in range(N-1,-1,-1):
    temp3=temp3+a[N-i-1][i]
    
if temp3!=k:
    error.append(0)
      
#En caso de que no haya errores
if len(error)==0:
    error.append(0)
    print error[0]
else:
    tam_error=len(error)
    error=sorted(error)
    print tam_error
    for i in range(tam_error):    
        print error[i]

