def getLines(f: str) -> list[str]:
    file = open(f)
    return [line.strip() for line in file.readlines()]

def parse1(lines: list[str]) -> list[(str, str)]:
    sacks = []
    for line in lines:
        l = len(line) // 2
        sacks.append((line[:l], line[l:]))
    return sacks

def parse2(lines: list[str]) -> list[(str, str, str)]:
    groups = []
    for i in range(len(lines) // 3):
        groups.append((lines[i * 3], lines[i * 3 + 1], lines[i * 3 + 2]))
    return groups

def chToP(ch):
    ascii = ord(ch)
    if ascii > 97:
        return ascii - 96
    else:
        return ascii - 64 + 26

def solve1(sacks: list[(str, str)]) -> int:
    total = 0
    for c1, c2 in sacks:
        same = set(c1).intersection(set(c2)).pop()
        total += chToP(same)
    return total

def solve2(groups: list[(str, str, str)]) -> int:
    total = 0
    for group in groups:
        same = set(group[0]).intersection(set(group[1])).intersection(set(group[2])).pop()
        total += chToP(same)
    return total

print(solve1(parse1(getLines("sample.txt"))))
print(solve1(parse1(getLines("input.txt"))))
print(solve2(parse2(getLines("sample.txt"))))
print(solve2(parse2(getLines("input.txt"))))