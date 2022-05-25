# Examples program for the book "Python Challenges"
#
# Copyright 2020 by Michael Inden


def calc(m, n):
    pass


def calc_v2(m, n):
    pass


def calc_sum_and_count_all_numbers_div_by_2_or_7(max_exclusive):
    pass


def calc_sum_and_count_all_numbers_div_by_2_or_7_v2(max_exclusive):
    pass


class ReturnCode:
    def __init__(self, sum, count):
        self.sum = sum
        self.count = count

    def __eq__(self, other):
        return self.sum == other.sum and \
               self.count == other.count

    def __str__(self):
        return "sum: " + str(self.sum) + " / count: " + str(self.count)


def is_even(n):
    pass


def is_odd(n):
    pass


def main():
    print(calc(6, 7))  # 0
    print(calc(3, 4))  # 6
    print(calc(5, 5))  # 5

    calc_sum_and_count_all_numbers_div_by_2_or_7(15)
    print(calc_sum_and_count_all_numbers_div_by_2_or_7(10))
    print(calc_sum_and_count_all_numbers_div_by_2_or_7_v2(4))
    print(calc_sum_and_count_all_numbers_div_by_2_or_7_v2(8))

    print("is_even:", is_even(7))
    print("is_odd:", is_odd(7))
    print("is_odd:", is_odd(-7))


if __name__ == "__main__":
    main()
