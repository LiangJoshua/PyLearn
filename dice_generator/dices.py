import random

array = [1, 2, 3, 4, 5, 6]


def roll(numbers):
    value = random.randint(numbers[0], numbers[5])
    return value


def goal(numbers, target):
    first = roll(numbers)
    second = roll(numbers)
    print(str(first) + " " + str(second))
    if target == first + second:
        print("you win")
    else:
        print("roll again\n")
        goal(numbers, target)


goal(array, 10)
