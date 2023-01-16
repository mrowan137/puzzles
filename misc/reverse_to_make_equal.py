"""
Given two arrays A and B of length N, determine if there is a way to make A
equal to B by reversing any subarrays from array B any number of times.
"""
import math
from collections import Counter


def are_they_equal(array_a, array_b):
    # consider 2 elements case. we can put 2nd in place, then make remainder match
    # consider 3 elements case. we can put 3rd in place, then make remainder match
    # ... 'induction'
    # consider n elements case. we can put nth in place, then make remainder to match
    # only way we could not be able to match, is the counts differ
    return Counter(array_a) == Counter(array_b)


# Tests we to determine if the solution is correct.
def printString(string):
    print('["', string, '"]', sep="", end="")


test_case_number = 1


def check(expected, output):
    global test_case_number
    result = False
    if expected == output:
        result = True
    rightTick = "\u2713"
    wrongTick = "\u2717"
    if result:
        print(rightTick, "Test #", test_case_number, sep="")
    else:
        print(
            wrongTick, "Test #", test_case_number, ": Expected ", sep="", end=""
        )
        printString(expected)
        print(" Your output: ", end="")
        printString(output)
        print()
    test_case_number += 1


if __name__ == "__main__":
    n_1 = 4
    a_1 = [1, 2, 3, 4]
    b_1 = [1, 4, 3, 2]
    expected_1 = True
    output_1 = are_they_equal(a_1, b_1)
    check(expected_1, output_1)

    n_2 = 4
    a_2 = [1, 2, 3, 4]
    b_2 = [1, 2, 3, 5]
    expected_2 = False
    output_2 = are_they_equal(a_2, b_2)
    check(expected_2, output_2)
