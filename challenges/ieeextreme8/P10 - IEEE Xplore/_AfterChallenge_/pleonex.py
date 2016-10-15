# -*- coding: utf-8 -*-
"""Solution to problem 10 by pleonex."""


def create_num(word):
    """Create a num from a word."""
    num = 0
    for char in word[::-1]:
        num <<= 8
        num |= ord(char)
    return num


def create_combinations(elements):
    """Create all the possible combinations."""
    combinations = set()
    if len(elements) == 1:
        return set(elements[0])

    for i in range(len(elements)):
        copy = elements[:]
        del copy[i]
        subcombinations = create_combinations(copy)
        for comb in subcombinations:
            combinations.add(elements[i] + comb)
    return combinations


def main(line):
    """Main application logic."""
    line = line[:line.find(".")]
    elements = [e for e in line]

    combinations = create_combinations(elements)
    numbers = [create_num(c) for c in combinations]

    count = 0
    limit = create_num(line)
    for num in numbers:
        if num <= limit:
            count += 1
    print "%02d" % count


if __name__ == "__main__":
    main(raw_input())
