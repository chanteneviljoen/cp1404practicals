MINIMUM_LENGTH = 4


def main():
    """Get and print password using functions."""
    password = get_password(MINIMUM_LENGTH)
    print_asterisks(password)


def get_password(MINIMUM_LENGTH):
    """Check if the password meets the minimum_length requirement."""
    password = input("Enter password of at least {} characters: ".format(MINIMUM_LENGTH))
    while len(password) < MINIMUM_LENGTH:
        print("Password too short")
        password = input("Enter password of at least {} characters: ".format(MINIMUM_LENGTH))
    return password


def print_asterisks(sequence):
    """Print an asterisks for the length of the password."""
    print('*' * len(sequence))


main()
