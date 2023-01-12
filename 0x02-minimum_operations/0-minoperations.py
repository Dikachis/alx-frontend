#!/usr/bin/python3

"""
    Method that determines the number of minmum operations given n characters
"""


def minOperations(n):
    """
        A function that calculates the fewest number of operations
        needed to give a result of exactly n H characters in a file
        args: n: Number of characters to be displayed
        return:
               number of min operations
    """

    chars_in_file = 1
    no_of_times_copied = 0  # how many times chars (H's) copied
    counter = 0  # operations counter
    while chars_in_file < n:
        remainder = n - chars_in_file
        if (remainder % chars_in_file == 0):
            no_of_times_copied = chars_in_file
            chars_in_file += no_of_times_copied
            counter += 2
        else:
            chars_in_file += no_of_times_copied
            counter += 1
    return counter
