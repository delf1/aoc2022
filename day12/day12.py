from collections import deque

def getLines(f):
    file = open(f)
    return [line.strip() for line in file.readlines()]

def parse(lines):
    grid = []
    start = None
    end = None
    for i, line in enumerate(lines):
        row = []
        for j, c in enumerate(line):
            if c == 'S':
                start = (i, j)
                row.append(ord('a'))
            elif c == 'E':
                end = (i, j)
                row.append(ord('z'))
            else:
                row.append(ord(c))
        grid.append(row)
    return grid, start, end

def solve(grid, starts, end):
    rows = len(grid)
    cols = len(grid[0])
    dq = deque()
    seen = set()
    for start in starts:
        dq.appendleft((start, 0)) 
        seen.add(start)
    while dq:
        curr, steps = dq.popleft()
        if curr == end:
            return steps
        
        x, y = curr
        for dx, dy in [(1, 0), (0, 1), (-1, 0), (0, -1)]:
            nx, ny = x + dx, y + dy
            if nx >= 0 and nx < rows and ny >= 0 and ny < cols and (nx, ny) not in seen and grid[nx][ny] - grid[x][y] <= 1 :
                nex = (nx, ny)
                seen.add(nex)
                dq.append((nex, steps + 1))

    return -1


def solve1(grid, start, end):
    return solve(grid, [start], end)

def solve2(grid, start, end):
    a = []
    for i, row in enumerate(grid):
        for j, c in enumerate(row):
            if c == ord('a'):
                a.append((i, j))
    return solve(grid, a, end)

print(solve1(*parse(getLines("sample.txt"))))
print(solve1(*parse(getLines("input.txt"))))
print(solve2(*parse(getLines("sample.txt"))))
print(solve2(*parse(getLines("input.txt"))))