# -*- coding: utf-8 -*-

class Error:
    def __init__(self, tipo, bad_rows):
        self.tipo      = tipo
        self.bad_rows  = bad_rows
    
    def get_tipo(self):
        return self.tipo
        
    def get_bad_rows(self):
        return self.bad_rows
      
    def __str__(self):
        if self.tipo == "1":
            return "i1=" + str(self.bad_rows+1)
        else:
            return "i1=" + str(self.bad_rows[0]+1) + " i2=" + str(self.bad_rows[1]+1)

    def __cmp__(self, other):
        if self.tipo == other.tipo:
            return self.bad_rows.__cmp__(other.bad_rows)
        elif self.tipo == "1":
            return 1
        else:
            return -1


def comprueba(n, m, t):
    errores = []    
    
    # Comprueba cada fila buscando que no se cumpla alguna de las condiciones
    for ri in range(n-1):        
        # Cada fila ha de cumplir dos condiciones
        cumple1 = False
        cumple2 = [False, ] * (n-ri-2)
        
        for ci in range(m):            
            # Condición 1
            if not cumple1:
                cumple1 = (t[ri][ci] != t[ri+1][ci]) and (t[ri+1][ci] == t[n-1][ci])
            
            # Condición 2
            for rj in range(ri+1, n-1):
                if not cumple2[rj-ri-1]:
                    cumple2[rj-ri-1] = (t[ri][ci] != t[ri+1][ci]) and (t[ri+1][ci] == t[rj][ci]) and  (t[rj][ci] == t[rj+1][ci])
            
        # Comprueba si ha habido errores
        if not cumple1:
            errores.append(Error("1", ri))
            
        for i in range(n-ri-2):
            if not cumple2[i]:
                errores.append(Error("2", [ri, i+ri+1]))
                
    return errores
    

# Leemos las dimensiones de la matriz
dim = raw_input().split(' ')
n = int(dim[0])
m = int(dim[1])

# Leemos la matriz
t = []
for i in range(n):
    elements = raw_input().split(' ')
    t.append([ int(e) for e in elements ])

errores = comprueba(n, m, t)

# Muestra los errores
print len(errores)
for e in errores:
    print e
    