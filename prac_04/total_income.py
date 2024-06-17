"""
CP1404/CP5632 Practical
Starter code for cumulative total income program
"""


def main():
    """Display income report for incomes over a given number of months."""
    incomes = []
    number_of_months = int(input("How many months? "))

    for number_of_months in range(1, number_of_months + 1):
        income = float(input(f"Enter income for month {number_of_months}: "))
        incomes.append(income)

    print_income_report(incomes, number_of_months)


def print_income_report(incomes, number_of_months):
    """Display the income report."""
    print("\nIncome Report\n-------------")
    total = 0
    for number_of_months in range(1, number_of_months + 1):
        income = incomes[number_of_months - 1]
        total += income
        print(f"Month {number_of_months:2} - Income: ${income:8.2f}\t\tTotal: ${total:8.2f}")


main()
