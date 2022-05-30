# Examples program for the book "Python Challenges"
#
# Copyright 2020 by Michael Inden


from challenges.ch02_math.intro.intro import find_proper_divisors


def is_perfect_number_simple(number):
    return sum(i for i in range(1, number // 2 + 1) if not number % i) == number


def calc_perfect_numbers(max_exclusive):
    return [i for i in range(1, max_exclusive) if is_perfect_number_simple(i)]


def calc_perfect_numbers_comprehension(max_exclusive):
    return [i for i in range(1, max_exclusive) if is_perfect_number_simple(i)]


def is_perfect_number_based_on_proper_divisors(number):
    return sum(i for i in range(1, number // 2 + 1) if not number % i) == number


def main():
    print(is_perfect_number_simple(6))
    print(is_perfect_number_simple(7))
    print(is_perfect_number_simple(24))
    print(is_perfect_number_simple(25))
    print(is_perfect_number_simple(28))

    print(calc_perfect_numbers(50))
    print(calc_perfect_numbers_comprehension(50))


if __name__ == "__main__":
    main()
