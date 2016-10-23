"""Solution to problem 11 of IEEEXtreme 10.0."""


def main():
    """Main application logic."""
    # Group all the piles together
    piles = []
    num_games = int(raw_input())
    for _ in range(num_games):
        raw_input()  # Num piles
        piles += [int(x) for x in raw_input().split()]

    # For every pile, the minimum number of turns to finish it is...
    num_turns = 0
    for pile in piles:
        if pile == 1:
            continue
        num_turns += pile // 2

    # If it's odd, then the winner is Alice, otherwise is Bob
    print "Bob" if num_turns % 2 == 0 else "Alice"


if __name__ == "__main__":
    NUM_TESTS = int(raw_input())
    for _ in range(NUM_TESTS):
        main()
