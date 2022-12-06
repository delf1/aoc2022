from collections import deque, Counter


def getLines(f):
    file = open(f)
    return [line for line in file.readlines()]


def parse(lines):
    return lines[0]


def solve(line, length):
    dq = deque(line[:length])
    counts = Counter(dq)
    i = length
    while len(counts) < length:
        rem = dq.popleft()
        counts[rem] -= 1
        if counts[rem] == 0:
            del counts[rem]
        counts[line[i]] += 1
        dq.append(line[i])
        i += 1
    return i


def solve1(line):
    return solve(line, 4)


def solve2(line):
    return solve(line, 14)


print(solve1(parse(getLines("sample.txt"))))
print(solve1(parse(getLines("input.txt"))))

print(solve2(parse(getLines("sample.txt"))))
print(solve2(parse(getLines("input.txt"))))
