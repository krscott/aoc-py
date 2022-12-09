from collections.abc import Iterator
from typing import TypeVar, Generator

T = TypeVar("T")

def chunks(iter: Iterator[T], size: int) -> Generator[list[T], None, None]:
    chunk: list[T] = []

    for x in iter:
        chunk.append(x)

        if len(chunk) == size:
            yield chunk
            chunk = []


def priority(char: str) -> int:
    assert len(char) == 1
    if 'a' <= char <= 'z':
        return ord(char) - ord('a') + 1
    if 'A' <= char <= 'Z':
        return ord(char) - ord('A') + 27
    assert False


def priority_of_common_item(rucksacks: list[str]) -> int:
    common_set = None

    for s in rucksacks:
        s = s.strip()

        if common_set is None:
            common_set = set(s)
        else:
            common_set = common_set.intersection(s)

    assert common_set and len(common_set) == 1

    return priority(list(common_set)[0])


with open("input/03.txt") as f:
    ans = sum(priority_of_common_item(chunk) for chunk in chunks(iter(f.readlines()), 3))
    print(ans)


