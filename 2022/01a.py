#!python

with open("input/01.txt") as f:
    calories = [0]
    for line in f.readlines():
        line = line.strip()
        if line == "":
            calories.append(0)
        else:
            calories[-1] += int(line)

    print(max(calories))
