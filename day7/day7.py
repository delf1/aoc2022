from collections import defaultdict, deque


def getLines(f):
    file = open(f)
    return [line.strip() for line in file.readlines()]


def parse(lines):
    size = defaultdict(int)
    children = defaultdict(set)

    dirStack = ['/']
    path = dirStack[0]
    for line in lines[1:]:
        if line == "$ ls":
            continue
        elif line[:4] == "$ cd":
            if line[5:] == "..":
                popped = dirStack.pop()
                path = path[:-len(popped) - 1]
            else:
                nextDir = line[5:]
                dirStack.append(line[5:])
                path = path + nextDir + "/"
        else:
            sizeOrDir, name = tuple(line.split())
            children[path].add(path + name + "/")
            if sizeOrDir.isnumeric():
                size[path + name + "/"] = int(sizeOrDir)

    def calcSizes(curr):
        nonlocal size
        if not children[curr]:
            return size[curr]
        for child in children[curr]:
            size[curr] += calcSizes(child)
        return size[curr]

    calcSizes('/')
    return children, size


def solve1(children, size):
    maxSize = 100000
    total = 0

    dq = deque(["/"])
    while dq:
        d = dq.pop()
        if children[d]:
            if size[d] <= maxSize:
                total += size[d]
            for child in children[d]:
                dq.append(child)

    return total


def solve2(children, size):
    diskSize = 70000000
    totalNeeded = 30000000
    stillNeeded = totalNeeded - (diskSize - size["/"])
    if stillNeeded <= 0:
        return 0

    currMin = float('inf')
    dq = deque(["/"])
    while dq:
        d = dq.pop()
        for child in children[d]:
            if children[child]:
                dq.append(child)
        if size[d] > stillNeeded:
            currMin = min(currMin, size[d])

    return currMin


print(solve1(*parse(getLines("sample.txt"))))
print(solve1(*parse(getLines("input.txt"))))
print(solve2(*parse(getLines("sample.txt"))))
print(solve2(*parse(getLines("input.txt"))))
