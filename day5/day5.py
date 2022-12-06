def getLines(f):
    file = open(f)
    return [line for line in file.readlines()]


def parse(lines):
    blank = 0
    while lines[blank] != '\n':
        blank += 1
    stacks = []
    for index, char in enumerate(lines[blank - 1]):
        if char.isnumeric():
            stack = []
            for i in range(blank - 2, -1, -1):
                letter = lines[i][index]
                if letter != " ":
                    stack.append(letter)
            stacks.append(stack)
    instructions = []
    for j in range(blank + 1, len(lines)):
        words = lines[j].split()
        num, fr, to = words[1], words[3], words[5]
        instructions.append((int(num), int(fr) - 1, int(to) - 1))

    return stacks, instructions


def solve1(stacks, instructions):
    for num, fr, to in instructions:
        for i in range(num):
            stacks[to].append(stacks[fr].pop())
    tops = []
    for stack in stacks:
        tops.append(stack[-1])
    return "".join(tops)


def solve2(stacks, instructions):
    for num, fr, to in instructions:
        stacks[fr], stacks[to] = stacks[fr][:-
                                            num], stacks[to] + stacks[fr][-num:]
    tops = []
    for stack in stacks:
        tops.append(stack[-1])
    return "".join(tops)


sampleStack, sampleInstr = parse(getLines("sample.txt"))
inputStack, inputInstr = parse(getLines("input.txt"))
print(solve1(sampleStack, sampleInstr))
print(solve1(inputStack, inputInstr))

sampleStack, sampleInstr = parse(getLines("sample.txt"))
inputStack, inputInstr = parse(getLines("input.txt"))
print(solve2(sampleStack, sampleInstr))
print(solve2(inputStack, inputInstr))
