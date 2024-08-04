import csv
from prac_07.guitar import Guitar


def load_guitars(filename):
    """Load guitars from a CSV file."""
    guitars = []
    in_file = open(filename, 'r', newline='')
    reader = csv.reader(in_file)

    for row in reader:
        guitars.append(Guitar(row[0], int(row[1]), float(row[2])))
    in_file.close()
    return guitars


def add_new_guitars(guitars):
    """Add new guitars to the list."""
    print("Enter your new guitars:")
    name = input("Name: ")
    while name:
        year = int(input("Year: "))
        cost = float(input("Cost: $"))
        guitars.append(Guitar(name, year, cost))
        name = input("Name: ")


def save_guitars(filename, guitars):
    """Save the list of guitars to a CSV file."""
    with open(filename, 'w', newline='') as file:
        writer = csv.writer(file)
        for guitar in guitars:
            writer.writerow([guitar.name, guitar.year, guitar.cost])


def main():
    guitars = load_guitars('guitars.csv')
    add_new_guitars(guitars)
    guitars.sort()
    for guitar in guitars:
        print(guitar)
    save_guitars('guitars.csv', guitars)


main()
