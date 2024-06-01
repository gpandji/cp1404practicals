def main():
    score = float(input("Enter score: "))
    print_sore(score)

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

main()