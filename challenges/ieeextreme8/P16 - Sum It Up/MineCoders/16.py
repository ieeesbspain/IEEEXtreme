# -*- coding: utf-8 -*-

# Prueba
#N = 10000
#
#A = range(1,N)
##print A
#
#Q=1000
#X = range(Q)

#Entrada
N = int(raw_input())
A_str = raw_input().split()
A = []
for a in A_str:
    A.append(int(a))
Q = int(raw_input())
X=[]
for q in range(Q):
    X.append(int(raw_input()))

#Displacement

for x in X:
    sum_displaced=[]
    for i in range(len(A)):
#        print (A[i], A[i-x])
        sum_displaced.append(A[i] + A[i-x])
    A=sum_displaced
#    print A
#print A

#Modulo

print str(sum(A) % (10**9+7))