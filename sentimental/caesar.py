from cs50 import get_string
import sys


def main():
    # Key used to shift plain text characters
    key = int(sys.argv[1]) % 26

    # Ensure only a numeric value was given
    if len(sys.argv) != 2 or not isinstance(key, int):
        sys.exit("Please enter a positive integer as a command line argument")

    plainText = get_string("plaintext: ")
    print("ciphertext: ", end="")

    for char in range(len(plainText)):

        if plainText[char].isalpha():

            # If lowercase, use lowercase 'a' and 'z' as a reference point
            if plainText[char].islower():
                start = ord('a')
                end = ord('z')

            # If UPPERCASE, use uppercase 'A' and 'Z' as a reference point
            elif plainText[char].isupper():
                start = ord('A')
                end = ord('Z')

            # If letter will shift past z, add the difference to the start point
            if ord(plainText[char]) + key > end:
                c = start + ord(plainText[char]) + key - end - 1
            else:
                c = ord(plainText[char]) + key

            # Convert back to character before printing
            c = chr(c)
            print(c, end="")

        # If character is not a letter, just print it
        else:
            print(plainText[char], end="")

    print()


if __name__ == "__main__":
    main()