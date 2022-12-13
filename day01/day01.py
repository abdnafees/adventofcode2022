file = open('day01/input.txt', 'r')
input = [i for i in file.read().strip('\n').split('\n\n')]


def part1(elves):
    calories = 0
    sumofcalories = []
    for elf in elves:
        calories = elf.split('\n')
        calories = map(int, calories)
        sumofcalories.append(sum(calories))
    return sumofcalories


listofsums = part1(input)
print(listofsums)
print(max(listofsums))
listofsums.sort(reverse=True)
print(sum(listofsums[0:3]))
