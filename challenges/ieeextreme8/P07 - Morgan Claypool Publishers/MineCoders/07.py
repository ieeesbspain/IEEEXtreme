# -*- coding: utf-8 -*-

first_line = raw_input().split()

n_subj = int(first_line[0])
n_cons = int(first_line[1])

constrains = []

for i in range(n_cons):
    s, u = raw_input().split()
    constrains.append((int(s), int(u))) # (S ,U)
    
study_plan = raw_input().split()

# Hash study subject positions to access them easily

studies = dict(zip(study_plan, range(0,len(study_plan))))

#print studies
#print constrains

for cons in constrains:
#    print cons
    if studies[str(cons[0])] >= studies[str(cons[1])]: # If subject S is not studied before U
        print "NO"
        break
else:
    print "YES"