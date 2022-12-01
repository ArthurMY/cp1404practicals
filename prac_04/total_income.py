"""
CP1404/CP5632 Practical
Starter code for cumulative total income program
"""


def main():
    """Display income report for incomes over a given number of month."""
    incomes = []
    month = int(input("How many month? "))

    month = time_entered(incomes, month)

    print("\nIncome Report\n-------------")
    total = 0
    summary_counting(incomes, month, total)


def summary_counting(incomes, month, total):
    for month in range(1, month + 1):
        income = incomes[month - 1]
        total += income
        print("Month {:2} - Income: ${:10.2f} Total: ${:10.2f}".format(month, income, total))


def time_entered(incomes, month):
    for month in range(1, month + 1):
        income = float(input(f"Enter income for month {month}:"))
        incomes.append(income)
    return month


main()
