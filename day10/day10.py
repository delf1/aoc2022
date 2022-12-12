def getLines(f):
    file = open(f)
    return [line.strip() for line in file.readlines()]


def parse(lines):
    instrs = []
    for line in lines:
        instr = line.split()
        if len(instr) == 1:
            instrs.append(None)
        else:
            instrs.append(int(instr[1]))

    return instrs
            
def getCycles(instrs):
    total = 1
    cycles = [total]
    for add in instrs:
        if add is None:
            cycles.append(total)
        else:
            cycles.append(total)
            total += add
            cycles.append(total)
        
    return cycles

def solve1(cycles):
    ret = 0
    for c in [20, 60, 100, 140, 180, 220]:
        ret += cycles[c - 1] * c
    return ret

def solve2(cycles):
    drawing = ['.'] * (40 * 6)
    for i, cycle in enumerate(cycles):
        d = i % 40
        if d - 1 <= cycle <= d + 1:
            drawing[i] = '#' 

    for i in range(6):
        print(drawing[i * 40: i * 40 + 40])

print(solve1(getCycles(parse(getLines("sample.txt")))))
print(solve1(getCycles(parse(getLines("input.txt")))))
solve2(getCycles(parse(getLines("sample.txt"))))
print()
solve2(getCycles(parse(getLines("input.txt"))))