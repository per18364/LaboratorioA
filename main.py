from infixToPosfix import *
from FNA import *


def main():
    r = input("Enter a regular expression: ")
    postfix = infix_to_postfix(r)
    print(f"Postfix notation: {postfix}")


main()
