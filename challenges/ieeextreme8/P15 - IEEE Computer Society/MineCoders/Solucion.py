# -*- coding: utf-8 -*-

def esPalindromo(s, start, end):
    if end - start < 2:
        return True
        
    if s[start] != s[end]:
        return False
    else:
        return esPalindromo(s, start+1, end-1)

def findAll(s, ch, start, end):
    found = []
    i = start
    while i < end and i != -1:
        i = s.find(ch, i, end)
        if i != -1:
            found.append(i)
            i = i + 1
            
    return found
    
def compare(s1, s2):
    return (s2[1] - s2[0]).__cmp__(s1[1] - s1[0])
     
def getPalindromo(s):
    posibles = []
    mitad = len(s) / 2
    for i in range(mitad):
        # Busca el caracter en el otro extremo y lo marca como posible
        # palíndromo        
        ch = s[i]
        found = findAll(s, ch, mitad, len(s))      
        for f in found:
            posibles.append([i, f])
            
    # Ya tenemos todos los posibles, los ordenamos y comprobamos
    posibles = sorted(posibles, cmp=compare)
    for p in posibles:
        loEs = esPalindromo(s, p[0], p[1])
        if loEs:
            return p[1] - p[0] + 1
            
    return 1
        
print getPalindromo("lukeiamyourfather")