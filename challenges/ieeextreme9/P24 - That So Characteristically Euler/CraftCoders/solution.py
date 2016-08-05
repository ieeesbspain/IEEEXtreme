#!/bin/python
# -*- coding: utf-8 -*-

conn_black = []
conn_white = []

def search_connection(x, y, connections, diag):
    for conn in connections:
        x_diff = conn[0] - x
        y_diff = conn[1] - y
        if (x_diff >= -1 and x_diff <= 1) and (y_diff >= -1 and y_diff <= 1):
            if diag or (not (x_diff != 0 and y_diff != 0)):
                return True
    
    return False


def process_line(y, line, regions, holes):
    for x in range(len(line)):
        if line[x] == 1:
            if len(conn_black) == 0 or not search_connection(x, y, conn_black, True):
                regions += 1
                
            conn_black.append((x, y))
        else:
            if len(conn_white) == 0 or not search_connection(x, y, conn_white, False):
                holes += 1
                
            conn_white.append((x, y))
    
    return [regions, holes]


def compute_case():
    height = int(input())
    width = int(input())
    
    regions = 0
    holes = 0    
    
    image = []
    for h in range(height):
        # Get image
        line = input()
        image_line = []
        for l in line:
            image_line.append(0 if l == 'O' else 1)
        image.append(image_line)
        
        # Process image
        regions, holes = process_line(h, image_line, regions, holes)
        
    # Print result
    print(regions - (holes - 1))


def main():
    num = int(input())
    for i in range(num):
        compute_case()


if __name__ == '__main__':
    main()
