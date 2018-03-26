# -*- coding: utf-8 -*-
"""Solution to problem 10."""


def get_number(word):
    """Get a word from the number."""
    num = 0
    for c in word[::-1]:
        num <<= 8
        num |= ord(c)
    return num


def generate_anagrams(chars):
    """Generate an anagram incrementing a number."""
    anagrams = []

    if len(chars) == 1:
        return [chars[0]]

    for i in range(len(chars)):
        cpy = chars[:]
        del cpy[i]

        combinations = generate_anagrams(cpy)
        for c in combinations:
            anagrams.append(chars[i] + c)

    return anagrams


def main(line):
    """Main application logic."""
    # Filter the input, it ends with the dot.
    line = line[:line.find(".")]

    limit = get_number(line)
    # print limit
    chars = [c for c in line]
    anagrams = generate_anagrams(chars)
    # print anagrams
    num = [get_number(w) for w in anagrams]
    # print num
    count = 0
    for n in num:
        if n <= limit:
            count += 1
    print "%02d" % count


if __name__ == "__main__":
    main(raw_input())
