#!/bin/python
# -*- coding: utf-8 -*-
import math

def calcule(pages, size, memoryAccesses):
    pagesFifo = [-1] * pages
    pagesLRU = [-1] * pages

    i = 0

    fifoReplacements = 0
    lruReplacements = 0

    fifoPointer = 0

    init = 0

    while i<memoryAccesses:
        new = int(raw_input())
        page = int(math.floor(new//size))


        #fifo
        if not page in pagesFifo:
            if not -1 in pagesFifo:
                pagesFifo[fifoPointer] = page
                fifoReplacements += 1
                fifoPointer+=1
                fifoPointer%=pages

            else:
                pagesFifo[init] = page
                init+=1

        #lru

        if not page in pagesLRU:
            if not -1 in pagesLRU:
                lruReplacements+=1
            pagesLRU = [page] + pagesLRU[0:len(pagesLRU)-1]
        else:
            pagesLRU = [page] + pagesLRU[0:pagesLRU.index(page)] + pagesLRU[pagesLRU.index(page)+1:]

        i+=1


    if lruReplacements<fifoReplacements:
        print("yes "+str(fifoReplacements)+" "+str(lruReplacements))
    else:
        print("no "+str(fifoReplacements)+" "+str(lruReplacements))

def main():
    tests = int(raw_input())

    i = 0

    while i<tests:
        i+=1

        p, s, n = raw_input().split(" ")
        p = int(p)
        s = int(s)
        n = int(n)
        calcule(p,s,n)



if __name__ == '__main__':
    main()
