import csv
from prac_07.guitar import Guitar


def load_guitars(filename):
    """Load guitars from a CSV file."""
    guitars = []
    in_file = open(filename, 'r', newline='')
    reader = csv.reader(in_file)

    for row in reader:
        guitars.append(Guitar(row[0], int(row[1]), float(row[2])))
    return guitars


def main():
    guitars = load_guitars('guitars.csv')
    for guitar in guitars:
        print(guitar)


main()
