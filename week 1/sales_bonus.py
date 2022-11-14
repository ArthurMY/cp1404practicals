"""
Program to calculate and display a user's bonus based on sales.
If sales are under $1,000, the user gets a 10% bonus.
If sales are $1,000 or over, the bonus is 15%.

pseudocode:
get sales
while sales >= 0
    calculate bonus
    get sales
do next thing
"""

BASICLINE = 0
DISCOUNTLINE = 1000
DISCOUNTLOW = 0.1
DISCOUNTHIGH = 0.15
sales = float(input("Enter sales: $"))
while sales >= BASICLINE:
    if sales < DISCOUNTLINE:
        price = sales * DISCOUNTLOW
    else:
        price = sales * DISCOUNTHIGH
    print(price)
    sales = float(input("Enter sales: $"))
