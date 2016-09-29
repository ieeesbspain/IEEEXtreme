# -*- coding: utf-8 -*-

def masDeUno(s, ch):
    count = 0
    for c in s:
        if c == ch:
            count = count + 1
        if count >= 2:
            return True
    
    return False

s = "lukeiamyourfather"
#s = "anynontrivialpropertyofrecursivelyenumerablelanguagesisundecidable"
s = list(s)
s2 = s[:]
a = []

abc = "abcdefghijklmnopqrstuvwxyz"
doubles = ""
for i in range(len(abc)):
    if masDeUno(s, abc[i]):
        doubles = doubles + abc[i]
    elif abc[i] in s2:
        f = s.index(abc[i])
        del s2[f]

print s2
#print sorted(s2)
print len(doubles) + 1