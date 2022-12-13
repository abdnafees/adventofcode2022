file = open('day06/input.txt', 'r')
input = file.read().strip()


def isUnique(array):
    return len(set(array)) == len(array)


def part01():
    slidingWindow = []
    for i in range(len(input)):
        slidingWindow.append(input[i])
        if len(slidingWindow) > 4:
            slidingWindow = slidingWindow[1:]
        print(slidingWindow)
        if len(slidingWindow) == 4 and isUnique(slidingWindow):
            print(i+1)
            break


def part02():
    windowLength = 14
    slidingWindow = []
    for i in range(len(input)):
        slidingWindow.append(input[i])
        if len(slidingWindow) > windowLength:
            slidingWindow = slidingWindow[1:]
        print(slidingWindow)
        if len(slidingWindow) == windowLength and isUnique(slidingWindow):
            print(i+1)
            break


part01()
part02()
