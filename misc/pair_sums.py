"""
Given a list of n integers arr[0..(n-1)], determine the number of different
pairs of elements within it which sum to k. If an integer appears in the list
multiple times, each copy is considered to be different; that is, two pairs are
considered different if one pair includes at least one array index which the
other doesn't, even if they include the same values.
"""
import math
from collections import defaultdict


def numberOfWays(arr, k):
    target_to_complement_idx = defaultdict(list)
    for i, v in enumerate(arr):
        target_to_complement_idx[k - v].append(i)

    # count pairs that sum to k
    res = 0
    seen = set()
    for i, v in enumerate(arr):
        if v in target_to_complement_idx.keys():
            for j in target_to_complement_idx[v]:
                if not (min(i, j), max(i, j)) in seen and i != j:
                    res += 1
                    seen.add((min(i, j), max(i, j)))

    return res


# Tests to determine if the solution is correct.
def printInteger(n):
    print("[", n, "]", sep="", end="")


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
        printInteger(expected)
        print(" Your output: ", end="")
        printInteger(output)
        print()
    test_case_number += 1


if __name__ == "__main__":
    k_1 = 6
    arr_1 = [1, 2, 3, 4, 3]
    expected_1 = 2
    output_1 = numberOfWays(arr_1, k_1)
    check(expected_1, output_1)

    k_2 = 6
    arr_2 = [1, 5, 3, 3, 3]
    expected_2 = 4
    output_2 = numberOfWays(arr_2, k_2)
    check(expected_2, output_2)
