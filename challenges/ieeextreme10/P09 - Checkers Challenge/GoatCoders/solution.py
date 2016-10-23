"""Solution for problem 9 of IEEEXtreme 10.0."""

WIDTH = 8
HEIGHT = 8


def check_finish(scenario):
    """Check if we have won."""
    for h in range(HEIGHT):
        for w in range(WIDTH):
            if scenario[h][w] != '.':
                return False
    return True


def update_scenario(scenario, old_pos, new_pos):
    """Update the scenario."""
    dir_h = 1 if new_pos[0] > old_pos[0] else -1
    dir_h = 1 if new_pos[0] == old_pos[0] else dir_h
    dir_w = 1 if new_pos[1] > old_pos[1] else -1
    dir_w = 1 if new_pos[1] == old_pos[1] else dir_w
    for h in range(old_pos[0], new_pos[0] + dir_h, dir_h):
        for w in range(old_pos[1], new_pos[1] + dir_w, dir_w):
            scenario[h][w] = "."


def sum_pos(pos1, pos2):
    """Sum two positions."""
    return (pos1[0] + pos2[0], pos1[1] + pos2[1])


def valid_pos(pos):
    """Check if the position is in the table."""
    return pos[0] < HEIGHT and pos[0] >= 0 and \
        pos[1] < WIDTH and pos[1] >= 0


def is_black(scenario, pos):
    """Check if the given position there is a black piece."""
    return scenario[pos[0]][pos[1]] == 'x'


def has_eaten(scenario, old_pos, new_pos):
    """Return if at least has eaten a piece."""
    dir_h = 1 if new_pos[0] > old_pos[0] else -1
    dir_h = 1 if new_pos[0] == old_pos[0] else dir_h
    dir_w = 1 if new_pos[1] > old_pos[1] else -1
    dir_w = 1 if new_pos[1] == old_pos[1] else dir_w
    for h in range(old_pos[0], new_pos[0] + dir_h, dir_h):
        for w in range(old_pos[1], new_pos[1] + dir_w, dir_w):
            if scenario[h][w] == 'x':
                return True
    return False


def get_positions(scenario, last_pos, pos, king):
    """Get all the possible movements."""
    directions = [(-1, 0), (0, 1), (0, -1)]
    if king:
        directions.append((1, 0))

    if last_pos is not None:
        dir_h = 1 if pos[0] > last_pos[0] else -1
        dir_h = 0 if pos[0] == last_pos[0] else dir_h
        dir_w = 1 if pos[1] > last_pos[1] else -1
        dir_w = 0 if pos[1] == last_pos[1] else dir_w
        directions.remove((dir_h * -1, dir_w * -1))

    positions = []
    for direct in directions:
        curr_pos = sum_pos(pos, direct)
        prev_pos = None
        stop = False
        while not stop:
            # Check if the position is valid
            if not valid_pos(curr_pos):
                stop = True
                continue

            # If we haven't detected a black piece, can't move
            piece = has_eaten(scenario, pos, curr_pos)
            if not piece:
                stop = not king
                curr_pos = sum_pos(curr_pos, direct)
                continue
            elif not prev_pos and is_black(scenario, curr_pos):
                stop = not king
                prev_pos = curr_pos
                curr_pos = sum_pos(curr_pos, direct)
                continue
            elif is_black(scenario, curr_pos) and is_black(scenario, prev_pos):
                stop = True
                continue

            # Valid position
            prev_pos = None
            positions.append(curr_pos)

            # If it's the king go on.
            stop = not king
            curr_pos = sum_pos(curr_pos, direct)

    return positions


def play(scenario, last_pos, pos, king):
    """Generate all the possible winner combinations."""
    result = []
    # Get the movements and iterate
    movements = get_positions(scenario, last_pos, pos, king)
    for mov in movements:
        # Update scenario
        new_king = king
        new_pos = mov
        new_scenario = [r[:] for r in scenario]
        update_scenario(new_scenario, pos, new_pos)

        # Check if we are king now
        if not new_king and new_pos[0] == 0:
            new_king = True

        if check_finish(new_scenario):
            result.append((new_pos,))
        else:
            recur = play(new_scenario, pos, new_pos, new_king)
            for r in recur:
                result.append((new_pos,) + r)

    return result


def read_scenario():
    """Read the scenario from the STDIN."""
    scenario = []
    pos = None
    for h in range(HEIGHT):
        row = []
        line = raw_input()
        for w in range(WIDTH):
            row.append(line[w])
            if line[w] == "o":
                pos = (h, w)
                row[len(row) - 1] = '.'
        scenario.append(row)
    return [pos, scenario]


def main():
    """Main application logic."""
    pos, scenario = read_scenario()
    king = pos[0] == 0
    result = play(scenario, None, pos, king)
    myset = set(result)
    print len(myset)


if __name__ == "__main__":
    NUM_TESTS = int(raw_input())
    for i in range(NUM_TESTS):
        if i > 0:
            raw_input()
        main()
