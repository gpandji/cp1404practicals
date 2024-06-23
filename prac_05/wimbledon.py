"""
wimbledon
Estimate: 90 minutes
Actual:   34 minutes
"""


def read_wimbledon_data(filename):
    """Reads each line from the csv file and returns it as a list."""
    with open(filename, "r", encoding="utf-8-sig") as in_file:
        data = [line.strip().split(",") for line in in_file.readlines()]
    return data


def process_champions(data):
    """reads list and counts the number of times each player has won"""
    champions_dict = {}
    for row in data[1:]:
        champion = row[2].strip()
        if champion in champions_dict:
            champions_dict[champion] += 1
        else:
            champions_dict[champion] = 1
    return champions_dict


def process_countries(data):
    """reads list and returns a sorted list of countries that have won"""
    countries = set()
    for row in data[1:]:
        country = row[1].strip()
        countries.add(country)
    return sorted(countries)


def main():
    filename = 'wimbledon.csv'
    data = read_wimbledon_data(filename)

    champions = process_champions(data)
    countries = process_countries(data)

    print("Wimbledon Champions:")
    for champion, wins in champions.items():
        print(f"{champion} {wins}")

    print("\nThese countries have won Wimbledon:")
    print(", ".join(countries))


main()
