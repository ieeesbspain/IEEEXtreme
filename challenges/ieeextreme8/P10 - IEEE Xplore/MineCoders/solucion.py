# -*- coding: utf-8 -*-

def compare(c1, c2):
    for i in range(len(c1)):
        if c1[i] != c2[i]:
            return c1[i].__cmp__(c2[i])
    return 0

def genera_numeros(digitos):
    digi_len = len(digitos)
    nums = []    
    
    if digi_len == 1:
        return [ [digitos[0], ] ]
    
    for i in range(digi_len):
        n = [digitos[i], ]
        
        subdigitos = digitos[:]
        del subdigitos[i]
        combinaciones = genera_numeros(subdigitos)      
        
        for c in combinaciones:
            nums.append(n + c)
            
    return nums

def resuelve(linea):
    entrada = ""
    for c in linea:
        if c == '.':
            break
        else:
            entrada = entrada + c
    
    # Obtiene el número y sus dígitos
    digitos = [ ord(e) for e in entrada ]
    num_final = list(reversed(digitos)) 
    
    # Genera todas las posibles combinaciones y las ordena
    similares = genera_numeros(digitos)
    similares = sorted(similares, cmp=compare)
    
    # Cuenta cuántas hay antes de llegar a sí mismo
    count = 0
    for s in similares:
        count = count + 1
        if compare(s, num_final) == 0:
            break
        
    print "%02d" % count
    
    
resuelve(raw_input())