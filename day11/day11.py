from collections import defaultdict, deque

def getLines(f):
    file = open(f)
    return [line.strip() for line in file.readlines()]


def parse(lines):
    monkeys = []
    for i in range(len(lines) // 6):
        stats = lines[i * 6:i * 6 + 6]
        items = deque([int(i) for i in stats[1].split(":")[1].split(",")])
        op = getFunc(stats[2].split()[3:])
        test = int(stats[3].split()[3])
        true = int(stats[4].split()[5])
        false = int(stats[5].split()[5])
        monkeys.append([items, op, test, true, false])
            
    return monkeys

def getFunc(op):
    a, operator, b = tuple(op)
    if b == "old":
        if operator == "*":
            return lambda x: x * x
        else:
            return lambda x: x + x
    else:
        if operator == "*":
            return lambda x: x * int(b)
        else:
            return lambda x: x + int(b)

def solve(monkeys, rounds, relief):
    inspected = defaultdict(int)
    mod = 1
    for monkey in monkeys:
        mod *= monkey[2]
    for _ in range(rounds):
        for monkey in range(len(monkeys)):
            items, op, test, true, false = monkeys[monkey]
            inspected[monkey] += len(items)
            for i in range(len(items)):
                item = items.popleft()
                worry = (op(item) // relief) % mod
                if worry % test == 0:
                    monkeys[true][0].append(worry)
                else:
                    monkeys[false][0].append(worry)
    s = list(inspected.values())
    s.sort()
    return s[-1] * s[-2]

def solve1(monkeys):
    return solve(monkeys, 20, 3)

def solve2(monkeys):
    return solve(monkeys, 10000, 1)

print(solve1(parse(getLines("sample.txt"))))
print(solve1(parse(getLines("input.txt"))))
print(solve2(parse(getLines("sample.txt"))))
print(solve2(parse(getLines("input.txt"))))