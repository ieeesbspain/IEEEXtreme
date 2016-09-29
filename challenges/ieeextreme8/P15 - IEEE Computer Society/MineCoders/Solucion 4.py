# -*- coding: utf-8 -*-

def findAll(s, ch, start, end):
    found = []
    i = start
    while i < end and i != -1:
        i = s.find(ch, i, end)
        if i != -1:
            found.append(i)
            i = i + 1
            
    return found

def masDeUno(s, ch):
    count = 0
    for c in s:
        if c == ch:
            count = count + 1
        if count >= 2:
            return True
    
    return False
    
#s = "anynontrivialpropertyofrecursivelyenumerablelanguagesisundecidable"
s = "lukeiamyourfather"
s2 = list(s)    
    
abc = "abcdefghijklmnopqrstuvwxyz"
doubles = ""
for i in range(len(abc)):
    if not masDeUno(s2, abc[i]) and abc[i] in s2:
        f = s2.index(abc[i])
        del s2[f]
print s2

der = []
izq = []
for i in range(1, len(s2)):
    izq = s2[:i]
    der = s2[i+1:]
    print izq
    print der
    #for j in range(len(izq)):
    #    idx = der.index(izq[j])
        
    
#for l in abc:
#    if l in s2:
#        found = findAll(s2, l, 0, len(s2))
        