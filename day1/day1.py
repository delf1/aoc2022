import random


def getLines(f: str) -> list[str]:
    file = open(f)
    return file.readlines()


def solve1(elves: list[list[int]]) -> int:
    m = 0
    for elf in elves:
        m = max(sum(elf), m)
    return m


def quickselect(nums: list[int], n: int) -> int:
    left = 0
    right = len(nums) - 1
    while left < right:
        pivot = random.randint(left, right)
        divider = left
        nums[left], nums[pivot] = nums[pivot], nums[left]
        for i in range(left, right + 1):
            if nums[i] < nums[divider]:
                nums[i], nums[divider] = nums[divider], nums[i]
                divider += 1
                nums[i], nums[divider] = nums[divider], nums[i]

        if divider == n:
            return nums[divider]
        if divider > n:
            right = divider - 1
        else:
            left = divider
        
    return nums[left]


def solve2(elves: list[list[int]]) -> int:
    nums = [sum(elf) for elf in elves]
    n = 3
    return sum([quickselect(nums, len(nums) - i) for i in range(1, n + 1)])


def parse(lines: list[str]) -> list[list[int]]:
    elves = []
    buffer = []
    for line in lines:
        if line == '\n':
            elves.append(buffer)
            buffer = []
        else:
            buffer.append(int(line))
    return elves


elves = parse(getLines("input.txt"))
print(solve1(elves))
print(solve2(elves))
