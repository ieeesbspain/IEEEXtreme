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


def main():
    width = int(input())
    height = int(input())

    alphabet_size = int(input())
    alphabet = {}

    for i in range(alphabet_size):
        ch = input()
        zoomed = []
        for h in range(height):
            line = input()
            line = line.ljust(width)
            zoomed.append(line)
        alphabet[ch] = zoomed

    num_strings = int(input())
    strings = []
    for i in range(num_strings):
        strings.append(input())

    for phrase in strings:
        for h in range(height):
            for ch in phrase:
                print(alphabet[ch][h], end="")
            print()


if __name__ == '__main__':
    main()
