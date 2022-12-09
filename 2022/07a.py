#!python
from __future__ import annotations
from dataclasses import dataclass
from typing import Optional

@dataclass
class Dir:
    parent: Optional[Dir]
    name: str
    dirs: dict[str, Dir]
    files: dict[str, int]

    def __init__(self, parent: Optional[Dir], name: str) -> None:
        self.name = name
        self.parent = parent
        self.dirs = {}
        self.files = {}

    def size(self) -> int:
        return sum(self.files.values()) + sum(d.size() for d in self.dirs.values())

    def add_dir(self, dirname: str):
        if dirname not in self.dirs:
            self.dirs[dirname] = Dir(self, dirname)

    def add_file(self, filename: str, size: int):
        self.files[filename] = size

    def flat_dirs(self) -> list[Dir]:
        out: list[Dir] = []

        for d in self.dirs.values():
            out.append(d)
            out.extend(d.flat_dirs())

        return out


with open("input/07.txt") as f:
    root = Dir(None, "/")
    pwd = root

    for line in f.readlines():
        line = line.strip()

        # print(line)

        if not line:
            pass
        elif line == "$ cd /":
            pwd = root
        elif line == "$ cd ..":
            pwd = pwd.parent
            assert pwd is not None
        elif line.startswith("$ cd "):
            pwd = pwd.dirs[line.split(' ')[-1]]
        elif line.startswith("$ ls"):
            pass
        elif line.startswith("dir "):
            pwd.add_dir(line.split(' ')[-1])
        else:
            size, filename = line.split(' ')
            pwd.add_file(filename, int(size))

    dir_sizes = [d.size() for d in root.flat_dirs() if d.size() <= 100000]

    print(sum(dir_sizes))



