"""Solution to P3 of IEEEXtreme 10.0."""
from sys import maxsize

LOOKUP = {}


# def gcd(a, b):
#     """Check if the greatest common divisor is 1."""
#     while b != 0:
#         mod = a % b
#         a = b
#         b = mod
#     return a

def gcd(u, v):
    if u == 0:
        return v
    if v == 0:
        return u

    shift = 0
    while ((u | v) & 1) == 0:
        u >>= 1
        v >>= 1
        shift += 1

    while ((u & 1) == 0):
        u >>= 1

    while v != 0:
        while (v & 1) == 0:
            v >>= 1

        if u > v:
            t = v
            v = u
            u = t
        v = v - u

    return u << shift


def main(current_count):
    """Main application logic."""
    line = raw_input().split()
    N = int(line[0])
    A = int(line[1])
    B = int(line[2])

    result = 0
    i = A
    while i <= B:
        l = (N, i)
        g = gcd(N, i)
        if l not in LOOKUP and current_count < maxsize:
            LOOKUP[l] = g
            current_count += 1
        if gcd(N, i) == 1:
            result += i
        i += 1
    print result % 1000000007
    return count


if __name__ == "__main__":
    num_tests = int(raw_input())
    count = 0
    for _ in range(num_tests):
        count = main(count)
