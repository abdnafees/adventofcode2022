import re
from collections import defaultdict

file = open('day05/input.txt', 'r')
rawStacks, instructions = file.read().split('\n\n')
rawStacks = rawStacks.split('\n')
instructions = instructions.split('\n')


def parseStacks(stacks):
    parsed = []
    spacedOut = [line.split('\n') for line in stacks]
    for char in spacedOut:
        for chr in char:
            c = re.findall(r'[A-Z1-9]', chr)
            parsed.append(c)
    return parsed


parsedStacks = parseStacks(rawStacks)
indexes = parsedStacks.pop()

stacks = {}
ordering = []


def part01():

    for line in parsedStacks:
        for i in range(len(line)):
            if line[i] != ' ':
                if indexes[i] not in stacks.keys():
                    stacks[indexes[i]] = []
                    ordering.append(indexes[i])
                stacks[indexes[i]].append(line[i])

    for move in instructions:
        if 'move' in move:
            match = re.findall(r'(\d+)', move)
            count = int(match[0])
            prev = int(match[1])
            next = int(match[2])
                
                stacks[next-1] = stacks[prev-1][:count][::-1] + stacks[next-1]
                stacks[prev-1] = stacks[prev-1][next:]
    print(stacks)


def part02():
    pass


if __name__ == '__main__':
    part01()
    part02(input)
