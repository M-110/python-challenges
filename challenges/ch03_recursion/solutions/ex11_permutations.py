# Examples program for the book "Python Challenges"
#
# Copyright 2020 by Michael Inden


import itertools
import time


def calc_permutations(input):
    pass


def is_blank(my_string):
    pass


def calc_permutations_mini_opt(input):
    pass


def __calc_permutations_mini_opt_helper(remaining, prefix):
    pass



def calc_permutations_built_in(input):
    pass


def calc_permutations_built_in_single_elements(input):
    pass






def main():
    print(calc_permutations("AB"))
    print(calc_permutations("ABC"))
    print(calc_permutations("ABCD"))

    print(calc_permutations_mini_opt("AB"))
    print(calc_permutations_mini_opt("ABC"))
    print(calc_permutations_mini_opt("ABCD"))

    print(calc_permutations_built_in("AB"))
    print(calc_permutations_built_in("ABC"))
    print(calc_permutations_built_in("ABCD"))

    start = time.process_time()
    print(calc_permutations_built_in("abcdefghijk"))
    end = time.process_time()
    print("calc_permutations_built_in took %.2f ms" % ((end - start) * 1000))
    # 3455.54 ms


if __name__ == "__main__":
    main()
