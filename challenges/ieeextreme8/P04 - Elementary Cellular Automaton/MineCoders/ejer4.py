# -*- coding: utf-8 -*-


N=8
datos=raw_input()
datos_lista=datos.split()
R=int(datos_lista[0])
itera=int(datos_lista[1])
tam=int(datos_lista[2])
seq=int(datos_lista[3])

n=1
#Generar
def obtener_bit(numero,pos):
        bit=(numero&pow(2,pos))>>pos
        return bit

def traduccion_regla(reglas,buf):
    for i in range(N):
        buf_reglas=reglas[i]>>1
        if buf_reglas==buf:
            return obtener_bit(reglas[i],0)

def crear_reglas(N_reglas):
    reglas=[]            
    for i in range(N):
        bit=obtener_bit(R,i) #Extrae el bit de la secuencia
        elemento=(i<<1)|(bit)#Crea el elemento de la tabla
        #print elemento
        reglas.append(elemento)
    return reglas
#Ir recorriendo el vector que dan y dar la solucion segun la tabla ¿Crear diccionario
def traduccion_iconos(seq,tam):
    cadena="-"
    for i in range(tam-1,-1,-1):    
        if obtener_bit(seq,i)==1:
            cadena=cadena+'*'
        else:
            cadena=cadena+' '
    cadena=cadena+'-'
    return cadena


def crear_seq(seq,tam):    
    reglas=crear_reglas(R)
    seq_n=0
    
    for i in range(tam-1,-1,-1):
         #Alguna forma de mejorar esto? esta alreves el orden
        n_bit3=i+1 #posicion donde estan los 3 bits a evaluar
        n_bit2=i
        n_bit1=i-1
        
        if n_bit3==tam+1:
            bit3=0
        else:
            bit3=obtener_bit(seq,i+1)    
    
        if n_bit1 == -1:
            bit1=0 
        else:
            bit1=obtener_bit(seq,i-1)
            
        bit2=obtener_bit(seq,i)
        
        buf=(bit3<<2)|(bit2<<1)|bit1 #Se crea un numero que contiene los tres bits q se tendran que buscar en las reglas
        seq_inter=traduccion_regla(reglas,buf)<<i #Se mira que regla es y se desplaza hasta la posicion q es
        seq_n=seq_n|(seq_inter) #Se une el numero con la secuencia nueva
    return seq_n


estable=False
while n<=itera and estable==False:
    seq_n=crear_seq(seq,tam)
    cadena= traduccion_iconos(seq,tam)

    if seq==seq_n: 
        estable=True
    else:
        numero=str(n)
        print numero.ljust(3," ")+' '+cadena      
        seq=seq_n
    
        n=n+1

#cadena=traduccion_iconos(seq_n)
#print cadena
  
    
    

#Desplazar los bits a la derecha de la tabla compara cual es igual y ea posicion es la salida