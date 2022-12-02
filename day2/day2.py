import random


def getLines(f: str) -> list[str]:
    file = open(f)
    return file.readlines()


beats = {
    "A": "Y",
    "B": "Z",
    "C": "X"
}

convert = {
    "A": "X",
    "B": "Y",
    "C": "Z"
}


def solve1(rounds: list[(int, int)]) -> int:
    shapeScore = {
        "X": 1,
        "Y": 2,
        "Z": 3
    }
    total = 0
    for opp, us in rounds:
        total += shapeScore[us]
        if convert[opp] == us:
            total += 3
        elif beats[opp] == us:
            total += 6
    return total


def solve2(rounds: list[(int, int)]) -> int:
    beatenBy = {
        "A": "Z",
        "B": "X",
        "C": "Y"
    }

    def us(opp, res):
        if res == "X":
            return beatenBy[opp]
        elif res == "Z":
            return beats[opp]
        else:
            return convert[opp]

    return solve1([(opp, us(opp, res)) for opp, res in rounds])


def parse(lines: list[str]) -> list[list[int]]:
    rounds = []
    for line in lines:
        rounds.append((line[0], line[2]))
    return rounds


print(solve1(parse(getLines("sample.txt"))))
print(solve1(parse(getLines("input.txt"))))
print(solve2(parse(getLines("sample.txt"))))
print(solve2(parse(getLines("input.txt"))))