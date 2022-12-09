#!python

WINS = ['A Y', 'B Z', 'C X']
DRAW = ['A X', 'B Y', 'C Z']
SCORES = {
    'X': 1,
    'Y': 2,
    'Z': 3,
}

with open("input/02.txt") as f:
    score = 0

    for line in f.readlines():
        code = line.strip()

        if code in WINS:
            score += 6
        elif code in DRAW:
            score += 3

        score += SCORES[code.split()[1]]

    print(score)


