import random


def main():
    """Get a score and display the result."""
    score = float(input("Score: "))
    print(determine_result(score))
    print(f"Random: {determine_random()}")


def determine_result(score):
    """Determine the result of a given score."""
    if score <= 50:
        return "Fail"
    elif score > 50:
        return "Passable"
    elif score > 70:
        return "Good job"
    elif score > 85:
        return "Excellent"
    else:
        return "Invalid score"


def determine_random():
    """Determine the random result."""
    return determine_result(random.randint(0, 100))


main()
