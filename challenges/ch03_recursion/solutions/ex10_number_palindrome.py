# Examples program for the book "Python Challenges"
#
# Copyright 2020 by Michael Inden


def calc_pow_of_ten(number):
    pass


# Funktioniert nur korrekt, wenn die Zahl keine Nullen enthält
def count_digits(number):
    pass


def is_number_palindrome(number):
    pass


def is_number_palindrome_rec(number):
    pass


def __is_number_palindrome_rec_helper(original_number, current_value,
                                      remaining_value):
    pass


def main():
    print("121", is_number_palindrome(121))
    # print("010", isNumberPalindrome(010))
    print("101", is_number_palindrome(101))
    print("10101", is_number_palindrome(10101))

    # darf keine Nullen enthalten
    # print(isNumberPalindrome(102343201))
    print("1234321", is_number_palindrome(1234321))

    print("---------------------------------")

    print("121", is_number_palindrome_rec(121))
    print("122", is_number_palindrome_rec(122))
    print("10101", is_number_palindrome_rec(10101))
    print("1234321", is_number_palindrome_rec(1234321))
    print("102343201", is_number_palindrome_rec(102343201))


if __name__ == "__main__":
    main()
