#!python

WIN = {
    'A': 'B',
    'B': 'C',
    'C': 'A',
}

LOSE = {
    'A': 'C',
    'B': 'A',
    'C': 'B',
}

SCORES = {
    'A': 1,
    'B': 2,
    'C': 3,
}



with open("input/02.txt") as f:
    score = 0

    for line in f.readlines():
        [opponent, strat] = line.strip().split()

        if strat == 'X':
            score += 0
            you = LOSE[opponent]
        elif strat == 'Y':
            score += 3
            you = opponent
        else:
            score += 6
            you = WIN[opponent]

        # print(you)

        score += SCORES[you]

    print(score)


