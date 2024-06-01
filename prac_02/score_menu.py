MENU_STRING = "(G)et a valid score (must be 0-100 inclusive)\n(P)rint result\n(S)how stars\n(Q)uit"
def main():
    score = get_score()
    print(MENU_STRING)
    choice = input()
    while choice != "Q":
        if choice == "G":
            get_score()
        elif choice == "P":
            print_sore(score)
        elif choice == "S":
            print_asterisks(score)
        else:
            print("invalid message")
        print(MENU_STRING)
        choice = input()
    print("Finished")
def get_score():
    """Print as many asterisks as the input score."""
    score = float(input("Enter score: "))
    return score

def print_sore(score):
    """Print respective result for input score."""
    if score < 0:
        print("Invalid score")
    elif score > 100:
        print("Invalid score")
    elif score > 90:
        print("Excellent")
    elif score > 50:
        print("Passable")
    elif score < 50:
        print("Bad")

def print_asterisks(score):
    """Print as many asterisks as the input score."""
    print('*' * int(score))

main()