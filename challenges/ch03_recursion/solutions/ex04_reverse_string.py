# Examples program for the book "Python Challenges"
#
# Copyright 2020 by Michael Inden


def reverse_string(input):
    pass


def main():
    print(reverse_string("ABC"))
    print(reverse_string("Michael"))
    print(reverse_string("RACEcar"))

    print("Michael"[::-1])
    print("".join(reversed("Michael")))


if __name__ == "__main__":
    main()
