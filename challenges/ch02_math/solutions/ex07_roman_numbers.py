# Examples program for the book "Python Challenges"
#
# Copyright 2020 by Michael Inden


def from_roman_number_v1(roman_number):
    pass


def from_roman_number(roman_number):
    pass


value_map = {"I": 1, "V": 5, "X": 10, "L": 50,
             "C": 100, "D": 500, "M": 1000}


def to_roman_number_v1(value):
    pass


def to_roman_number(value):
    pass

# intuitive Variante, dann aber nicht korrekte
# XXXIIII
# XXXXVIIII
int_to_roman_digit_map_v1 = {1: "I", 5: "V", 10: "X", 50: "L",
                             100: "C", 500: "D", 1000: "M"}

int_to_roman_digit_map = {1: "I", 4: "IV", 5: "V", 9: "IX", 10: "X",
                          40: "XL", 50: "L", 90: "XC", 100: "C",
                          400: "CD", 500: "D", 900: "CM", 1000: "M"}


def main():
    print(from_roman_number("VII"))
    print(from_roman_number("XXII"))
    print(from_roman_number("XXIXV"))

    print(to_roman_number(7))
    print(to_roman_number(15))
    print(to_roman_number(34))
    print(to_roman_number(49))


if __name__ == "__main__":
    main()
