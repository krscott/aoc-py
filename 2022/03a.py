#!python

def priority(char: str) -> int:
    assert len(char) == 1
    if 'a' <= char <= 'z':
        return ord(char) - ord('a') + 1
    if 'A' <= char <= 'Z':
        return ord(char) - ord('A') + 27
    assert False

def priority_of_common_item(rucksack: str) -> int:
    rucksack = rucksack.strip()
    pivot = len(rucksack) // 2

    left = set(rucksack[:pivot])
    right = set(rucksack[pivot:])

    common_item = list(left.intersection(right))[0]

    return priority(common_item)

with open("input/03.txt") as f:
    ans = sum(priority_of_common_item(line) for line in f.readlines())
    print(ans)


