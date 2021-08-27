import random

NUMBERS_PER_LINE = 6
MINIMUM = 1
MAXIMUM = 45


def main():
    """Generate random numbers."""
    number_of_picks = int(input("How many quick picks? "))
    while number_of_picks < 0:
        print("Invalid Input")
        number_of_picks = int(input("How many quick picks? "))

    for pick in range(number_of_picks):
        quick_picks = []
        for line in range(NUMBERS_PER_LINE):
            number = random.randint(MINIMUM, MAXIMUM)
            while number in quick_picks:
                number = random.randint(MINIMUM, MAXIMUM)
            quick_picks.append(number)
        quick_picks.sort()
        print(" ".join("{:2}".format(number) for number in quick_picks))


main()
