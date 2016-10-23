"""Solution to problem 8 of IEEEXtreme 10.0."""


def safe_divide(a, b):
    """Do a safe integer division."""
    if a % b != 0:
        return -1
    else:
        return a / b


def main():
    """Main application logic."""
    line = raw_input().split()
    atoms = [int(line[0]), int(line[1]), int(line[2])]

    glucose = safe_divide(4 * atoms[0] + atoms[1] - 2 * atoms[2], 24)
    dioxide = safe_divide(2 * atoms[2] - atoms[1], 4)
    water = safe_divide(atoms[1] + 2 * atoms[2] - 4 * atoms[0], 4)
    if glucose < 0 or dioxide < 0 or water < 0:
        print "Error"
    else:
        print "%d %d %d" % (water, dioxide, glucose)


if __name__ == "__main__":
    main()
