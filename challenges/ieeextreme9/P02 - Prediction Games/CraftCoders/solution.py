#!/bin/python
# -*- coding: utf-8 -*-


def main():
    partidas=int(input())
    for i in range(partidas): #partida
        inicio=input()
        inicio=inicio.split()
        jugadores=int(inicio[0])
        competiciones=int(inicio[1])
        resumen={}
        resultados=[]
        for j in range(jugadores):
            nombre=input()
            predicciones=[]
            for h in range(competiciones):
                prediccion=input()
                prediccion=prediccion.split()  
                prediccion=[int(prediccion[0]),int(prediccion[1])]
                predicciones.append(prediccion)
            resumen[nombre]=predicciones
        for i in range(competiciones):
            resultado=input()
            resultado=resultado.split()
            if resultado[0]=='?':
                resultado=[-1,-1]#ATENCION PUEDE QUE SOLO UNO DE LOS RESULTADOS SEA ? Y EL OTRO NO
            else:
                resultado=[int(resultado[0]),int(resultado[1])]
            resultados.append(resultado)
        #Hacer todas las operaciones
        #COmprobar si es -1
        puntuacion={}
        puntuacion[nombre]=0
        desconocidos=[]
        for nombre in resumen:#recorremos todos los jugadores en esa competicion
            puntuacion[nombre]=0
    
        for n in range(competiciones):
            p1=False#Inicio del partido
            p2=False
            p1p=False
            p2p=False
            
            if resultados[n][0]==-1: #Vemos si no se saben los resultados
                desconocidos.append(n)
                #poner marca
                #-mirar si sale que ganan los dos
                #Suponer que sale el mismo que uno
                #sumarle 25 puntos
                #calcularle los puntos al otro
                #Hacerlo al reves
                #hacer algo
            else:
                #partido: es el resultado de la competicion actual
                #presultado: es la prediccion de la competicion actual de una persona
                #Vemos quien ha ganado:
                partido=resultados[n]
                if partido[0]>partido[1]:
                    p1=True#ganador
                    p2=False
                else:
                    p2=True
                    p1=False
                for nombre in resumen:#recorremos todos los jugadores en esa competicion
                    puntos=0
                    presultado=resumen[nombre][n]#Predicciones de esa ronda para una persona
    
                    #Vemos quien ha dicho quien es el ganador
                    if presultado[0]>presultado[1]:
                        p1p=True
                        p2p=False
                    else:
                        p1p=False
                        p2p=True
                        
                    if p1p==p1:#Si ha acertado con el ganador
                        puntos=puntos+10#Si ha acertado sumamos +10
                    #---Puntos de Equipos------
                    #Equipo 1
                    diferencia=abs(presultado[0]-partido[0])# Diferencia de prediccion
                    
                    if diferencia<=5: #Si la diferencia es menor o igual que 5
                        puntos=puntos+abs(5-diferencia)
                   
                   #Equipo 2
                    diferencia=abs(presultado[1]-partido[1])# Diferencia de prediccion
                    
                    if diferencia<=5: #Si la diferencia es menor o igual que 5
                        puntos=puntos+abs(5-diferencia)
                    #Puntos de propagacion
                    propagacion=abs((presultado[0]-presultado[1])-(partido[0]-partido[1]))
                    if propagacion<=5:
                        puntos=puntos+(5-propagacion)
                    puntuacion[nombre]=puntuacion[nombre]+puntos
    
                    
                #calcular puntos
        if len(desconocidos)==1:
            for j in range(len(desconocidos)): #Recooremos todos los casos de desconocidos  
                pos=desconocidos[j] #posicion de la competicion desconocida
    
                vecfpuntuaciones=[]
                for nombre in resumen: #Recorremos todos los posibles opciones
                    fpuntuaciones={}
                    correcto=resumen[nombre][pos]# Este es el partido de los resultados
                    
                    #---Comprobamos el ganador---
    
    
                    if correcto[0]>correcto[1]:
                        p1=True#ganador
                        p2=False
                    else:
                        p2=True
                        p1=False
                    #-----                
                    
                    #calcular la puntuacion de los demas nombres
                    fpuntuaciones[nombre]=puntuacion[nombre]+25
                
                    for otros_nombres in resumen:
                        if otros_nombres != nombre:
    
                            puntos=0
                            presultado=resumen[otros_nombres][pos]
                            #vemos cual es mayor
    
                            if presultado[0]>presultado[1]:
                                p1p=True
                                p2p=False
                            else:
                                p1p=False
                                p2p=True
                            #calcular puntos
                            #
                            
                            
                    #---------------
    
                        
                            if p1p==p1:#Si ha acertado con el ganador
                                puntos=puntos+10#Si ha acertado sumamos +10
    
                            #---Puntos de Equipos------
                            #Equipo 1
                            diferencia=abs(presultado[0]-correcto[0])# Diferencia de prediccion
                            
                            if diferencia<=5: #Si la diferencia es menor o igual que 5
                                puntos=puntos+abs(5-diferencia)
    
                           
                           #Equipo 2
                            diferencia=abs(presultado[1]-correcto[1])# Diferencia de prediccion
                            
                            if diferencia<=5: #Si la diferencia es menor o igual que 5
                                puntos=puntos+abs(5-diferencia)
    
                            #Puntos de propagacion
                            propagacion=abs((presultado[0]-presultado[1])-(correcto[0]-correcto[1]))
                            if propagacion<=5:
                                puntos=puntos+(5-propagacion)
                            fpuntuaciones[otros_nombres]=puntuacion[otros_nombres]+puntos
    
                    #----------------                
                    vecfpuntuaciones.append(fpuntuaciones)
    
            maximo=-1
            persona_max=[]
            personas_maximas=[]
            for i in range(len(vecfpuntuaciones)):#Recorro el vector de diccionario
                maximo=-1
                dicc=vecfpuntuaciones[i]
    
                for name in dicc:
                    point=dicc[name]
                    if point>maximo:
                        persona_max=[]
                        maximo=point
                        persona_max.append(name)
                    elif point==maximo:
                        persona_max.append(name)
                for m in persona_max:
                    personas_maximas.append(m)
    
            lista_final=list(set(personas_maximas))
            lista_final=sorted(lista_final)
    
            #--------------
            salida=lista_final[0]
            if len(lista_final)>1:
                for e in range(len(lista_final)):
                    if e<len(lista_final)-1:
                        salida=salida+' '+lista_final[e+1]
            print(salida)
                    
                      
        elif len(desconocidos)>1:
            lista=[]
            for nombre in resumen:
                lista.append(nombre)
            lista_final=sorted(lista)
            salida=lista_final[0]
            if len(lista_final)>1:
                for e in range(len(lista_final)):
                    if e<len(lista_final)-1:
                        salida=salida+' '+lista_final[e+1]
            print(salida)
            
        else:
            maximo=-1
            persona_max=[]
            for name in puntuacion:
                point=puntuacion[name]
                if point>maximo:
                    persona_max=[]
                    maximo=point
                    persona_max.append(name)
                elif point==maximo:
                    persona_max.append(name)
            persona_max=sorted(persona_max)  
            salida=persona_max[0]
            if len(persona_max)>1:
                for e in range(len(persona_max)):
                    if e<len(persona_max)-1:
                        salida=salida+' '+persona_max[e+1]
            print(salida)



if __name__ == '__main__':
    main()
