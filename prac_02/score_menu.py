MENU_STRING = "(G)et a valid score (must be 0-100 inclusive)\n(P)rint result\n(S)how stars\n(Q)uit"
def main():
    score = get_score()
    print(MENU_STRING)
    choice = input()
    while choice != "Q":
        if choice == "G":
            score=get_score()
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
    """get a valid score."""
    while True:
        try:
            score = float(input("Enter score: "))
        except ValueError:
            # Not a valid number
            print("You must enter a number")
        else:
            while score < 0 and score > 100:
                print("You must enter a number between 0 to 100")
                score = input("Enter score: ")
            else:
                return score

def print_sore(score):
    """Print respective result for input score."""
    if score > 90:
        print("Excellent")
    elif score > 50:
        print("Passable")
    elif score < 50:
        print("Bad")

def print_asterisks(score):
    """Print as many asteri-sks as the input score."""
    print('*' * int(score))

main()