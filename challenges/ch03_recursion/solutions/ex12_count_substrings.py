# Examples program for the book "Python Challenges"
#
# Copyright 2020 by Michael Inden


def count_substrings(input, value_to_find):
    pass


def count_substrings_v2(input, value_to_find):
    pass


def count_substrings_optimized(input, value_to_find):
    pass


def count_substrings_helper(input, value_to_find, left):
    pass


def main():
    print(count_substrings("xhixhix", "x"))  # 3
    print(count_substrings("xhixhix", "hi"))  # 2
    print(count_substrings("mic", "mic"))  # 1
    print(count_substrings("haha", "ho"))  # 0
    print(count_substrings("xxxxyz", "xx"))  # 2

    print("-----------------")
    print(count_substrings_v2("xhixhix", "x"))  # 3
    print(count_substrings_v2("xhixhix", "hi"))  # 2
    print(count_substrings_v2("mic", "mic"))  # 1
    print(count_substrings_v2("haha", "ho"))  # 0
    print(count_substrings_v2("xxxxyz", "xx"))  # 3

    print("-----------------")
    print(count_substrings_optimized("xhixhix", "x"))  # 3
    print(count_substrings_optimized("xhixhix", "hi"))  # 2
    print(count_substrings_optimized("mic", "mic"))  # 1
    print(count_substrings_optimized("haha", "ho"))  # 0
    print(count_substrings_optimized("xxxxyz", "xx"))  # 2

    print("-----------------")
    print("-----------------")
    print("xhixhix".count("x"))
    print("xhixhix".count("hi"))
    print("mic".count("mic"))
    print("haha".count("ho"))
    print("xxxxyz".count("xx"))



if __name__ == "__main__":
    main()
