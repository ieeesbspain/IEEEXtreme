# -*- coding: utf-8 -*-

def nekops_nu(seq):
    output = []
    
    number = seq[0]
    instances = 1    
    
    for i in range(1,len(seq)):
        if seq[i] == number:
            instances += 1
        else:
            output.append(instances)
            output.append(number)
            number = seq[i]
            instances = 1
    output.append(instances)
    output.append(number)
    
    return output

def print_seq(nekops_str, pad_len):
#    print pad_len
    extra_dot = pad_len-len(nekops_str)
    if extra_dot < 0:
        extra_dot = 0
        
    n_dots_right = extra_dot / 2
    n_dots_left = extra_dot - n_dots_right
#    print n_dots_left, n_dots_right
    
    dots_left = ""
    
    for i in range(n_dots_left):
        dots_left = dots_left + "."

    mid_str = dots_left + nekops_str

    dots_right = ""
    for i in range(n_dots_right):
        dots_right = dots_right + "."    
    
    out_str = mid_str + dots_right
    print out_str

    
def join_ints(int_list):
    joined_str = ""
    for i in int_list:
        joined_str = joined_str + str(i) + " "
    return joined_str[:-1]
 

entrada = raw_input().split() # secuencia original

n_exec = int(entrada[0])

orig_seq = []

for s in entrada[1:]: 
    orig_seq.append(int(s))

comp_seq = [orig_seq]
comp_str = [join_ints(orig_seq)]
lengths_seq = [0] #tamaño en numeros. Entrada original no cuenta para el tamaño
lengths_str = [len(join_ints(orig_seq))] #tamaño en caracteres


# No olvidar el caso K=0!!!!!

for i in range(1, n_exec+1):
    s = nekops_nu(comp_seq[i-1]) # Calcular nekops-nu sobre el anterior cálculo
    
    comp_seq.append(s)
    lengths_seq.append(len(s))
    
    s_str = join_ints(s)
    comp_str.append(s_str)# Agregar calculo a la lista
    lengths_str.append(len(s_str)) # Agregar tamaño numerico a la lista

max_len_seq = max(lengths_seq)
max_len_str = max(lengths_str)


for seq in comp_str:
    print_seq(seq,max_len_str)

print max_len_seq