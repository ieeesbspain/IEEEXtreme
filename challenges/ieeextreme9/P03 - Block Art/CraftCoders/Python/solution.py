#!/bin/python
# -*- coding: utf-8 -*-
############################################################################
#  Copyright (C) 2015 Benito Palacios Sánchez                              #
#                                                                          #
#  This program is free software: you can redistribute it and/or modcify   #
#  it under the terms of the GNU General Public License as published by    #
#  the Free Software Foundation, either version 2 of the License, or       #
#  (at your option) any later version.                                     #
#                                                                          #
#  This program is distributed in the hope that it will be useful,         #
#  but WITHOUT ANY WARRANTY; without even the implied warranty of          #
#  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the            #
#  GNU General Public License for more details.                            #
#                                                                          #
#  You should have received a copy of the GNU General Public License       #
#  along with this program. If not, see <http://www.gnu.org/licenses/>.    #
############################################################################


def edit_matrix(matrix, cols, start, end, diff):
    for x in range(start[0], end[0] + 1):
        for y in range(start[1], end[1] + 1):
            matrix[y*cols + x] = matrix[y*cols + x] + diff


def count_matrix(matrix, cols, start, end):
    count = 0
    for x in range(start[0], end[0] + 1):
        for y in range(start[1], end[1] + 1):
            count = count + matrix[y*cols + x]

    print(count)


def main():
    dimensions = input().split()
    rows = int(dimensions[0])
    cols = int(dimensions[1])
    matrix = [0] * (rows * cols)

    num_queries = int(input())
    for i in range(num_queries):
        args = input().split()

        cmd = args[0]
        start = (int(args[2]) - 1, int(args[1]) - 1)
        end = (int(args[4]) - 1, int(args[3]) - 1)
        if cmd == "a":
            edit_matrix(matrix, cols, start, end, 1)
        elif cmd == "r":
            edit_matrix(matrix, cols, start, end, -1)
        else:
            count_matrix(matrix, cols, start, end)


if __name__ == '__main__':
    main()
