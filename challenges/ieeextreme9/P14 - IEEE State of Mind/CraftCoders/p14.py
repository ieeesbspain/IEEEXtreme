# -*- coding: utf-8 -*-
"""
Created on Sat Oct 24 13:50:25 2015

@author: nitehack
"""

letras=["A", "B", "C", "D", "E", "F", "G", "H", "I", "J" ]
#Recogida de datos
#-------------------
NM=input()
NM=NM.split()
n_estados=int(NM[0])
variables=int(NM[1])
estados=[]

for n in range(n_estados): #Recorro lineas
    linea=input()
    linea=linea.split()
    salida_s=int(linea[0])
    ntrans=int(linea[1])
    transiciones=[]
    
    estado_completo=[]

    for p in range(ntrans): #Recorro dentro de la linea
        conjunto=[]
        entradas=[-1]*variables
        transicion=linea[p+2]
        indice_letra=0
        salir=False
        while not salir: #Cuidao hasta donde se lee lo mismo hay que calcularlo antes
            name=transicion[indice_letra]
            entrada=int(transicion[indice_letra+2])
            indice_l=letras.index(name)
            entradas[indice_l]=entrada
            if transicion[indice_letra+3]=="/":
                next_estado=int(transicion[indice_letra+4])
                salir=True
            else:
                indice_letra=indice_letra+4
        conjunto.append(entradas)
        conjunto.append(next_estado)
        transiciones.append(conjunto)
    estado_completo.append(transiciones)#guardamos las transiciones
    estado_completo.append(salida_s)
    estados.append(estado_completo) #Guardamos las transiciones en la lista de estados

#Guardar ticks
info_tick=input()
info_tick=info_tick.split()
ntick=int(info_tick[0])
ini_esta=int(info_tick[1])

ticks=[] #Son todos los ticks

for n in range(ntick):
    tick=[]#Ojo esto es solo un tick
    tick_linea=input()
    tick_linea=tick_linea.split()
    for v in range(variables):
        tick.append(int(tick_linea[v]))
    ticks.append(tick)

#---------------------------------

actu_esta=ini_esta
cadena_estados=[]
for n in range(ntick): #Evaluamos todos los ticks de todas las entradas
    transicion_tick_completa=estados[actu_esta] #Coge las transiciones asociadas al tick
    transicion_tick=transicion_tick_completa[0]
    salida=transicion_tick_completa[1]

    for t in range(len(transicion_tick)):#Hacemos un barrido de las posibles transiciones
        cuenta=0
        bien=0
        for v in range(variables): #Recorreomos todas las variables comparando
            if transicion_tick[t][0][v] !=-1:
                cuenta=cuenta+1
                if transicion_tick[t][0][v]==ticks[n][v]:
                    bien=bien+1
        if cuenta==bien:
            actu_esta=transicion_tick[t][1]
    cadena_estados.append(actu_esta)
cadena_salida=[]
for n in cadena_estados:
    cadena_salida.append(estados[n][1])

#-------------------Imprimir
#Preparacion de lineas
lineas=0
lineas=int(ntick/16)
mod=ntick%16
if mod!=0:
    lineas=lineas+1
#---

#Imprmir
for l in range(lineas):
    print("Tick"+" "+"#"+str(l*16+1))
    #Entradas:
    for ent in range(variables):
        #generar dibujo senial
        senial=""
        senial_out=""
        senial_estado=""
        tick_fin=l*16+16
        if ntick<tick_fin:
            tick_fin=ntick
        tick_rango=range((l*16),tick_fin)
        for num in tick_rango:
            if ticks[num][ent] ==1:
                senial=senial+"***"
            else:
                senial=senial+"___"
            if cadena_salida[num]==1:
                senial_out=senial_out+"***"
            else:
                senial_out=senial_out+"___"
            if cadena_estados[num]==1:
                senial_estado=senial_estado+"  1"
            else:
                senial_estado=senial_estado+"  0"
        print(letras[ent]+"     "+senial)
    print("OUT"+"   "+senial_out)
    print("STATE"+" "+senial_estado)
    if l<(lineas-1):
        print("")
    
    

 

