# Examples program for the book "Python Challenges"
#
# Copyright 2020 by Michael Inden


import functools


def sum_rec(values):
    pass


def sum_helper(values, pos):
    pass


def sum_tail(values):
    pass


def sum_tail_helper(values, pos):
    pass


def sum_lambda(values):
    pass


def main():
    print(sum([1, 2, 3, 4, 5]))
    print(sum([7, 3, 8, 2, 1]))
    print(sum([7, 3, 8, 2, 1]))

    print(sum_rec([1, 2, 3, 4, 5]))
    print(sum_rec([7, 3, 8, 2, 1]))
    print(sum_rec([7, 3, 8, 2, 1]))

    print(sum_lambda([1, 2, 3, 4, 5]))
    print(sum_lambda([7, 3, 8, 2, 1]))
    print(sum_lambda([7, 3, 8, 2, 1]))


if __name__ == "__main__":
    main()
