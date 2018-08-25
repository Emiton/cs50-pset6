from cs50 import get_int

print("It's a me, Mario!")

height = -1

while height < 0 or height > 23:
    height = get_int("Please enter a number between 0 and 23: ")

# Row x will have x blocks in each half pyramid, therefore height * 2
# Also, add 2 for the 2 spaces between the half pyramids in every row
rowLength = height * 2 + 2

for row in range(height):
    for col in range(height):
        if col <= row:
            print("#", end="")
    print()

print()


