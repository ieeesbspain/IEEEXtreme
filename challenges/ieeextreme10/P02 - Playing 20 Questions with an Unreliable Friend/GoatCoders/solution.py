"""Solution to P2 of IEEEXtreme 10.0."""


def valid_input(question, counts):
    """Check if the input question is valid."""
    if ' and ' in question:
        subquestions = question.split(' and ')
    elif ' or ' in question:
        subquestions = question.split(' or ')
    else:
        subquestions = [question]

    result = True
    for sub in subquestions:
        commands = sub.split()
        if commands[0] == 'count':
            color = commands[1]
            num = int(commands[2])
            counts[color] += num
        elif commands[0] == 'color':
            num = int(commands[1])
            color = commands[2]
        else:
            result = False

        # Check the color and numbers are in the limits
        num = 0
        color = 0
        if num > 10 or num < 1:
            result = False
        if color not in ['r', 'g', 'b']:
            result = False

    num_ballons = 0
    for _, num in counts.iteritems():
        num_ballons += num
    if num_ballons > 10:
        result = False
    return result


def analyze(ballons, counts, lies, hints):
    """Analyze if the current state is consistent and iterate for more."""
    num_hints = len(hints)
    # Check if we are done
    if num_hints == 0:
        return ballons

    # Get the next hint
    hint = hints.pop()

    # Gets if we should try to trust the reply or not
    orig_reply = hint[1]
    replies = [orig_reply, not orig_reply]

    # If the number of remaining lies is the same as the number of hints, lies!
    if lies == num_hints:
        replies = [replies[1]]
    # If there isn't any lie, then trust.
    elif lies == 0:
        replies = [replies[0]]

    # For every possible reply, try
    for rep in replies:
        question = hint[0]

        # First, let's validate the question
        if not valid_input(question, counts):
            if not rep:  # If we already knew it's false, it's ok, it's false
                continue
            elif rep != orig_reply:  # Otherwise, it's a lieeee
                lies -= 1
                continue

        # Divide into subquestions
        if ' and ' in question:
            operation = 'and'
            subquestions = question.split(' and ')
        elif ' or ' in question:
            operation = 'or'
            subquestions = question.split(' or ')
        else:
            subquestions = [question]

        # Select the subsubqestions to negate
        # TODO

        scenarios = []
        for subq in subquestions:
            commands = subq.split()
            sce = ballons[:]

            # ... Apply suggestions
            if commands[0] == 'color':
                num = int(commands[1])
                color = commands[2]
                sce[num].add(color)
            else:
                color = commands[1]
                num = int(commands[2])
                counts[color] += num

            # ... Check if it's consistent

            scenarios.append(sce)

        # Merge the returned scenarios
        new_ballons = [set()] * 10
        for sce in scenarios:
            for i in range(10):
                new_ballons[i] &= sce[i]  # append ballons colors

        # Run the rests of hints
        result = analyze(new_ballons, counts.copy(), lies, hints)

        # If it is not None, it the way to go back
        if result is not None:
            return result
    return None


def print_result(ballons):
    """Print the result."""
    for i in range(10):
        if len(ballons[i]) == 0:
            ballons[i] &= set(['r', 'g', 'b'])
    print " ".join(["".join(b) for b in ballons])


def main():
    """Main application logic."""
    ballons = [set()] * 10

    line = raw_input().split()
    questions = int(line[0])
    lies = int(line[1])

    hints = []
    for _ in range(questions):
        hints += [[raw_input(), raw_input() == "yes"]]

    counts = {'r': 0, 'g': 0, 'b': 0}
    result = analyze(ballons, counts, lies, hints)
    # print_result(result)


if __name__ == "__main__":
    NUM_TESTS = int(raw_input())
    for _ in range(NUM_TESTS):
        raw_input()
        main()
