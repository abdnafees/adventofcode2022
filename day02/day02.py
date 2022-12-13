from functools import reduce

file = open('day02/input.txt', 'r')
input = [i for i in file.read().strip().split('\n')]
lines = list(map(lambda x: x.split(' '), input))

moves = {
    'rock': 1,
    'paper': 2,
    'scissors': 3
}

mapInput = {
    'A': moves['rock'],
    'B': moves['paper'],
    'C': moves['scissors'],
    'X': moves['rock'],
    'Y': moves['paper'],
    'Z': moves['scissors']
}


def score(opponentMove, ourMove):

    if (opponentMove == ourMove):
        return ourMove + 3

    elif (opponentMove == moves['rock'] and ourMove == moves['paper'] or
            opponentMove == moves['paper'] and ourMove == moves['scissors'] or
            opponentMove == moves['scissors'] and ourMove == moves['rock']):
        return ourMove + 6

    else:
        return ourMove


def part01(input):
    scores = []
    for line in input:
        opponentMove = mapInput[line[0]]
        ourMove = mapInput[line[1]]
        scores.append(score(opponentMove, ourMove))
    return reduce(lambda x, y: x+y, scores)


desiredOutcomes = {
    'A': {'X': moves['scissors'], 'Y': moves['rock'], 'Z': moves['paper']},
    'B': {'X': moves['rock'], 'Y': moves['paper'], 'Z': moves['scissors']},
    'C': {'X': moves['paper'], 'Y': moves['scissors'], 'Z': moves['rock']},
}


def part02(input):
    scores = []
    for line in input:
        opponentMove = mapInput[line[0]]

        ourMove = desiredOutcomes[line[0]][line[1]]
        scores.append(score(opponentMove, ourMove))
    return reduce(lambda x, y: x+y, scores)


print(part01(lines))
print(part02(lines))
