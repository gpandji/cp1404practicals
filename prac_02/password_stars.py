
def main():
    """Get and print password using functions."""
    password = get_password(3)
    print_asterisks(password)


def get_password(minimum_length):
    """Get password, with at least the minimum length."""
    password = input(f"Enter password with least {minimum_length} characters:")
    while len(password) < minimum_length:
        name = (input("please re-enter password: "))
        password = '*' * len(name)
        print(f"password: {password}")
    return password


def print_asterisks(sequence):
    """Print as many asterisks as there are characters in the passed-in sequence."""
    print('*' * len(sequence))

main()

