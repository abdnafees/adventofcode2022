import re

file = open('day03/input.txt', 'r')
input = [i for i in file.read().strip().split('\n')]


def letterToPriority(letter):
    if (re.search(r'[a-z]', letter)):
        return ord(letter) - 96
    else:
        return ord(letter) - 65 + 27


def part01(input):
    priority01 = 0
    for line in input:
        lineLength = int(len(line))
        smCase = line[0:int(lineLength/2)]
        uppCase = line[int(lineLength/2):]
        for letter in smCase:
            if letter in uppCase:
                value = letterToPriority(letter)
                priority01 += value
                break
    print(priority01)


def part02(input):
    priority02 = 0
    counter = 0
    while counter < len(input):
        bag1 = input[counter]
        bag2 = input[counter + 1]
        bag3 = input[counter + 2]
        for item in bag1:
            if item in bag2 and item in bag3:
                value = letterToPriority(item)
                priority02 += value
                counter += 3
                break
    print(priority02)


if __name__ == '__main__':
    part01(input)
    part02(input)
