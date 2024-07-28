from prac_06.guitar import Guitar


def main():
    """Test Guitar class."""
    gibson = Guitar("Gibson L-5 CES", 1924, 16035.40)
    another = Guitar("Another Guitar", 2015, 765.40)
    strato = Guitar("Strato Guitar", 1974, 16035.40)

    print(f"{gibson.name} get_age() - Expected 100. Got {gibson.get_age()}")
    print(f"{another.name} get_age() - Expected 9. Got {another.get_age()}")
    print(f"{gibson.name} is_vintage() - Expected True. Got {gibson.is_vintage()}")
    print(f"{another.name} is_vintage() - Expected False. Got {another.is_vintage()}")
    print(f"{strato.name} get_age() - Expected 50. Got {strato.get_age()}")
    print(f"{strato.name} is_vintage() - Expected True. Got {strato.is_vintage()}")

main()
