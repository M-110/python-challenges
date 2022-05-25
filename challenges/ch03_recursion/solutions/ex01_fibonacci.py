# Examples program for the book "Python Challenges"
#
# Copyright 2020 by Michael Inden


def fib_rec(n):
    pass


def fib_iterative(n):
    pass


def main():
    print(fib_rec(5))
    print(fib_rec(10))

    print(fib_iterative(5))
    print(fib_iterative(10))

    #########################

    # RecursionError: maximum recursion depth exceeded in comparison
    # print(fibRec(1000))

    print(fib_rec(10))
    print(fib_iterative(1000))
    print(fib_iterative(10000))

    fib = lambda n: n if n < 2 else fib(n - 1) + fib(n - 2)
    print("fib(10)", fib(10))



if __name__ == "__main__":
    main()
