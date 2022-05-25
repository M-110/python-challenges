# Examples program for the book "Python Challenges"
#
# Copyright 2020 by Michael Inden


def is_power_of_2(n):
    pass


def is_power_of_2_short(n):
    pass


def power_of(value, exponent):
    pass


def power_of_optimized(value, exponent):
    pass

def power_of_iterative(value, exponent):
    pass


def main():
    print(is_power_of_2(10))
    print(is_power_of_2(11))
    print(is_power_of_2(16))

    print(is_power_of_2_short(10))
    print(is_power_of_2_short(11))
    print(is_power_of_2_short(16))

    print(power_of(4, 2))
    print(power_of(5, 3))
    print(power_of(2, 8))
    print(power_of(10, 3))

    print(power_of_optimized(4, 2))
    print(power_of_optimized(5, 3))
    print(power_of_optimized(2, 8))
    print(power_of_optimized(10, 3))

    print(power_of_iterative(4, 2))
    print(power_of_iterative(5, 3))
    print(power_of_iterative(2, 8))
    print(power_of_iterative(10, 3))


if __name__ == "__main__":
    main()
