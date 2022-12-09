#!python

with open("input/05.txt") as f:
    lines = iter(f.readlines())

    # Read current state
    rows: list[list[str]] = []
    while True:
        line = next(lines)
        if line.startswith(" 1 "): break

        row: list[str] = []
        i = 1
        while i < len(line):
            row.append(line[i])
            i += 4

        rows.append(row)



    # Convert rows to stacks
    stacks: list[list[str]] = [[] for _ in range(len(rows[0]))]

    for row in reversed(rows):
        for i, x in enumerate(row):
            if x != ' ':
                stacks[i].append(x)

    # print(stacks)

    # Read commands

    for line in lines:
        line = line.strip()
        if not line: continue

        cmd = line.split(' ')
        assert len(cmd) == 6

        amount = int(cmd[1])
        stack_from = int(cmd[3]) - 1
        stack_to = int(cmd[5]) - 1

        hold: list[str] = []
        for _ in range(amount):
            hold.insert(0, stacks[stack_from].pop())
        stacks[stack_to].extend(hold)

    # print(stacks)

    print(''.join(stack[-1] for stack in stacks))
