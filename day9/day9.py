from functools import reduce

def getLines(f):
    file = open(f)
    return [line.strip() for line in file.readlines()]


def parse(lines):
    motions = []
    for line in lines:
        dir, steps = tuple(line.split())
        motions.append((dir, int(steps)))
    return motions

def moveTail(head, tail):
    hx, hy = head
    tx, ty = tail
    if abs(hx - tx) <= 1 and abs(hy - ty) <= 1:
        return tail
    else:
        rx, ry = head
        if abs(hx - tx) > 1:
            if hx > tx:
                rx -= 1
            else:
                rx += 1
        if abs(hy - ty) > 1:
            if hy > ty:
                ry -= 1
            else:
                ry += 1
        return rx, ry

delta = {
    'R': (1, 0),
    'L': (-1, 0),
    'U': (0, 1),
    'D': (0, -1)
}   
    
def solve(motions, length):
    knots = [(0, 0)] * length
    visited = set([knots[-1]])

    for dir, steps in motions:
        dx, dy = delta[dir]
        for _ in range(steps):
            hx, hy = knots[0]
            knots[0] = hx + dx, hy + dy
            for knot in range(1, len(knots)):
                knots[knot] = moveTail(knots[knot - 1], knots[knot])
            visited.add(knots[-1])
    return len(visited)

def solve1(motions):
    return solve(motions, 2)

def solve2(motions):
    return solve(motions, 10)

print(solve1(parse(getLines("sample.txt"))))
print(solve1(parse(getLines("input.txt"))))
print(solve2(parse(getLines("sample2.txt"))))
print(solve2(parse(getLines("input.txt"))))