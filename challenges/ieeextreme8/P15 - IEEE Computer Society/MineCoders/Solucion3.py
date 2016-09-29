# -*- coding: utf-8 -*-
#s = "lukeiamyourfather"
s = "anynontrivialpropertyofrecursivelyenumerablelanguagesisundecidable"

#s = sorted(s)

abc = "abcdefghijklmnopqrstuvwxyz"
count = 0
for l in abc:
    c = s.count(l)
    count = count + c / 2

print count + 1
#
#def eliminaEnMedio(v, start, end):
#    res = v[:start - 1] + v[end:]
#    return res
#    
#
#usados = []
#count = 1
#for i in range(len(s)):
#    if s[i] not in usados:
#        usados.append(s[i])
#    else:
#        count = count + 2
#        end = len(usados)
#        start = usados.index(s[i]) + 1
#        print usados
#        usados = eliminaEnMedio(usados, start, end)
#        print usados
#
#print count
#print usados