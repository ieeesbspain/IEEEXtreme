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


MAX_TIME = 60
TIME_PER_ROUND = 5
MAX_ROUNDS = MAX_TIME / TIME_PER_ROUND


def update_game(game, i, j):
    win = 0
    lose = 0
    if game[i] <= game[j]:
        win = i
        lose = j
    else:
        win = j
        lose = i

    # Update status
    game[lose] -= game[win]
    game[win] += game[win]


def play(game, rounds):
    if rounds >= MAX_ROUNDS:
        return None

    for i in range(3):
        if game[i] == 0:
            return [game]

    best_guess = None
    for i in range(3):
        for j in range(i + 1, 3):
            # i vs j
            new_game = game[:]
            update_game(new_game, i, j)

            # Play again
            result = play(new_game, rounds + 1)
            if result is not None:
                current_guess = [game] + result
                if best_guess is None or len(best_guess) > len(current_guess):
                    best_guess = current_guess
                elif len(best_guess) == len(current_guess):
                    # print(current_guess)
                    pass

    return best_guess


def main():
    game = [int(value) for value in input().split()]
    result = play(game, 0)

    if not result:
        print("Ok")
    else:
        # print(result)
        for g in result:
            r = str(g).replace('[', '').replace(']', '').replace(',', '')
            print(r)


if __name__ == '__main__':
    main()
