#!python


def id_range_to_set(s: str) -> set[int]:
    start, end = s.split('-')
    return set(range(int(start), int(end) + 1))


with open("input/04.txt") as f:
    count = 0

    for line in f.readlines():
        left, right = line.strip().split(',')

        left = id_range_to_set(left)
        right = id_range_to_set(right)

        both = left.intersection(right)

        if len(both) > 0:
            count += 1

    print(count)
