# A program which calculates the minimum amount of coins needed
# to give change to a user. US denominations are used.
from cs50 import get_float

change = -1.0
coins = 0

while change < 0:
    change = get_float("Change owed: ")

# Multiply by 100 and round to avoid working with floats
change = round(change * 100)

while change > 0:
    if change >= 25:
        change -= 25
        coins += 1
    elif change >= 10:
        change -= 10
        coins += 1
    elif change >= 5:
        change -= 5
        coins += 1
    elif change >= 1:
        change -= 1
        coins += 1

print(coins)