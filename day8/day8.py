from functools import reduce


def getLines(f):
    file = open(f)
    return [line.strip() for line in file.readlines()]


def parse(lines):
    return [[int(num) for num in line] for line in lines]

def solve1(lines):
    rows, cols = len(lines), len(lines[0])
    visible = [[False] * cols for row in range(rows)]

    for row in range(rows):
        m = -float('inf')
        for col in range(cols):
            if lines[row][col] > m:
                visible[row][col] = True
                m = lines[row][col]

        m = -float('inf')
        for col in range(cols - 1, -1, -1):
            if lines[row][col] > m:
                visible[row][col] = True
                m = lines[row][col]
    
    for col in range(cols):
        m = -float('inf')
        for row in range(rows):
            if lines[row][col] > m:
                visible[row][col] = True
                m = lines[row][col]

        m = -float('inf')
        for row in range(rows - 1, -1, -1):
            if lines[row][col] > m:
                visible[row][col] = True
                m = lines[row][col]

    total = 0
    for row in range(rows):
        for col in range(cols):
            if visible[row][col]:
                total += 1

    return total


def solve2(lines):
    rows, cols = len(lines), len(lines[0])
    maxScore = 0
    for row in range(1, rows - 1):
        for col in range(1, cols - 1):
            height = lines[row][col]
            scores = []
            for dx, dy in [(1, 0), (0, 1), (-1, 0), (0, -1)]:
                curr = 1
                x = row + dx
                y = col + dy
                while x > 0 and x < rows - 1 and y > 0 and y < cols - 1 and lines[x][y] < height:
                    curr += 1
                    x += dx
                    y += dy
                scores.append(curr)
            maxScore = max(maxScore, reduce(lambda a, b: a * b, scores))

    return maxScore




print(solve1(parse(getLines("sample.txt"))))
print(solve1(parse(getLines("input.txt"))))
print(solve2(parse(getLines("sample.txt"))))
print(solve2(parse(getLines("input.txt"))))
