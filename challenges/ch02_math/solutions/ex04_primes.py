# Examples program for the book "Python Challenges"
#
# Copyright 2020 by Michael Inden


import itertools
import math


def is_prime(potentially_prime):
    return all(potentially_prime % i for i in range(2, potentially_prime))


def erase_multiples_of_current(values, number):
    pass


def build_primes_list(is_potentially_prime):
    pass


def build_primes_list_old(is_potentially_prime):
    pass


def calc_primes_up_to(max_value):
    return [i for i in range(2, max_value+1) if is_prime(i)]


def calc_primes_up_to_v2(max_value):
    A = [True] * (max_value + 1)
    for i in range(2, int(math.sqrt(max_value)) + 1):
        if A[i]:
            for j in range(i**2, max_value + 1, i):
                A[j] = False
    A[:2] = [False, False]
    return [i for i in range(max_value + 1) if A[i]]



def main():
    print(calc_primes_up_to(50))
    print(calc_primes_up_to_v2(50))


if __name__ == "__main__":
    main()
