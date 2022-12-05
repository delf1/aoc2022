def getLines(f: str) -> list[str]:
    file = open(f)
    return [line.strip() for line in file.readlines()]

def parse(lines: list[str]) -> list[((str, str), (str, str))]:
    pairs = []
    for line in lines:
        ranges = line.split(',')
        range1, range2 = ranges[0].split('-'), ranges[1].split('-')
        pairs.append(((int(range1[0]), int(range1[1])), (int(range2[0]), int(range2[1]))))
    return pairs

def solve1(pairs: list[((str, str), (str, str))]) -> int:
    count = 0
    for elf1, elf2 in pairs:
        elf1Start, elf1End = elf1
        elf2Start, elf2End = elf2

        if elf1Start < elf2Start:
            if elf1End >= elf2End:
                count += 1
        elif elf2Start < elf1Start:
            if elf2End >= elf1End:
                count += 1
        else:
            count += 1

    return count

def solve2(pairs: list[((str, str), (str, str))]) -> int:
    count = 0
    for elf1, elf2 in pairs:
        elf1Start, elf1End = elf1
        elf2Start, elf2End = elf2

        if elf1Start < elf2Start:
            if elf1End >= elf2Start:
                count += 1
        elif elf2Start < elf1Start:
            if elf2End >= elf1Start:
                count += 1
        else:
            count += 1

    return count

print(solve1(parse(getLines("sample.txt"))))
print(solve1(parse(getLines("input.txt"))))
print(solve2(parse(getLines("sample.txt"))))
print(solve2(parse(getLines("input.txt"))))