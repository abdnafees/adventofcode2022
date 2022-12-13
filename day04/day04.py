file = open('day04/input.txt', 'r')
input = [i for i in file.read().strip().split('\n')]

print(input)


def part01(section):
    overlapQ1 = 0

    for s in section:
        s1, s2 = s.split(',')
        s1Start, s1End = map(int, s1.split('-'))
        s2Start, s2End = map(int, s2.split('-'))

        if (s1Start <= s2Start and s2End <= s1End) or (s2Start <= s1Start and s1End <= s2End):
            overlapQ1 += 1

    print(overlapQ1)


def part02(section):
    overlapQ2 = 0

    for s in section:
        s1, s2 = s.split(',')
        s1Start, s1End = map(int, s1.split('-'))
        s2Start, s2End = map(int, s2.split('-'))

        if set(range(s1Start, s1End + 1)) & set(range(s2Start, s2End + 1)):
            overlapQ2 += 1

    print(overlapQ2)


if __name__ == '__main__':
    part01(input)
    part02(input)
