from cs50 import get_int

height = -1

while height < 0 or height > 23:
    height = get_int("Please enter a number between 0 and 23: ")

# Row x will have x blocks in each half pyramid, therefore height * 2
# Also, add 2 for the 2 spaces between the half pyramids in every row
rowLength = height * 2 + 2

for row in range(height):
    for col in range(rowLength):
        # Determine boundaries for first half of pyramid
        if height - row - 1 <= col and col < height:
            print("#", end="")
        # Determine boundaries for second half of pyramid
        elif col > height + 1 and col <= height + 2 + row:
            print("#", end="")
        # Anything not in boundaries, print a blank character
        elif col <= height + 1:
            print(" ", end="")
    print()