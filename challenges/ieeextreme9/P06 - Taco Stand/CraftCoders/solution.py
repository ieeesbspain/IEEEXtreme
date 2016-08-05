#!/bin/python
# -*- coding: utf-8 -*-


def get_tacos(ingredientes):
    ingredientes.sort()
    if ingredientes[0] == ingredientes[1] == 0:
        return 0
    
    for_last = ingredientes[-1] // 2
    for_middle = ingredientes[-1] - for_last
    
    used_last = min(for_last, ingredientes[0])
    used_middle = min(for_middle, ingredientes[-2])
    
    used = used_last + used_middle
    
    remaining_most = for_last - used_last + (for_middle - used_middle)
    remaining_middle = ingredientes[-2] - used_middle
    remaining_last = ingredientes[0] - used_last
    
    ingredientes = [remaining_most, remaining_middle, remaining_last]
    return get_tacos(ingredientes) + used


def main():
    dias = int(input())
    for n in range(dias):
        ingredientes = [int(i) for i in input().split()]
        max_tacos = get_tacos(ingredientes[1:4])
        if ingredientes[0] < max_tacos:
            print(ingredientes[0])
        else:
            print(max_tacos)

if __name__ == '__main__':
    main()
