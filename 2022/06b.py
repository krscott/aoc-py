#!python

SIGNAL_LEN = 14

with open("input/06.txt") as f:
    text = f.readline().strip()

    for i in range(SIGNAL_LEN, len(text) + 1):
        if len(set(text[i-SIGNAL_LEN:i])) == SIGNAL_LEN:
            print(i)
            break

